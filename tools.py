# tools.py
"""
All custom / third-party tools used by our CodeAgent.
"""

from smolagents import (
    DuckDuckGoSearchTool,
    PythonInterpreterTool,
    Tool,
)


class PythonFileReaderTool(Tool):
    """
    Simple helper that lets the agent read a local text file and return its
    contents as a string.  ❗  Only text files are supported.
    """

    # A short, unique slug that appears in tool calls
    name = "read_file"

    # Human-readable description (shown to the LLM)
    description = "Read a UTF-8 text file from disk and return its content."

    # OpenAPI-style schema for inputs / outputs
    inputs = {
        "file_path": {
            "type": "string",
            "description": "Absolute or relative path of the file to read.",
        }
    }
    output_type = "string"

    # NOTE: The method **must** be named `forward` and take parameters that
    # exactly match the keys of `inputs`.
    def forward(self, file_path: str) -> str:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            # Return a plain-text error so the agent can reason about it
            return f"ERROR: {e}"


def build_tools():
    """
    Factory used by evaluate.py / run_agent.py
    Add or remove tools here as you wish.
    """
    return [
        DuckDuckGoSearchTool(),
        PythonInterpreterTool(),
        PythonFileReaderTool(),
    ]
