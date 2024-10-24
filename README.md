Python playground area where I practice python for Data Science from Scratch , and play with Datas using python libraries

### **Python Data Science Interview Test.**

**Instructions:**

- You may use Python 3 for solving these questions.
- You can use libraries such as `pandas`, `numpy`, `matplotlib`, `seaborn`, and `scikit-learn` where applicable.
- Please write clear, commented code, and include explanations for your approach where necessary.

---

#### **Part 1: Python Programming Basics (30 minutes)**

1.  **List and String Manipulation (5 points)**  
    Write a function `reverse_even_strings(strings: list)` that takes a list of strings and returns a new list where all strings with even lengths are reversed. Strings with odd lengths should remain unchanged.

    Example:

    ```python
    Input: ["data", "science", "is", "fun"]
    Output: ["atad", "ecneics", "is", "fun"]
    ```

2.  **Dictionary Manipulation (5 points)**  
    Given a dictionary `data = {'Alice': 45, 'Bob': 78, 'Charlie': 62, 'David': 53}`, write a Python function `pass_students(data: dict, threshold: int)` that returns a new dictionary containing only students who scored above the given `threshold`.

    Example:

    ```python
    Input: pass_students({'Alice': 45, 'Bob': 78, 'Charlie': 62, 'David': 53}, 60)
    Output: {'Bob': 78, 'Charlie': 62}
    ```

3.  **Lambda Functions and Sorting (5 points)**  
    You have a list of tuples representing employees and their ages: `employees = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]`. Write a Python function `sort_by_age(employees: list)` that returns a list sorted by age in ascending order using `lambda` and `sorted`.

    Example:

    ```python
    Output: [('Bob', 25), ('Alice', 30), ('Charlie', 35)]
    ```

---

#### **Part 2: Data Manipulation with Pandas (30 minutes)**

4.  **Pandas DataFrame Operations (10 points)**  
    Given the following dataset:

    ```python
    import pandas as pd

    data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
            'Age': [24, 27, 22, 32, 29],
            'Department': ['HR', 'IT', 'Finance', 'HR', 'IT'],
            'Salary': [50000, 60000, 45000, 52000, 62000]}
    df = pd.DataFrame(data)
    ```

    - (a) Write code to compute the average salary by department.
    - (b) Write code to filter all employees whose age is greater than 25.
    - (c) Add a new column `Bonus` where the bonus is 10% of the salary.

    Example output:

    ```python
    Output for (a): {'HR': 51000.0, 'IT': 61000.0, 'Finance': 45000.0}
    ```

5.  **Handling Missing Data (5 points)**  
    You are given a DataFrame with some missing values:

    ```python
    data = {'A': [1, 2, None, 4], 'B': [5, None, None, 8], 'C': [None, 2, 3, 4]}
    df = pd.DataFrame(data)
    ```

    - Write Python code to replace all `None` values with the mean of their respective columns.

---

#### **Part 3: Data Visualization (20 minutes)**

6.  **Matplotlib Visualization (5 points)**  
    Using the `matplotlib` library, create a bar plot showing the number of employees in each department from the dataset in Part 2, question 4.
7.  **Seaborn Visualization (5 points)**  
    Using `seaborn`, create a box plot showing the distribution of salaries by department from the dataset in Part 2, question 4.

---

#### **Part 4: Basic Machine Learning (40 minutes)**

8.  **Train-Test Split and Model Training (10 points)**  
    You are given the famous Iris dataset:

    ```python
    from sklearn.datasets import load_iris
    data = load_iris()
    X, y = data.data, data.target
    ```

    - (a) Split the dataset into training and testing sets with an 80-20 ratio.
    - (b) Train a Logistic Regression model to classify the iris species using the `scikit-learn` library.
    - (c) Print the accuracy score of the model on the test set.

9.  **Evaluation and Feature Scaling (10 points)**  
    Continuing from the previous question:

    - (a) Apply `StandardScaler` to scale the features before training the model again.
    - (b) Print the updated accuracy score after feature scaling.

10. **Feature Importance (5 points)**  
    Train a RandomForestClassifier on the same Iris dataset and print out the feature importance scores for each feature.


    Example:

    ```python
    Feature 1 importance: 0.2
    Feature 2 importance: 0.3
    Feature 3 importance: 0.1
    Feature 4 importance: 0.4
    ```

---

### **Total Points: 50**

- Part 1: 15 points
- Part 2: 15 points
- Part 3: 10 points
- Part 4: 20 points

**Good luck!**

---

This test covers core Python programming, data manipulation with pandas, basic visualization, and fundamental machine learning techniques, providing a well-rounded assessment of Python proficiency in data science.
