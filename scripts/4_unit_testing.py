import pandas as pd

# Expected Output  = {'Hogan', 'jr', 'Schwarzenegger', 'Macy', 'Smith', 'Garcia', 'Hernandez'}

data = {
    'order_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'name': ['Hulk Hogan', 'Alex jr', 'Hulk Hogan', 'Arnold Schwarzenegger ', 'Leta jr', 'Abraham Macy', 'Michael Smith', 'James Smith', 'Maria Garcia', 'Maria Hernandez'],
    'product_name': ['Ipad', 'AC', 'Laptop', 'CPU', 'Tab', 'HeadPhones', 'iPod', 'PSv5', 'AC', 'Laptop'],
    'product_proce': [33000, 65000, 50000, 30000, 40000, 20000, 40500, 80000, 55000, 40000],
}


df = pd.DataFrame(data)
rows = df.name.unique()
unique_last_name_list = set()

for row in rows:
    split_name = row.split()
    last_name = split_name[len(split_name)-1]
    if last_name not in unique_last_name_list:
        unique_last_name_list.add(last_name)

print(unique_last_name_list)

