#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import getpass
from IPython.display import clear_output
def pt():
        #Periodic table  
        print("----- \t\t\t\t\t\t\t\t\t\t\t      -----") 

        print("|"," H "," |","\t\t\t\t\t\t\t\t\t\t\t","      |"," He ","|",sep="")

        print("-----+----+","\t\t\t\t\t\t\t","    +----+----+----+----+----+----+")

        print("|","Li","|","Be","|","\t\t\t\t\t\t\t","    |","B"," |","C ","|"," N","|"," O","|"," F","|","Ne","|",sep=" ")

        print("-----+----+","\t\t\t\t\t\t\t","    +----+----+----+----+----+----+")

        print("|","Na","|","Mg","|","\t\t\t\t\t\t\t","    |","Al","|","Si","|"," P","|"," S","|","Cl","|","Ar","|",sep=" ")

        print("-----+----+   +----+----+-----+----+----+----+----+----+----+----+   +----+----+----+----+----+----+")

        print("| K  |","Ca","|","  | Sc","|","Ti","|"," V ","|","Cr","|","Mn","|","Fe","|","Co","|","Ni","|","Cu","|","Zn","|","  | Ga","|","Ge","|","As","|","Se","|","Br","|","Kr","|",sep=" ")

        print("-----+----+   +----+----+-----+----+----+----+----+----+----+----+   +----+----+----+----+----+----+")
        print("|"," Rb |", " Sr ","|","   |"," Y  ","|"," Zr ","|"," Nb  ","|"," Mo ","|"," Tc ","|"," Ru ","|"," Rh ","|"," Pd ","|"," Ag ","|"," Cd ","|","   |" ," In ","|"," Sn ","|"," Sb ","|"," Te ","|","  I ","|"," Xe ","|",sep="")
        print("-----+----+   +----+----+-----+----+----+----+----+----+----+----+   +----+----+----+----+----+----+")
        print("|"," Cs |", " Ba ","|","   |"," La ","|"," Hf ","|"," Ta  ","|","  W ","|"," Re ","|"," Os ","|"," Ir ","|"," Pt ","|"," Au ","|"," Hg ","|","   |" ," Tl ","|"," Pb ","|"," Bi ","|"," Po ","|"," At ","|"," Rn ","|",sep="")
        print("-----+----+   +----+----+-----+----+----+----+----+----+----+----+   +----+----+----+----+----+----+")
        print("|"," Fr |", " Ra ","|","   |"," Ac ","|"," Rf ","|"," Db  ","|"," Sg ","|"," Bh ","|"," Hs ","|"," Mt ","|"," Ds ","|"," Rg ","|"," Cn ","|","   |" ," Nh ","|"," Fl ","|"," Mc ","|"," Lv ","|"," Ts ","|"," Og ","|",sep="")
        print("*****************************************************************************************************")
        ##############################################################################################################################


SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")


