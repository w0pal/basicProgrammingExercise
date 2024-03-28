# Import library time
import time

# Cosmetic Data
cosmetic_data = {
    "Names": ["Lipstick", "Powder", "Mascara", "Eyeshadow"],
    "Purchase Price": [10000, 15000, 20000, 25000],
    "Number Purchased": [0, 0, 0, 0],
}

# Display Cosmetic List
print("List of Cosmetics:")
for i in range(len(cosmetic_data["Names"])):
    print(f"{i + 1}. {cosmetic_data['Names'][i]} - Rp{cosmetic_data['Purchase Price'][i]}")

# Perform Transaction
while True:
    chosen_item = int(input("Choose item number (0 to exit): "))
    if chosen_item == 0:
        break
    elif chosen_item > len(cosmetic_data["Names"]):
        print("Invalid choice!")
        continue

    purchase_quantity = int(input("Enter purchase quantity: "))

    # Calculate Selling Price and Profit
    selling_price = int(cosmetic_data["Purchase Price"][chosen_item - 1] * 1.1)
    profit = selling_price - cosmetic_data["Purchase Price"][chosen_item - 1]

    # Store Transaction Results
    cosmetic_data["Number Purchased"][chosen_item - 1] += purchase_quantity

    # Display Transaction Results
    while True:
        another_item = input("Do you want to add another item? (y or n): ")
        if another_item in ("y", "n"):
            break
        else:
            print("Invalid choice, select 'y' or 'n'.")

    if another_item == "n":
        for i in range(len(cosmetic_data["Names"])):
            if cosmetic_data["Number Purchased"][i] > 0:
                print("="*32)
                print(f"Item Name: {cosmetic_data['Names'][i]}")
                print(f"Selling Price: Rp{int(cosmetic_data['Purchase Price'][i] * 1.1)}")
                print(f"Number Purchased: {cosmetic_data['Number Purchased'][i]}")

        # Display Total Transaction and Profit
        total_transaction = 0
        total_profit = 0
        for i in range(len(cosmetic_data["Names"])):
            total_transaction += int(cosmetic_data["Purchase Price"][i] * 1.1) * cosmetic_data["Number Purchased"][i]
            total_profit += int((cosmetic_data["Purchase Price"][i] * 0.1) * cosmetic_data["Number Purchased"][i])
        print(f"\nTotal Transaction: Rp{total_transaction}")
        print(f"Total Profit: Rp{total_profit}")
        print("="*32)

        # Tampilkan hitungan mundur 5 detik
        for i in range(5, 0, -1):
            print(f"Program will close in {i} seconds...")
            time.sleep(1)

        break