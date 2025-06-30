from smolagents import PythonInterpreterTool, DuckDuckGoSearchTool

class PythonFileReaderTool:
    name = "read_file"
    description = "Reads a file from disk and returns its content"
    def __call__(self, file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            return f"ERROR: {e}"

def build_tools():
    return [
        DuckDuckGoSearchTool(),
        PythonInterpreterTool(),
        PythonFileReaderTool(),
        # Add other tools as needed
    ]
