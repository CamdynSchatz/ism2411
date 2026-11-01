# SELF ASSESMENT QUESTIOBS
# 1. I first noticed that there wasnt a : on line ten. I noticed this first because I know that a for loop needs a colon.
# 2. It applies a discount from a items price based on the tier that customer has. Its inputs are price and tier and its 
# outputs are the price after the discount. I think a colleguege could clearly read this beause it is clearly labeled.
# 3. Ai disclosure: Ai was was used to help explain the code to me and help explain to me what when wrong within the code 
# for exercise 5. Ai helped build my understanding on what to look for while coding and what you need to make sure you 
# have in your code.




# Exercise 1 ---

# Defining a function
def calculate_tax(price, rate):
    return price * rate

# Calling the function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7% ${tax1:.2f}")
print(f"Tax for $250 at 8% ${tax2:.2f}")
print(f"Tax for $350 at 5% ${calculate_tax(350, 0.05):.2f}")

# --- Exercise 2 ---

# Defining a function with multiple parameters
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

# Calling the function with different tiers
original_price = 200

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")

# --- Exercise 3 ---

def final_price(price, tax_rate, discount_tier):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

# Calling the final_price function
print(f"final_price(200, 0.07, 'gold'): = ${final_price(200, 0.07, 'gold'):.2f}")

# --- Exercise 4 ---

order = [{200, 'gold'}, {150, 'silver'}, {100, 'bronze'}, {500, 'none'}]

rate = 0.07
for price, tier in order:
    total = final_price(price, rate, tier)
    print(f"Order: ${price} with {tier} discount = ${total:.2f}")

# --- Exercise 6 ---
  
x = 100

def double_it():
    x = 999
    return x * 2

print(x) 
print(double_it())
print(x)  