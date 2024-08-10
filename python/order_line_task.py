order_lines = [
    {'description': 'SET-KASTRON SPLIT 2 TON', 'quantity': 2, 'unit_price': 180, 'tax_percentage': 0.1, 'subtotal': 360, 'total': 396},
    {'description': 'SET-KASTRON AQUACHILL 1.5 TON', 'quantity': 1, 'unit_price': 200, 'tax_percentage': 0.1, 'subtotal': 200, 'total': 220},
    {'description': 'SAMSUNG 43" CU-7000', 'quantity': 1, 'unit_price': 119, 'tax_percentage': 0.1, 'subtotal': 119, 'total': 130.9},
]

# Discounts
discounts = [10, 5, 1]

# Loop to apply discounts through each order
for i, line in enumerate(order_lines):
    
    # Add the discount to the dictionary
    discount = discounts[i]
    line['discount'] = discount
    
    # Recalculate the subtotal after discount
    line['subtotal'] -= discount
    
    # Recalculate the total after applying the tax to the new subtotal
    line['total'] = line['subtotal'] * (1 + line['tax_percentage'])

# Display the updated order lines
for line in order_lines:
    print(line)