E={"H":{"Name":"Hydrogen","Period":1,"Group":1,"Atomic_no":1,"Mass":"1.008u","Type":"Non-metal","Electronegativity":2.2,"Confi":"1s"+"1".translate(SUP)}

,"Li":{"Name":"Lithium","Period":2,"Group":1,"Atomic_no":3,"Mass":"7u","Type":"Alkali-metal","Electronegativity":.98,"Confi":"[He]2s"+"1".translate(SUP)}
,"Na":{"Name":"Sodium","Period":3,"Group":1,"Atomic_no":11,"Mass":"22u","Type":"Alkali-Metal","Electronegativity":0.93,"Confi":"[Ne]3s+1"} 
,"K":{"Name":"Potassium","Period":4,"Group":1,"Atomic_no":19,"Mass":"39.098u","Type":"Alkali-Metal","Electronegativity":0.82,"Confi":"[Ar]4s"+"1".translate(SUP)}
,"Rb":{"Name":"Rubidium","Period":5,"Group":1,"Atomic_no":37,"Mass":"85.4u","Type":"Alkali-Metal","Electronegativity":0.82,"Confi":"[Kr]5s"+"1".translate(SUP)}

 
   
   
,"Be":{"Name":"Beryllium","Period":2,"Group":2,"Atomic_no":4,"Mass":"9.04u","Type":"Alkaline Earth-metal","Electronegativity":1.57,"Confi":"[He]2s"+"2".translate(SUP)}  
,"Mg":{"Name":"Magnesium","Period":3,"Group":2,"Atomic_no":12,"Mass":"24u","Type":"Alkaline Earth-Metal","Electronegativity":1.31,"Confi":"[Ne]3s+2"}
,"Ca":{"Name":"Calcium","Period":4,"Group":2,"Atomic_no":20,"Mass":"40u","Type":"Alkaline Earth-Metal","Electronegativity":1,"Confi":"[Ar]4s"+"2".translate(SUP)}
,"Sr":{"Name":"Strontium","Period":5,"Group":2,"Atomic_no":38,"Mass":"87.6u","Type":"Alkaline Earth-Metal","Electronegativity":0.95,"Confi":"[Kr]5s"+"2".translate(SUP)}

,"Sc":{"Name":"Scandium","Period":4,"Group":3,"Atomic_no":21,"Mass":"44.95u","Type":"Transition Metal","Electronegativity":1.36,"Confi":"[Ar]4s"+"2".translate(SUP)+'3d'+'1'.translate(SUP)}
,"Y":{"Name":"Yttrium","Period":5,"Group":3,"Atomic_no":39,"Mass":"88.90u","Type":"Transition Metal","Electronegativity":1.22,"Confi":"[Kr]5s"+"2".translate(SUP)+'4d'+'1'.translate(SUP)}


,"Ti":{"Name":"Titanium","Period":4,"Group":4,"Atomic_no":22,"Mass":"47.87u","Type":"Transition Metal","Electronegativity":1.54,"Confi":"[Ar]4s"+"2".translate(SUP)+'3d'+'2'.translate(SUP)}
,"Zi":{"Name":"Zirconium","Period":5,"Group":4,"Atomic_no":40,"Mass":"91.22u","Type":"Transition Metal","Electronegativity":1.33,"Confi":"[Kr]5s"+"2".translate(SUP)+'4d'+'2'.translate(SUP)}

 
,"V":{"Name":"Vanadium","Period":4,"Group":5,"Atomic_no":23,"Mass":"50.94u","Type":"Transition Metal","Electronegativity":1.63,"Confi":"[Ar]4s"+"2".translate(SUP)+'3d'+'3'.translate(SUP)}
,"Nb":{"Name":"Niobium","Period":5,"Group":5,"Atomic_no":41,"Mass":"92.9.9u","Type":"Transition Metal","Electronegativity":1.6,"Confi":"[Kr]5s"+"1".translate(SUP)+'4d'+'4'.translate(SUP)}


,"Cr":{"Name":"Chromium","Period":4,"Group":6,"Atomic_no":24,"Mass":"51.9u","Type":"Transition Metal","Electronegativity":1.66,"Confi":"[Ar]4s"+"1".translate(SUP)+'3d'+'5'.translate(SUP)}
,"Mo":{"Name":"Molybdenum","Period":5,"Group":6,"Atomic_no":42,"Mass":"96.0u","Type":"Transition Metal","Electronegativity":2.16,"Confi":"[Kr]5s"+"1".translate(SUP)+'4d'+'5'.translate(SUP)}
   
,"Mn":{"Name":"Manganese","Period":4,"Group":7,"Atomic_no":25,"Mass":"54.93u","Type":"Transition Metal","Electronegativity":1.55,"Confi":"[Ar]4s"+"2".translate(SUP)+'3d'+'5'.translate(SUP)}
,"Tc":{"Name":"Technetium","Period":5,"Group":7,"Atomic_no":43,"Mass":"97.90u","Type":"Transition Metal","Electronegativity":1.9,"Confi":"[Kr]5s"+"2".translate(SUP)+'4d'+'5'.translate(SUP)}
  
,"Fe":{"Name":"Iron","Period":4,"Group":8,"Atomic_no":26,"Mass":"55.84","Type":"Transition Metal","Electronegativity":1.83,"Confi":"[Ar]4s"+"2".translate(SUP)+'3d'+'6'.translate(SUP)}
,"Ru":{"Name":"Ruthenium","Period":5,"Group":8,"Atomic_no":44,"Mass":"101.1u","Type":"Transition Metal","Electronegativity":2.2,"Confi":"[Kr]5s"+"1".translate(SUP)+'4d'+'7'.translate(SUP)}
 
,"Co":{"Name":"Cobalt","Period":4,"Group":9,"Atomic_no":27,"Mass":"58.9u","Type":"Transition Metal","Electronegativity":1.88,"Confi":"[Ar]4s"+"2".translate(SUP)+'3d'+'7'.translate(SUP)}
,"Rh":{"Name":"Rhodium","Period":5,"Group":9,"Atomic_no":45,"Mass":"102.9u","Type":"Transition Metal","Electronegativity":2.28,"Confi":"[Kr]5s"+"1".translate(SUP)+'4d'+'8'.translate(SUP)}

,"Ni":{"Name":"Nickel","Period":4,"Group":10,"Atomic_no":28,"Mass":"58.6u","Type":"Transition Metal","Electronegativity":1.91,"Confi":"[Ar]4s"+"2".translate(SUP)+'3d'+'8'.translate(SUP)}
,"Pd":{"Name":"Palladium","Period":5,"Group":10,"Atomic_no":46,"Mass":"106.4u","Type":"Transition Metal","Electronegativity":2.2,"Confi":"[Kr]"+'4d'+'10'.translate(SUP)}

,"Cu":{"Name":"Copper","Period":4,"Group":11,"Atomic_no":29,"Mass":"63.5u","Type":"Transition Metal","Electronegativity":1.9,"Confi":"[Ar]"+'4s'+"1".translate(SUP)+'3d'+'10'.translate(SUP)}
,"Ag":{"Name":"Silver","Period":5,"Group":11,"Atomic_no":47,"Mass":"107.87u","Type":"Transition Metal","Electronegativity":1.93,"Confi":"[Kr]"+'5s'+"1".translate(SUP)+'4d'+'10'.translate(SUP)}

,"Zn":{"Name":"Zinc","Period":4,"Group":12,"Atomic_no":30,"Mass":"65.4u","Type":"Transition Metal","Electronegativity":1.65,"Confi":"[Ar]"+'4s'+"2".translate(SUP)+'3d'+'10'.translate(SUP)}
,"Cd":{"Name":"Cadium","Period":5,"Group":12,"Atomic_no":48,"Mass":"112.41u","Type":"Transition Metal","Electronegativity":1.69,"Confi":"[Kr]"+'5s'+"2".translate(SUP)+'4d'+'10'.translate(SUP)}
   
   
,"B":{"Name":"Boron","Period":2,"Group":13,"Atomic_no":5,"Mass":"10.81u","Type":"Metalloid","Electronegativity":2.04,"Confi":"[He]2s"+"2".translate(SUP)+"2p"+"1".translate(SUP)}
,"Al":{"Name":"Aluminium","Period":3,"Group":13,"Atomic_no":13,"Mass":"26u","Type":"Metal","Electronegativity":1.61,"Confi":"[Ne]3s"+"2".translate(SUP)+ "3p"+"1".translate(SUP)}
,"Ga":{"Name":"Gallium","Period":4,"Group":13,"Atomic_no":31,"Mass":"69.7u","Type":"Metal","Electronegativity":1.81,"Confi":"[Ar]4s"+"2".translate(SUP)+ "3d"+"10".translate(SUP)+"4p"+"1".translate(SUP)}
,"In":{"Name":"Indium","Period":5,"Group":13,"Atomic_no":49,"Mass":"114.82u","Type":"Metal","Electronegativity":1.78,"Confi":"[Kr]5s"+"2".translate(SUP)+ "4d"+"10".translate(SUP)+"5p"+"1".translate(SUP)}

   
   
,"C":{"Name":"Carbon","Period":2,"Group":14,"Atomic_no":6,"Mass":"12u","Type":"Non-Metal","Electronegativity":2.55,"Confi":"[He]2s"+"2".translate(SUP)+ "2p"+"2".translate(SUP)}
,"Si":{"Name":"Silicon","Period":3,"Group":14,"Atomic_no":14,"Mass":"28u","Type":"Metalloid","Electronegativity":1.9,"Confi":"[Ne]3s+2 3p+2"}
,"Ge":{"Name":"Germanium","Period":4,"Group":14,"Atomic_no":32,"Mass":"72.6u","Type":"Metalloid","Electronegativity":2.01,"Confi":"[Ar]4s"+"2".translate(SUP)+ "3d"+"10".translate(SUP)+"4p"+"2".translate(SUP)}
,"Sn":{"Name":"Tin","Period":5,"Group":14,"Atomic_no":50,"Mass":"118.71u","Type":"Metalloid","Electronegativity":1.96,"Confi":"[Kr]5s"+"2".translate(SUP)+ "4d"+"10".translate(SUP)+"5p"+"2".translate(SUP)}

   
,"N":{"Name":"Nitrogen","Period":2,"Group":15,"Atomic_no":7,"Mass":"14u","Type":"Non-Metal","Electronegativity":3.04,"Confi":"[He]2s"+"2".translate(SUP)+"2p"+"3".translate(SUP)}
,"P":{"Name":"Phosphorus","Period":3,"Group":15,"Atomic_no":15,"Mass":"30.9u","Type":"Non-Metal","Electronegativity":2.19,"Confi":"[Ne]3s"+"2".translate(SUP)+ "3p"+"3".translate(SUP)}
,"As":{"Name":"Arsenic","Period":4,"Group":15,"Atomic_no":33,"Mass":"74.9u","Type":"Metalloid","Electronegativity":2.18,"Confi":"[Ar]4s"+"2".translate(SUP) +"3d"+"10".translate(SUP)+"4p"+"3".translate(SUP)}
,"Sb":{"Name":"Antimony","Period":5,"Group":15,"Atomic_no":51,"Mass":"121.76u","Type":"Metalloid","Electronegativity":2.05,"Confi":"[Kr]5s"+"2".translate(SUP) +"4d"+"10".translate(SUP)+"5p"+"3".translate(SUP)}

   

,"O":{"Name":"Oxygen","Period":2,"Group":16,"Atomic_no":8,"Mass":"16u","Type":"Non-metal","Electronegativity":3.44,"Confi":"[He]2s+2 2p+4"}  
,"S":{"Name":"Sulphur","Period":3,"Group":16,"Atomic_no":16,"Mass":"32.07u","Type":"Non-Metal","Electronegativity":2.58,"Confi":"[Ne]3s"+"2".translate(SUP)+ "3p"+"4".translate(SUP)}
,"Se":{"Name":"Selenium","Period":4,"Group":16,"Atomic_no":34,"Mass":"78.97u","Type":"Non-Metal","Electronegativity":2.55,"Confi":"[Ar]4s"+"2".translate(SUP)+"3d"+"10".translate(SUP) +"4p"+"4".translate(SUP)}
,"Te":{"Name":"Tellurium","Period":5,"Group":16,"Atomic_no":52,"Mass":"127.6u","Type":"Non-Metal","Electronegativity":2.1,"Confi":"[Kr]5s"+"2".translate(SUP)+"4d"+"10".translate(SUP) +"5p"+"4".translate(SUP)}

,"F":{"Name":"Fluorine","Period":2,"Group":17,"Atomic_no":9,"Mass":"18.9u","Type":"Halogen","Electronegativity":3.98,"Confi":"[He]2s+2 2p+5"}  
,"Cl":{"Name":"Chlorine","Period":3,"Group":17,"Atomic_no":17,"Mass":"35.5u","Type":"Halogen","Electronegativity":3.16,"Confi":"[Ne]3s"+"2".translate(SUP) +"3p"+"5".translate(SUP)}
,"Br":{"Name":"Bromine","Period":4,"Group":17,"Atomic_no":35,"Mass":"79.9u","Type":"Halogen","Electronegativity":2.96,"Confi":"[Ar]4s"+"2".translate(SUP)+"3d"+"10".translate(SUP)  +"4p"+"5".translate(SUP)}
,"I":{"Name":"Iodine","Period":5,"Group":17,"Atomic_no":53,"Mass":"126.9u","Type":"Halogen","Electronegativity":2.66,"Confi":"[Kr]5s"+"2".translate(SUP)+"4d"+"10".translate(SUP)  +"5p"+"5".translate(SUP)}


,"He":{"Name":"Helium","Period":1,"Group":18,"Atomic_no":2,"Mass":"4.002u","Type":"Noble-Gas","Electronegativity":0,"Confi":"1s"+"2".translate(SUP)}
,"Ne":{"Name":"Neon","Period":2,"Group":18,"Atomic_no":10,"Mass":"20.81u","Type":"Noble-Gas","Electronegativity":0,"Confi":"[He]2s+2 2p+6"}
,"Ar":{"Name":"Argon","Period":3,"Group":18,"Atomic_no":18,"Mass":"39.9u","Type":"Noble Gas","Electronegativity":0,"Confi":"[Ne]3s"+"2".translate(SUP)+"3p"+"6".translate(SUP)}
,"Kr":{"Name":"Krypton","Period":4,"Group":18,"Atomic_no":36,"Mass":"83.8u","Type":"Noble Gas","Electronegativity":3,"Confi":"[Ar]4s"+"2".translate(SUP)+'3d'+'10'.translate(SUP)+"4p"+"6".translate(SUP)}
,"Xe":{"Name":"Xenon","Period":5,"Group":18,"Atomic_no":54,"Mass":"131.29u","Type":"Noble Gas","Electronegativity":2.6,"Confi":"[Kr]5s"+"2".translate(SUP)+'4d'+"10".translate(SUP)+"5p"+"6".translate(SUP)}
}
cont='y'
while cont=='Y'or cont=='y':
    #Menu:-

    pt()
    op=input('''What you want to do:
    \t1.Full data extraction :-
    \t2.Comparison of two elements:-
    \t3.Element game:-
    \t4.Nomenclature creater of element >100 :-\n\t''')
    ######################## FULL DATA EXTRACTION #######################
    if op=="1":
        x="y"
        while x=="y":
            e=input("Type Standard Element Symbol:")
            s=E[e].items()  
            i=1
            k=3
            for ky,vl in s:
                if i==4:
                    print(ky,"\t"*(k-1),":",vl)
                elif i==7:    
                    print(ky,"\t"*(k-2),":",vl) 
                else:
                    print(ky,"\t"*(k),":",vl)
                i+=1
            print()
            print()
            x=input("Wanna enter again (y/n):")
    ###################### ATOMIC RADIUS COMPARIOSN ##########################    
    if op=="2":
        op=input('''Choose  type of comparison:
        \ta.Atomic radius comparison:-
        \tb.Electronegativity Comparison:-
        \tc.Atomic mass comparison:-\n\t''')
        if op=="a":
            Ele1=input("Enter 1st element:-")
            Ele2=input("Enter element to be compared:-")
            x=y=0
            x=E[Ele1]["Atomic_no"]  
            y=E[Ele2]["Atomic_no"]
            if Ele1=="Al"or Ele1=="Ga" and Ele2=="Ga" or Ele2== "Al":
                print("\n\t!!!Exception case found!!!")
                print(" \tAl has a greater radius than Ga "," (Poor shielding effect)")

            elif Ele1=="In" or Ele1=="Tl" and Ele2=="Tl"or Ele2=="In":
                print("\n\t!!!! Exception case found !!!!")
                print("\tIn and Tl have approximately equal radius","(Lanthanoid Contraction)")

            elif x>y:
                print("\n\t",Ele1,"have a greater radius than",Ele2) 
            elif x<y:
                print("\n\t",Ele2,'have a greater radius than',Ele1)
            else:
                print("\n\t",'Dear User!!!\n You have entered the same element in both columns!!!')
        ###################### ELECTRONEGATIVITY COMPARER #####################
        if op=="b":
            Ele1=input("Enter 1st element:-")
            Ele2=input("Enter 2nd element:-")
            e1=e2=0
            e1=E[Ele1]["Electronegativity"]
            e2=E[Ele2]["Electronegativity"]
            if e1>e2:
                print('\n\t',Ele1,"is more electronegative than",Ele2)
            elif e1<e2:
                print('\n\t',Ele2,"is more electronegative than",Ele1)
            else:
                print('\n\t',"Same electronegative element")
        ##################ATOMIC MASS COMPARRISON######################
        if op=="c":
            Ele=input("Enter 1st element:-")
            Ele_=input("Enter 2nd element:-")
            e1=e2=0
            e1=float(E[Ele]["Mass"][:-1])
            e2=float(E[Ele_]["Mass"][:-1])
            if e1>e2:
                print("\n\tMass of",Ele,"is greater than",Ele_)
            elif e1<e2:
                print("\n\tMass of",Ele_,"is greater than",Ele)
            else:
                print("\n\tSame mass or same element")
    ################################### 1 PLAYER MODE #########################    
    if op=='3':
        op=input('''Choose the Mode:
        \tA.1 Player
        \tB.2 Player\n\t''')
        if op=="A":
            n=input("Enter name:-")
            c=0
            r=0
            for i in range(5):
                Sel=random.randint(1,54)
                q=''
                for i in E:
                    if E[i]["Atomic_no"]==Sel:
                        q=i
                print()
                print("\tIndentify the secret element:-")
                print("\t--------------------------")
                print("\t|","Configuration:-",E[q]["Confi"],"|","\n\t","|","Atomic mass:-",E[q]["Mass"],"|","\n\t","|","Group:-",E[q]["Group"],"|","\n\t")
                print("\tDear" ,n,",you have 3 chances to guess the element each wrong guess will give you lower  point:-\n")

                for i in range(3):
                    if i==0:
                        k=input("\t\tChance 1..Guess the element:-")
                        if k==q:
                            print("\t\t\tCongrats 100 points!!!")
                            c+=100
                            r+=1    
                            break
                        else:
                            print("\t\t\tSorry wrong guess 20 points deduced")
                            c-=20

                    elif i==1:

                        k=input("\t\tChance 2..Guess the element:-")
                        if k==q:
                            print("\t\t\tCongrats 50 points!!!")
                            c+=50
                            r+=1
                            break
                        else:
                            print("\t\t\tSorry wrong guess 30 points deducted")
                            c-=30
                    else:
                       k=input("\t\tChance 3..Guess the element:-")
                       if k==q:
                           print("\t\t\tCongrats 10 points!!!")
                           c+=10
                           r+=1
                           break
                       else: 
                           print("\t\t\tSorry wrong guess 40 points deducted")
                           c-=40
            
            print("\tYour final score is",c)  
            print("\tYou answered rightly",r,"out of 5 elements")
        ############################## 2 PLAYER MODE ###########################
        if op=="B":
            print("\t2 Player Mode:-")
            print("\t$========WELCOME========$")
            pass
            a=getpass.getpass("\t\tEnter 1st element:-")
            b=getpass.getpass("\t\tEnter 2nd element:-")
            n=int(input("\t\tEnter number of turns other player can have to guess each element:-"))
            for i in range(1):
                for j in range(n+1):
                    print("\t\t\t|","Configuration:-",E[a]["Confi"],"|","\n","|","Atomic mass:-",E[a]["Mass"],"|","\n","|","Group:-",E[a]["Group"],"|","\n")
                    g=input("\n\t\tGuess element 1:-")
                    if j+1==n and g!=a:
                        print("\t\t__!!!!Chances over!!!!__")
                        break
                    if g==a:
                        print("\t\t!!!Rightly guessed!!! :)")
                        break
                    else:
                        print("\t\tGuess again")
                for j in range(n+1):
                    print("\t\t\t|","Configuration:-",E[b]["Confi"],"|","\n","|","Atomic mass:-",E[b]["Mass"],"|","\n","|","Group:-",E[b]["Group"],"|","\n")            
                    g=input("\n\t\tGuess element 2:-")
                    if j+1==n and g!=b:
                        print("\t\t__!!!!Chances over!!!!__")
                        break
                    if g==b:
                        print("\t\t!!!Rightly guessed!!! :)")
                        break
                    else:
                        print("\t\tGuess again")  
    
    ############################ NOMENCLATURE ########################
    if op=="4":
        nmc=["nil","un","bi","tri","quad","pent","hex","sept","oct","enn","ium","um"]
        nomen=int(input("\tEnter element number above 100:-"))
        while nomen<100:
            nomen=int(input("\tEnter again:-"))
        s=list(str(nomen))
        name=''
        for i in s:
            name+=nmc[int(i)]
        if name[-1]=="i":
            name+=nmc[11]
        else:
            name+=nmc[10]
        print("\t\t",name.upper())
    clear_output(wait=True)    
    cont=input('Wanna go back to the menu (y/n):')


# In[ ]:





# In[ ]:




