# IntellQ - AI-Powered Interview Question Generator  


**IntellQ** is an AI-powered document analysis tool that intelligently extracts key insights from PDFs and generates structured interview questions based on their content. Utilizing **Large Language Models (LLMs)**, **Natural Language Processing (NLP)**, and **FastAPI**, this tool automates question-answer generation for research papers, technical reports, and study materials. 

## 🚀 Features  
-  **Upload & Analyze PDFs** – Users can upload a PDF document for AI-driven analysis.  
-  **AI-Based Question Generation** – Automatically generates interview questions based on the document’s content.  
-  **CSV Output** – Download the generated questions and answers in a structured CSV file.  
-  **FastAPI Backend** – Utilizes FastAPI for efficient API endpoints.  
-  **Bootstrap UI** – Responsive web interface.  

---

## 🛠️ Tech Stack  
- **Backend:** FastAPI 
- **Frontend:** HTML, CSS, Bootstrap, jQuery  
- **LLM model** gemini-1.5-pro
- **Vectore Database:** FAISS
- **Storage:** Local static files  
- **Deployment:** Uvicorn (FastAPI Server)  

---



## 📦 Installation  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/kalyan4270/IntellQ.git
cd IntellQ
```
---

### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate     # On Windows
---
```
### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```
---

## ▶️ Usage

``` bash
uvicorn app:app --reload
```
---
 
1. Upload & Analyze PDFs
2. Open the web interface.
3. Upload a PDF file.
4. Enter a filename and submit.
5. Download the generated interview questions CSV.
---

## 📝 API Endpoints  

| Method | Endpoint      | Description |
|--------|-------------|-------------|
| `GET`  | `/`         | Renders the UI |
| `POST` | `/upload`   | Uploads a PDF file |
| `POST` | `/analyse`  | Analyzes the uploaded file & generates questions |

---
