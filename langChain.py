from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0,
                 groq_api_key="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")

template = """What is the capital of France?"""

prompt = PromptTemplate.from_template(template)

chain = prompt | llm | StrOutputParser()

response = chain.invoke({})

print(response)