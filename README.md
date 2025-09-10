🩺 Medical Chatbot with LLMs, LangChain, Pinecone, Flask & AWS 🚀

An intelligent AI-powered Medical Chatbot that leverages Large Language Models (LLMs), LangChain, Pinecone, Flask, and AWS to provide medical information, symptom assistance, and healthcare-related guidance.
⚠️ Disclaimer: This chatbot is for educational and informational purposes only and should not replace professional medical advice.

📌 Features

 Conversational AI powered by LLMs + LangChain

 Vector Database integration with Pinecone for medical knowledge retrieval

 Flask Backend for API & chatbot services

 AWS Deployment for scalability (EC2 / Lambda / S3)

 Secure Key Management with .env files

 Extensible Design – easy to add new knowledge sources

🏗️ Tech Stack

Backend: Python, Flask

AI/ML: LLMs (OpenAI / HuggingFace), LangChain

Vector DB: Pinecone

Cloud: AWS (EC2, Lambda, S3, IAM)

----------------------------------
⚡ Installation & Setup:::
---------------------------------
1️⃣ Clone Repository
git clone https://github.com/your-username/medical-chatbot.git
cd medical-chatbot

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Set Environment Variables

Create a .env file in the root directory:

OPENAI_API_KEY=your_openai_key (ex: AIzNaSybQuM6euF3FOx_s4GTaSmNliD2MGTY56IO1NJ )
PINECONE_API_KEY=your_pinecone_key
PINECONE_ENV=your_pinecone_env
FLASK_ENV=development
AWS_ACCESS_KEY_ID=your_aws_key
AWS_SECRET_ACCESS_KEY=your_aws_secret

5️⃣ Run Flask App
python app.py


Now visit 👉 http://127.0.0.1:5000/
