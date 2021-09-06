"""
Name: Priyanka Gnanasekaran
Class: CS 521 - Fall 1
Date:10/8/2020
Final Project - Home Expense & Retirement Calculator
"""

#Requirement: The class must be imported by main program 
from gpriyan_final_classes import Monthly
import datetime

print("\nHome Expense and Retirement Calculator.\n") 
 
#Requirement: User-Defined Functions
def retire_calc(current_savings,current_age,retirement_age,
                avg_annual_return,yearly_contribution):
    '''This function calculates retirement amount and returns it.'''
    
    #Requirement: assert unit test
    assert retirement_age >= current_age, 'Please enter your valid age!'
    year_s = retirement_age - current_age
    
    #retirement main calculation
    retire_amt = current_savings * ((avg_annual_return) ** (year_s))
    while year_s > 0:
        year_s -= 1
        retire_amt += yearly_contribution * (avg_annual_return ** year_s)
    retire_amt = round(retire_amt,2)
    assert retire_amt != 0, 'Please enter valid data!'
    #Requirement: assert unit test
    
    return retire_amt

      
if __name__ == "__main__":
    
    print("\nPlease enter your choice of calculation:(e.g m for monthly)")
    u_choi=input("Bi-weekly = bw, Weekly = w,"
                 "\nMonthly = m, Semi-Monthly = sm:")
    u_choi=u_choi.lower() #taking input as lower case
    
    #Requirement: Iteration type WHILE and FOR
    while u_choi.isalnum():
        
        #Requirement: try blocks
        try:
            #calcuations for four types of income.
            #Requirement: Conditional IF
            if u_choi == 'bw':
            
                salary_in= float(input("Please Enter your Bi-weekly income:$"))
                Expense=input("Type bi-weekly expenses with space inbetween:")
                G_expense = Expense.split() 
                #sum of all expenses in list
                #Requiement: container type and iteration type
                g_expense=sum([float(e) for e in G_expense])
                print("\nTotal Amount spent for this bi-week:$",g_expense)
                #instantiate class methods
                res= Monthly.bi_weekly_cal(salary_in,g_expense)
                print("Amount saved per year:$",round(res,2))
               
            elif u_choi== 'm':
            
                salary_in= float(input("Please Enter your monthly income:$"))
                Expense=input("Type monthly expenses with spaces inbetween:")
                G_expense = Expense.split()
                #sum of all expenses in list
                #Requiement: container type and iteration type
                g_expense=sum([float(e) for e in G_expense]) 
                print("\nTotal Amount spent for this month:$",g_expense)
                #instantiate class Monthly
                rest = Monthly(salary_in,g_expense)
                print((rest)) 
                        
            elif u_choi == 'w':
            
                salary_in= float(input("Please Enter your weekly income:$"))
                Expense=input("Type weekly expenses with spaces inbetween:")
                G_expense = Expense.split()
                #sum of all expenses in list
                #Requiement: container type anf iteration type
                g_expense=sum([float(e) for e in G_expense])
                print("\nTotal Amount spent this week:$",g_expense)
                #calling class  method
                res= Monthly.weekly_cal(salary_in,g_expense)
                print("Amount saved per year:$",round(res,2))
                     
            elif u_choi == 'sm':
            
                salary_in= float(
                    input("Please Enter your semi-months income:$"))
                Expense=input("Type semi-month expenses with space inbetween:")
                G_expense = Expense.split()
                #sum of all expenses in list 
                #Requiement: container type and iteration type
                g_expense=sum([float(e) for e in G_expense])
                print("\nTotal Amount spent for this semi-month:$",g_expense)
                #calling class method
                res= Monthly.semimon_cal(salary_in,g_expense)
                print("Amount saved per year:$",round(res,2))
            
            elif u_choi == 'r':
                
                #Retirement calculations
                print("\nRetirement calculation.")
                u_name=input("Enter your name for record reference:")
                current_savings=float(
                    input("Enter current saving for retirement:"))
                current_age=float(
                    input ("Enter your current age:"))
                retirement_age=float(
                    input ("Enter your desired retirement age:"))
                yearly_contribution=float(
                    input("Enter yearly contribution:"))
                print("\nAverage annual return is a ratio:",
                       " 1.07 is a 7% annual return")
                avg_annual_return=float(
                    input("Enter the average annual return:"))
            
                #calling retire_calc fuction
                retire_amt = retire_calc(float(current_savings),
                                         float(current_age),
                                 float(retirement_age),float(avg_annual_return),
                                 float(yearly_contribution))
            
                #printing retirement amount
                age= retirement_age - current_age
                print("\nHi {}!! In {} years, the retirement amount will be: {}"
                  .format(u_name,int(age),retire_amt))
            
                #Requirement: Input and/or Output file
                #Saving the retirement calculated amount in a file.
                new_file= open("new_test.txt","a+")
                print("\nHi {name}! In {age} years retirement amount will be:"
                      "${amt} record saved on {dt}".format(
                      name=u_name,
                      age=int(age),
                      amt=retire_amt,
                      dt=(datetime.datetime.now().strftime('%Y-%m-%d %H:%M')))
                     ,file = new_file)
                new_file.close() #close the files.
            
                #Testing the input file for existence and 
                #printing an error message, if the file does not exist.
                print("\nText file has been updated!!")
                report =input("Do you want to review your file type Yes or No:")
                report = report.lower()
            
                if report == 'yes':
                    new_temp_file= open("new_test.txt","r")
                    if new_temp_file != 0:
                        file_content = new_temp_file.read()
                        print(file_content)
                        print("\nThank you for using Home Expense ",
                          "& Retirement Calculator.")
                        break
                    else:
                        print("file doesn't exists")
                    new_temp_file.close() #close the file.  
                
                elif report == 'no':
                    print("\nThank you for using Home Expense",
                      " & Retirement Calculator.")  
                    break
                
            else:
                print("Error: Please enter a valid choice")
                break
            
            print("\nPlease enter your choice of calculation:")
            u_choi=input("Bi-weekly = bw, Weekly = w,"
                 "\nMonthly = m, Semi-Monthly = sm, Retirement = r:")
             
        #Requirement: try-except blocks
        except TypeError:
            print("TypeError: Please enter a valid input")
            break
         
        #Requirement: try-except blocks
        except ValueError:
            print("ValueError: Please enter a valid input")
            break
    else:
        print("Error: Please enter a valid choice")