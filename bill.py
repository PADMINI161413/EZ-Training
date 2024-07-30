
'''# Define items, quantities, and their prices
item1 = "Item 1"
quantity1 = 2
price_per_item1 = 10.00
total1 = quantity1 * price_per_item1

item2 = "Item 2"
quantity2 = 3
price_per_item2 = 15.50
total2 = quantity2 * price_per_item2

item3 = "Item 3"
quantity3 = 1
price_per_item3 = 5.75
total3 = quantity3 * price_per_item3

# Calculate the total
subtotal = total1 + total2 + total3

# Print the bill
print("===== Your Bill =====")
print(f"{item1} x{quantity1}: ${price_per_item1:.2f} each = ${total1:.2f}")
print(f"{item2} x{quantity2}: ${price_per_item2:.2f} each = ${total2:.2f}")
print(f"{item3} x{quantity3}: ${price_per_item3:.2f} each = ${total3:.2f}")
print("======================")
print(f"Subtotal: ${subtotal:.2f}")
tax_rate = 0.08  # 8% tax rate
tax_amount = subtotal * tax_rate
print(f"Tax ({tax_rate * 100}%): ${tax_amount:.2f}")
total = subtotal + tax_amount
print("======================")
print(f"Total: ${total:.2f}")
print("======================")
print("Thank you for your purchase!")
'''
# Define items, quantities, and their prices
item1 = "Item 1"
quantity1 = 2
price_per_item1 = 10.00
total1 = quantity1 * price_per_item1

item2 = "Item 2"
quantity2 = 3
price_per_item2 = 15.50
total2 = quantity2 * price_per_item2

item3 = "Item 3"
quantity3 = 1
price_per_item3 = 5.75
total3 = quantity3 * price_per_item3

# Calculate the total
subtotal = total1 + total2 + total3

# Print the bill
print("===== Your Bill =====")
print(f"{item1} x{quantity1}: ${price_per_item1:.2f} each = ${total1:.2f}")
print(f"{item2} x{quantity2}: ${price_per_item2:.2f} each = ${total2:.2f}")
print(f"{item3} x{quantity3}: ${price_per_item3:.2f} each = ${total3:.2f}")
print("======================")
print(f"Subtotal:      ${subtotal:.2f}")
tax_rate = 0.08  # 8% tax rate
tax_amount = subtotal * tax_rate
print(f"Tax ({tax_rate * 100}%):   ${tax_amount:.2f}")
total = subtotal + tax_amount
print("======================")
print(f"Total:         ${total:.2f}")
print("======================")
print("Thank you for your purchase!")
