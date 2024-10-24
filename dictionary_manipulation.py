# 2.  Dictionary Manipulation. (5 points) 
#     Given a dictionary `data = {'Alice': 45, 'Bob': 78, 'Charlie': 62, 'David': 53}`, write a Python function `pass_students(data: dict, threshold: int)` that returns a new dictionary containing only students who scored above the given `threshold`.

#     Example:

#    
#     Input: pass_students({'Alice': 45, 'Bob': 78, 'Charlie': 62, 'David': 53}, 60)
#     Output: {'Bob': 78, 'Charlie': 62}

def pass_students(idata: dict,t):
    passed_stud ={}
    for key , value in idata.items():
        if value >= t:
            passed_stud[key] = value
    return passed_stud
            

input_data = {
    'Alice': 45,
    'Bob': 78,
    'Charlie': 62, 
    'David': 53
    }
threshold = 60
print(pass_students(input_data,threshold))
