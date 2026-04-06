from transformers import pipeline

# Load GPT-2 model
generator = pipeline("text-generation", model="gpt2")

# Try different prompts
prompts = [
    "Startup idea:",
    "Story about a hacker:",
    "How to become rich:",
    "Explain AI in simple words:"
]

# Generate output for each prompt
for prompt in prompts:
    print("\nPrompt:", prompt)
    
    result = generator(
        prompt,
        max_length=50,
        num_return_sequences=3
    )
    
    for i, res in enumerate(result):
        print(f"Output {i+1}:", res['generated_text'])