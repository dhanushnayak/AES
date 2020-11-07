from Crypto.Cipher import AES
import pandas as pd
import os
class sender():
    def set_key(self,key):
        self.key = bytes(key,'utf-8')
    def encode(self,data):
        self.data = bytes(data,'utf-8')
        cipher = AES.new(self.key, AES.MODE_GCM)
        self.nonce = cipher.nonce
        self.ciphertext, self.tag = cipher.encrypt_and_digest(self.data)
    def create_keys(self):
        d={}
        d['Key']=str(self.key)
        d['Ciphertext']=str(self.ciphertext)
        d['Tag']=str(self.tag)
        d['Nonce']=str(self.nonce)
        df=pd.DataFrame([d]).set_index("Key").to_csv(str(self.key,'utf-8')+'.csv', encoding='utf-8')
        print("File stored in {}".format(os.getcwd()))
        
