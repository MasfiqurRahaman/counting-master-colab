import os

for i in range(0,5):
    os.system("mkdir " + "A_" + str(i))
    os.system("mkdir " + "A_" + str(i) + "_testing")
    os.system("mkdir " + "B_" + str(i))
    os.system("mkdir " + "B_" + str(i) + "_testing")
