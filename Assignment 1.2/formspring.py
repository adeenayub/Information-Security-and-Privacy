import hashlib 
import sys
  
dictfile = open("/home/adeenayub/Documents/ISP/rockyou_utf8.txt", "r")
pswrdfile = open("formspring.txt", "r")
rsltfile = open("formspringcrackedpasswords.txt", "w+")

passwrds = set()
for line in pswrdfile:
  passwrds.add(line.replace("\n","")) 

#counter is maintained to ensure not more than 1K cracked passwords are written to the file(as said in the instructions)
counter = 0
for line in dictfile:
	str2 = line.replace("\n","")
	#run a for loop to generate a hash of salt+word in the range 0-99
	for x in range(100):
		#convert salt to string
		y = str(x)
		#compute hash of salt+word
		result2 = hashlib.sha256(y.encode() + str2.encode())
		crackedhash = result2.hexdigest()
		#check if found in passwords set
		if crackedhash in passwrds:
			counter = counter +1
			#only write to file if cracked passwords is <=1000
			if counter <= 1000:
				rsltfile.write(crackedhash + " " + str2 + "\n")
				#print(crackedhash, " " , str2, " ", counter)
		
			else:
				exit()

dictfile.close()
pswrdfile.close()
rsltfile.close()
