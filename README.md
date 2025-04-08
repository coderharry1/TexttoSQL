🚀 Gemini-Powered Natural Language SQL Query App

Transform plain English questions into executable SQL queries with the power of Google Gemini Pro and a simple, elegant Streamlit interface. This project bridges the gap between human language and structured database querying—perfect for rapid data exploration, education, or automation.

🌟 Features
💡 Natural Language to SQL Translation using gemini-1.5-pro-002
⚡️ Real-time Query Execution on an SQLite database
🧠 Built-in Prompt Engineering for domain-specific adaptation
🌐 Fully interactive web UI built with Streamlit
🔐 Secure API key management using .env
🛠️ Technologies Used
Tool/Library	Purpose
google-generativeai	Gemini LLM integration for NLU tasks
Streamlit	Lightweight front-end for interactivity
SQLite3	Lightweight embedded database engine
dotenv	Environment variable management
Python 3.11+	Core programming language
🎯 Use Case
This app was designed for:

Data analysts needing quick access to insights without SQL expertise
Educators demonstrating how LLMs can interface with structured data
Dev teams prototyping AI-driven analytics features
Business users wanting self-serve data querying capabilities
🧠 How It Works
User inputs a question in plain English (e.g., "How many students are in Data Science?")
Prompt-engineered input is passed to the Gemini model via google-generativeai
The generated SQL query is executed against a local SQLite database
Results are displayed instantly via Streamlit
📦 Installation
# Clone the repo
git clone https://github.com/yourusername/sql-gemini-app.git
cd sql-gemini-app

# Install dependencies
pip install -r requirements.txt

# Add your API key
echo "GOOGLE_API_KEY=your_api_key_here" > .env

# Run the app
streamlit run app.py
🧪 Sample Prompt Engineering
You are an expert in converting English questions to SQL queries!
The SQL database has a STUDENT table with the following columns: NAME, CLASS, SECTION.
...
This structured prompt ensures the model provides precise, executable, and safe SQL statements.

📸 App UI
Screenshot Placeholder
A user types: “Show all students from Data Science class.” The app responds with a table of relevant entries in real time.
🔐 API Key Security
This app uses python-dotenv to securely manage your GOOGLE_API_KEY. Do not hardcode secrets. Always use .env.

💡 Future Enhancements
✅ Add table schema introspection via Gemini
🔄 Support other SQL dialects (PostgreSQL, MySQL)
📊 Visualize query results (bar, pie, etc.)
🗣️ Voice-to-query input
🤝 Contribution & Licensing
Open to PRs, ideas, and collaborations!
Distributed under the MIT License.

📬 Contact
Author: S. Harish Krishnan
LinkedIn: Your LinkedIn
Blog: Medium Articles
