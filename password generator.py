 
import random
password="ABCDEFGHIJKLMNOPQRSTWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$%^&*_" 
l=int(input("Enter the length of password:"))
p="".join(random.sample(password,l))
print("The password given length",l,"is ",p)