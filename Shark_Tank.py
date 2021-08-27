# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 23:10:06 2021

@author: JIBIN
"""

def Shark_Tank():
    import numpy as np 
    import time
    import sys
    initial=1000000
    a=np.random.randint(5,50)
    b=np.random.random(1)
    capital=int(np.random.random(1)*100)
    equity=int(np.random.choice(51))
    valuation=capital/(equity/100)
    print("We are seeking an investment of ",capital, " thousand with an equity stake of ",equity,"% of our company")
    print("Business Valuation is ",valuation," thousand")
    print("Revenue: USD",int(np.random.random(1)*60), "thousand")
    print("Counter Offer? (1.Yes/2.No/3. Not Interested)")
    d=int(input("Enter your choice(1/2/3):"))
    if d==1:
        counter_capital=int(input("I will give you capital of USD "))
        counter_equity=int(input("for an equity percentage of "))
        print("That would be for a valuation of USD ", counter_capital/(counter_equity/100)," thousand")
        time.sleep(2)
    elif d==2:
        time.sleep(2)
        print("I will give you what you ask for. I like your offer")
        sys.exit(0)
             
    else:
        print("Not interested in investing, but goood luck)")
        sys.exit(0)
        
    z=np.random.randint(2)
    if z==0:
        time.sleep(3)
        print("The counter offer looks good. We have a deal!")
        initial=initial-counter_capital
        sys.exit(0)
    else:
        time.sleep(2)
        e_counter_equity=np.random.randint(equity-20,counter_equity)
        e_counter_capital=np.random.randint(counter_capital-10,capital)
        print("How about we give ", e_counter_equity,"% of our company for USD ",e_counter_capital," thousand?")
        time.sleep(2)
        print("That would be a business valuation of ", e_counter_capital/(e_counter_equity/100), "thousand")
    j=int(input("Will you take the counter offer of the entrepreneur? (1.Yes/2.No)"))
    if j==1:
        time.sleep(2)
        print("I will take that offer! Thats a deal!")
    else:
        print("Sorry mate, I cannot give you that with this valuation")
        
    
Shark_Tank()
