
def count_ID(value):
    sum = 0
    while value != 0:
        sum += value % 10
        value = value // 10
    return sum

def func1(n_customers):
    groups = {}
    for i in range(n_customers):
        g_id = count_ID(i)
        if g_id in groups:
            groups[g_id] += 1
        else:
            groups[g_id] = 1
    return groups

def func2(n_first_id, n_customers):
    groups = {}
    for i in range(n_first_id, n_first_id + n_customers):
        g_id = count_ID(i)
        if g_id in groups:
            groups[g_id] += 1
        else:
            groups[g_id] = 1
    return groups

if __name__ == '__main__':
    # print(count_ID(123))
    print(func1(9999999))
    print(func2(1000, 1000))