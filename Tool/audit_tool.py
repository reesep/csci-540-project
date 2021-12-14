
## TO DO: Import functions as we finish more stuff

import test_for_hashed_info
import test_for_password_complexity
import test_for_rainbow_vulnerability
import test_for_weak_passwords
import test_for_salt
import test_for_hashing_algorithm

### TO DO: Replace .test() with appropriate function name (or change other .py
##                                                                                        (files to have .test func)

'''
Function checks for different for information and database vulnerabilities 
'''
def run_audit_tool():

    ## Read in all columns that should be checked
    config = open("config.csv","r")
    columns_to_check = config.read().strip().split(",") ## convert into list

    ## test_for_sql_injection.test() ## TO DO
    test_for_hashing_algorithm.test()

    for each in columns_to_check:  

        file = open("../Data/user.csv","r")
        columns = file.readline().strip().replace('"',"").split(",")
        index = columns.index(each)

        da_list = []
        for e in file:
            x = e.split(",")
            da_list.append(x[index])
        file.close()


        if test_for_hashed_info.test(each,da_list):
            test_for_rainbow_vulnerability.test(da_list,each)
            test_for_salt.test(da_list)
            pass
        else:

            pass

            '''
            if each == "password":
                test_for_weak_passwords.test(da_list)  ## Need to rework some things
                test_for_password_complexity.test(da_list) ## Need to rework some things
            '''
        

if __name__ == "__main__":

    run_audit_tool()
