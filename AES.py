from Sender import sender
from Receiver import receiver

def main():
    send = sender()
    send.set_key("ahanushppassword")
    #set_key must be 16
    send.encode("DHanush")
    send.create_keys()
    rec = receiver()
    rec.load_key("D://Programs/AES/ahanushppassword.csv")
    rec.decode()

main()