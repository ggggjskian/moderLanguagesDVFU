import os
import csv
import random
import pandas as pd
from concurrent.futures import ProcessPoolExecutor as Pool


def generate_file(count_numbers: int) -> bool:
    try:
        os.mkdir("assets")
    except Exception as e:
        pass

    letters = ["A","B","C","D"]
    for n in range(0,5):
        temp_list = [("Категория", "Значение")]
        for i in range (0,count_numbers):
            random_letter = random.choice(letters)
            random_number = random.random()
            temp_list.append((random_letter,random_number))
        with open(f'assets/inputData{n}.csv',"w", newline='') as f:
            csv.writer(f).writerows(temp_list)
    return True

 


def count_median(filepath: str) -> pd.DataFrame:
    dt=pd.read_csv(filepath)
    result = dt.groupby("Категория")["Значение"].apply(list).reset_index()
    result["Медиана"] = result["Значение"].apply(lambda x : pd.Series(x).median())    
    return  result




def main () -> None:
    param = os.listdir("assets")
    path_to_file = [f"assets/{x}" for x in param]
    with Pool(max_workers=5) as executor:
        results = list(executor.map(count_median, path_to_file))
    
    #for elements in results:
    #    print(elements, "\n")

    a = pd.concat(results, ignore_index=True)
    a = a.groupby("Категория")["Медиана"].apply(list).reset_index()
    #print(a, "\n")
    a["Медиана медиан"] = a["Медиана"].apply(lambda x : pd.Series(x).median())   
    a["Стандартное отклонение"] = a["Медиана"].apply(lambda x : pd.Series(x).std())   
    print(a)



generate_file(10)
main()