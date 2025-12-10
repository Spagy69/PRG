class Account:
    def __init__(self, username, followers):
        self.username = username
        self.followers = followers

    def addFollowers(self, count):
        self.followers += count

        if self.followers < 0:
            self.followers = 0

    def __str__(self):
        return (f"Uživatel: {self.username}, sledujících: {self.followers}")

    def __del__(self):
        print(f"Uživatel {self.username} byl odstraněn ze systému.")

class VerifiedAccount(Account):
    def __init__(self, username, followers, badge_color):
        super().__init__(username, followers)
        self.badge_color = badge_color

    def __str__(self):
        return super().__str__() + f", ověřený účet (odznak: {self.badge_color})"

    def promote(self, count):
        self.followers += count

        if self.followers < 0:
            self.followers = 0

        print(f"Účet {self.username} získal {count} nových sledujících!")


user1 = Account("vit.machac", 150)
user1.addFollowers(12)
print(user1.__str__())
del user1

print(100 * "-")

star = VerifiedAccount("opikula28", 6800, "fialová")
star.promote(670)
print(star.__str__())
del star