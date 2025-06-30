from smolagents import CodeAgent, DuckDuckGoSearchTool, LiteLLMModel

# Use your Ollama model (e.g. deepseek-r1:14b)
model = LiteLLMModel(
    model_id="ollama_chat/deepseek-r1:14b",
    api_base="http://localhost:11434",  # default Ollama HTTP server
    num_ctx=8192
)

agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()],
    model=model,
    additional_authorized_imports=["requests"]  # if needed
)

result = agent.run("How many seconds to run 100 m at 10 m/s?")
print("Final answer:", result)
