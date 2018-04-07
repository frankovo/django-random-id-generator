import string
import random

LENGTH = 11

def id_generator():
    random_string = string.digits
    key = ''.join([random.SystemRandom().choice(random_string) for i in range(random.randint(11, LENGTH))])
    print ('FJK-'+key)
    
    
id_generator()
