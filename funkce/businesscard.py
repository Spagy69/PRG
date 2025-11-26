def businessCard(**person):
    print("*" * 30)
    print("* First Name:", person["fname"])
    print("* Last Name:", person["lname"])
    print("* Job:", person["job"])
    print("*" * 30)

businessCard(fname="Vít", lname="Machač", job="Developer")
businessCard(fname="Matěj", lname="Adamec", job="CEO")
businessCard(fname="Samuel", lname="Pele", job="Janitor")        