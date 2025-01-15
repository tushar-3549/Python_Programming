        # API  to JSON data processing 

import requests
import json
response = requests.get("https://jsonplaceholder.typicode.com/posts")
posts = response.json()
# print(json.dumps(posts, indent=4))

        # Count the number of posts by each user
from collections import Counter
cnt = Counter(post['userId'] for post in posts)
print("Number of posts by each user: ", cnt)
       # Extract all unique titles
unique_titles = {post["title"] for post in posts}
print("\nUnique Titles (Count):", len(unique_titles))

        # Complex Nested JSON Parsing and Manipulation
'''
import json

data = '''
{
    "employees": [
        {
            "id": 1,
            "name": "John Doe",
            "department": "Engineering",
            "skills": ["Python", "FastAPI", "PostgreSQL"]
        },
        {
            "id": 2,
            "name": "Jane Smith",
            "department": "Design",
            "skills": ["Figma", "Sketch"]
        }
    ],
    "company": "TechCorp",
    "location": "San Francisco"
}
'''
parsed_data = json.loads(data)
# print(parsed_data)
formated_json = json.dumps(parsed_data, indent=4)
# print(formated_json)

         # print all employees name
print("Employee's name: ")
for emp in parsed_data["employees"]:
    print(emp["name"])

         # add new employee

new_employee = {
    "id": 3,
    "name": "Alice Johnson",
    "department": "HR",
    "skills": ["Recruitment", "Communication"]
}
parsed_data["employees"].append(new_employee)
# print(parsed_data)

         # Find an employee by department
for eng in parsed_data["employees"]:
    if eng["department"] == "Engineering":
        # print(eng["id"])
        print(eng)

       # convert back json string 

updated_json = json.dumps(parsed_data, indent=4)
# print(updated_json)
with open("updated_json.json", "w") as f:
    json.dump(parsed_data, f, indent=4)
print("Updated Json file exported successfully")

       # delete where id = 3

# parsed_data["employees"] = [emp for emp in parsed_data["employees"] if emp["id"] != 3]
# print("After Deleting Employee with ID 3:")
# print(json.dumps(parsed_data, indent=4))

for i, emp in enumerate(parsed_data["employees"]):
    if emp["id"] == 3:
        del parsed_data["employees"][i]
        break
print("After Deleting Employee with ID 3:")
print(json.dumps(parsed_data, indent=4))
      
       # count total employees
total_employees = len(parsed_data["employees"])
print(f"Total Employees: {total_employees}")

      # update the department of "John Doe" to "Data Science" 
for emp in parsed_data["employees"]:
    if emp["name"] == "John Doe":
        emp["department"] = "Data Science"
        emp["skills"].append("Machine Learning")
print("After Updating John Doe's Information:")
print(json.dumps(parsed_data, indent=4))

       # Find employees with the skill "Python"
python_dev = [emp for emp in parsed_data["employees"] if "Python" in emp["skills"]]
print(python_dev)
    
       # Sort employees by name
sorted_employees = sorted(parsed_data["employees"], key=lambda x: x["name"])
print(sorted_employees)
       
       # Check if "Alice Johnson" exists
employee_exists = any(emp["name"] == "John Doe" for emp in parsed_data["employees"])
print(f"Alice Johnson Exists: {employee_exists}")

      # Get a set of all unique skills
all_skills = [skill for emp in parsed_data["employees"] for skill in emp["skills"]]
print(set(all_skills))

     # read as json file
with open('updated_json.json', 'r') as f:
    data = json.load(f)
print(json.dumps(data, indent=4))
'''
              # Json Schema Validation
'''            
from jsonschema import validate, ValidationError

# JSON Schema
schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer", "minimum": 18},
        "email": {"type": "string", "format": "email"}
    },
    "required": ["name", "age", "email"]
}

# Example JSON Data
data = {
    "name": "Tushar Ahmed",
    "age": 25,
    "email": "md.tushar@example.com"
}

try:
    validate(instance=data, schema=schema)
    print("JSON is valid!")
except ValidationError as e:
    print(f"Validation Error: {e.message}")
 
'''