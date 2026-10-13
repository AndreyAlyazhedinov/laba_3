from abc import ABC, abstractmethod


class PricingStrategy(ABC):
    @abstractmethod
    def calculate(self, base_price):
        pass


class RegularPricing(PricingStrategy):
    def calculate(self, base_price):
        return base_price


class DiscountPricing(PricingStrategy):
    def __init__(self, discount_percent):
        self.discount_percent = discount_percent

    def calculate(self, base_price):
        return base_price * (1 - self.discount_percent / 100)


class Order:
    def __init__(self, base_price, strategy: PricingStrategy):
        self.base_price = base_price
        self.strategy = strategy

    def total(self):
        return self.strategy.calculate(self.base_price)


if __name__ == "__main__":
    regular_order = Order(1000, RegularPricing())
    discount_order = Order(1000, DiscountPricing(15))
    print("Обычная цена:", regular_order.total())
    print("Цена со скидкой:", discount_order.total())
