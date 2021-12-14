
## TO DO: Import functions as we finish more stuff

import test_for_hased_info
import test_for_password_complexity
import test_for_rainbow_vulnerability
import test_for_weak_passwords


### TO DO: Replace .test() with appropriate function name (or change other .py
##                                                                                        (files to have .test func)

'''
Function checks for different for information and database vulnerabilities 
'''
def run_audit_tool():

    ## Read in all columns that should be checked
    config = open("config.csv","r")
    columns_to_check = config.read().strip().split(",") ## convert into list

    test_for_sql_injection.test() ## TO DO
    test_for_hashing_algorithm.test() ## TO DO

    for each in columns_to_check:  

        file = open("user.csv","r")
        columns = file.readline().strip().replace('"',"").split(",")
        index = columns.index(each)

        da_list = []
        for each in file:
            x = each.split(",")
            da_list.append(x[index])
        file.close()

        if test_for_hashed_info.test(da_list)
            test_for_rainbow_vulnerability.test(da_list)
            test_for_salt(da_list)  ## TO DO
        else:

            if each == "password":
                test_for_weak_passwords.test(da_list)  ## Need to rework some things
                test_for_password_complexity.test(da_list) ## Need to rework some things
            
        

if __name__ == "__main__":

    run_audit_tool()