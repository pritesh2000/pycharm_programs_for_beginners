import pickle

# # Pickling a python object
# # MINE : here we made a file by running this program
# cars = ["Audi", "BMW", "Maruti Suzuki", "Harryti Tuzuki"]
# file = "mycar.pkl"
# fileobj = open(file, 'wb')
# pickle.dump(cars, fileobj)
# fileobj.close()


file = "mycar.pkl"
fileobj = open(file, 'rb')      # This will read binary
mycar = pickle.load(fileobj)
print(mycar)
print(type(mycar))
