'''
Problem-13 Design a simple address book which stores the contacts.
'''

try:
    import cPickle as pickle
except:
    import pickle
from hashlib import sha256

class Contact:
    def __init__(self,name,email,phone):
        self.name = name
        self.email=email
        self.phone = phone

    def __str__(self):
        return "Name:{0}\nEmail address:{1}\nPhone:{2}".format(self.name,self.email,self.phone)

    def change_name(self,name):
        self.name = name

    def change_email(self,email):
        self.email = email

    def change_phone(self,phone):
        self.phone = phone


class PhoneBook:
    def __init__(self,name):
        try:
            self.__name =self.createName(name) +'.db'
            self.__db = open(self.__name,'rb')
            self.__entries = pickle.load(self.__db)
            self.__db.close()
        except:
            self.__db = open(self.__name, 'wb')
            self.__entries = {}
            self.__db.close()

    def  __update(self):
        self.__db = open(self.__name,'wb')
        pickle.dump(self.__entries, self.__db, -1)
        self.__db.close()

    def addEntry(self,contact):
        name = contact.name
        if name in self.__entries:
            print("Contact already added")
        else:
            self.__entries[name] = contact
            self.__update()
            print("Contact added successfully")



    @staticmethod
    def createName(mname):
        hsh = sha256(mname.encode('utf-8')).hexdigest()
        print(hsh)
        return ''.join(hsh[1::3])



ph = PhoneBook("jithu")
ph.addEntry(Contact("jithu","jithsmy@gmail.com","xxxxxxxx"))