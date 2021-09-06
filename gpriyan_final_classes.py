"""
Name: Priyanka Gnanasekaran
Class: CS 521 - Fall 1
Date:10/19/2020
Final Project - Home Expense & Retirement Calculator
"""

#Requirement User-Defined Class
class Monthly():
    '''This class calculates and return amount saved per month and per year.'''
    
    def __init__(self, monthly_income, monthly_expense,__r=""):
        #Requirement: an init() method that takes at least 1 argument 
        #Requirement: at least 1 private and 2 public self attributes
        
        self.monthly_in = monthly_income
        self.monthly_exp = monthly_expense
        
        #Requirement: assert unit test
        assert isinstance(monthly_income, float), 'Expense not in numbers!'
        self.__r= __r
    
    #Requirement:at least 1 private that take arguments, 
    #return values and are used by your program 
    def __sub__(self,monthly_income, monthly_expense):
        '''This private magic method helps calculate monthly amount'''
        
        self.__r = (self.monthly_in)-(self.monthly_exp)
        #Requirement: assert unit test
        assert self.__r != 0, 'Zero income, check your expense!' 
        return self.__r
    
    #Requirement:and 1 public method that take arguments, 
    #return values and are used by your program
    def monthly_cal(self):
        '''This public method calculates yearly amount'''
        
        self.__sub__(self.monthly_in, self.monthly_exp)
        result = self.__r * 12
        return result
     
    #Requirement: a repr() method          
    def __repr__(self):
        
        result=self.monthly_cal()
        return("Amount saved per month:${:,.2f}\nAmount saved per year:${:,.2f}"
                    .format(self.__r,result))
        
    def bi_weekly_cal(salary_in,g_expense):
        '''This static method returns monthly and yearly amounts'''
        
        while salary_in > 0:
            bi_w = salary_in - g_expense
            #Requirement: assert unit test
            assert bi_w != 0, 'Zero income, check your expense!'
            month_cal= (bi_w * 26) / 12 #bi-weekly to monthly calc
            amount_cal = month_cal * 12
            print("Amount saved per month:$",round(month_cal,2))
            break
        return amount_cal
    
    def weekly_cal(salary_in,g_expense):
        '''This static method returns monthly and yearly amounts'''
        
        while salary_in > 0:
            weekly_bal= salary_in - g_expense
            #Requirement: assert unit test
            assert weekly_bal != 0, 'Zero income, check your expense!'
            monthly_cal= (weekly_bal * 52) / 12 #weekly to monthly calc
            amt_cal = monthly_cal * 12
            print("Amount saved per month:$",round(monthly_cal,2))
            break
        return amt_cal
    
    def semimon_cal(salary_in,g_expense):
         '''This static method returns monthly and yearly amounts'''
        
         while salary_in > 0:
            semi_mon =salary_in - g_expense
            #Requirement: assert unit test
            assert semi_mon != 0, 'Zero income, check your expense!'
            monthly_cal = (semi_mon * 2) #semi-month to monthly calc
            amt_cal = monthly_cal * 12
            print("Amount saved per month:$",round(monthly_cal,2))
            break
         return amt_cal