#Read data from files into two matrices train and test
#and for labels into trainlabels and testlabels

data = "C:\\Users\\aks23\\Documents\\Sollers\\Data\\climate"    
for k in range(0, 10, 1):
    f = open(data + "\\train."+str(k))
    mylist = f.readlines()
    train = []
    for i in range(0,len(mylist),1):
        l = mylist[i].split()
        for j in range(0,len(l),1):
            l[j] = float(l[j])
        train.append(l)
    f.close()

    f = open(data + "\\test."+str(k))
    mylist = f.readlines()
    test = []
    for i in range(0,len(mylist),1):
        l = mylist[i].split()
        for j in range(0,len(l),1):
            l[j] = float(l[j])
        test.append(l)
    f.close()

    f = open(data + "\\trainlabels."+str(k))
    n0 = 0
    n1 = 0
    mylist = f.readlines()
    trainlabels = []
    for i in range(0,len(mylist),1):
        mylist[i] = float(mylist[i])
        trainlabels.append(mylist[i])
        if(trainlabels[i] == -1):
            n0 += 1
        if(trainlabels[i] == 1):
            n1 += 1
    f.close()

    f = open(data + "\\testlabels."+str(k))
    mylist = f.readlines()
    testlabels = []
    for i in range(0,len(mylist),1):
        mylist[i] = float(mylist[i])
        testlabels.append(mylist[i])
    f.close()
    
    #Compute mean of each class
    rows = len(train)
    cols = len(train[0])
    m0 = []
    m1 = []

    for i in range(0,cols,1):
        m0.append(0.01)
        m1.append(0.01)

    for j in range(0,cols,1):
        for i in range(0,rows,1):
            if(trainlabels[i] == -1):
                m0[j] = m0[j] + train[i][j]
            if(trainlabels[i] == 1):
                m1[j] = m1[j] + train[i][j]
        
    for i in range(0,cols,1):
        m0[i] /= n0
        m1[i] /= n1
        
    #For each test datapoint determine the distance to the mean
    v0 = []
    v1 = []
    for i in range(0,cols,1):
                   v0.append(0)
                   v1.append(0)
    for j in range(0,cols,1):
        for i in range(0,rows,1):
            if(trainlabels[i] == -1):
             v0[j] += (m0[j] - train[i][j])**2
            if(trainlabels[i] == 1):
             v1[j] += (m1[j] - train[i][j])**2

    for i in range(0,cols,1):
        v0[i] /= n0
        v1[i] /= n1              

    error = 0
    for i in range(0, len(test), 1):
        d0 = 0
        d1 = 0
        for j in range(0, cols, 1):
             d0 += (m0[j] - test[i][j])**2/v0[j] 
             d1 += (m1[j] - test[i][j])**2/v1[j]
       #     d0 += (m0[j] - test[i][j])**2 #for nearest means
       #     d1 += (m1[j] - test[i][j])**2 #for nearest means
        if(d0 < d1):
            prediction = -1
        else:
            prediction = 1
        if(prediction != testlabels[i]):
            error += 1

    error /= len(test)
    error *= 100
    print("Error is ", error)

    
