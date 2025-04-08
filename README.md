# 🚀 Gemini-Powered Natural Language SQL Query App

Transform human language into precise SQL commands using Google Gemini Pro and an elegant Streamlit interface.
This intelligent application eliminates the barrier between natural language and database querying—ideal for data analysts, business users, and developers alike.

Built with ✨ Gemini 1.5 Pro, 🚀 Streamlit, and 🗃️ SQLite — engineered for real-time, secure, and accurate database interaction.
🌟 Key Features

💡 AI-Powered SQL Generation — Leverages gemini-1.5-pro-002 for contextual understanding of natural language.
⚡ Real-Time Query Execution — Seamlessly runs AI-generated SQL queries against a local SQLite database.
🧠 Domain-Specific Prompt Engineering — Ensures robust and secure SQL generation for academic datasets.
🖥️ Interactive Streamlit UI — Instant feedback loop from input to result with a clean, reactive interface.
🔐 .env-Based Key Management — Securely handles your API credentials using python-dotenv.
🛠️ Tech Stack

Tool / Library	Role
google-generativeai	Access to Gemini LLM for query generation
Streamlit	Frontend for user interaction
SQLite3	Lightweight local database engine
dotenv	Secure management of environment variables
Python 3.11+	Core programming language
🎯 Use Cases

This application is tailored for:

📊 Data Analysts – Access insights with no need to write SQL manually.
📚 Educators – Demonstrate how LLMs translate human queries into structured logic.
🧪 Dev Teams – Prototype AI-driven analytics features for intelligent applications.
🧍‍♀️ Business Users – Empower non-technical users to self-serve from internal databases.
🧠 How It Works

User enters a natural language question (e.g., “List students in Data Science class.”)
A custom-engineered prompt is sent to the Gemini 1.5 Pro model.
The model returns a clean, executable SQL query (without code blocks or SQL prefix).
The query is executed on a local SQLite database.
Results are rendered interactively in Streamlit.
🚀 Getting Started

🧪 Sample Prompt Engineering

The Gemini model is primed with an advanced system prompt:

You are an expert in converting English questions to SQL queries!
The SQL database has a STUDENT table with columns: NAME, CLASS, SECTION.
Examples:
- "How many records exist?" ➝ SELECT COUNT(*) FROM STUDENT;
- "List all students in Data Science" ➝ SELECT * FROM STUDENT WHERE CLASS="Data Science";
This ensures precision, robustness, and domain-aligned responses without redundant formatting.

📸 Live Demo Preview

User types: “Provide me the average marks of all students.”
![image](https://github.com/user-attachments/assets/a2136f1b-198b-4799-88a6-15269992f897)
The app responds with a real-time SQL result from the STUDENT database.
🔐 Security Best Practices

This app uses python-dotenv to manage your API key securely.
☑️ Do not hardcode credentials.
☑️ Ensure your .env file is excluded from version control.

🌱 Roadmap & Future Enhancements

✅ Gemini-powered table schema introspection
🔄 Support for PostgreSQL / MySQL connectors
📊 Visualizations of query results (matplotlib/altair)
🧑‍🎤 Voice-to-query and multi-modal input support
📦 Deploy on Hugging Face Spaces or DockerHub
🤝 Contributing

We welcome contributions! Please fork the repo and submit a PR.
For large changes, open an issue first to discuss your ideas.

This project is licensed under the MIT License.

📬 Contact & Attribution

👨‍💻 Author: S. Harish Krishnan
🌐 LinkedIn: https://www.linkedin.com/in/harishkds/
