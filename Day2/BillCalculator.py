if __name__ == "__main__":
    total_bill = input("Total Bill ($): ")
    tip_percent = input("Tip Percentage (e.g. 10, 12, 15): ")
    people = input("Number of People: ")

    total_bill = float(total_bill)
    tip_percent = float(tip_percent)
    people = int(people)

    tip_amount = (tip_percent / 100) * total_bill
    total_with_tip = total_bill + tip_amount
    per_person = round(total_with_tip / people, 2)

    print(f"Each Person Should Pay: ${per_person}")
