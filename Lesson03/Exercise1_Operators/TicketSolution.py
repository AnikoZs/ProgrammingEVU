class Ticket:
    # Constructor
    def __init__(self, age, has_ticket, is_banned):
        self.age = age
        self.has_ticket = has_ticket
        self.is_banned = is_banned

    # Check festival entry rules
    def can_enter(self):
        if self.age >= 18 and self.has_ticket and not self.is_banned:
            return "Enjoy the festival!"
        else:
            return "You cannot enter."


def test():
    age = int(input("How old are you? "))
    has_ticket = input("Do you have a ticket? (true/false): ").lower() == "true"
    is_banned = input("Are you banned? (true/false): ").lower() == "true"

    ticket = Ticket(age, has_ticket, is_banned)

    print(ticket.can_enter())


test()