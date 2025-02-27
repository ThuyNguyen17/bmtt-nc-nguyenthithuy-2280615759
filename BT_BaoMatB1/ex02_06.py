input_str = input("Nhap X,Y: ")
dimensions = [int(x) for x in input_str.split(',')]
rowNum = dimensions[0]
colNum = dimensions[1]
# multiList = []
# for row in range(rowNum):
#     multiList.append([0] * colNum)
multiList = [[0 for col in range(colNum)] for row in range(rowNum)]
for row in range(rowNum):
    for col in range(colNum):
        multiList[row][col]= row*col
print(multiList)
