#Selenium Grid download

'''🔷 What is Selenium Grid?

Selenium Grid allows you to run your Selenium tests on multiple machines, browsers, and operating systems simultaneously.

Instead of running tests only on your local system, Selenium Grid helps you:

• Run tests in parallel
• Run tests on different browsers (Chrome, Firefox, Edge)
• Run tests on different OS (Windows, Linux, Mac)
• Reduce execution time'''

#? ---> https://www.selenium.dev/downloads/

# download it to the project folder 

# then open cmd --->  java -jar selenium-server-4.40.0.jar standalone

#also download the java in the machine

# now run the pytest code



#~ Selenium Grid is mainly used to connect different machines so tests can run in parallel across multiple browsers, operating systems, or computers.

#to connect and run the hub and node , we need to run both hub and run in same machine........................

#! HUB

'''java -jar selenium-server-4.40.0.jar hub ^

--host localhost ^

--port 4444 ^

--publish-events tcp://localhost:4442 ^

--subscribe-events tcp://localhost:4443

 '''

#! NODE

"""
java -jar selenium-server-4.40.0.jar node ^

--hub http://localhost:4444 ^

--publish-events tcp://localhost:4442 ^

--subscribe-events tcp://localhost:4443
'"""

#! running node and hub in different machines
# 
# hub on machine 1

'''java -jar selenium-server-4.40.0.jar hub ^

--host 0.0.0.0 ^

--port 4444 ^

--publish-events tcp://192.168.1.10:4442 ^

--subscribe-events tcp://192.168.1.10:4443

'''
 
# node on machine 2
''''
java -jar selenium-server-4.40.0.jar node ^

--hub http://192.168.1.10:4444 ^

--publish-events tcp://192.168.1.10:4442 ^

--subscribe-events tcp://192.168.1.10:4443


 '''