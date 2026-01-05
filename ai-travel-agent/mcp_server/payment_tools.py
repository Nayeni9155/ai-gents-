import stripe, os

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

def create_payment(amount, currency="inr"):
    intent = stripe.PaymentIntent.create(
        amount=int(amount * 100),
        currency=currency,
        payment_method_types=["card"]
    )
    return {"client_secret": intent.client_secret}
