ten_year = 1000 * ( 1 + 0.07) ** 10
twenty_year = ten_year * ( 1 + 0.07) ** 10
thirty_year = twenty_year * ( 1 + 0.07) ** 10

print(f"After 10 years, the investment will be: ${ten_year:.2f}")
print(f"After 20 years, the investment will be: ${twenty_year:.2f}")
print(f"After 30 years, the investment will be: ${thirty_year:.2f}")
