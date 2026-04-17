🤖 My Chatbot AI (OpenAI Model)

This project is part of my AI development learning journey through the IBM course. It demonstrates how to build a simple AI-powered chatbot using Python, a web interface, and modern AI APIs.

🚀 Overview

The goal of this project is to create a functional chatbot that can:

Accept user input via a web interface
Send the input to an AI model
Generate intelligent responses
Display the response back to the user in real time

This project helps understand the full pipeline of building an AI application, from frontend interaction to backend processing.

🧠 How It Works

The chatbot is built using three core layers:

1. Frontend (HTML, CSS, JavaScript)
Provides a simple UI for users to interact with the chatbot
Captures user input and sends it to the backend via HTTP requests
2. Backend (Flask)
Built using Flask
Handles API requests from the frontend
Processes user input and communicates with the AI model
3. AI Model (OpenAI API)
Uses OpenAI API to generate responses
Sends prompts and receives natural language outputs
🛠️ Technologies Used
Python 3.x
Flask
HTML, CSS, JavaScript
OpenAI API
RESTful APIs
📂 Project Structure
my-chatbot-ai-openai-model/
│
├── app.py                # Main Flask application
├── templates/           # HTML files
├── static/              # CSS and JS files
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
⚙️ Installation & Setup

Follow these steps to run the project locally:

1. Clone the repository
git clone https://github.com/NathStt/my-chatbot-ai-openai-model.git
cd my-chatbot-ai-openai-model
2. Create a virtual environment
python3 -m venv my_env
source my_env/bin/activate   # Mac/Linux
3. Install dependencies
pip install -r requirements.txt
4. Set up environment variables

Create a .env file and add your API key:

OPENAI_API_KEY=your_api_key_here
▶️ Running the Application

Start the Flask server:

python app.py

Then open your browser and go to:

http://127.0.0.1:5000
💬 Example Usage
Type a message in the chat interface
The message is sent to the backend
The backend calls the AI model
The response is displayed instantly
📚 Learning Objectives

This project helped me understand:

How AI chatbots work end-to-end
How to use APIs in real applications
How frontend and backend communicate
How to deploy and structure a Python project
Basics of prompt-based AI interaction
🔐 Notes
Make sure your API key is never exposed publicly
Always use environment variables for sensitive data
📈 Future Improvements
Add conversation memory
Improve UI/UX design
Add multi-language support
Deploy to cloud (e.g., IBM Cloud or AWS)
Integrate authentication
🙌 Acknowledgment

This project was developed as part of an AI course by IBM, focusing on practical AI application development.

📎 Repository Link

👉 https://github.com/NathStt/my-chatbot-ai-openai-model
