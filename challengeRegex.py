import re

    
txt = "almdrasa is your way to learn programming the right way. Almdrasa motivate students to do more. Almdrasa help students practice on what they have learned through the course. Almdrasa are one of a kind because they were made by professionals. almdrasa look and feel is one of a kind. almdrasa wishes you a good learning. thanks."    

regex = re.sub("almdrasa \w{3}","Almdrasa",txt,3)

print(regex)