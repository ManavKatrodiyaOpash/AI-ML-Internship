from langchain_community.llms.fake import FakeListLLM

llm = FakeListLLM(responses=["Jon Snow is a Stark."])

print(llm.invoke("Who is Jon Snow?"))

#########################################################

from langchain_core.prompts import PromptTemplate
from langchain_community.llms.fake import FakeListLLM

# Fake LLM
llm = FakeListLLM(responses=["Arya Stark is a warrior."])

# Prompt
prompt = PromptTemplate.from_template(
    "Answer this question: {question}"
)

# Chain (NEW WAY)
chain = prompt | llm

# Run
response = chain.invoke({"question": "Who is Arya Stark?"})
print(response)