# IntellQ - AI-Powered Interview Question Generator  


**IntellQ** is an AI-powered tool that analyzes PDFs and generates intelligent interview questions based on the content. It leverages **Large Language Models (LLMs)** to extract key insights and create meaningful questions to assist in interview preparation.  

---

## 🚀 Features  
- 📄 **Upload & Analyze PDFs** – Users can upload a PDF document for AI-driven analysis.  
- 🤖 **AI-Based Question Generation** – Automatically generates interview questions based on the document’s content.  
- 📊 **CSV Output** – Download the generated questions and answers in a structured CSV file.  
- ⚡ **FastAPI Backend** – Utilizes FastAPI for efficient API endpoints.  
- 🎨 **Bootstrap UI** – Responsive web interface.  

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
