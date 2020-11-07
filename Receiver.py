from Crypto.Cipher import AES
import pandas as pd

class receiver():
    def load_key(self,path):
        try:
            df=pd.read_csv(path)
        except:
            print("File not found in {}".format(path))
        try:
            self.key=bytes(df['Key'].values[0][2:-1],'utf-8')
        except:
            print("Key Not Found ")
        try:
            self.ciphertext = bytes(df['Ciphertext'].values[0][2:-1],'utf-8')
        except:
            print("Data Error")
        try:
            self.nonce = bytes(df['Nonce'].values[0][2:-1],'utf-8')
        except:
            print("Nonce Error")
        try:
            self.tag = bytes(df['Tag'].values[0][2:-1],'utf-8')
         
        except:
            print("Tag not Found")
        #print(df)
    def decode(self):
        
            cipher = AES.new(self.key, AES.MODE_GCM,nonce=self.nonce)
            plaintext = cipher.decrypt_and_verify(self.ciphertext,self.tag)
            try:
                cipher.verify(self.tag)
                print("The message is authentic:", str(plaintext,'utf-8') )
            except ValueError:
                print("Key incorrect or message corrupted")
        

