'''

    creation Date and time: 20th Dec 2017, 9:00 PM
    @Author : Venkanna Karne

'''

import faker
import xlwt
import time

data = faker.Faker()

wk = xlwt.Workbook()
ws = wk.add_sheet("Sheet1")


def displayWelcomeMessage():
    print("*****************************************************************************\n\n")
    print("              Welcome to Test Data Generation By Venkanna Karne              \n\n")
    print("*****************************************************************************\n\n")


def enterNumberOfRecords():
    nor = input("Enter No of Records to Generate: ")
    return nor


def selectGenerateOptions():
    print("Please Data which you want to Generate\n\n")
    print("Enter 1 for Name")
    print("Enter 2 for email")
    print("Enter 3 for Phone Number")
    print("Enter 4 for Address\n")
    opt = input("Please Enter your Choice (use commas in case of multiple options:")
    return opt


def generateData(rec, data1):
    r = int(rec)
    li = data1.split(",")
    for i in range(0, r):
        cnt = 0
        for j in (li):
            if (j == "1"):
                ws.write(i, cnt, data.name())
                cnt = cnt + 1
            elif (j == "2"):
                ws.write(i, cnt, data.email())
                cnt = cnt + 1
            elif (j == "3"):
                ws.write(i, cnt, data.phone_number())
                cnt = cnt + 1
            elif (j == "4"):
                ws.write(i, cnt, data.address())
                cnt = cnt + 1
    fileName = "DataFile" + str(round(time.time()*1000))+".xls"
    saveDirectory = "/home/vkarne/Documents/testdata/"
    destinationFile = saveDirectory+fileName

    wk.save(destinationFile)