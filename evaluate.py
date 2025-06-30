import json
import os
from smolagents import CodeAgent, LiteLLMModel
from tools import build_tools

# Path setup
GAIA_TASKS = "GAIA/2023/test/metadata.jsonl"
GAIA_FILES_DIR = "GAIA/2023/test"
SUBMISSION = "submission.jsonl"

def get_file_path(file_name):
    if not file_name:
        return None
    abs_path = os.path.join(GAIA_FILES_DIR, file_name)
    return abs_path if os.path.isfile(abs_path) else None

def main():
    # Load tasks
    with open(GAIA_TASKS, "r", encoding="utf-8") as f:
        tasks = [json.loads(line) for line in f]

    # Setup model and agent
    model = LiteLLMModel(
    model_id="ollama_chat/llama3:8b",     # <- Update this line
    api_base="http://localhost:11434",    # Ollama's default API address
    num_ctx=8192                          # or lower if needed
    )
    
    agent = CodeAgent(
        tools=build_tools(),
        model=model,
        additional_authorized_imports=["requests"]
    )

    # Write answers
    with open(SUBMISSION, "w", encoding="utf-8") as out_f:
        for task in tasks:
            task_id = task.get("id") or task.get("task_id")
            question = task.get("question") or task.get("input")
            file_path = get_file_path(task.get("file_name"))

            # Compose input
            if file_path:
                prompt = f"{question}\nAssociated file: {file_path}"
            else:
                prompt = question

            try:
                result = agent.run(prompt)
                # Try to extract answer and reasoning if dict, else just use result as answer
                if isinstance(result, dict):
                    answer = result.get("final_answer") or result.get("answer") or ""
                    reasoning = result.get("reasoning") or ""
                else:
                    answer = str(result)
                    reasoning = ""
            except Exception as e:
                answer = "ERROR"
                reasoning = str(e)

            # Write result in GAIA format
            json.dump({
                "task_id": task_id,
                "model_answer": answer,
                "reasoning_trace": reasoning
            }, out_f)
            out_f.write("\n")

            print(f"[{task_id}] Done")

if __name__ == "__main__":
    main()
