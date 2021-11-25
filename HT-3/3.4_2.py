# Визнаю, воно дивне і мало працювати з першою частиною, але знань
# мені ще не вистачає, щоб зробити щось нормальне.

def coffee_drinks():
    coffee_drinks = {'espresso': 1,
           'ristretto': 2,
           'americano': 3,
           'cappuccino': 4,
           'frappuccino': 5,
           'macchiato': 6,
           'mochaccino': 7
            }
    return coffee_drinks

def recipes():
    water = [15, 'ml']
    milk = [50, 'ml']
    coffee_beans = [7, 'g']
    chocolate = [5, 'g']
    hot_chocolate = [50, 'ml']
    sugar = [5, 'g']
    ice = [3, 'spoons']
    def espresso():
        espresso = water[0]*2 + coffee_beans[0]
        print('You\'ve got', espresso, 'ml', 'of your Espresso. Just enjoy!')
    def ristretto():
        ristretto = water[0] + coffee_beans[0]
        print('You\'ve got', ristretto, 'ml', 'of your Ristretto. Just enjoy!')
    def americano():
        americano = water[0]*4 + coffee_beans[0]*2
        print('You\'ve got', americano, 'ml', 'of your Americano. Just enjoy!')
    def cappuccino():
        cappuccino = water[0]*2 + coffee_beans[0] + milk[0] + chocolate[0]
        print('You\'ve got', cappuccino, 'ml', 'of your Cappuccino. Just enjoy!')
    def frappuccino():
        frappuccino = water[0]*2 + coffee_beans[0]*3 + milk[0]*3 + hot_chocolate[0] + sugar[0] + ice[0]
        print('You\'ve got', frappuccino, 'ml', 'of your Frappuccino. Just enjoy!')
    def macchiato():
        macchiato = water[0]*2 + coffee_beans[0] + milk[0]
        print('You\'ve got', macchiato, 'ml', 'of your Macchiato. Just enjoy!')
    def mochaccino():
        mochaccino = hot_chocolate[0] + milk[0]*2 + water[0]*2 + coffee_beans[0] + chocolate[0]
        print('You\'ve got', mochaccino, 'ml', 'of your Mochaccino. Just enjoy!')
    coffee_recipes = {1: espresso,
           2: ristretto,
           3: americano,
           4: cappuccino,
           5: frappuccino,
           6: macchiato,
           7: mochaccino
            }
    drinks = coffee_drinks()
    for key in drinks:
        print(key, '->', drinks[key])
    choice = int(input('Enter the number your choice: '))
    output = coffee_recipes.get(choice)()

recipes()
