from langchain_model import que_ans

question = input("Please enter your question :- ")
answer = que_ans(question)

print(answer)