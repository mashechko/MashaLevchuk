tax = ''
comb = ['TAX', 'TBX', 'TEX']
taxi_in = ['9',
            '7 TAX 9215',
            '6 TEX 9125',
            'a236ye 73',
            '21-14 BOT',
            '3412 0321 GR',
            '1 TBX 0021-7',
            '2-TBX 0001',
            '1 TBX 0000',
            '1 TBX 0020']
taxi_out = []
for car in taxi_in:
    if len(car) == 10:
        try:
            tax = car.split()
            if tax[0].isdigit() and tax[2].isdigit() and int(tax[2]) > 0:
                if 1 <= int(tax[0]) <= 6 and tax[1] in comb[:2]:
                    taxi_out.append(car)
                elif int(tax[0]) == 7 and tax[1] in comb:
                    taxi_out.append(car)
        except IndexError:
            continue

print(taxi_out)