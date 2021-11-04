def maximize_profits(stockvalues):

    dobuy = [1]*len(stockvalues)  # 1 for buy, 0 for sell
    prof = 0
    m = 0
    for i in range(len(stockvalues)-1, -1, -1):  # reverse loop
        ai = stockvalues[i]  # shorthand name
        if m <= ai:
            dobuy[i] = 0
            m = ai
        prof += m-ai
    return prof


print(maximize_profits([5, 3, 2]))
