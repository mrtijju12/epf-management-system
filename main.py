from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Temporary database
employees = []

# Employee Model
class Employee(BaseModel):
    employee_id: int
    employee_name: str
    department: str
    designation: str
    salary: float

# Home API
@app.get("/")
def home():
    return {
        "message": "EPF Management System Running Successfully"
    }

# Create Employee
@app.post("/employees")
def create_employee(employee: Employee):
    employees.append(employee)
    
    return {
        "message": "Employee Created Successfully",
        "employee": employee
    }

# Get All Employees
@app.get("/employees")
def get_all_employees():
    return employees

# Get Employee By ID
@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):

    for employee in employees:
        if employee.employee_id == employee_id:
            return employee

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )

# Update Employee
@app.put("/employees/{employee_id}")
def update_employee(employee_id: int,
                    updated_employee: Employee):

    for index, employee in enumerate(employees):

        if employee.employee_id == employee_id:

            employees[index] = updated_employee

            return {
                "message": "Employee Updated Successfully",
                "employee": updated_employee
            }

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )

# Delete Employee
@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):

    for index, employee in enumerate(employees):

        if employee.employee_id == employee_id:

            employees.pop(index)

            return {
                "message": "Employee Deleted Successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )