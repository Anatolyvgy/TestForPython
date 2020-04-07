#Привет
#Демонстрирует создание переменных

#request = "Привет, как тебя зовут?"
#print(request.title())
#print("Привет, назовите ваше имя")
#name = input()
#print("Привет, ", name)
#input("Click Enter key to Exit")
#comments
print("Введите пожалуйста Ваш вес")
weight = float(input())
moon_weight = weight/6
print("Знаете ли вы, сколько бы вы весили на Луне?")
print("Нажмите 1, если хотите это узнать, если не хотите, нажмите 0")
moon = int(input())
if moon == True:
    print("Ваш вес:  ", moon_weight, " кг")
else:
    print("Значит в другой раз")
print("А хотите знать, сколько на Солнце?")
print("Нажмите 1, если хотите это узнать, если не хотите, нажмите 0")
sun = int(input())
if sun == True:
    print("Ваш вес: ", weight*2.71, "кг")
else:
    print("Значит в другой раз")
print("Спасибо что приняли участие в нашем опросе")
print("До свидания")


#sun = weight * 2.71


    
