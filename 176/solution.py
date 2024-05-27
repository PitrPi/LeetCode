import pandas as pd


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    sol = list(employee["salary"].drop_duplicates().nlargest(2))
    result = pd.DataFrame(data=[sol[1] if len(sol)>=2 else None], columns=["SecondHighestSalary"])
    return result
