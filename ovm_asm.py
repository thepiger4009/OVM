"""
OVM - Owl Virtual Machine Assembler
Development Build: 72123r1

Copyright (c) 2022-2023
"""

from sys import argv
from linecache import getline

input = argv[1]
output = open(argv[2],"w+")
LinePosition = 1
VirtualBytes = 0
LastAddress = 0

labelNameList = [0]*1000
labelAddressList = [0]*1000
labelCount = 0

variableNameList = [0]*1000
variableAddressList = [0]*1000
variableCount=0

def getVarAddr(varName):
    for x in range(1000):
        if varName == variableNameList[x]:
            break
    return variableAddressList[x]

def getLabelAddress(labelName):
    for x in range(1000):
        if labelName == labelNameList[x]:
            break
    return labelAddressList[x]

while 1: # Pre-Interpret
    Line = getline(input,LinePosition).rstrip("\n")
    SplitLine = Line.split()

    match SplitLine[0]:
        case ".lt": # Label This
            if "$" in SplitLine[2]:
                temp_address = SplitLine[2].split("$"[0])
                variableNameList[variableCount] = SplitLine[1]
                variableAddressList[variableCount] = temp_address[1]
                variableCount+=1
            if SplitLine[2] == "*":
                distance = int(LastAddress) + int(VirtualBytes)
                variableNameList[variableCount] = SplitLine[1]
                variableAddressList[variableCount] = distance
                variableCount+=1
                VirtualBytes+=1

        case "*=":
            aon = SplitLine[1]
            if "@" in aon:
                try:
                    n = aon.split("@"[0])
                except:
                    next
                distance = int(LastAddress) + int(VirtualBytes)
                labelNameList[labelCount] = n[1]
                labelAddressList[labelCount] = distance
                labelCount+=1
                output.write("ADDR\n"+str(distance)+"\n")
                print("[ovm_asm]: Label",n[1]," - Addr:",distance)
            else:
                temp_address = aon.split("$"[0])[1]
                LastAddress = temp_address
                output.write("ADDR\n"+str(temp_address)+"\n")
        case "LD":
            VirtualBytes+=3
        case "TRF":
            VirtualBytes+=3
        case "ADD":
            VirtualBytes+=3
        case "SUB":
            VirtualBytes+=3
        case "CMP":
            VirtualBytes+=3
        case "CPA":
            VirtualBytes+=3
        case "INC":
            VirtualBytes+=2
        case "DEC":
            VirtualBytes+=2
        case "ST":
            VirtualBytes+=3
        case "JMP":
            VirtualBytes+=2
        case "JOE":
            VirtualBytes+=2
        case "JNE":
            VirtualBytes+=2
        case "JSP":
            VirtualBytes+=2
        case "RTP":
            VirtualBytes+=1
        case "DSP":
            match SplitLine[1]:
                case "V":
                    VirtualBytes+=3
                case "v":
                    VirtualBytes+=3
                case "A":
                    VirtualBytes+=3
                case "a":
                    VirtualBytes+=3
                case "nl":
                    VirtualBytes+=2
                case "NL":
                    VirtualBytes+=2
                case "sp":
                    VirtualBytes+=2
                case "SP":
                    VirtualBytes+=2
                case "bp":
                    VirtualBytes+=2
                case "BP":
                    VirtualBytes+=2
        case "PSH":
            VirtualBytes+=2
        case "PUL":
            VirtualBytes+=2
        case "ld":
            VirtualBytes+=3
        case "trf":
            VirtualBytes+=3
        case "add":
            VirtualBytes+=3
        case "sub":
            VirtualBytes+=3
        case "cmp":
            VirtualBytes+=3
        case "cpa":
            VirtualBytes+=3
        case "inc":
            VirtualBytes+=3
        case "dec":
            VirtualBytes+=3
        case "st":
            VirtualBytes+=3
        case "jmp":
            VirtualBytes+=2
        case "joe":
            VirtualBytes+=2
        case "jne":
            VirtualBytes+=2
        case "jsp":
            VirtualBytes+=2
        case "rtp":
            VirtualBytes+=2
        case "dsp":
            match SplitLine[1]:
                case "V":
                    VirtualBytes+=3
                case "v":
                    VirtualBytes+=3
                case "A":
                    VirtualBytes+=3
                case "a":
                    VirtualBytes+=3
                case "l":
                    VirtualBytes+=2
                case "L":
                    VirtualBytes+=2
                case "s":
                    VirtualBytes+=2
                case "S":
                    VirtualBytes+=2
                case "b":
                    VirtualBytes+=2
                case "B":
                    VirtualBytes+=2
        case "psh":
            VirtualBytes+=2
        case "pul":
            VirtualBytes+=2



        case "break":
            break
    LinePosition+=1
   
    
LinePosition = 1


