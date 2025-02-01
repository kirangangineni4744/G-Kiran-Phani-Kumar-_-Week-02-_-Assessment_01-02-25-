class Payment():
    def process_payment(self):
        print("Processing payment")

class CreditCardPayment(Payment):
    def process_payment(self):
        print("Processing Credit Card Payment")

class PayPalPayment(Payment):
    def process_payment(self):
        print("Processing PayPal payment")

class BitCoinPayment(Payment):
    def process_payment(self):
        print("Processing BitCoin Payment")

credit_card=CreditCardPayment()
paypal=PayPalPayment()
bitcoin=BitCoinPayment()

credit_card.process_payment()
paypal.process_payment()
bitcoin.process_payment()