from dotenv import load_dotenv

load_dotenv()


import streamlit as st
import os
import sqlite3
import google.generativeai as genai


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt, question])

    return response.text


def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)

    return rows



prompt =    """
    You are an expert in converting English questions to SQL queries! The SQL database has the name "Employee" and has the following columns: "EMPLOYEE_ID" (unique integer), "NAME" (string), "LEVEL" (string), "SALARY" (integer).

Examples:

Input: "How many employees are there in the database?"
Output: SELECT COUNT(*) FROM Employee;

Input: "Show me all the employees."
Output: SELECT * FROM Employee;

Input: "Show me the names and levels of all employees."
Output: SELECT NAME, LEVEL FROM Employee;

Input: "Show me the employees who are seniors."
Output: SELECT * FROM Employee WHERE LEVEL='Senior';

Input: "Add a new employee named 'Alice' with level 'Junior' and salary 60000."
Output: INSERT INTO Employee (EMPLOYEE_ID, NAME, LEVEL, SALARY) VALUES (101, 'Alice', 'Junior', 60000);

Input: "Update the salary of employee with ID 101 to 70000."
Output: UPDATE Employee SET SALARY=70000 WHERE EMPLOYEE_ID=101;

Input: "Delete the employee with ID 101."
Output: DELETE FROM Employee WHERE EMPLOYEE_ID=101;

Your converter should handle these basic CRUD operations and provide the corresponding SQL queries as output.

"""




## Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

# if submit is clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)

    st.subheader("SQL Query from LLM")
    st.write(response)
    response=read_sql_query(response,"sample.db")
    st.subheader("The Response is")
    for row in response:
        print(row)
        st.header(row)