def find_next_distinct_year(year):
    year += 1
    while len(set(str(year))) != 4:
        year += 1
    return year

# Test the function
year = int(input())
next_distinct_year = find_next_distinct_year(year)
print(next_distinct_year)
