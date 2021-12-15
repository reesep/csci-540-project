# csci-540-project

Auditing tool that checks for different database weakness and vulnerabilities such as:  

* SQL Injection vulnerabilities  
* Hashing of sensitivve information  
* Weak passwords and password complexity
* Rainbow table vulnerabilities  
* Safe Hashing Algorithm  
* Presenece of Salt in passwords  

__Requirements:__  
The PHP code must exist in `Website/`  
The database (csv file) should be in `Data/`  
The columns to be checked can be configured in `tool/config.csv`  

**Warning:** Functionality for cracking passwords with rainbow tables (`test_fot_rainbow_vulnerability.py`) does not work on Linux currently  

To run the tool:  
```
python audit_tool.py
```  

Made by Reese Pearsall and Susan McCartney.  
[Advanced Database Systems (CSCI 540) - Fall 2021](https://github.com/msu/csci-540-fall2021) taught by Dr. Dave Millman
