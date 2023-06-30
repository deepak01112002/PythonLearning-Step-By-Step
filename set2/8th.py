#objecttype

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

output = {employee: defaults for employee in employees}

print(output)