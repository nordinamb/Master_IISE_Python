import time 
def printv2(script) :
    print(script)
    return script
def error_log(message) :
    with open("error.log", "a") as f:
        f.write(+str(time.ctime()) "  :" + message + "\n")

def read_file(filename):
    try :
        file=open (filename, "r")
        lignes = file.readlines()
        for ligne in lignes:
            print (ligne) 
        
    except FileNotFoundError:
        m= printv2("le fichier n'existe pas")
        error_log(m)
        
    finally:
        if 'file' in locals():
            file.close()

read_file("example.txt")

