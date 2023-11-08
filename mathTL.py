'''
This is the maths T Level library
'''

class MathTL():
    '''The MathTL libray developed by T level students
       This will provide a range of commonly used algorithems
       and helper utilities for computer science
    '''

    @staticmethod
    def add(n1:float,n2:float) -> float:
        '''
        This is a demonstration method only, adding 2 numbers
        Behaviour for other datatypes is not implimented

        Parameters
        ----------
        n1 : float
            The first addend
        n2: float
            The second addend

        Returns
        -------
        float
            The Sum of the addends
        '''

        try:
            n1 = float(n1)
        except ValueError:
            n1 = 0
       
        return n1 + n2

    @staticmethod
    def sub(n1:float,n2:float) -> float:
        '''
        This is a demonstration method only, subtracting 2 numbers
        Behaviour for other datatypes is not implimented
        Submitted by Paul Smith

        Parameters
        ----------
        n1 : float
            The minuend
        n2: float
            The subtrahend

        Returns
        -------
        float
            The Sum of the addends
        '''

        try:
            n1 = float(n1)
        except ValueError:
            n1 = 0

        return n1 - n2

    def bubble_sort(num):
      num2 = num.copy()
      n = len(num2)
      #nested loops
      for i in range(0, n-1): # outer loop
          for j in range(0,n-i-1):#inner loop

              if num2[j]>num2[j+1]: # check if swap
                  #swap # easy way
                  num2[j],num2[j+1] = num2[j+1],num2[j]

      return num2 
    def Selection_sort(data:list):#you need 2 lists one is the
    
      sorted_list=[] 
      unsorted_list = data #sorted list 2nd is the unsorted list
      for i in range(0,len(unsorted_list)):
        if unsorted_list[0]=int(unsorted_list):
          smallest=99999999999999
        else:
            smallest='Z'
        for j in range(0,len(unsorted_list)):  
         if unsorted_list[j]<smallest:
            smallest=unsorted_list[j]
        sorted_list.append(smallest)
        unsorted_list.pop(unsorted_list.index(smallest))
      return(sorted_list)  


