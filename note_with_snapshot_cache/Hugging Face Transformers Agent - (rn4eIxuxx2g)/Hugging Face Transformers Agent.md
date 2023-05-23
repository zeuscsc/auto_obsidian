## Hugging Face Transformers Agent
### Hugging Face Transformers Agent Introduction [![[/snapshots/rn4eIxuxx2g/00-00-02.png]]](<https://youtu.be/rn4eIxuxx2g?t=0s>)
Hugging Face released the Transformers agent to connect and execute transformer models hosted on Hugging Face. It is similar to Linechain agents and offers three options: Star Coder, Open Assistant, and OpenAI. The Transformer agents use various tools, such as image generator model, image captioner model, text-to-speech model, etc., and the Python syntax to generate the output. [![[/snapshots/rn4eIxuxx2g/00-00-10.png]]](<https://youtu.be/rn4eIxuxx2g?t=8s>)

### Transformers Agent vs. Linechain Agent [![[/snapshots/rn4eIxuxx2g/00-00-14.png]]](<https://youtu.be/rn4eIxuxx2g?t=11s>)
Transformers agent mainly uses models for specific tasks, whereas Linechain agent uses external APIs. Linechain tools are mostly external APIs and not models. Both offer tools that can contribute to each other's use. The prompt selection between the two agents is different. Transformers agent's scope is narrower and executes Python codes only, while Linechain agent aims for a larger scope and use. 

### Examples and Benefits of Transformers Agent [![[/snapshots/rn4eIxuxx2g/00-00-29.png]]](<https://youtu.be/rn4eIxuxx2g?t=27s>)
Transformers agent provides capabilities that large language models cannot do alone, such as converting text to speech. The combination of tools makes the process more accurate and easier for specific tasks. Transformers agent tools can be extended or contributed to with ease by using Python code. It handles tasks like image generation, image captioning, speech to text, and text classification effectively. [![[/snapshots/rn4eIxuxx2g/00-07-52.png]]](<https://youtu.be/rn4eIxuxx2g?t=470s>)

### Creating New Tools
New tools can be created for Transformers agent by creating a new class that depends on the superclass 'tool'. Examples show how a Cat Image Fetcher tool can be created and used by the agent. This demonstrates the flexibility and extensibility of creating new tools in the Transformers agent framework. 

Source: [🤗 Hugging Face Transformers Agent | LangChain comparisons - YouTube](https://www.youtube.com/watch?v=rn4eIxuxx2g)
