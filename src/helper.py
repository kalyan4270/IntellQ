import os 
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import TokenTextSplitter , CharacterTextSplitter,RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.summarize import load_summarize_chain
from langchain.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_community.embeddings import HuggingFaceEmbeddings
import re
import time
from src.prompt import *
from dotenv import load_dotenv

load_dotenv()  

api_key = os.getenv("GOOGLE_API_KEY")  



def file_processing(file_path):
    loader = PyPDFLoader(file_path=file_path)
    data = loader.load()
    question_gen = ""
    for page in data:
        question_gen += page.page_content
    doc  = [Document(page_content=question_gen)]
    splitter_que = RecursiveCharacterTextSplitter(
    chunk_size=1000,   
    chunk_overlap=100  
    )
    ques_chunk = splitter_que.split_documents(doc) 
    splitter_ans = RecursiveCharacterTextSplitter(
    chunk_size=4000,   
    chunk_overlap=200  
    )
    ans_chunk = splitter_ans.split_documents(ques_chunk)

    return ques_chunk, ans_chunk

def llm_pipeline(file_path):

    document_ques_gen, document_ans_gen =  file_processing(file_path)

    llm_question_gen = ChatGoogleGenerativeAI(
        model = "gemini-1.5-pro",
        temperature=0.5)
    Prompt_Questions = PromptTemplate(template = prompt_template,input_variables = ["test"])
    Refined_Prompt_Questions = PromptTemplate(template = Refine_template,input_variables = ["existing_answer","test"])

    ques_gen_chain = load_summarize_chain(llm= llm_question_gen,
                                      chain_type="refine",
                                      verbose=True,
                                      question_prompt = Prompt_Questions,
                                      refine_prompt = Refined_Prompt_Questions)
    
    ques = ques_gen_chain.run(document_ques_gen)

    embeddings = HuggingFaceEmbeddings()
    vectore_store = FAISS.from_documents(document_ans_gen,embeddings)

    llm_answer_gen = ChatGoogleGenerativeAI(
        model = "gemini-1.5-pro",
        temperature=0.5)
    
    ques_list = ques.split("\n")
    cleaned_list = [q for q in ques_list if q.strip() and not re.match(r'^\*{2}.*\*{2}$', q.strip())]

    ans_gen_chain = RetrievalQA.from_chain_type(llm= llm_answer_gen,
                            chain_type = "stuff",
                            retriever = vectore_store.as_retriever())
    
    return ans_gen_chain, cleaned_list