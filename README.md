This project is a web application that allows users to convert **English queries** into **SQL queries** and perform **CRUD operations on a database table**.

**Features**
1. **English to SQL Conversion:** Convert English queries into SQL queries for database operations.
2. **CRUD Operations:** Perform basic CRUD operations (CREATE, READ, UPDATE, DELETE) on a database table.
3. **Gemini-Pro:** Powered by Gemini-Pro for natural language processing.
4. **Streamlit:** Built with Streamlit for easy web application development.
   
**Setup**

**Clone the repository:**

git clone https://github.com/RagalaSantosh/Text_to_SQL_using_LLM.git

**Install the dependencies:**

1. pip install -r requirements.txt
2. streamlit run app.py
3. Access the application at http://localhost:8501.

**Usage**
1. Enter an English query in the input box.
2. Click the "Convert" button to see the corresponding SQL query.
3. To perform CRUD operations, select the operation (CREATE, READ, UPDATE, DELETE) and provide the necessary details.
4. Click the corresponding button to execute the operation.
   
**Example Queries**

**Input:** "Show all employees."
**Output:** "SELECT * FROM Employees;"

**Input:** "Add a new employee with name 'Alice' and level 'Senior'."
**Output:** "INSERT INTO Employees (NAME, LEVEL) VALUES ('Alice', 'Senior');"
