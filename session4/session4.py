# Variable Declaration
item_name = []
purchase_price = []

# Loop to add items
while True:
  # Adding items
  item_name.append(input("Item Name: "))
  purchase_price.append(int(input("Purchase Price (Rp): ")))

  # Ask if user wants to add another item
  while True:
    add_item = input("Do you want to add another item? (y/n): ")
    if add_item.lower() in ("y", "n"):
      break
    else:
      print("Invalid input. Enter 'y' or 'n'.")

  if add_item.lower() == "n":
    break

# Calculate selling price
profit_percentage = 10.0 # Profit percentage (10%)
selling_price = []
for i in range(len(item_name)):
  selling_price.append(purchase_price[i] + (purchase_price[i] * profit_percentage / 100))

# Display results with separators
for i in range(len(item_name)):
  print("="*32)
  print(f"Item Name: {item_name[i]}")
  print(f"Purchase Price: Rp{purchase_price[i]}")
  print(f"Profit Percentage: {profit_percentage}%")
  print(f"Selling Price: Rp{selling_price[i]}")

print("="*32)

