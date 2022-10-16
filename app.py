from collections import Counter

def count_ID(value):
    sum = 0
    while value != 0:
        sum += value % 10
        value = value // 10
    return sum

def func1(n_customers):
    g = map(count_ID, list(range(n_customers)))
    return dict(Counter(g))

def func2(n_first_id, n_customers):
    g = map(count_ID, list(range(n_first_id, n_first_id + n_customers)))
    return dict(Counter(g))

if __name__ == '__main__':
    # print(count_ID(123))
    print(func1(9999999))
    print(func2(1000, 1000))