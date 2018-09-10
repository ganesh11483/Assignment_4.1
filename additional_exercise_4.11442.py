
# coding: utf-8

# In[9]:


import fibo


# In[10]:


fibo.fib2(10)


# In[11]:


import palindrome


# In[12]:


palindrome.ispalindrome('maddam')


# Write a Python program which accepts a list named : randomList = ['a', 0,
# 2]. Use exception handling using try-catch which gives the output as:

# In[17]:


def reciprocal_List(list_rec):
    for list1 in list_rec:
        print("The Entry is {}".format(list1))
        try:
            r=1/list1
        except Exception as ex:
            print("Oops! {} occured.".format(ex.__class__))
        else:
            print("The reciprocal of {} is {} occured.".format(list1,r))
        finally:
            print("Next Entry.")
            
randomList = ['a', 0, 2]
reciprocal_List(randomList)

