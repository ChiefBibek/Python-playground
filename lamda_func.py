# 3.  Lambda Functions and Sorting (5 points)  
#     You have a list of tuples representing employees and their ages: `employees = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]`. Write a Python function `sort_by_age(employees: list)` that returns a list sorted by age in ascending order using `lambda` and `sorted`.

#     Example:

#     
#     Output: [('Bob', 25), ('Alice', 30), ('Charlie', 35)]
#     
def  sort_by_age(employees : list):
    sorted_data = sorted(employees , key = lambda x:x[1])
    return sorted_data


employees = [('Bob', 25), ('Alice', 30), ('Charlie', 35)]
print(sort_by_age(employees))
