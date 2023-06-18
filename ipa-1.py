
#first problem

password=input("what is your password? ")
correct_password= "dodo"
if correct_password==password:
    print("tama")
else:
    print("mali")
    
#second problem 

temperature=int(input("what is the temperature today? "))
degree_or_farenheit=input("Is this in C or F? ")
def temp_conv(temperature):
        if degree_or_farenheit=="C":
            converted=9/5*temperature+32
            output="New Temperature is " + str(converted) + "°F"
        elif degree_or_farenheit=="F":
            converted=((temperature-32)*5/9)
            output="New Temperature is " + str(converted) + "°C"
        else:
            return "error"
        return output

print(temp_conv(temperature))
                
#third problem
def change(x):

    thousands=x//1000
    output="1000 bill = " + str(thousands) + "\n"  
    x=x%1000
    five_hundreds=x//500
    output=output +"500 bill = " + str(five_hundreds) + "\n"
    x=x%500
    two_hundreds=x//200
    output=output +"200 bill = " + str(two_hundreds) + "\n"
    x=x%200
    hundreds=x//100
    output=output +"100 bill = " + str(hundreds) + "\n"
    x=x%100
    fifties=x//50
    output=output +"50 bill = " + str(fifties) + "\n"
    x=x%50
    twenties=x//20
    output=output +"20 bill = " + str(twenties) + "\n"
    x=x%20
    tens=x//10
    output=output +"10 bill = " + str(tens) + "\n"
    x=x%10
    fives=x//5
    output=output +"5 bill = " + str(fives) + "\n"
    x=x%5
    ones=x//1
    output=output +"1 bill = " + str(ones) + "\n"
    return(output)
print(change(9821))
    
#my first attempt of the fourth problem which used min function
eggs=65//1
wheat=10//3
milk=108//3
sugar=99//2

print("you can bake " + str(min(eggs,wheat,milk,sugar)) + " cakes")

#my second attempt of the fourth problem which uses ifs
eggs=65//1
wheat=10//3
milk=108//3
sugar=99//2

if eggs <= wheat and eggs<=milk and eggs<=sugar:
    print("you can bake",eggs,"cake")
elif wheat <= eggs and wheat<=milk and wheat<=sugar:
    print("you can bake",wheat,"cake")
elif milk <= eggs and milk<=wheat and milk<=sugar:
    print("you can bake",milk,"cake")
elif sugar <= eggs and sugar<=wheat and sugar<=milk:
    print("you can bake",sugar,"cake")
else:
    print("error")