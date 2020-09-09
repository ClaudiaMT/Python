import os
os.system('cls')
#   Date introduse ***************************************
name=input("\nIntroduceti numele: ")
brut=int(input("Introduceti salariul brut: "))
spVechime=int(input("Introduceti vechimea in %: "))


if spVechime<0 or spVechime>25 or spVechime%5==5:
    print("\nVechimea este introdusa gresit!\n")
    

DP=int(input("Introduceti deducerea personala: "))
av=int(input("Introduceti avansul: "))
#   Calcule **********************************************
calcSpVech=round(brut*(spVechime/100))
calcBrut=brut+calcSpVech
CAS=round(calcBrut*0.25)
CASS=round(calcBrut*0.10)
x=int(calcBrut-CAS-CASS)
y=int(x-DP)
imp=round(y*0.1)
net=x-imp
rest=net-av
#   Scriere în fişier ************************************
f=open("fluturi.txt","at")
f.write("\n\nSalarii")
f.write("\n*****************************")
f.writelines("\nNume:   ")
f.writelines(name)
f.write("\nSalariul incadrare: ")
f.write(str(brut))
f.write("\nSpor vechime:       ")
f.writelines(str(calcSpVech))
f.write("\nSalariul brut:      ")
f.writelines(str(calcBrut))
f.write("\nCAS:                ")
f.writelines(str(CAS))
f.write("\nCASS:               ")
f.writelines(str(CASS))
f.write("\nDeducere personala: ")
f.writelines(str(DP))
f.write("\nImpozit:            ")
f.writelines(str(imp))
f.write("\nSalariul net:       ")
f.writelines(str(net))
f.write("\nAvans:              ")
f.writelines(str(av))
f.write("\n*****************************")
f.write("\nRest de plata:      ")
f.writelines(str(rest))
f.write("\n______________________________\n")
f.close()

#   Citire din fişier - la consola ******************
f = open('fluturi.txt', 'r')
print(f.read())
f.close()
#********************************************************