import json
from smolagents import CodeAgent, LiteLLMModel
from tools import build_tools

def main():
    # Update to your GAIA dev/test set file path
    with open('gaia_tasks.jsonl', 'r', encoding='utf-8') as f:
        tasks = [json.loads(line) for line in f]

    model = LiteLLMModel(
        model_id="ollama_chat/deepseek-r1:14b",
        api_base="http://localhost:11434",
        num_ctx=8192
    )
    agent = CodeAgent(
        tools=build_tools(),
        model=model,
        additional_authorized_imports=["requests"]
    )

    with open("submission.jsonl", "w", encoding='utf-8') as out_f:
        for task in tasks:
            task_id = task['id'] if 'id' in task else task['task_id']
            question = task['question'] if 'question' in task else task['input']

            try:
                result = agent.run(question, return_reasoning=True)
                answer = result.get("final_answer") if isinstance(result, dict) and "final_answer" in result else result
                reasoning = result.get("reasoning") if isinstance(result, dict) and "reasoning" in result else ""
            except Exception as e:
                answer = "ERROR"
                reasoning = str(e)

            out_f.write(json.dumps({
                "task_id": task_id,
                "model_answer": answer,
                "reasoning_trace": reasoning
            }) + "\n")

if __name__ == "__main__":
    main()
