import hashlib 
  
dictfile = open("rockyou_utf8.txt", "r")
pswrdfile = open("eharmony passwords.txt", "r")
rsltfile = open("crackedpasswords.txt", "w+")

passwrds = set()
for line in pswrdfile:
  passwrds.add(line.replace("\n","")) 

#counter is maintained to ensure not more than 1K cracked passwords are written to the file(as said in the instructions)
counter = 0
for line in dictfile:
	#print(line)
	str = line.replace("\n","").upper()
	result = hashlib.md5(str.encode())
	#for line1 in passfile:
	#	passwrds = line1.replace("\n","")
	if result.hexdigest() in passwrds:
		counter = counter+1
		#only write to the file if less than 1K passwords are cracked and written
		if counter <= 1000:  
			rsltfile.write(result.hexdigest()+" "+ str+"\n")
		else:
			rsltfile.close()
		#print(result.hexdigest()," ", str," ",counter)
