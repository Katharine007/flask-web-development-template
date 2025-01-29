from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database URI and disable tracking modifications for performance
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///activity_8.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with the Flask app
db = SQLAlchemy(app)

# Define the Department model (representing a department in the database)
class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary key for the department
    name = db.Column(db.String(100), nullable=False)  # Department name (required field)
    # Relationship with the Employee model
    employees = db.relationship('Employee', backref='department', lazy=True)

# Define the Employee model (representing an employee in the database)
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary key for the employee
    name = db.Column(db.String(100), nullable=False)  # Employee name (required field)
    department_id = db.Column(
        db.Integer, 
        db.ForeignKey('department.id'), 
        nullable=False
    )  # Foreign key linking the employee to a department

# Route to create a new department and associated employees
@app.route('/create-department')
def create_department():
    with app.app_context():  # Ensure the database context is active
        db.create_all()  # Create tables in the database if they don't exist

        # Create a new department and associated employees
        dept = Department(name="Engineering")
        emp1 = Employee(name="Alice", department=dept)  # Associate Alice with the department
        emp2 = Employee(name="Bob", department=dept)  # Associate Bob with the department
        
        # Add the department and employees to the session and commit them to the database
        db.session.add_all([dept, emp1, emp2])
        db.session.commit()

    return "Department and Employees created successfully!"

# Route to display all departments and their employees
@app.route('/display-department')
def display_department():
    # Query all departments from the database
    departments = Department.query.all()
    output = []  # List to store formatted department and employee information

    # Loop through each department and get its employees
    for dept in departments:
        # Create a comma-separated string of employee names for the department
        employees = ", ".join([emp.name for emp in dept.employees])
        # Add formatted information to the output list
        output.append(f"Department: {dept.name}, Employees: {employees}")

    # Return the formatted output as an HTML-safe string
    return "<br>".join(output)

# Entry point of the application
if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask application in debug mode
