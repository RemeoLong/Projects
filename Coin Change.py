# Coin Change
# Object of this program is to give the correct change for a dollar amount.
# We, also, need to know which coins were used and how many were used.
# Data TYpe: Float
# 12 Different Variables

total_sum = (100)
cash = ()
sum = ()
coins = 0
quarter = 25
quarter_count = 0
dime = 10
dime_count = 0
nickel = 5
nickel_count = 0
penny = 1
penny_count = 0

cash = int(input("Enter a number: "))
sum = total_sum - cash
print("Your change amount is:", sum, "cents.")

while coins != sum:
    if coins <= sum:
        coins += quarter
        quarter_count += 1
        if coins == sum:
            break
        elif coins >= sum:
            coins -= quarter
            quarter_count -= 1
            coins += dime
            dime_count += 1
            if coins == sum:
                break
            if coins >= sum:
                coins -= dime
                dime_count -= 1
                coins += nickel
                nickel_count += 1
                if coins == sum:
                    break
                if coins >= sum:
                    coins -= nickel
                    nickel_count -= 1
                    coins += penny
                    penny_count += 1

print("You were given", quarter_count, "quarters,", dime_count, "dimes,", nickel_count,
      "nickels, and", penny_count, "pennies.")

