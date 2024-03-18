# 모델을 가져와 응답을 할 수 있도록 설정해준다.
from langchain_community.llms import Ollama
llm = Ollama(model="llama2")

result = llm.invoke("how can langsmith help with testing?")
print(result)