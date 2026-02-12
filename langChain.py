from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0,
                 groq_api_key=os.getenv("GROQ_API_KEY"))

template = """What is the capital of France?"""

prompt = PromptTemplate.from_template(template)

chain = prompt | llm | StrOutputParser()

response = chain.invoke({})

print(response)