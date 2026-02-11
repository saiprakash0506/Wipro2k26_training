import pandas as pd

data={
    "Employee":["John","Alice","Bob","Eva","Mark"],
    "Department":["IT","HR","IT","Finance","HR"],
    "Salary":[50000,60000,55000,65000,62000]
}

df=pd.DataFrame(data)

it_employees=df[df["Department"]=="IT"]
print("IT Employees:")
print(it_employees)

avg_sal=df.groupby("Department")["Salary"].mean()
print("\n Average Salary per Department:")
print(avg_sal)

df["Salary_Adjusted"]= df["Salary"]*1.10
print("\n Adjusted salary:")
print(df)