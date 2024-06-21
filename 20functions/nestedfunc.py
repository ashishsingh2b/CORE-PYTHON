def myname():
    def mysurname():
        print("Singh")
    print("Ashish")
    mysurname()

myname()


def myname():
    def mysurname():
        return "Singh"
    result= mysurname() +  " Ashish"
    return result
    


    

ad=myname()
print(ad)
