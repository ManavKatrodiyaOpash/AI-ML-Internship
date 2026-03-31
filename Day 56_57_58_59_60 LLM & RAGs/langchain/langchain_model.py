from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os

os.environ["HF_HOME"] = "D:/huggingface_cache"

llm = HuggingFacePipeline.from_model_id(
    model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = "text-generation",
    pipeline_kwargs={
        "temperature" : 0.7,
        "max_new_tokens" : 100,
    }
)

model = ChatHuggingFace(llm=llm)

# response = model.invoke("What is the capital of France?")
# print(response.content)

def que_ans(question):
    response = model.invoke(question)
    return response.content