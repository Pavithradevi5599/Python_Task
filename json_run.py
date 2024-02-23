import json

def main():
    # Open the JSON file
    with open('check_json.json') as json_file:
        data = json.load(json_file)  # Load JSON data from the file

    # Accessing data from the JSON object
    company_name = data['company']['name']
    employee_name = data['company']['employee']['name']
    salary = data['company']['employee']['payble']['salary']
    bonus = data['company']['employee']['payble']['bonus']

    # Printing the retrieved data
    print(f"Company Name: {company_name}")
    print(f"Employee Name: {employee_name}")
    print(f"Salary: {salary}")
    print(f"Bonus: {bonus}")

if __name__ == "__main__":
    main()
