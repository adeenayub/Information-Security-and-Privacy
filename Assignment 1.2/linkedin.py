import hashlib 
import sys
  
dictfile = open("rockyou_utf8.txt", "r")
pswrdfile = open("SHA1.txt", "r")
rsltfile = open("linkycrackedpasswords.txt", "w+")

passwrds = set()
for line in pswrdfile:
  passwrds.add(line.replace("\n","")) 

#counter is maintained to ensure not more than 1K cracked passwords are written to the file(as said in the instructions)
counter = 0
for line in dictfile:
	#print(line)
	str = line.replace("\n","").upper()
	#str2 = line.replace("\n","")
	#result = hashlib.sha1(str.encode())
	result2 = hashlib.sha1(str.encode())
	crackedhash = result2.hexdigest()
	#the leaked file has 00000 prepended to the hashes that have probably been already cracked by hackers
	newhash = '0'*5 + crackedhash[5:]

	#if result.hexdigest() in passwrds:
	#	counter = counter+1
		#only write to the file if less than 1K passwords are cracked and written
	#	if counter <= 10:  
	#		rsltfile.write(result.hexdigest()+" "+ str+"\n")
	#		print(result.hexdigest()," ", str," ",counter)
		
	if newhash in passwrds:
		counter = counter +1
		if counter <= 1000:
			rsltfile.write(newhash + " " + str + "\n")
			print(newhash, " " , str, " ", counter)
	
		else:
			rsltfile.close()
			dictfile.close()
			pswrdfile.close()
			print("1K passwords cracked Alhamdulillah. Program exiting")
			break
