

def read_txt_file():
    fr = open("/home/vkarne/Documents/testdata/TestReadDataFile.txt", 'r')
    print(fr.read())
#    print(fr.readline())


def write_txt_file():
    fw = open("/home/vkarne/Documents/testdata/TestWriteDataFile.txt", 'a+')
    fw.write("\nTest Writing data Text into file")
    fw.close()


read_txt_file()
write_txt_file()