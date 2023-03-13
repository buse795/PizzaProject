import csv
import datetime

# Pizza üst sınıfı oluşturulur
class Pizza:
    def get_description(self):
        return self.__class__.__name__

    def get_cost(self):
        return self.__class__.cost

# Pizza alt sınıf oluşturulur
class Klasik(Pizza):
    cost = 80.0

    def __init__(self):
        # Her alt satıra özellikleri yazılır
        self.description = "Klasik malzemeler: mozzarella peyniri, kırmızı biber, domates, mantar, siyah zeytin, sosis"
        print(self.description +"\n")

class Margarita(Pizza):
    cost = 70.0

    def __init__(self):
        self.description = "Margarita malzemeler: domates, mozarella, fesleğen, zeytinyağı"
        print(self.description +"\n")
class TurkPizza(Pizza):
    cost = 90.0

    def __init__(self):
        self.description = "Türk Pizza malzemeler: kaşar peyniri, mozzarella peyniri, kırmızı biber, domates, mantar"
        print(self.description +"\n")
class SadePizza(Pizza):
    cost = 50.0

    def __init__(self):
        self.description = "Sade Pizza malzemeler: mantar, mısır , biber, domates, vegan peynir, zeytin"
        print(self.description +"\n")

# Decorator üst sınıf oluşturulur
class Decorator(Pizza):
    def __init__(self, topping):
        self.component = topping
    
    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() + ' ;' + Pizza.get_description(self)
    
# Decorator alt sınıf oluşturulur 
class Zeytin(Decorator):
    cost = 3.0

    def __init__(self, topping):
        Decorator.__init__(self, topping)


class Mantar(Decorator):
    cost = 4.0

    def __init__(self, topping):
        Decorator.__init__(self, topping)


class Peynir(Decorator):
    cost = 5.0

    def __init__(self, topping):
        Decorator.__init__(self, topping)


class Et(Decorator):
    cost = 11.0

    def __init__(self, topping):
        Decorator.__init__(self, topping)


class Sogan(Decorator):
    cost = 5.0

    def __init__(self, topping):
        Decorator.__init__(self, topping)


class Misir(Decorator):
    cost = 5.0

    def __init__(self, topping):
        Decorator.__init__(self, topping)

# Menuyu ekrana yazdırmak için main fonksiyonu oluşturulur
def main():
    with open("Pizza_Order_System\Menu.txt") as cust_menu:
        for i in cust_menu:
            print(i, end="")

    class_dict = {1: Klasik, 
                  2: Margarita, 
                  3: TurkPizza, 
                  4: SadePizza,
                  5: Zeytin, 
                  6: Mantar,
                  7: Peynir,
                  8: Et, 
                  9: Sogan, 
                  10: Misir} 
    

    code = input("Lütfen Pizzanızı Seçiniz: ")
    while code not in ["1", "2", "3", "4"]:
        code = input("Yanlış Tuşlama Yaptınız: ")

    order = class_dict[int(code)]()

    while code != "*":
        code = input("Ek Malzeme Almak İçin Tuşlama Yapınız (Direkt Siparişinizi Onaylamak İçin '*' Tuşuna Basınız): ")
        if code in ["5","6","7","8","9","10"]:
            order = class_dict[int(code)](order)

    print("\n"+order.get_description().strip() +
          "; $" + str(order.get_cost()))
    print("\n")

    #Sipariş bilgileri oluşturulur
    print("Sipariş Bilgileri\n")
    isim = input("İsminiz: ")
    TC = input("TC numaranız: ")
    KKN = input("Kredi kartı numaranız giriniz: ")
    KKS = input("Kredi Kartı şifrenizi giriniz: ")
    time_of_order = datetime.datetime.now()

    with open('Orders_Database.csv', 'a') as orders:
        orders = csv.writer(orders, delimiter=',')
        orders.writerow([isim, TC, KKN,KKS, order.get_description(), time_of_order])
    print("Siparişiniz Onaylandı")


main()