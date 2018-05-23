
import xlrd
import xlwt


def read_data_from_excel():
    wkr = xlrd.open_workbook('/home/vkarne/Documents/testdata/TestReadExcelFile.xls')
    print(wkr.nsheets)
    wsr = wkr.sheet_by_index(1)
    print(wsr.nrows)
    for i in range(0,2):
        clr = wsr.cell(i,1)
        print(clr)


def write_data_to_excel():
    wkw = xlwt.Workbook()
    wsw = wkw.add_sheet("Sheet1")
    wsw.write(0, 0, "A1 Cell data in Sheet1")
    wsw.write(0, 1, "B1 Cell data in Sheet1")
    wsw.write(1, 0, "A2 Cell data in Sheet1")
    wsw.write(1, 1, "B2 Cell data in Sheet1")
    wkw.save('/home/vkarne/Documents/testdata/TestWriteExcelFile.xls')


read_data_from_excel()
write_data_to_excel()