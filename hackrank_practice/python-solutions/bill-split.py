def bonAppetit(bill, k, b):
    ana_sum = 0

    for i in range(len(bill)):
        if i != k:
            ana_sum += bill[i]
    ana_pay = ana_sum // 2

    if ana_pay == b:
        print("Bon Appetit")
    else:
        print(b - ana_pay)


# calculates the split of the bill
# k is the index of the item that Anna did not eat
# b is the amount that Anna paid
# we need to see if she was overcharged or not
