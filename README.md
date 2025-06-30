# Cem Kaya HG Agents Course

## Usage

1. Start Ollama with your DeepSeek model:

ollama serve



2. Install dependencies:

pip install smolagents[toolkit] litellm



3. Edit your `gaia_tasks.jsonl` file as needed.

4. Run single prompt:
python run_agent.py

markdown
Copy
Edit

5. Run GAIA batch evaluation:
python evaluate.py



## Directory Structure

- `tools.py` — defines all agent tools
- `ollama_connector.py` — (optional) custom model class
- `run_agent.py` — single question test/demo
- `evaluate.py` — batch GAIA submission generator
- `submission.jsonl` — your GAIA submission file