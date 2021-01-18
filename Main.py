import math
import decimal

lista = [11.5, 10.2, 10, 13, 11.1, 13.2, 13.4, 10.4, 11.3, 14.4, 11.2, 12.3, 10.5, 14.2, 15.5, 14.3, 9.3, 12.4, 9, 10,
         14.2, 15.2, 10.3, 14.3, 10, 14.5, 8.2, 14, 13, 12.4, 12.2, 11.5, 15.3, 11.5, 13.5, 12.4, 8.5, 11.3, 12.2, 9.1,
         11.2, 12.5, 14.4, 13, 15.3, 12.5, 9.1, 14.3, 12.1, 9.2]

min = min(lista)
max = max(lista)

mid = decimal.Decimal(str(max)) - decimal.Decimal(str(min))


class Values:
    def __init__(self, section, total, percentage, percStack):
        self.section = section
        self.total = total
        self.percentage = percentage
        self.percStack = percStack

    def __repr__(self):
        return "| % s | % s | % s | % s |" % (self.section, self.total, self.percentage, self.percStack)


def totalCalc(num1, num2):
    cont = 0
    for x in lista:
        if num1 <= x < num2:
            cont += 1
    #print(cont)
    return cont


if mid % 1 != 0:  # if mid!=x.00
    partition = decimal.Decimal(str(mid)) / decimal.Decimal('5') # calculate the partition value always 5

    nextVal = decimal.Decimal(str(min)) + decimal.Decimal(str(partition))  # next analyzable value
    timesAppear = totalCalc(min, nextVal)  # how many numbers are between those values

    value = Values("[" + str(min) + " - " + str(nextVal) + ")", timesAppear, timesAppear / len(lista),
                   timesAppear / len(lista))
    previousPerStack = value.percStack

    valList = [value]

    while nextVal < max:
        timesAppear = totalCalc(nextVal, decimal.Decimal(nextVal)+decimal.Decimal(partition))
        elem = Values("[" + str(nextVal) + " - " + str(nextVal + partition) + ")", timesAppear,
                      timesAppear / len(lista),
                      decimal.Decimal(str(timesAppear / len(lista))) + decimal.Decimal(str(previousPerStack)))

        nextVal = decimal.Decimal(str(nextVal))+decimal.Decimal(str(partition))  # update nextVal
        previousPerStack = elem.percStack  # previous elems Stacked percentage
        valList.append(elem)  # add the element to the array

    for x in valList:
        print(x)

else:
    print('txorizo')
