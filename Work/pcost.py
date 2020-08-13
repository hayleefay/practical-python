# pcost.py
#
# Exercise 1.27

total_cost = 0

with open('Data/portfolio.csv', 'rt') as f:
    header = next(f)
    for line in f:
        row = line.split(',')
        name = row[0]
        shares = int(row[1])
        price = float(row[2])

        total_cost += (price * shares)

print(f'Total cost {total_cost}')



