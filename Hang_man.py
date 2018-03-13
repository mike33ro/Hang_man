
import os
def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

def inceput(continuam):
    while continuam==True:
        clear_screen()
        prop=input('State the propozition >  ')
        Incercari=int(input('Nb of tries> '))
        hide_propozitie(prop,Incercari)
    else:
        continuam=False
        quit()

def hide_propozitie(prop,Incercari):
    clear_screen()
    print('You have {} tries !'.format (Incercari))
    hide=[]
    lista=list(prop)
    for word in lista:

        if word !=' ':
            word='*'
            hide.append(word)
        else:
            word="|"
            hide.append(word)
    hide=''.join(hide)
    print(hide)
    verif_litera(hide,prop,Incercari)

    return hide

def verif_litera(hide,prop,Incercari):

    lista=tuple(prop)
    n=0
    continuare= True
    while continuare is True:
        litera = input('Write the letter> ').lower()
        i=0
        x=0
        hide = list(hide)
        for word in prop :

            if litera.lower() == word.lower():
                hide[x]=word
                i+=1
                x+=1
            else:
                x+=1
                continue
        if i==0 :
            print('You are wrong !')
            n+=1
            print('You still have {} tries!'.format(Incercari-n) )
            if n==Incercari:
                print('You overpassed nb of tries {} ! '.format(Incercari))
                print('The proposition was: \n {}'.format(prop))
                print('You lost !!!!!!!!!')
                continuam = input('Continue with another one ? Y/n')
                if continuam.lower() != 'y':
                    continuare = False
                    quit()
                else:
                    continuam=True
                    inceput(True)
            else:
                continue
        hide=''.join(hide)
        print(hide)
        if '*' not in hide:
            print ('--------You won--------')
            print('------from {} tries------'.format(Incercari-n))
            print('******CONGRATS******')
            continuam=input('Continue with another proposition ? Y/n')
            if continuam.lower()!='y':
                continuare=False
                quit()
            else:
                continuam=True
                inceput(True)

        else:
            continuare=True

clear_screen()
inceput(True)





