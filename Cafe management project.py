import json

def get_rating(reviews):
    return '⭐' * (sum(reviews) // len(reviews) if reviews else 5)

# Load the menu from a JSON file
with open('menu.json', 'r') as f:
    data = json.load(f)

items = data.get('items', [])

while True:
    print('-' * 50)
    print('DIAMOND 💎 CAFE')
    print('-' * 50)
    print('1. Show Menu')
    print('2. Order Items')
    print('3. Add Your Feedback')
    print('4. Exit')
    print('-' * 50)
    choice = int(input())

    if choice == 1:
        print('ID\tName\t\tPrice\tRating')
        print('-' * 50)
        for item in items:
            print(f'{item["id"]}\t{item["name"]}\t{item["price"]}\t{get_rating(item.get("reviews", []))}')
        print('-' * 50)

    elif choice == 2:
        order_food = list(map(int, input("Place Your Order (comma separated item IDs): ").split(',')))
        print('-' * 50)
        print('ID\tName\t\tPrice')
        print('-' * 50)
        total_bill = 0
        for order_id in order_food:
            for item in items:
                if item['id'] == order_id:
                    print(f'{item["id"]}\t{item["name"]}\t{item["price"]}')
                    total_bill += int(item.get('price', 0))
                    break
        print('-' * 50)
        print(f'\t Total Amount: {total_bill}')
        print('-' * 50)

    elif choice == 3:
        item_no = int(input("Enter the item No.: "))
        rating = int(input("Give your rating (1-5): "))
        for item in items:
            if item['id'] == item_no:
                item.setdefault('reviews', []).append(rating)
                break
        print('Thank you for your rating!')

    elif choice == 4:
        print('🙂 Visit Again 🙂')
        break

    else:
        print('Invalid choice. Please try again.')
