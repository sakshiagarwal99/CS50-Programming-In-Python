def main():
    denominations = [5, 10, 25]
    total_paid = 0
    amount_due = 50

    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        coin_inserted = int(input("Insert Coin: "))

        if coin_inserted not in denominations:
            continue

        total_paid += coin_inserted
        amount_due = 50 - total_paid

    change_owed = abs(amount_due)
    print(f"Change Owed: {change_owed}")

main()
