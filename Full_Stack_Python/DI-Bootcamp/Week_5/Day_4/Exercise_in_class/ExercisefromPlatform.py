# f = open('namelist.txt', 'r')

# print(f.read())
# f.close()


lineNo = [4]
result = []
i = 0

# f = open('namelist.txt', 'r')
# while True:
#     lineNo = f.readline()[4]
#     if i in lineNo:
#         result.append(lineNo.strip())
#         if i > lineNo[-1]:
#             break
#         i = i +1

# print(result)
# f.close()

# def readlines(i)
# f = open('namelist.txt', 'r')
# for number, line in enumerate(f):
#     if number == i:



# print(f.readline()[5])
# f.close()

# lineNo = [4]
result = []
i = 0

def get_lines(fp, line_numbers):
    return (x for i, x in enumerate(fp) if i in line_numbers)

f = open('namelist.txt', 'r')
lines = get_lines(f, [5])
for line in lines:
        print(line.strip())
f.close()

