def calculate_discount(price, discount_percent):
    """Calculate the final price after applying a discount if it is 20% or more."""

    if discount_percent >= 20:
        discount_percent = (discount_percent / 100) * price

        # apply the discount
        return price - discount_percent 
    
    # return original price if discount is less than 20%
    return price

# get user input
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# calculate the final price
final_price = calculate_discount(price, discount_percent)

# print the result
if discount_percent >= 20:
    print(f"Discount applied! Final price: R{final_price:.2f}")
else:
    print(f"No discount applied. Final price: R{final_price:.2f}")