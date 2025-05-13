# Chatbot-Project

📄 NotePad LLM - PDF Analyzer

This project is designed to leverage LLM-powered text analysis for extracting and summarizing content from PDF documents. Using Streamlit, it provides an intuitive UI where users can upload PDFs and submit queries related to the document's content.
Key Features:
* PDF Text Extraction: Uses PyPDF2 to extract text from uploaded PDFs.
* LLM-Powered Summarization: Integrates with Gemini AI (via langchain_google_genai) to process and summarize document content dynamically.
* User-Friendly Interface: Built with Streamlit, enabling easy interactions through a sidebar API key input and buttons for submission.
* Error Handling: Displays warnings for missing inputs and gracefully handles processing errors.

🛠 Installation Steps:

Follow these steps to set up NotePad LLM - PDF Analyzer on your local machine:


1️⃣ Clone the Repository:

git clone https://github.com/your-username/notepad-llm-pdf-analyzer.git
cd notepad-llm-pdf-analyzer

2️⃣ Create a Virtual Environment (Optional but Recommended):

python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows


3️⃣ Install Dependencies:

pip install -r requirements.txt


4️⃣ Set Up Environment Variables:

Create a .env file in the project folder and add your Gemini API Key:
GEMNI_Api_Key="your_api_key_here"


5️⃣ Run the Application:

streamlit run app.py


Once you see the Streamlit UI, you're good to go! 🚀
Let me know if you need additional setup guidance.

📌 Usage Instructions


Once you've installed NotePad LLM - PDF Analyzer, follow these steps to use it effectively:


1️⃣ Start the Application
Run the command:
streamlit run app.py
This will launch the Streamlit UI in your browser.


2️⃣ Enter Your Gemini API Key:
- Locate the sidebar section on the left.
- Input your Gemini API Key (required for AI-generated summaries).


3️⃣ Upload a PDF Document:
- Click on the 📎 Upload your PDF file button.
- Select a PDF document from your device.
- Ensure it's a valid PDF file, or you'll see a warning message.


4️⃣ Enter Your Query:
- Type a question or topic related to the document in the input field:
Example: "Summarize the chapter on machine learning techniques."


5️⃣ Generate AI Summary:
- Click 🚀 Submit to start analysis.
- The AI will extract text from the PDF and generate a summary related to your query.


6️⃣ View Results:
- Once the process is complete, the summary appears on the page.
- If an error occurs (e.g., API issues), an appropriate warning message is displayed.
This tool makes document analysis seamless! 🎯 Let me know if you want any refinements.



