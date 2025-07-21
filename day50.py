# f=open('myfile.txt','w')
# lines = ['Piyush Mandloi \n', 'Neeraj Makashree \n', 'Ayush Rathod \n']
# f.writelines(lines)
# f.close()

# f=open('myfile.txt','w')
# lines = ['A1 Mandloi \n', 'A2 Makashree \n', 'A3 Rathod \n']
# for line in lines:
#     f.write(line)
# f.close()

f=open('myfile.txt', 'r')
while True:
    line=f.readlines()
    print(line)
    if not line:
        break