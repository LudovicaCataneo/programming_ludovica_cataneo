#open the file
filename = open("./model8.pdb", "r")
#for each model in the file, we would like
#to create a list which contains the coordinates of the Carbon alfa atoms
import math
biglist= [] #crea una lista che contenga tutto!
a = -1 #faccio questo per poter partire dal primo elemento*
for line in filename: #per ogni riga del file 
	if "MODEL" in line: #se c'è la scritta "model"
		a+= 1# ecco*
		biglist.append([]) #aggiungi alla grade lista una lista vuota 
		#in cui inseriremo cose: ora capiamo cosa...
	if "CA" in line:
		line= line.split()
		if "A" in line:
			inc= 1
		else:
			inc= 0
		line= line[5+inc:8+inc]
		for k in range (len(line)):
			line[k]= float(line[k])
		biglist[a].append(line)

x=0
for i in range(len(biglist[a])):
	#print(biglist[0][i],biglist[1][i])
	for j in range (3):
		cord1= float(biglist[0][i][j])
		cord2= float(biglist[1][i][j])
		t=cord1-cord2
		t=t**2
		x=x+t
rmsd= math.sqrt((x/len(biglist[a])))
print(rmsd)