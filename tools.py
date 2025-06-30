from smolagents import (
    DuckDuckGoSearchTool, 
    GoogleSearchTool,
    WikipediaSearchTool,
    VisitWebpageTool,
    PythonInterpreterTool,
    SpeechToTextTool,
)

def build_tools():
    tools = []
    tool_classes = [
        DuckDuckGoSearchTool,
        GoogleSearchTool,
        WikipediaSearchTool,
        VisitWebpageTool,
        PythonInterpreterTool,
        SpeechToTextTool,
    ]
    for tool_cls in tool_classes:
        try:
            tools.append(tool_cls())
        except Exception as e:
            print(f"Tool {tool_cls.__name__} could not be loaded: {e}")
    return tools
