# Product details
products = ["Product A", "Product B", "Product C"]
prices = [20, 40, 50]

# Discount rules
flat10_discount = 10
bulk5_discount = 5
bulk10_discount = 10
tiered50_discount = 50
tiered_discount_threshold = 30
tiered_discount_quantity = 15

# Fees
gift_wrap_fee = 1
shipping_fee_per_package = 5
items_per_package = 10

quantities = []
gift_wrap_flags = []

# Get quantity and gift wrap information for each product
for product in products:
    quantity = int(input(f"Enter the quantity of {product}: "))
    quantities.append(quantity)
    
    gift_wrap = input(f"Wrap {product} as a gift? (yes/no): ").lower()
    gift_wrap_flags.append(gift_wrap == "yes")

# Calculate the subtotal
subtotal = sum(prices[i] * quantities[i] for i in range(len(products)))
# Apply the most beneficial discount
discount_amount = 0
discount_name = "No discount applied"

if subtotal > 200:
    discount_amount = flat10_discount
    discount_name = "flat_10_discount"
elif any(quantity > 10 for quantity in quantities):
    discount_amount = sum(prices[i] * quantities[i] * bulk5_discount / 100 for i in range(len(products)) if quantities[i] > 10)
    discount_name = "bulk_5_discount"
elif sum(quantities) > 20:
    discount_amount = bulk10_discount
    discount_name = "bulk_10_discount"
elif sum(quantities) > tiered_discount_threshold and any(quantity > tiered_discount_quantity for quantity in quantities):
    discount_amount = sum((prices[i] * (quantities[i] - tiered_discount_quantity) * tiered50_discount / 100) for i in range(len(products)) if quantities[i] > tiered_discount_quantity)
    discount_name = "tiered_50_discount"
# Calculate fees
gift_wrap_fee_total = sum(quantity * gift_wrap_fee for quantity, flag in zip(quantities, gift_wrap_flags) if flag)
shipping_fee_total = (sum(quantities) // items_per_package) * shipping_fee_per_package
if sum(quantities) % items_per_package != 0:
    shipping_fee_total += shipping_fee_per_package

# Calculate the total
total = subtotal - discount_amount + gift_wrap_fee_total + shipping_fee_total
# Output the details
print("\nProduct Details:")
for i in range(len(products)):
    product_amount = prices[i] * quantities[i]
    print(f"{products[i]} - Quantity: {quantities[i]}, Total Amount: ${product_amount}")

print("\nSubtotal: ${:.2f}".format(subtotal))
print("Discount Applied: {} - Amount: ${:.2f}".format(discount_name, discount_amount))
print("Gift Wrap Fee: ${:.2f}".format(gift_wrap_fee_total))
print("Shipping Fee: ${:.2f}".format(shipping_fee_total))
print("Total: ${:.2f}".format(total))
