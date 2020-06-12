path = r'C:\Users\Aayush\Desktop\macro.txt'
f = open(path, 'r')
#Open the macro file and read only
contents = f.read().split("\n")
#Split at /n
mnt, mdt, ala, pass1, pass2, arg, arg1, hashes, r, commas = [], [], [], [], [], [], [], [], [], []
mntc = 1
mdtc = 1
flag = 0
check = 0
i = 1
for line in contents:
    if line == "MACRO":         #Will go here when macro is called
        flag = 1
        check = 1
        k = 1
    elif flag == 1:             #Will go here post the macro name has been called and before MEND
        i = line.split(" ")
        for j in i:
            if check == 1:
                if not j.startswith('&') and not j.isalpha():         #To find the macro name
                    mnt.append([mntc, j, mdtc])
                    mntc += 1
                elif j.isalpha():
                    pass
                else:
                    if j.endswith(","):                                 #For , between arguments
                        j = j.replace(",", "")
                    if k == 1:
                        if "=" in j:                                    #To select the first word before =
                            j = j.split("=")[0]
                        ala.append([k, j])
                    else:
                        if "=" in j:
                            j = j.split("=")[0]
                        ala.append([k, j])
                    k += 1
        check = 0
        if "=" in line:
            line = line.split("=")[0]
        mdt.append([mdtc, line])
        mdtc += 1
        if line == "MEND":
            flag = 0
    else:                                           #Will go here when it is not Macro
        pass1.append(line)
count = 1
for i in mdt:
    for j in i:
        if not str(j).isdigit():
            if count == 1:
                count = 2
            elif j == "MEND":
                count = 1
            else:
                for m in ala:
                    if m[-1] in j:
                            p = j.replace(m[-1], " #" + str(m[0]))
                            count1 = 0
                            for q in p:
                                if count1 == 1:
                                    r += q.replace(" ","")
                                elif q == " ":
                                    count1 = 1
                                    r += q
                                else:
                                    r += q
                            for q in p:
                                count1 = 0
                                if q == " " and count1 == 1:
                                    p = p.replace(q,"")
                                elif q == " ":
                                    count1 = 1

                            print(p)
                            mdt[mdt.index(i)][i.index(j)] = p
                            j = p
print()
print("MDT Table")
for i in mdt:
    for t in i:
        print(t, end="\t")
    print()
print()
print("MNT Table")
for i in mnt:
    for t in i:
        print(t, end="\t")
    print()
print()
for i in ala:
    for t in i:
        if t == 1:
            print()
            print("ALA Table")
        print(t, end="\t")
    print()
print()
print("Intermediate Code")
for i in pass1:
    print(i)
print()
print()
print("Pass 2")
for i in pass1:
    count = 1
    for j in mnt:
        if str(j[1]) in i:
            count = 2
            mdtp = int(j[2])
            arg = pass1[pass1.index(i)].split(str(j[1]))  # splitted on the macro name
            mdtp += 1
            print("ALA TABLE FOR PASS 2")
            for y in arg:
                if y != "":
                    arg1 = y.split(",")
            for y in arg1:
                print(arg1.index(y)+1, end="\t")
                print(y)
            print()
            for k in mdt:
                if int(mdt[mdt.index(k)][0]) == int(mdtp):
                    z = mdt.index(k)
                    while mdt[z][1] != "MEND":
                        no = 0
                        for w in mdt[z][1]:
                            #print(w)
                            if w == "#":
                                no += 1      #no of hashes in a line
                            #print(no)

                        hashes = mdt[z][1].split("#")   #macro definition splitted on
                        for q in hashes:
                            commas = q.split(",")       #split on commas for 2nd hash
                            #print(commas)
                            #print('aAA')
                            for q in commas:
                                #print(q)
                                #for r in q:
                                 #   if r == "'":
                                  #      q.replace("r", "")
                                #print("sas")
                                #print(q)
                                # commas = q.split(",")
                                # print(commas)
                                # print("bbb")
                                # hashes = hashes.replace(" ","")
                                # hashes = hashes.replace(",","")
                                if q.isdigit():
                                    mdt[z][1] = mdt[z][1].replace("#" + q, arg1[int(q)-1])
                                    print(mdt[z][1])
                        pass2.append(mdt[z][1])
                        z += 1

    if count == 1:
        pass2.append(i)
for i in pass2:
    print(i)
