import csv
from BTrees.OOBTree import OOBTree
from timeit import timeit

# === Функції додавання ===

def add_item_to_tree(tree, item):
    tree[item["ID"]] = item

def add_item_to_dict(dictionary, item):
    dictionary[item["ID"]] = item

# === Функції діапазонного запиту ===

def range_query_tree(tree, min_price, max_price):
    return [item for item in tree.values() if min_price <= item["Price"] <= max_price]

def range_query_dict(dictionary, min_price, max_price):
    return [item for item in dictionary.values() if min_price <= item["Price"] <= max_price]

# === Завантаження даних з CSV ===

def load_data(filename):
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        items = []
        for row in reader:
            items.append({
                "ID": int(row["ID"]),
                "Name": row["Name"],
                "Category": row["Category"],
                "Price": float(row["Price"])
            })
        return items

# === Основна логіка ===

def main():
    items = load_data("generated_items_data.csv")

    tree = OOBTree()
    dictionary = {}

    # Додаємо товари
    for item in items:
        add_item_to_tree(tree, item)
        add_item_to_dict(dictionary, item)

    # Діапазон цін (можна змінити на свій вибір)
    min_price = 20.0
    max_price = 80.0

    # Замір часу виконання діапазонних запитів
    tree_time = timeit(lambda: range_query_tree(tree, min_price, max_price), number=100)
    dict_time = timeit(lambda: range_query_dict(dictionary, min_price, max_price), number=100)

    # Результати
    print(f"Total range_query time for OOBTree: {tree_time:.6f} seconds")
    print(f"Total range_query time for Dict: {dict_time:.6f} seconds")

if __name__ == "__main__":
    main()
