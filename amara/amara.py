import csv
testFile = open('testimport3.csv')
testReader = csv.reader(testFile)
testData = list(testReader)[1]
ipGen = (str(i)+'.'+str(j) for i in range(248,257) for j in range(1,255)) #generator expression for ip
g = ipGen
outputFile = open('testimport3.csv','at',newline='')
outputWriter = csv.writer(outputFile)
for k in range(1,1001):
	ks = str(k)
	#temp = [testData[0]+ks,testData[1],testData[2],testData[3],testData[4]+ks,testData[5]+ks,'IP','','',testData[9],'IP',testData[11],'',testData[13],testData[14],'','','','','','','','',''])
	temp = list(testData)
	temp[0] += ks
	temp[4] += ks
	temp[5] += ks
	a = testData[6][:5]+next(g)  #slicing the ip address for the first two octects eg: 10.3.4.5 until 10.3.
	temp[6] = a
	temp[10] = a
	outputWriter.writerow(temp)
