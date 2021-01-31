import decimal
from tkinter import *


class List:
    def __init__(self, strList):
        list1 = strList.split(',')
        res = list(map(float, list1))
        print(res)
        self.list = res
        self.mini = min(res)
        self.maxi = max(res)
        self.mid = decimal.Decimal(str(max(res))) - decimal.Decimal(str(min(res)))

    def calcHistogram(self):
        if self.mid % 1 != 0:  # if mid!=x.00
            partition = decimal.Decimal(str(self.mid)) / decimal.Decimal('5')  # calculate the partition value always 5

            nextVal = decimal.Decimal(str(self.mini)) + decimal.Decimal(str(partition))  # next analyzable value
            timesAppear = List.totalCalc(self, self.mini, nextVal)  # how many numbers are between those values

            value = Values("[" + str(self.mini) + " - " + str(nextVal) + ")", timesAppear, timesAppear / len(self.list),
                           timesAppear / len(self.list))
            previousPerStack = value.percStack

            valList = [value]

            while nextVal < max:
                timesAppear = self.totalCalc(nextVal, decimal.Decimal(nextVal) + decimal.Decimal(partition))
                elem = Values("[" + str(nextVal) + " - " + str(nextVal + partition) + ")", timesAppear,
                              timesAppear / len(self.list),
                              decimal.Decimal(str(timesAppear / len(self.list))) + decimal.Decimal(str(previousPerStack)))

                nextVal = decimal.Decimal(str(nextVal)) + decimal.Decimal(str(partition))  # update nextVal
                previousPerStack = elem.percStack  # previous elems Stacked percentage
                valList.append(elem)  # add the element to the array

            for x in valList:
                print(x)

        else:
            print('txorizo')

    def totalCalc(self, num1, num2):
        #how many numbers are there between the given values
        count = 0
        for x in self.list:
            if num1 <= x < num2:
                count += 1
        # print(cont)
        return count


class Values:
    def __init__(self, section, total, percentage, percStack):
        self.section = section
        self.total = total
        self.percentage = percentage
        self.percStack = percStack

    def __repr__(self):
        return "| % s | % s | % s | % s |" % (self.section, self.total, self.percentage, self.percStack)


def checkPressed():
    inputList = List(inputtxt.get("1.0", "end-1c"))
    List.calcHistogram(inputList)


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
btnCheck["command"] = lambda :checkPressed()
btnCheck["height"] = 2
btnCheck["width"] = 10
btnCheck.pack()

mainloop()

# Input the list i.e: [1,2,3,4]
