# check_dependencies.py

libraries = [
    "langchain",
    "langgraph",
    "langchain_huggingface",
    "langsmith",
    "streamlit",
    "transformers",
    "torch"
]

for lib in libraries:
    try:
        __import__(lib)
        print(f"✅ {lib} is installed successfully.")
    except ImportError:
        print(f"❌ {lib} is NOT installed. Please install it using: pip install {lib}")
