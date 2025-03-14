

teasCost = {
    'Earl Grey': 0.58,
    'Green Tea': 0.58,
    'Lemon Ginger': 0.58,
    'Mint': 0.58,
    'Dandilion': 0.58,
    'English Breakfast': 0.58,
    'English Afternoon': 0.58,
    'Hibiscus': 0.58,
    'Peppermint': 0.58,
    'Chai': 0.58

}

# initialize the variable

avg_price = 0

cost_per_unit = 0

total_profit = 0


# This is how you get the total of the entire list
# print(len(teasCost))

while avg_price > -1:
    for item in teasCost:
        print('{} | ${}'.format(item, teasCost[item], end=' '))
    print()

    # Takes 2 inputs for Avg price and cost per unit
    avg_price = float(input('Enter the average price per Unit: '))
    cost_per_unit = float(input('Enter the cost per unit: '))

    # Calculates Total Profit
    total_profit = avg_price - cost_per_unit

    # Calculates Gross Margin
    gross_margin = 0
    gross_margin = (avg_price - cost_per_unit) * 0.1 * 100
    high_risk = 30.0
    
    if gross_margin < high_risk:
        print()
        print(" ALERT!! This product is very high risk" + " " + '\n' "SUGGESTION: Find an effective way to produce this item.")
    print()
    print('Gross Margin per individual unit is' + ' ' + '{:.2f}%'.format(gross_margin))
    print()
    print('Total product profit is', '${:.2f}'.format(total_profit),'per unit' )
    print()
    # cost_per_unit = cost_per_unit + 1

# When a desire to change exists

# teasCost = {}
# teasCost['Earl Grey'] = 0.65
# teasCost['Mint'] = 0.67
