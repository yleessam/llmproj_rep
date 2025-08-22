from dotenv import load_dotenv
import os
load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
print("API Key configured:", "OPENAI_API_KEY" in os.environ)

#랭체인
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model='gpt-4o-mini')

def investment_report(symbol, company, stock):
  prompt = ChatPromptTemplate.from_messages()
  output_parser = StrOutputParser()
  
  chain = prompt | llm | output_parser
  response = chain.invoke(
    'company':company,
    'business_info': stock.get_
  )
  
  return response