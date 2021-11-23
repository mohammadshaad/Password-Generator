import random
import string
import array

passLen = 16

strUp = list(string.ascii_uppercase)
strLow = list(string.ascii_lowercase)
strDig = list(string.digits)
strPun = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']

strAll = strUp + strLow + strPun + strDig

randUp = random.choice(strUp)
randLow = random.choice(strLow)
randDig = random.choice(strDig)
randPun = random.choice(strPun)

randAll = randUp + randLow + randPun + randDig
randAllList = []

for x in range(passLen - 4):
    randAll += random.choice(strAll)
    randAllList = array.array("u", randAll)
    random.shuffle(randAllList)

password = ""
for y in randAllList:
    password += str(y)

print(password)



