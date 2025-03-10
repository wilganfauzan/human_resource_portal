import streamlit as st
import pandas as pd
from employee import Employee
from training import Training


st.title("HR Portal")

def show_employees():
    st.title("Employee List")
    employees = Employee("employees.csv").get_all()
    df = pd.DataFrame(employees, columns=["id", "Name", "Position", "Department", "Monthly Salary", "Years of Service"])
    st.dataframe(df, use_container_width=True)

    st.subheader("Add New Employee")
    with st.form("add_employee_form"):
        name = st.text_input("Name")
        position = st.text_input("Position")
        department = st.text_input("Department")
        salary = st.number_input("Monthly Salary", min_value=0, step=100)
        years_of_service = st.number_input("Years of Service", min_value=0, step=1)

        submitted = st.form_submit_button("Add Employee")
        if submitted:
            new_id = len(df) + 1  
            new_employee = [new_id, name, position, department, salary, years_of_service]

            
            df.loc[len(df)] = new_employee
            df.to_csv("employees.csv", index=False)

            st.success(f"Employee {name} added successfully!")
            st.rerun()

def show_trainings():
    st.title("Training List")
    training = Training("training.csv").get_all()
    df = pd.DataFrame(training, columns=["Employee_ID", "Name", "Training", "Date", "Status"])
    st.dataframe(df, use_container_width=True)

    st.subheader("Add New Training")
    with st.form("add_training_form"):
        name = st.text_input("Name")
        training = st.text_input("Training")
        date = st.text_input("Date")
        status = st.number_input("Status")

        submitted = st.form_submit_button("Add Training")
        if submitted:
            new_id = len(df) + 1  
            new_training = [new_id, name, training, date, status]

            
            df.loc[len(df)] = new_training
            df.to_csv("employees.csv", index=False)

            st.success(f"Training {training} added successfully!")
            st.rerun()

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Menu", ["Employees", "Trainings"])
    
    if page == "Employees":
        show_employees()
    elif page == "Trainings":
        show_trainings()

if __name__ == "__main__":
    main()