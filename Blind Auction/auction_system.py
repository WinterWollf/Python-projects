def auction(bidders_log):
    max_value = 0
    higher_bidder = ""

    for key in bidders_log:
        if int(bidders_log[key]) > max_value:
            higher_bidder = key
            max_value = int(bidders_log[key])

    print(f"The winner is {higher_bidder} with a bid of ${bidders_log[higher_bidder]}")