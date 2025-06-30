from smolagents.tools.web import DuckDuckGoSearchTool, WebBrowserTool
from smolagents.tools.calc import CalculatorTool
from smolagents.tools.wikipedia import WikipediaTool
from smolagents.tools.files import FileReaderTool

def build_tools():
    return [
        DuckDuckGoSearchTool(),
        WebBrowserTool(),
        CalculatorTool(),
        WikipediaTool(),
        FileReaderTool(),
    ]
