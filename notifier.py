# Kafka related imports
from kafka import KafkaConsumer

# Twilio related imports
from twilio.rest import Client

account_sid = "AC01b9db6780e4c48742ddd13434b292fe"
auth_token = "ecc5932e2b26b029fd6530ff016f5cd6"

TWILIO_NUMBER = "+16197176634"
TARGET_NUMBER = "+27798792873"

client = Client(account_sid, auth_token)

def send_notification(text):
    message = client.messages.create(
            to=TARGET_NUMBER,
            from_=TWILIO_NUMBER,
            body=text)

if __name__ == '__main__':
    consumer = KafkaConsumer('REFILL')
    for event in consumer:
        print(f'Dispenser requires refill: {event}')
        send_notification(event.value)
