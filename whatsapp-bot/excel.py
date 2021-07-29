from openpyxl import load_workbook

def load_file(fname):
    workbook = load_workbook(filename=fname)

    sheet = workbook.active

    currentval = sheet["A1"].value
    count = 1
    list1=[]
    while(currentval != None):
        list1.append(currentval)
        count += 1
        string = "A" + str(count)
        currentval = sheet[string].value
    return list1

