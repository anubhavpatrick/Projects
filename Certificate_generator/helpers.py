'''A module containing helper functions for the Certificate Generator'''

#Reference -https://www.geeksforgeeks.org/python-print-initials-name-last-name-full/
def abbreviated_name(s):
    '''python program to print initials of a name '''

    # split the string into a list 
    l = s.split()
    new = ""
  
    # traverse in the list 
    for i in range(len(l)-1):
        s = l[i]
          
        # adds the capital first character 
        new += (s[0].upper()+'.')
          
    # l[-1] gives last item of list l. We
    # use title to print first character in
    # capital.
    new += l[-1].title()
      
    return new 
 