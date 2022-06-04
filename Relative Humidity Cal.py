'''Q: Make a Program named “YourName’s Weather Forecast”. It will show the user a welcome message.
Then asks the User’s name. Then Addressing his name, your program will ask the user about the region you stay in.
Then it will ask for the temperature in degrees Celsius,
and Dew Point in degrees Celsius. Make the program such, so that the user can compare the Relative Humidity in
as many regions as he/she wants. It will show the user, which region has the highest and the lowest Relative Humidity
of all inputs. It also should show the sequence from low humidity to high humidity. If the user does not want to
compare, he/she can calculate RH for only one region. You can also make the program more user friendly,
by taking input from any unit (Celsius or Fahrenheit).'''

print("Dibakar’s Weather Forecast")
print("𝑤𝑒𝑙𝑐𝑜𝑚𝑒 𝑡𝑜 𝐷𝑖𝑏𝑎𝑘𝑎𝑟’𝑠 𝑊𝑒𝑎𝑡ℎ𝑒𝑟 𝐹𝑜𝑟𝑒𝑐𝑎𝑠𝑡")
User_Name = str(input("please enter your name:"))
print(User_Name)
Region_Name = str(input("please enter the region you stay in (A, B, C, D, E):"))
print(Region_Name, '\n')
T_c = float(input("please enter the temperature:"))
print('T_c=',T_c,'Deg C')
DP_c = float(input("please enter the Dew point:"))
print('DP_c=', DP_c,'Deg C')

Converter1 = str(input("Do you want to convert T_c unit in Fahrenheit:"))
Converter2 = str(input("Do you want to convert Dp_c unit in Fahrenheit:"))
print("\n")
if Converter1 == "yes" and Converter2 == "yes":
    T_f = (T_c * 1.8)+ 32
    DP_f = (DP_c * 1.8) + 32
    print('T_f=',T_f, 'Deg F', '\n')
    print('DP_f', DP_f, 'Deg F', '\n')
elif Converter1 != "yes" and Converter2 == "yes":
    print("Need to input equivalent unite")
    Converter1 = str(input("Do you want to convert T_c unit in Fahrenheit:"))
    T_f = (T_c * 1.8) + 32
    DP_f = (DP_c * 1.8) + 32
    print('T_f=', T_f, 'Deg F', '\n')
    print('DP_f', DP_f, 'Deg F', '\n')
elif Converter1 == "yes" and Converter2 != "yes":
    print("Need to input equivalent unite")
    Converter2 = str(input("Do you want to convert Dp_c unit in Fahrenheit:"))
    T_f = (T_c * 1.8) + 32
    DP_f = (DP_c * 1.8) + 32
    print('T_f=', T_f, 'Deg F', '\n')
    print('DP_f', DP_f, 'Deg F', '\n')
else:
    print('T_c=', T_c, 'Deg F', '\n')
    print('DP_c', DP_c, 'Deg F', '\n')



while Converter1 == Converter2:
    import math
    if Converter1 == "yes" and Converter2 == "yes":
        xf = ((17.625 * DP_f) % (243.04 + DP_f))
        print(math.exp(xf), '\n')
        yf = ((17.625 * T_f) % (243.04 + T_f))
        print(math.exp(yf), '\n')
        RH = 100 * (xf % yf)
        print('RH=',RH, '\n')

    elif Converter1 == "no" and Converter2 == "no":
        xc = ((17.625 * DP_c) % (243.04 + DP_c))
        print(math.exp(xc), '\n')
        yc = ((17.625 * T_c) % (243.04 + T_c))
        print(math.exp(yc), '\n')
        RH = 100 * (xc % yc)
        print('RH=',RH, '\n')
    else:
        print("start again")
    break
print("Thank you")

while Converter1 == Converter2:
    Comparison = str(input("Do you want to compare the Relative Humidity in different regions:"))
    if Comparison == "yes":
        Region = str(input("please enter the region(A, B, C, D, E):"))
        Unite = str(input("please enter preferred unite (C/F):"))
        if Unite == "C":
            T_c = float(input("please enter the temperature:"))
            DP_c = float(input("please enter the Dew point:"))
            xc = ((17.625 * DP_c) % (243.04 + DP_c))
            print(math.exp(xc), '\n')
            yc = ((17.625 * T_c) % (243.04 + T_c))
            print(math.exp(yc), '\n')
            RH1 = 100 * (xc % yc)
            print('RH1=',RH1, '\n')
            if RH > RH1:
                print('RH > RH1')
            elif RH < RH1:
                print('RH > RH1')
            else:
                print('RH = RH1')

        elif Unite == "F":
            T_f = float(input("please enter the temperature:"))
            DP_f = float(input("please enter the Dew point:"))
            xf = ((17.625 * DP_f) % (243.04 + DP_f))
            print(math.exp(xf), '\n')
            yf = ((17.625 * T_f) % (243.04 + T_f))
            print(math.exp(yf), '\n')
            RH1 = 100 * (xf % yf)
            print('RH1=',RH1, '\n')
            if RH > RH1:
                print('RH > RH1')
            elif RH < RH1:
                print('RH > RH1')
            else:
                print('RH = RH1')

    else:
        print("Thanks for choosing the application", '\n')

    Comparison = str(input("Do you want to compare the Relative Humidity in different regions:"))
    if Comparison == "yes":
        Region = str(input("please enter the region(A, B, C, D, E):"))
        Unite = str(input("please enter preferred unite (C/F):"))
        if Unite == "C":
            T_c = float(input("please enter the temperature:"))
            DP_c = float(input("please enter the Dew point:"))
            xc = ((17.625 * DP_c) % (243.04 + DP_c))
            print(math.exp(xc), '\n')
            yc = ((17.625 * T_c) % (243.04 + T_c))
            print(math.exp(yc), '\n')
            RH2 = 100 * (xc % yc)
            print('RH2=',RH2, '\n')
            if RH > RH1 > RH2:
                print('RH > RH1 > RH2')
            elif RH < RH1 <RH2:
                print('RH < RH1 <RH2')
            elif RH1 < RH <RH2:
                print('RH1 < RH <RH2')
            elif RH1 > RH >RH2:
                print('RH1 > RH >RH2')
            elif RH > RH2 >RH1:
                print('RH > RH2 >RH1')
            elif RH < RH2 < RH1:
                print('RH < RH2 <RH1')
            else:
                print('RH = RH1 = RH2')

        elif Unite == "F":
            T_f = float(input("please enter the temperature:"))
            DP_f = float(input("please enter the Dew point:"))
            xf = ((17.625 * DP_f) % (243.04 + DP_f))
            print(math.exp(xf), '\n')
            yf = ((17.625 * T_f) % (243.04 + T_f))
            print(math.exp(yf), '\n')
            RH2 = 100 * (xf % yf)
            print('RH2=',RH2, '\n')
            if RH > RH1 > RH2:
                print('RH > RH1 > RH2')
            elif RH < RH1 < RH2:
                print('RH < RH1 <RH2')
            elif RH1 < RH < RH2:
                print('RH1 < RH <RH2')
            elif RH1 > RH > RH2:
                print('RH1 > RH >RH2')
            elif RH > RH2 > RH1:
                print('RH > RH2 >RH1')
            elif RH < RH2 < RH1:
                print('RH < RH2 <RH1')
            else:
                print('RH = RH1 = RH2')
    else:
        print("Thanks for choosing the application", '\n')
    break
print("Thanks for choosing the application")

