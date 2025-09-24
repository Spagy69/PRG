def playerCard(*prise_money, **person):
    prise_money_sum = sum(prise_money)
    print("*" * 30)
    print("* First Name:", person["fname"])
    print("* Last Name:", person["lname"])
    print("* Ranking:", person["ranking"])
    print("* Prise Money Sum:", prise_money_sum)
    print("*" * 30)

playerCard(9000, 8500, 11900, 230000, fname="Novak", lname="Djokovic", ranking=1)
playerCard(300000, 100000, fname="Rafael", lname="Nadal", ranking=2)