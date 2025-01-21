import logging
def printv2(script) :
    print(script)
    return script
def error_log(message) :
    logging.basicConfig(filename="error.log",
                    format='%(asctime)s %(message)s',
                    filemode='a')
    logger = logging.getLogger()
    logger.error(message)
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

