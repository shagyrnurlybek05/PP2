def all_true(elements: tuple) -> bool:
    return all(elements)

tuple_data = (True, 0, "hello", [])
print(all_true(tuple_data))  
