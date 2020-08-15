denominations_list = [1, 2, 5, 10, 20, 50, 100]
# 100p is £1


def return_change(change, denominations):
    # makes a list size of length denominations filled with 0
    to_give_back = [0] * len(denominations)

    # goes backwards through denominations list
    # and also keeps track of the counter, pos.
    for pos, coin in reversed(list(enumerate(denominations))):
        # while we can still use coin, use it until we can't
        while coin <= change:
            print(f"position is {pos}")
            print(f"coin is {coin}")
            change = change - coin
            to_give_back[pos] += 1
    return to_give_back


print(return_change(4, denominations_list))
# returns [0, 0, 0, 1, 1, 0, 0]
# 1x 10p, 1x 20p
