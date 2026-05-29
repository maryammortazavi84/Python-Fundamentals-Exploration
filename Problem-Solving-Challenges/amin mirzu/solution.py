def assign_tables(groups: dict[str, list[str]], tables_num: int) -> tuple[dict[str, int], list[tuple[str, int, str]]]:
    assigned_tables : dict[str, int] = {}
    collisions : list[tuple[str, int, str]] = []
    for group_name in groups:
        group = groups[group_name]
        table_number = _cal_table_number(group, tables_num)
        assigned_tables[group_name] = table_number

    table_to_team : dict[int, str] = {}
    for group_name in assigned_tables:
        table_number = assigned_tables[group_name]
        if table_number in table_to_team:
            collisions.append((group_name, table_number, table_to_team[table_number]))
        table_to_team[table_number] = group_name
        


    return assigned_tables, collisions

def _fibonacci (n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return _fibonacci(n - 1) + _fibonacci(n - 2)
    

def _hash_name(name: str) -> int:
    total = 0
    for i in range(len(name)):
        num = ord(name[i]) * _fibonacci(i + 1)
        total += num
    return total

def _cal_sum_hash(group: list[str]) -> int:
    sum_hash = 0
    for name in group:
        sum_hash += _hash_name(name)
    return sum_hash

def _cal_table_number(group: list[str], tables_num: int) -> int:
    sum_hash = _cal_sum_hash(group)
    return (sum_hash * len(group)) % tables_num
    

