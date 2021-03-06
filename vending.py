
eur_coins = [200, 100, 50, 20, 10, 5, 2, 1]
us_coins = [100, 50, 25, 10, 5, 1]

def get_change(amount, coins = eur_coins):
    change = []
    
    for coin in coins:
        while coin <= amount:
            change.append(coin)
            amount -= coin

    return change

assert get_change(0) == [], "Zero change should return an empty List"

assert get_change(1) == [1], "1 cent change should return a 1 cent coin"
assert get_change(2) == [2], "2 cent change should return a 2 cent coin"
assert get_change(5) == [5], "5 cent change should return a 5 cent coin"
assert get_change(10) == [10], "10 cent change should return a 10 cent coin"
assert get_change(20) == [20], "20 cent change should return a 20 cent coin"
assert get_change(50) == [50], "50 cent change should return a 50 cent coin"
assert get_change(100) == [100], "100 cent change should return a €1 coin"
assert get_change(200) == [200], "200 cent change should return a €2 coin"

assert get_change(3) == [2, 1], "3 cent should return two coins a 2 cent and a 1 cent"
assert get_change(7) == [5, 2], "7 cent should return two coins a 5 cent and a 2 cent"
assert get_change(11) == [10, 1], "11 cent should return two coins a 10 cent and a 1 cent"

assert get_change(9) == [5, 2, 2], "9 cent should return three coins a 10 cent and two 2 cent"

assert get_change(35, us_coins) == [25, 10], "In US 35 cent should return two coins a 25 cent and a 10 cent"

print("All tests pass")
