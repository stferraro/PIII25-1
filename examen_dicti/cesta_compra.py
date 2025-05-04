def create_shopping_basket():
    """
    Create a shopping basket with a list of items.
    """
    shopping_basket = {}
    while True:
        item = input("Enter the item name (or 'done' to finish): ")
        if item.lower() == 'done':
            break
        price = float(input(f"Enter the price for {item}: "))
        shopping_basket[item] = price
    return shopping_basket

def personal_data():
    """
    Collect personal data from the user.
    """
    name = input("Enter your name: ")
    first_name = input("Enter your first name: ")
    cedula = input("Enter your ID number: ")
    telephone = input("Enter your telephone number: ")
    return {"name": name, 
            "first_name": first_name,
            "cedula": cedula,
            "telephone": telephone
            }
    
def total_valor(shopping_basket):
    """
    Calculate the total value of the shopping basket.
    """
    total = sum(shopping_basket.values())
    iva = total * 0.16
    total_with_iva = total + iva
    return {
        'SubTotal': total, 
        'IVA': iva, 
        'Total': total_with_iva
        }

def main():
    """
    Main function to run the shopping basket program.
    """
    print("Welcome to the shopping basket program!")
    personal_info = personal_data()
    shopping_basket = create_shopping_basket()
    totals = total_valor(shopping_basket)
    
    print("\n--- Shopping Basket Summary ---")
    print(f"Name: {personal_info.get('name')}")
    print(f"First Name: {personal_info.get('first_name')}")
    print(f"ID Number: {personal_info.get('cedula')}")
    print(f"Telephone: {personal_info.get('telephone')}")
    
    print("\nItems in your shopping basket:")
    for item, price in shopping_basket.items():
        print(f"{item}: ${price:.2f}")
        
    print("\n--- Total Summary ---")
    print(f"Subtotal: ${totals.get('SubTotal'):.2f}")
    print(f"IVA: ${totals.get('IVA'):.2f}")
    print(f"Total: ${totals.get('Total'):.2f}")
    
    
main()