while 1: # Main-Interpret
    Line = getline(input,LinePosition).rstrip("\n")
    SplitLine = Line.split()

    if SplitLine[0] == "LD" or SplitLine[0] == "ld":
        SplitArg = SplitLine[1].split(","[0])
        if "#" in SplitArg[0]:
            Num = SplitArg[0].split("#"[0])[1]
            match SplitArg[1]:
                case "x":
                    output.write("100\n1\n"+str(Num)+"\n")
                case "X":
                    output.write("100\n1\n"+str(Num)+"\n")
                case "y":
                    output.write("100\n2\n"+str(Num)+"\n")
                case "Y":
                    output.write("100\n2\n"+str(Num)+"\n")
                case "t":
                    output.write("100\n3\n"+str(Num)+"\n")
                case "T":
                    output.write("100\n3\n"+str(Num)+"\n")
                case "p":
                    output.write("100\n4\n"+str(Num)+"\n")
                case "P":
                    output.write("100\n4\n"+str(Num)+"\n")
                case "u":
                    output.write("100\n5\n"+str(Num)+"\n")
                case "U":
                    output.write("100\n5\n"+str(Num)+"\n")
        if "$" in SplitArg[0]:
            Address = SplitArg[0].split("$"[0])[1]
            match SplitArg[1]:
                case "x":
                    output.write("101\n1\n"+str(Address)+"\n")
                case "X":
                    output.write("101\n1\n"+StopIteration(Address)+"\n")
                case "y":
                    output.write("101\n2\n"+str(Address)+"\n")
                case "Y":
                    output.write("101\n2\n"+str(Address)+"\n")
                case "t":
                    output.write("101\n3\n"+str(Address)+"\n")
                case "T":
                    output.write("101\n3\n"+str(Address)+"\n")
                case "p":
                    output.write("101\n4\n"+str(Address)+"\n")
                case "P":
                    output.write("101\n4\n"+str(Address)+"\n")
                case "u":
                    output.write("101\n5\n"+str(Address)+"\n")
                case "U":
                    output.write("101\n5\n+"+str(Address)+"\n")
        if "%" in SplitArg[0]:
            Address = SplitArg[0].split("%"[0])[1]
            if "u" in Address:
                Register = 1
                Address = Address.split("u"[0])[1]
            if "p" in Address:
                Register = 2
                Address = Address.split("p"[0])[1]
            if "U" in Address:
                Register = 1
                Address = Address.split("U"[0])[1]
            if "P" in Address:
                Register = 2
                Address = Address.split("P"[0])[1]
            match Register:
                case 1: # P
                    match SplitArg[1]:
                        case "x":
                            output.write("102\n1\n"+str(Address)+"\n")
                        case "y":
                            output.write("102\n2\n"+str(Address)+"\n")
                        case "t":
                            output.write("102\n3\n"+str(Address)+"\n")
                        case "p":
                            output.write("102\n4\n"+str(Address)+"\n")
                        case "u":
                            output.write("102\n5\n"+str(Address)+"\n")
                        case "X":
                            output.write("102\n1\n"+str(Address)+"\n")
                        case "Y":
                            output.write("102\n2\n"+str(Address)+"\n")
                        case "T":
                            output.write("102\n3\n"+str(Address)+"\n")
                        case "P":
                            output.write("102\n4\n"+str(Address)+"\n")
                        case "U":
                            output.write("102\n5\n"+str(Address)+"\n")
                case 2: # U
                    match SplitArg[1]:
                        case "x":
                            output.write("103\n1\n"+str(Address)+"\n")
                        case "y":
                            output.write("103\n2\n"+str(Address)+"\n")
                        case "t":
                            output.write("103\n3\n"+str(Address)+"\n")
                        case "p":
                            output.write("103\n4\n"+str(Address)+"\n")
                        case "u":
                            output.write("103\n5\n"+str(Address)+"\n")
                        case "X":
                            output.write("103\n1\n"+str(Address)+"\n")
                        case "Y":
                            output.write("103\n2\n"+str(Address)+"\n")
                        case "T":
                            output.write("103\n3\n"+str(Address)+"\n")
                        case "P":
                            output.write("103\n4\n"+str(Address)+"\n")
                        case "U":
                            output.write("103\n5\n"+str(Address)+"\n")
    if SplitLine[0] == "TRF" or SplitLine[0] == "trf":
        SplitArg = SplitLine[1].split(","[0])
        r1 = SplitArg[0]
        r2 = SplitArg[1]
        match r1:
            case "x":
                match r2:
                    case "x":
                        output.write("104\n1\n1\n")
                    case "y":
                        output.write("104\n2\n1\n")
                    case "t":
                        output.write("104\n3\n1\n")
                    case "p":
                        output.write("104\n4\n1\n")
                    case "u":
                        output.write("104\n5\n1\n")
                    case "X":
                        output.write("104\n1\n1\n")
                    case "Y":
                        output.write("104\n2\n1\n")
                    case "T":
                        output.write("104\n3\n1\n")
                    case "P":
                        output.write("104\n4\n1\n")
                    case "U":
                        output.write("104\n5\n1\n")
            case "y":
                match r2:
                    case "x":
                        output.write("104\n1\n2\n")
                    case "y":
                        output.write("104\n2\n2\n")
                    case "t":
                        output.write("104\n3\n2\n")
                    case "p":
                        output.write("104\n4\n2\n")
                    case "u":
                        output.write("104\n5\n2\n")
                    case "X":
                        output.write("104\n1\n2\n")
                    case "Y":
                        output.write("104\n2\n2\n")
                    case "T":
                        output.write("104\n3\n2\n")
                    case "P":
                        output.write("104\n4\n2\n")
                    case "U":
                        output.write("104\n5\n2\n")
            case "t":
                match r2:
                    case "x":
                        output.write("104\n1\n3\n")
                    case "y":
                        output.write("104\n2\n3\n")
                    case "t":
                        output.write("104\n3\n3\n")
                    case "p":
                        output.write("104\n4\n3\n")
                    case "u":
                        output.write("104\n5\n3\n")
                    case "X":
                        output.write("104\n1\n3\n")
                    case "Y":
                        output.write("104\n2\n3\n")
                    case "T":
                        output.write("104\n3\n3\n")
                    case "P":
                        output.write("104\n4\n3\n")
                    case "U":
                        output.write("104\n5\n3\n")
            case "p":
                match r2:
                    case "x":
                        output.write("104\n1\n4\n")
                    case "y":
                        output.write("104\n2\n4\n")
                    case "t":
                        output.write("104\n3\n4\n")
                    case "p":
                        output.write("104\n4\n4\n")
                    case "u":
                        output.write("104\n5\n4\n")
                    case "X":
                        output.write("104\n1\n4\n")
                    case "Y":
                        output.write("104\n2\n4\n")
                    case "T":
                        output.write("104\n3\n4\n")
                    case "P":
                        output.write("104\n4\n4\n")
                    case "U":
                        output.write("104\n5\n4\n")
            case "u":
                match r2:
                    case "x":
                        output.write("104\n1\n5\n")
                    case "y":
                        output.write("104\n2\n5\n")
                    case "t":
                        output.write("104\n3\n5\n")
                    case "p":
                        output.write("104\n4\n5\n")
                    case "u":
                        output.write("104\n5\n5\n")
                    case "X":
                        output.write("104\n1\n5\n")
                    case "Y":
                        output.write("104\n2\n5\n")
                    case "T":
                        output.write("104\n3\n5\n")
                    case "P":
                        output.write("104\n4\n5\n")
                    case "U":
                        output.write("104\n5\n5\n")

            case "X":
                match r2:
                    case "x":
                        output.write("104\n1\n1\n")
                    case "y":
                        output.write("104\n2\n1\n")
                    case "t":
                        output.write("104\n3\n1\n")
                    case "p":
                        output.write("104\n4\n1\n")
                    case "u":
                        output.write("104\n5\n1\n")
                    case "X":
                        output.write("104\n1\n1\n")
                    case "Y":
                        output.write("104\n2\n1\n")
                    case "T":
                        output.write("104\n3\n1\n")
                    case "P":
                        output.write("104\n4\n1\n")
                    case "U":
                        output.write("104\n5\n1\n")
            case "Y":
                match r2:
                    case "x":
                        output.write("104\n1\n2\n")
                    case "y":
                        output.write("104\n2\n2\n")
                    case "t":
                        output.write("104\n3\n2\n")
                    case "p":
                        output.write("104\n4\n2\n")
                    case "u":
                        output.write("104\n5\n2\n")
                    case "X":
                        output.write("104\n1\n2\n")
                    case "Y":
                        output.write("104\n2\n2\n")
                    case "T":
                        output.write("104\n3\n2\n")
                    case "P":
                        output.write("104\n4\n2\n")
                    case "U":
                        output.write("104\n5\n2\n")
            case "T":
                match r2:
                    case "x":
                        output.write("104\n1\n3\n")
                    case "y":
                        output.write("104\n2\n3\n")
                    case "t":
                        output.write("104\n3\n3\n")
                    case "p":
                        output.write("104\n4\n3\n")
                    case "u":
                        output.write("104\n5\n3\n")
                    case "X":
                        output.write("104\n1\n3\n")
                    case "Y":
                        output.write("104\n2\n3\n")
                    case "T":
                        output.write("104\n3\n3\n")
                    case "P":
                        output.write("104\n4\n3\n")
                    case "U":
                        output.write("104\n5\n3\n")
            case "P":
                match r2:
                    case "x":
                        output.write("104\n1\n4\n")
                    case "y":
                        output.write("104\n2\n4\n")
                    case "t":
                        output.write("104\n3\n4\n")
                    case "p":
                        output.write("104\n4\n4\n")
                    case "u":
                        output.write("104\n5\n4\n")
                    case "X":
                        output.write("104\n1\n4\n")
                    case "Y":
                        output.write("104\n2\n4\n")
                    case "T":
                        output.write("104\n3\n4\n")
                    case "P":
                        output.write("104\n4\n4\n")
                    case "U":
                        output.write("104\n5\n4\n")
            case "U":
                match r2:
                    case "x":
                        output.write("104\n1\n5\n")
                    case "y":
                        output.write("104\n2\n5\n")
                    case "t":
                        output.write("104\n3\n5\n")
                    case "p":
                        output.write("104\n4\n5\n")
                    case "u":
                        output.write("104\n5\n5\n")
                    case "X":
                        output.write("104\n1\n5\n")
                    case "Y":
                        output.write("104\n2\n5\n")
                    case "T":
                        output.write("104\n3\n5\n")
                    case "P":
                        output.write("104\n4\n5\n")
                    case "U":
                        output.write("104\n5\n5\n")

    if SplitLine[0] == "add" or SplitLine[0] == "ADD":
        SplitArg = SplitLine[1].split(","[0])
        r1,r2 = SplitArg[0],SplitArg[1]

        match r1:
            case "x":
                match r2:
                    case "x":
                        output.write("105\n1\n1\n")
                    case "y":
                        output.write("105\n2\n1\n")
                    case "t":
                        output.write("105\n3\n1\n")
                    case "p":
                        output.write("105\n4\n1\n")
                    case "u":
                        output.write("105\n5\n1\n")
                    case "X":
                        output.write("105\n1\n1\n")
                    case "Y":
                        output.write("105\n2\n1\n")
                    case "T":
                        output.write("105\n3\n1\n")
                    case "P":
                        output.write("105\n4\n1\n")
                    case "U":
                        output.write("105\n5\n1\n")
            case "y":
                match r2:
                    case "x":
                        output.write("105\n1\n2\n")
                    case "y":
                        output.write("105\n2\n2\n")
                    case "t":
                        output.write("105\n3\n2\n")
                    case "p":
                        output.write("105\n4\n2\n")
                    case "u":
                        output.write("105\n5\n2\n")
                    case "X":
                        output.write("105\n1\n2\n")
                    case "Y":
                        output.write("105\n2\n2\n")
                    case "T":
                        output.write("105\n3\n2\n")
                    case "P":
                        output.write("105\n4\n2\n")
                    case "U":
                        output.write("105\n5\n2\n")
            case "t":
                match r2:
                    case "x":
                        output.write("105\n1\n3\n")
                    case "y":
                        output.write("105\n2\n3\n")
                    case "t":
                        output.write("105\n3\n3\n")
                    case "p":
                        output.write("105\n4\n3\n")
                    case "u":
                        output.write("105\n5\n3\n")
                    case "X":
                        output.write("105\n1\n3\n")
                    case "Y":
                        output.write("105\n2\n3\n")
                    case "T":
                        output.write("105\n3\n3\n")
                    case "P":
                        output.write("105\n4\n3\n")
                    case "U":
                        output.write("105\n5\n3\n")
            case "p":
                match r2:
                    case "x":
                        output.write("105\n1\n4\n")
                    case "y":
                        output.write("105\n2\n4\n")
                    case "t":
                        output.write("105\n3\n4\n")
                    case "p":
                        output.write("105\n4\n4\n")
                    case "u":
                        output.write("105\n5\n4\n")
                    case "X":
                        output.write("105\n1\n4\n")
                    case "Y":
                        output.write("105\n2\n4\n")
                    case "T":
                        output.write("105\n3\n4\n")
                    case "P":
                        output.write("105\n4\n4\n")
                    case "U":
                        output.write("105\n5\n4\n")
            case "u":
                match r2:
                    case "x":
                        output.write("105\n1\n5\n")
                    case "y":
                        output.write("105\n2\n5\n")
                    case "t":
                        output.write("105\n3\n5\n")
                    case "p":
                        output.write("105\n4\n5\n")
                    case "u":
                        output.write("105\n5\n5\n")
                    case "X":
                        output.write("105\n1\n5\n")
                    case "Y":
                        output.write("105\n2\n5\n")
                    case "T":
                        output.write("105\n3\n5\n")
                    case "P":
                        output.write("105\n4\n5\n")
                    case "U":
                        output.write("105\n5\n5\n")

            case "X":
                match r2:
                    case "x":
                        output.write("105\n1\n1\n")
                    case "y":
                        output.write("105\n2\n1\n")
                    case "t":
                        output.write("105\n3\n1\n")
                    case "p":
                        output.write("105\n4\n1\n")
                    case "u":
                        output.write("105\n5\n1\n")
                    case "X":
                        output.write("105\n1\n1\n")
                    case "Y":
                        output.write("105\n2\n1\n")
                    case "T":
                        output.write("105\n3\n1\n")
                    case "P":
                        output.write("105\n4\n1\n")
                    case "U":
                        output.write("105\n5\n1\n")
            case "Y":
                match r2:
                    case "x":
                        output.write("105\n1\n2\n")
                    case "y":
                        output.write("105\n2\n2\n")
                    case "t":
                        output.write("105\n3\n2\n")
                    case "p":
                        output.write("105\n4\n2\n")
                    case "u":
                        output.write("105\n5\n2\n")
                    case "X":
                        output.write("105\n1\n2\n")
                    case "Y":
                        output.write("105\n2\n2\n")
                    case "T":
                        output.write("105\n3\n2\n")
                    case "P":
                        output.write("105\n4\n2\n")
                    case "U":
                        output.write("105\n5\n2\n")
            case "T":
                match r2:
                    case "x":
                        output.write("105\n1\n3\n")
                    case "y":
                        output.write("105\n2\n3\n")
                    case "t":
                        output.write("105\n3\n3\n")
                    case "p":
                        output.write("105\n4\n3\n")
                    case "u":
                        output.write("105\n5\n3\n")
                    case "X":
                        output.write("105\n1\n3\n")
                    case "Y":
                        output.write("105\n2\n3\n")
                    case "T":
                        output.write("105\n3\n3\n")
                    case "P":
                        output.write("105\n4\n3\n")
                    case "U":
                        output.write("105\n5\n3\n")
            case "P":
                match r2:
                    case "x":
                        output.write("105\n1\n4\n")
                    case "y":
                        output.write("105\n2\n4\n")
                    case "t":
                        output.write("105\n3\n4\n")
                    case "p":
                        output.write("105\n4\n4\n")
                    case "u":
                        output.write("105\n5\n4\n")
                    case "X":
                        output.write("105\n1\n4\n")
                    case "Y":
                        output.write("105\n2\n4\n")
                    case "T":
                        output.write("105\n3\n4\n")
                    case "P":
                        output.write("105\n4\n4\n")
                    case "U":
                        output.write("105\n5\n4\n")
            case "U":
                match r2:
                    case "x":
                        output.write("105\n1\n5\n")
                    case "y":
                        output.write("105\n2\n5\n")
                    case "t":
                        output.write("105\n3\n5\n")
                    case "p":
                        output.write("105\n4\n5\n")
                    case "u":
                        output.write("105\n5\n5\n")
                    case "X":
                        output.write("105\n1\n5\n")
                    case "Y":
                        output.write("105\n2\n5\n")
                    case "T":
                        output.write("105\n3\n5\n")
                    case "P":
                        output.write("105\n4\n5\n")
                    case "U":
                        output.write("105\n5\n5\n")

    if SplitLine[0] == "sub" or SplitLine[0] == "SUB":
        SplitArg = SplitLine[1].split(","[0])
        r1,r2 = SplitArg[0],SplitArg[1]

        match r1:
            case "x":
                match r2:
                    case "x":
                        output.write("106\n1\n1\n")
                    case "y":
                        output.write("106\n1\n2\n")
                    case "t":
                        output.write("106\n1\n3\n")
                    case "p":
                        output.write("106\n1\n4\n")
                    case "u":
                        output.write("106\n1\n5\n")
                    case "X":
                        output.write("106\n1\n1\n")
                    case "Y":
                        output.write("106\n1\n2\n")
                    case "T":
                        output.write("106\n1\n3\n")
                    case "P":
                        output.write("106\n1\n4\n")
                    case "U":
                        output.write("106\n1\n5\n")
            case "y":
                match r2:
                    case "x":
                        output.write("106\n2\n1\n")
                    case "y":
                        output.write("106\n2\n2\n")
                    case "t":
                        output.write("106\n2\n3\n")
                    case "p":
                        output.write("106\n2\n4\n")
                    case "u":
                        output.write("106\n2\n5\n")
                    case "X":
                        output.write("106\n2\n1\n")
                    case "Y":
                        output.write("106\n2\n2\n")
                    case "T":
                        output.write("106\n2\n3\n")
                    case "P":
                        output.write("106\n2\n4\n")
                    case "U":
                        output.write("106\n2\n5\n")
            case "t":
                match r2:
                    case "x":
                        output.write("106\n3\n1\n")
                    case "y":
                        output.write("106\n3\n2\n")
                    case "t":
                        output.write("106\n3\n3\n")
                    case "p":
                        output.write("106\n3\n4\n")
                    case "u":
                        output.write("106\n3\n5\n")
                    case "X":
                        output.write("106\n3\n1\n")
                    case "Y":
                        output.write("106\n3\n2\n")
                    case "T":
                        output.write("106\n3\n3\n")
                    case "P":
                        output.write("106\n3\n4\n")
                    case "U":
                        output.write("106\n3\n5\n")
            case "p":
                match r2:
                    case "x":
                        output.write("106\n4\n1\n")
                    case "y":
                        output.write("106\n4\n2\n")
                    case "t":
                        output.write("106\n4\n3\n")
                    case "p":
                        output.write("106\n4\n4\n")
                    case "u":
                        output.write("106\n4\n5\n")
                    case "X":
                        output.write("106\n4\n1\n")
                    case "Y":
                        output.write("106\n4\n2\n")
                    case "T":
                        output.write("106\n4\n3\n")
                    case "P":
                        output.write("106\n4\n4\n")
                    case "U":
                        output.write("106\n4\n5\n")
            case "u":
                match r2:
                    case "x":
                        output.write("106\n5\n1\n")
                    case "y":
                        output.write("106\n5\n2\n")
                    case "t":
                        output.write("106\n5\n3\n")
                    case "p":
                        output.write("106\n5\n4\n")
                    case "u":
                        output.write("106\n5\n5\n")
                    case "X":
                        output.write("106\n5\n1\n")
                    case "Y":
                        output.write("106\n5\n2\n")
                    case "T":
                        output.write("106\n5\n3\n")
                    case "P":
                        output.write("106\n5\n4\n")
                    case "U":
                        output.write("106\n5\n5\n")

            case "X":
                match r2:
                    case "x":
                        output.write("106\n1\n1\n")
                    case "y":
                        output.write("106\n1\n2\n")
                    case "t":
                        output.write("106\n1\n3\n")
                    case "p":
                        output.write("106\n1\n4\n")
                    case "u":
                        output.write("106\n1\n5\n")
                    case "X":
                        output.write("106\n1\n1\n")
                    case "Y":
                        output.write("106\n1\n2\n")
                    case "T":
                        output.write("106\n1\n3\n")
                    case "P":
                        output.write("106\n1\n4\n")
                    case "U":
                        output.write("106\n1\n5\n")
            case "Y":
                match r2:
                    case "x":
                        output.write("106\n2\n1\n")
                    case "y":
                        output.write("106\n2\n2\n")
                    case "t":
                        output.write("106\n2\n3\n")
                    case "p":
                        output.write("106\n2\n4\n")
                    case "u":
                        output.write("106\n2\n5\n")
                    case "X":
                        output.write("106\n2\n1\n")
                    case "Y":
                        output.write("106\n2\n2\n")
                    case "T":
                        output.write("106\n2\n3\n")
                    case "P":
                        output.write("106\n2\n4\n")
                    case "U":
                        output.write("106\n2\n5\n")
            case "T":
                match r2:
                    case "x":
                        output.write("106\n3\n1\n")
                    case "y":
                        output.write("106\n3\n2\n")
                    case "t":
                        output.write("106\n3\n3\n")
                    case "p":
                        output.write("106\n3\n4\n")
                    case "u":
                        output.write("106\n3\n5\n")
                    case "X":
                        output.write("106\n3\n1\n")
                    case "Y":
                        output.write("106\n3\n2\n")
                    case "T":
                        output.write("106\n3\n3\n")
                    case "P":
                        output.write("106\n3\n4\n")
                    case "U":
                        output.write("106\n3\n5\n")
            case "P":
                match r2:
                    case "x":
                        output.write("106\n4\n1\n")
                    case "y":
                        output.write("106\n4\n2\n")
                    case "t":
                        output.write("106\n4\n3\n")
                    case "p":
                        output.write("106\n4\n4\n")
                    case "u":
                        output.write("106\n4\n5\n")
                    case "X":
                        output.write("106\n4\n1\n")
                    case "Y":
                        output.write("106\n4\n2\n")
                    case "T":
                        output.write("106\n4\n3\n")
                    case "P":
                        output.write("106\n4\n4\n")
                    case "U":
                        output.write("106\n4\n5\n")
            case "U":
                match r2:
                    case "x":
                        output.write("106\n5\n1\n")
                    case "y":
                        output.write("106\n5\n2\n")
                    case "t":
                        output.write("106\n5\n3\n")
                    case "p":
                        output.write("106\n5\n4\n")
                    case "u":
                        output.write("106\n5\n5\n")
                    case "X":
                        output.write("106\n5\n1\n")
                    case "Y":
                        output.write("106\n5\n2\n")
                    case "T":
                        output.write("106\n5\n3\n")
                    case "P":
                        output.write("106\n5\n4\n")
                    case "U":
                        output.write("106\n5\n5\n")

    if SplitLine[0] == "cmp" or SplitLine[0] == "CMP":
        SplitArg = SplitLine[1].split(","[0])
        r1,Value = SplitArg[0],SplitArg[1].split("#"[0])[1]
        match r1:
            case "x":
                output.write("107\n1\n"+str(Value)+"\n")
            case "X":
                output.write("107\n1\n"+str(Value)+"\n")
            case "y":
                output.write("107\n2\n"+str(Value)+"\n")
            case "Y":
                output.write("107\n2\n"+str(Value)+"\n")
            case "t":
                output.write("107\n3\n"+str(Value)+"\n")
            case "T":
                output.write("107\n3\n"+str(Value)+"\n")
            case "p":
                output.write("107\n4\n"+str(Value)+"\n")
            case "P":
                output.write("107\n4\n"+str(Value)+"\n")
            case "u":
                output.write("107\n5\n"+str(Value)+"\n")
            case "U":
                output.write("107\n5\n"+str(Value)+"\n")

    if SplitLine[0] == "cpa" or SplitLine[0] == "CPA":
        SplitArg = SplitLine[1].split(","[0])
        Address,Value = SplitArg[0].split("$"[0])[1],SplitArg[1].split("#"[0])[1]
        output.write("108\n"+str(Address)+"\n"+str(Value)+"\n")

    if SplitLine[0] == "inc" or SplitLine[0] == "INC":
        r1 = SplitLine[1]
        match r1:
            case "x":
                output.write("109\n1\n")
            case "X":
                output.write("109\n1\n")
            case "y":
                output.write("109\n2\n")
            case "Y":
                output.write("109\n2\n")
            case "t":
                output.write("109\n3\n")
            case "T":
                output.write("109\n3\n")
            case "p":
                output.write("109\n4\n")
            case "P":
                output.write("109\n4\n")
            case "u":
                output.write("109\n5\n")
            case "U":
                output.write("109\n5\n")

    if SplitLine[0] == "dec" or SplitLine[0] == "DEC":
        r1 = SplitLine[1]
        match r1:
            case "x":
                output.write("110\n1\n")
            case "X":
                output.write("110\n1\n")
            case "y":
                output.write("110\n2\n")
            case "Y":
                output.write("110\n2\n")
            case "t":
                output.write("110\n3\n")
            case "T":
                output.write("110\n3\n")
            case "p":
                output.write("110\n4\n")
            case "P":
                output.write("110\n4\n")
            case "u":
                output.write("110\n5\n")
            case "U":
                output.write("110\n5\n")

    if SplitLine[0] == "st" or SplitLine[0] == "ST":
        SplitArg = SplitLine[1].split(","[0])
        r1 = SplitArg[0]
        if "$" in SplitArg[1]:
            Address = SplitArg[1].split("$"[0])[1]
            match r1:
                case "x":
                    output.write("111\n1\n"+str(Address)+"\n")
                case "X":
                    output.write("111\n1\n"+str(Address)+"\n")
                case "y":
                    output.write("111\n2\n"+str(Address)+"\n")
                case "Y":
                    output.write("111\n2\n"+str(Address)+"\n")
                case "t":
                    output.write("111\n3\n"+str(Address)+"\n")
                case "T":
                    output.write("111\n3\n"+str(Address)+"\n")
                case "p":
                    output.write("111\n4\n"+str(Address)+"\n")
                case "P":
                    output.write("111\n4\n"+str(Address)+"\n")
                case "u":
                    output.write("111\n5\n"+str(Address)+"\n")
                case "U":
                    output.write("111\n5\n"+str(Address)+"\n")
        if "%" in SplitArg[1]:
            Address = SplitArg[0].split("%"[0])[1]
            if "u" in Address:
                Register = 1
                Address = Address.split("u"[0])[1]
            if "U" in Address:
                Register = 1
                Address = Address.split("U"[0])[1]
            if "p" in Address:
                Register = 1
                Address = Address.split("p"[0])[1]
            if "P" in Address:
                Register = 1
                Address = Address.split("P"[0])[1]
            match Register:
                case 1: # P
                    match SplitArg[1]:
                        case "x":
                            output.write("112\n1\n"+str(Address)+"\n")
                        case "X":
                            output.write("112\n1\n"+str(Address)+"\n")
                        case "y":
                            output.write("112\n2\n"+str(Address)+"\n")
                        case "Y":
                            output.write("112\n2\n"+str(Address)+"\n")
                        case "t":
                            output.write("112\n3\n"+str(Address)+"\n")
                        case "T":
                            output.write("112\n3\n"+str(Address)+"\n")
                        case "p":
                            output.write("112\n4\n"+str(Address)+"\n")
                        case "P":
                            output.write("112\n4\n"+str(Address)+"\n")
                        case "u":
                            output.write("112\n5\n"+str(Address)+"\n")
                        case "U":
                            output.write("112\n5\n"+str(Address)+"\n")
                case 2:
                    match SplitArg[1]:
                        case "x":
                            output.write("113\n1\n"+str(Address)+"\n")
                        case "X":
                            output.write("113\n1\n"+str(Address)+"\n")
                        case "y":
                            output.write("113\n2\n"+str(Address)+"\n")
                        case "Y":
                            output.write("113\n2\n"+str(Address)+"\n")
                        case "t":
                            output.write("113\n3\n"+str(Address)+"\n")
                        case "T":
                            output.write("113\n3\n"+str(Address)+"\n")
                        case "p":
                            output.write("113\n4\n"+str(Address)+"\n")
                        case "P":
                            output.write("113\n4\n"+str(Address)+"\n")
                        case "u":
                            output.write("113\n5\n"+str(Address)+"\n")
                        case "U":
                            output.write("113\n5\n"+str(Address)+"\n")

    if SplitLine[0] == "jmp" or SplitLine[0] == "JMP":
        JumpPoint = SplitLine[1]
        if "@" in JumpPoint:
            Name = JumpPoint.split("@"[0])[1]
            Address = getLabelAddress(Name)
            output.write("114\n"+str(Address)+"\n")
        if "$" in JumpPoint:
            Address = JumpPoint.split("$"[0])[1]
            output.write("114\n"+str(Address)+"\n")

    if SplitLine[0] == "joe" or SplitLine[0] == "JOE":
        JumpPoint = SplitLine[1]
        if "@" in JumpPoint:
            Name = JumpPoint.split("@"[0])[1]
            Address = getLabelAddress(Name)
            output.write("115\n"+str(Address)+"\n")
        if "$" in JumpPoint:
            Address = JumpPoint.split("$"[0])[1]
            output.write("115\n"+str(Address)+"\n")

    if SplitLine[0] == "jne" or SplitLine[0] == "JNE":
        JumpPoint = SplitLine[1]
        if "@" in JumpPoint:
            Name = JumpPoint.split("@"[0])[1]
            Address = getLabelAddress(Name)
            output.write("116\n"+str(Address)+"\n")
        if "$" in JumpPoint:
            Address = JumpPoint.split("$"[0])[1]
            output.write("116\n"+str(Address)+"\n")

    if SplitLine[0] == "jsp" or SplitLine[0] == "JSP":
        JumpPoint = SplitLine[1]
        if "@" in JumpPoint:
            Name = JumpPoint.split("@"[0])[1]
            Address = getLabelAddress(Name)
            output.write("117\n"+str(Address)+"\n")
        if "$" in JumpPoint:
            Address = JumpPoint.split("$"[0])[1]
            output.write("117\n"+str(Address)+"\n")

    if SplitLine[0] == "rtp" or SplitLine[0] == "RTP":
        output.write("118\n")

    if SplitLine[0] == "dsp" or SplitLine[0] == "DSP":
        if SplitLine[1] == "nl" or SplitLine[1] == "NL":
            output.write("119\n3\n")   
        elif SplitLine[1] == "sp" or SplitLine[1] == "SP":
            output.write("119\n4\n")
        elif SplitLine[1] == "bp" or SplitLine[1] == "BP":
            output.write("119\n5\n")
        else:
            SplitArg = SplitLine[1].split(","[0])
            match SplitArg[0]:
                case "v":
                    match SplitArg[1]:
                        case "x":
                            output.write("119\n1\n1\n")
                        case "X":
                            output.write("119\n1\n1\n")
                        case "y":
                            output.write("119\n1\n2\n")
                        case "Y":
                            output.write("119\n1\n2\n")
                        case "t":
                            output.write("119\n1\n3\n")
                        case "T":
                            output.write("119\n1\n3\n")
                        case "p":
                            output.write("119\n1\n4\n")
                        case "P":
                            output.write("119\n1\n4\n")
                        case "u":
                            output.write("119\n1\n5\n")
                        case "U":
                            output.write("119\n1\n5\n")
                case "V":
                    match SplitArg[1]:
                        case "x":
                            output.write("119\n1\n1\n")
                        case "X":
                            output.write("119\n1\n1\n")
                        case "y":
                            output.write("119\n1\n2\n")
                        case "Y":
                            output.write("119\n1\n2\n")
                        case "t":
                            output.write("119\n1\n3\n")
                        case "T":
                            output.write("119\n1\n3\n")
                        case "p":
                            output.write("119\n1\n4\n")
                        case "P":
                            output.write("119\n1\n4\n")
                        case "u":
                            output.write("119\n1\n5\n")
                        case "U":
                            output.write("119\n1\n5\n")
                case "a":
                    match SplitArg[1]:
                        case "x":
                            output.write("119\n2\n1\n")
                        case "X":
                            output.write("119\n2\n1\n")
                        case "y":
                            output.write("119\n2\n2\n")
                        case "Y":
                            output.write("119\n2\n2\n")
                        case "t":
                            output.write("119\n2\n3\n")
                        case "T":
                            output.write("119\n2\n3\n")
                        case "p":
                            output.write("119\n2\n4\n")
                        case "P":
                            output.write("119\n2\n4\n")
                        case "u":
                            output.write("119\n2\n5\n")
                        case "U":
                            output.write("119\n2\n5\n")
                case "A":
                    match SplitArg[1]:
                        case "x":
                            output.write("119\n2\n1\n")
                        case "X":
                            output.write("119\n2\n1\n")
                        case "y":
                            output.write("119\n2\n2\n")
                        case "Y":
                            output.write("119\n2\n2\n")
                        case "t":
                            output.write("119\n2\n3\n")
                        case "T":
                            output.write("119\n2\n3\n")
                        case "p":
                            output.write("119\n2\n4\n")
                        case "P":
                            output.write("119\n2\n4\n")
                        case "u":
                            output.write("119\n2\n5\n")
                        case "U":
                            output.write("119\n2\n5\n")
    
    if SplitLine[0] == "psh" or SplitLine[0] == "PSH":
        match SplitLine[1]:
            case "x":
                output.write("120\n1\n")
            case "X":
                output.write("120\n1\n")
            case "y":
                output.write("120\n2\n")
            case "Y":
                output.write("120\n2\n")
            case "t":
                output.write("120\n3\n")
            case "T":
                output.write("120\n3\n")
            case "p":
                output.write("120\n4\n")
            case "P":
                output.write("120\n4\n")
            case "u":
                output.write("120\n5\n")
            case "U":
                output.write("120\n5\n")

    if SplitLine[0] == "pul" or SplitLine[0] == "PUL":
        match SplitLine[1]:
            case "x":
                output.write("121\n1\n")
            case "X":
                output.write("121\n1\n")
            case "y":
                output.write("121\n2\n")
            case "Y":
                output.write("121\n2\n")
            case "t":
                output.write("121\n3\n")
            case "T":
                output.write("121\n3\n")
            case "p":
                output.write("121\n4\n")
            case "P":
                output.write("121\n4\n")
            case "u":
                output.write("121\n5\n")
            case "U":
                output.write("121\n5\n")

            


        

        

        






    LinePosition+=1
    match SplitLine[0]:
        case "break":
            break

output.close()
