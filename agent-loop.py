import os
import subprocess
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(override=True)

# 注意：BASE_URL 通常为 https://api.deepseek.com
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"), 
    base_url=os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
)
# 建议使用 deepseek-chat 或 deepseek-reasoner
MODEL = os.getenv("MODEL_ID", "deepseek-chat") 

SYSTEM = f"You are a coding agent at {os.getcwd()}. Use bash to solve tasks. Act, don't explain."

# 工具定义格式调整为 OpenAI/DeepSeek 标准格式
TOOLS = [{
    "type": "function", # 必须指定 type 为 function
    "function": {
        "name": "bash",
        "description": "Run a shell command.",
        "parameters": { # 对应 Anthropic 的 input_schema
            "type": "object",
            "properties": {"command": {"type": "string"}},
            "required": ["command"],
        },
    }
}]

def run_bash(command: str) -> str:
    dangerous = ["rm -rf /", "sudo", "shutdown", "reboot", "> /dev/"]
    if any(d in command for d in dangerous):
        return "Error: Dangerous command blocked"
    try:
        r = subprocess.run(command, shell=True, cwd=os.getcwd(),
                           capture_output=True, text=True, timeout=120)
        out = (r.stdout + r.stderr).strip()
        return out[:50000] if out else "(no output)"
    except subprocess.TimeoutExpired:
        return "Error: Timeout (120s)"

def agent_loop(messages: list):
    if messages[0].get("role") != "system":
        messages.insert(0, {"role": "system", "content": SYSTEM})

    while True:
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
            tool_choice="auto"
        )
        
        message = response.choices[0].message
        # 保存 Assistant 消息时需处理 OpenAI 的特殊对象格式
        messages.append(message) 

        # 判断是否需要继续调用工具 (finish_reason)
        if message.tool_calls is None:
            return

        # 执行工具调用并反馈结果
        for tool_call in message.tool_calls:
            import json
            # 解析参数
            args = json.loads(tool_call.function.arguments)
            command = args.get("command")
            
            print(f"\033[33m$ {command}\033[0m")
            output = run_bash(command)
            print(output[:200])
            
            # 结果反馈的消息结构
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": output
            })

if __name__ == "__main__":
    history = []
    while True:
        try:
            query = input("\033[36ms01 >> \033[0m")
        except (EOFError, KeyboardInterrupt):
            break
        if query.strip().lower() in ("q", "exit", ""):
            break
        
        history.append({"role": "user", "content": query})
        agent_loop(history)
        
        # 打印最后一条消息的文本内容
        last_msg = history[-1]
        if hasattr(last_msg, 'content') and last_msg.content:
             print(last_msg.content)
        elif isinstance(last_msg, dict) and last_msg.get("role") == "assistant":
             print(last_msg.get("content"))
        print()