import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Ensure your .env file has GOOGLE_API_KEY=your_key_here
load_dotenv()

# 1. Define your prompts
prompt1 = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
)

# 2. Initialize Gemini Model
# You can use "gemini-1.5-flash" for speed or "gemini-1.5-pro" for higher quality
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

parser = StrOutputParser()

# 3. Create the Chain
# Note: The output of the first model must be passed to the second prompt as 'text'
chain = (
    prompt1 | model | parser | (lambda output: {"text": output}) | prompt2 | model | parser
)

# 4. Execute
result = chain.invoke({'topic': 'Unemployment in India'})

print("--- Summary Report ---")
print(result)

# 5. Visualize the graph
chain.get_graph().print_ascii()