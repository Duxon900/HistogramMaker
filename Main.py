import decimal
from tkinter import *

root = Tk()
# Set Tkinter Size And Location
root.geometry("500x500")

# Set Tkinter Title
root.title("Histogram Maker")

mainLabel = Label(root)
mainLabel["text"] = "Histogram Maker app"
mainLabel.pack()

inputtxt = Text(root)
inputtxt["height"] = 10
inputtxt["width"] = 25
inputtxt["bg"] = "light pink"
inputtxt.pack()

btnCheck = Button(root)
btnCheck["text"] = "Check"
btnCheck["command"] = lambda: List(inputtxt.get("1.0", "end-1c"))
btnCheck["height"] = 2
btnCheck["width"] = 10
btnCheck.pack()


# Input the list i.e: [1,2,3,4]

class List:
    def __init__(self, list1):
        print(type(list1))
        self.list = list1
        self.mini = min(list1)
        self.maxi = max(list1)
        self.mid = decimal.Decimal(str(max(list1))) - decimal.Decimal(str(min(list1)))


    def calcHistogram(self):
        if self.mid % 1 != 0:  # if mid!=x.00
            partition = decimal.Decimal(str(self.mid)) / decimal.Decimal('5')  # calculate the partition value always 5

            nextVal = decimal.Decimal(str(min)) + decimal.Decimal(str(partition))  # next analyzable value
            timesAppear = self.totalCalc(min, nextVal)  # how many numbers are between those values

            value = Values("[" + str(min) + " - " + str(nextVal) + ")", timesAppear, timesAppear / len(list),
                           timesAppear / len(list))
            previousPerStack = value.percStack

            valList = [value]

            while nextVal < max:
                timesAppear = self.totalCalc(nextVal, decimal.Decimal(nextVal) + decimal.Decimal(partition))
                elem = Values("[" + str(nextVal) + " - " + str(nextVal + partition) + ")", timesAppear,
                              timesAppear / len(list),
                              decimal.Decimal(str(timesAppear / len(list))) + decimal.Decimal(str(previousPerStack)))

                nextVal = decimal.Decimal(str(nextVal)) + decimal.Decimal(str(partition))  # update nextVal
                previousPerStack = elem.percStack  # previous elems Stacked percentage
                valList.append(elem)  # add the element to the array

        for x in valList:
            print(x)

        else:
            print('txorizo')


    def totalCalc(num1, num2):
        count = 0
        for x in list:
            if num1 <= x < num2:
                count += 1
        # print(cont)
        return count


mainloop()


class Values:
    def __init__(self, section, total, percentage, percStack):
        self.section = section
        self.total = total
        self.percentage = percentage
        self.percStack = percStack

    def __repr__(self):
        return "| % s | % s | % s | % s |" % (self.section, self.total, self.percentage, self.percStack)
