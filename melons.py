import random

"""Classes for melon orders."""

class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from."""

    order_type = None
    tax = 0
    
    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False
    

    def get_base_price(self):
        """Calculates base price"""

        base_price = random.choice(range(5, 10))

        return base_price

    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()
        flat_fee = 3.00
        total = (1 + self.tax) * self.qty * base_price
        if self.species == "christmas":
            total *= 1.5
        if self.order_type == "international" and self.qty < 10:
            total += flat_fee

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        super().__init__(species, qty)
        """Initialize melon order attributes."""
        self.country_code = country_code


    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """Government order"""

    order_type = "government"
    tax = 0.00

    def __init__(self, species, qty):
        super().__init__(species, qty)
        self.passed_inspection = False

    def mark_inspection(self, passed):
        self.passed_inspection = passed