from langchain_ollama import OllamaLLM

def load_llm():
    return OllamaLLM(model="llama3.2:1b")

def run_prompt(prompt: str) -> str:
    llm = load_llm()
    return llm.invoke(prompt)
