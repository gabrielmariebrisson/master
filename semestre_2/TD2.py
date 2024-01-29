import random

def CreateSAT(clause,variable):
    SAT=[]
    for m in range( clause ):
        Disjonction=[]
        for i in range (3):
            value=random.randint(0,variable)
            if random.randint(0,1)==0:
                Disjonction+=[value]
            else:
                Disjonction+=[-value]
        SAT+=[Disjonction]
    return SAT

SAT=CreateSAT(5,30)
print (SAT)

def fusionSAT(disjonction1, disjonction2, position1, position2):

def fusionSAT(disjonction1, disjonction2, position1, position2,resultat):


def parcour(disjonction1, disjonction2, position1, position2,resultat,taille1, taille2):
    if disjonction1[position1]==-disjonction2[position2]:
        if resultat== -1:
            resultat=fusionSAT(disjonction1, disjonction2, position1, position2)
            parcour(disjonction1, disjonction2, position1, taille2-1,resultat,taille1, taille2)

        else:
            resultat=fusionSAT(disjonction1, disjonction2, position1, position2,resultat)
            parcour(disjonction1, disjonction2, position1, taille2-1,resultat,taille1, taille2)
    if position2==0:
        parcour(disjonction1, disjonction2, position1-1, taille2,resultat,taille1, taille2)
    if position1==0 and position2==0:
        return resultat
    
def deductionSAT(SAT):
    for conjonction1 in SAT:
        for conjonction2 in SAT:
            parcour(conjonction1,conjonction2,len(conjonction1),len(conjonction2),-1,len(conjonction1),len(conjonction2))