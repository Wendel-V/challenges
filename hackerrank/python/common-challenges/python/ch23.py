b = 5
keyboards = [4]
drives = [5]

def getMoneySpent(keyboards, drives, b):
    orders = []
    for keyboard in keyboards:
        for drive in drives:
            buy = drive + keyboard
            if buy <= b:
                orders.append(buy)
    if orders:
        return max(orders)
    else:
        return -1

print(getMoneySpent(keyboards, drives, b))