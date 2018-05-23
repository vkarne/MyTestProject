import faker
import xlwt
import time

data = faker.Faker()

wk = xlwt.Workbook()
ws = wk.add_sheet("Sheet1")

for i in range(0, 50):
    ws.write(i, 0, data.name())
    ws.write(i, 1, data.email())
    ws.write(i, 2, data.phone_number())
    ws.write(i, 3, data.address())

fileName = "DataFile" + str(round(time.time() * 1000)) + ".xls"
saveDirectory = "/home/vkarne/Documents/testdata/"
destinationFile = saveDirectory + fileName

wk.save(destinationFile)