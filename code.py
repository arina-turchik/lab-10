import my_package

s = 27
minn = 489
maxx = 594437

gen = my_package.module9.random_number(s, minn, maxx)
for r in range(10):
    random_n = next(gen)
    print(random_n)

hero=my_package.module8.hero_hp()
hero(20)

