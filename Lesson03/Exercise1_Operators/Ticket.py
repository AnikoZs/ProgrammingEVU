class Ticket:
    def __init__(self, age, has_ticket):
        self.age = age
        self.has_ticket = has_ticket

    def can_enter(self):
        if self.age >= 18 and self.has_ticket:
            return "Velkommen ind!"
        elif self.age < 18 and self.has_ticket:
            return "Du har billet, men du er for ung."
        else:
            return "Du kan ikke komme ind."


def test():
    age = int(input("Hvor gammel er du? "))

    has_ticket = input("Har du billet? (true/false): ").lower() == "true"

    ticket = Ticket(age, has_ticket)

    print(ticket.can_enter())


if __name__ == "__main__":
    test()
