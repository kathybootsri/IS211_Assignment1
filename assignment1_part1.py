# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 09:32:53 2020

@author: kbootsri
"""

"""Part 1: Exceptions:"""

class ListDivideException(Exception):
    """Type Error: First parameter must be a list"""
    pass

class ZeroDivide(Exception):
    """Value Error: Divide value cannot be zero"""
    pass

 
"""Part 1: ListDivide Function: Returns either the number of valid values divisible by divide value or exceptions"""   
def listDivide(numbers, divide=2):
    try: 
        if not isinstance(numbers, list):
            raise ListDivideException
            
        if divide == 0:
            raise ZeroDivide
            
        divisibles = []
        if len(numbers) == 0:
            print(0)
        else: 
            for x in numbers:
                if x%divide == 0:
                    divisibles.append(x)
                
            print(len(divisibles))
        
    except ListDivideException:
        print("Type Error: First parameter must be a list")
    except ZeroDivide:
        print("Value Error: Divide value cannot be zero")
    except Exception as e:
        print(str(e))
        
 
"""Part 1: testListDivide Function: Only returns exceptions"""   

def testListDivide(numbers, divide=2):
    try: 
        if not isinstance(numbers, list):
            raise ListDivideException
            
        if divide == 0:
            raise ZeroDivide
            
        divisibles = []
        if len(numbers) == 0:
            return 0
        else: 
            for x in numbers:
                if x%divide == 0:
                    divisibles.append(x)
                    
    except ListDivideException:
        print("Type Error: First parameter must be a list")
    except ZeroDivide:
        print("Value Error: Divide value cannot be zero")
    except Exception as e:
        print(str(e))
     
"""Part 1: Test Inputs for Functions"""  
listDivide([1,2,3,4,5])
listDivide([2,4,6,8,10])
listDivide([30, 54, 63,98, 100], divide=10)
listDivide([])
listDivide([1,2,3,4,5], 1)


testListDivide([1,2,3,4,5]) #Expected Output: No output
testListDivide('dog')
testListDivide([30, 54, 63,98, 100], divide=0)