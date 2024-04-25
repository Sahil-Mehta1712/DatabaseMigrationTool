import datetime
import sys
import time
import os

# Possible Values for databaseName: DATAHUB, RECEPTION, ADF, RBS, infaRepo, etc.
# Python home needs to be set to find the config folder path: export PYTHON_HOME=/u01/programs/python/Hadoop/trunk
def getDatabaseConnectionDetail(srcDatabase,databaseIdentifier):
#{
	#print (srcDatabase + databaseIdentifier)
	#print('In getDatabaseConnectionDetail:'+str(datetime.datetime.now()))
	
	databaseHostName=""
	databasePort=0
	databaseServiceName=""
	databaseUserName=""
	databasePassword=""
	databaseAuthMechanism=""
	databaseName=""
	checkDatabaseConnectionList=""
	databaseConnectionList = []
	
	oldCurrentDirectory = os.path.dirname(os.path.realpath(__file__))
	currentWorkingDirectory = os.getcwd()
	
	if (oldCurrentDirectory != currentWorkingDirectory):
	#{
		raise SystemExit("Python Script invoked from wrong directory. Please change directory to where \"createJARFiles.py\" script is present.")
	#}
	
	currentDirectory = os.path.dirname(os.path.realpath(__file__))
	databaseConnectionPath = os.path.join(currentDirectory, "..")
	databaseConnectionPath = os.path.join(databaseConnectionPath, "common_properties")
	databaseConnectionPath = os.path.join(databaseConnectionPath, "database-connection.properties")
	
	if srcDatabase.lower() == "oracle":
	#{
		propertyPrefix = srcDatabase.lower() + "." + databaseIdentifier.lower() + "."
	
		filePtr=open(databaseConnectionPath, "r")
		
		for line in filePtr:
		#{
			#print "line:"+line
			
			tmpPosition = line.find("=")
			#print("tmpPosition:"+str(tmpPosition))
			tmpFilepropertyPrefix = line[0:tmpPosition]
			tmpFilepropertyPrefix = tmpFilepropertyPrefix.lower()
			#print("tmpFilepropertyPrefix:"+tmpFilepropertyPrefix)
			
			if tmpFilepropertyPrefix == propertyPrefix+"host":
			#{
				#print("propertyPrefix:"+propertyPrefix+"host")
				databaseHostName = line[tmpPosition+1:len(line)].strip().strip("\n")
				databaseConnectionList.append(databaseHostName)
				#print(databaseHostName)
			#}
			elif tmpFilepropertyPrefix == propertyPrefix+"port":
			#{
				#print("propertyPrefix:"+propertyPrefix+"port")
				databasePort = line[tmpPosition+1:len(line)].strip().strip("\n")
				databaseConnectionList.append(databasePort)
				#print(databasePort)
			#}
			elif tmpFilepropertyPrefix == propertyPrefix+"username":
			#{
				#print("propertyPrefix:"+propertyPrefix+"username")
				databaseUserName = line[tmpPosition+1:len(line)].strip().strip("\n")
				databaseConnectionList.append(databaseUserName)
				#print(databaseUserName)
			#}
			elif tmpFilepropertyPrefix == propertyPrefix+"password":
			#{
				#print("propertyPrefix:"+propertyPrefix+"password")
				databasePassword = line[tmpPosition+1:len(line)].strip().strip("\n")
				databaseConnectionList.append(databasePassword)
				#print(databasePassword)
			#}
			elif tmpFilepropertyPrefix == propertyPrefix+"serviceName".lower():
			#{
				#print("propertyPrefix:"+propertyPrefix+"databaseName")
				databaseServiceName = line[tmpPosition+1:len(line)].strip().strip("\n")
				databaseConnectionList.append(databaseServiceName)
				#print(serviceName)
			#}
		#}
		
		filePtr.close()
	#}
	elif srcDatabase.lower() == "mssql":
	#{
		propertyPrefix = srcDatabase.lower() + "." + databaseIdentifier.lower() + "."
	
		filePtr=open(databaseConnectionPath, "r")
		
		for line in filePtr:
		#{
			#print "line:"+line
			
			tmpPosition = line.find("=")
			#print("tmpPosition:"+str(tmpPosition))
			tmpFilepropertyPrefix = line[0:tmpPosition]
			tmpFilepropertyPrefix = tmpFilepropertyPrefix.lower()
			#print("tmpFilepropertyPrefix:"+tmpFilepropertyPrefix)
			
			if tmpFilepropertyPrefix == propertyPrefix+"host":
			#{
				#print("propertyPrefix:"+propertyPrefix+"host")
				databaseHostName = line[tmpPosition+1:len(line)].strip().strip("\n")
				databaseConnectionList.append(databaseHostName)
				#print(databaseHostName)
			#}
			elif tmpFilepropertyPrefix == propertyPrefix+"schema":
			#{
				#print("propertyPrefix:"+propertyPrefix+"port")
				databaseName = line[tmpPosition+1:len(line)].strip().strip("\n")
				databaseConnectionList.append(databaseName)
				#print(databasePort)
			#}
			elif tmpFilepropertyPrefix == propertyPrefix+"username":
			#{
				#print("propertyPrefix:"+propertyPrefix+"username")
				databaseUserName = line[tmpPosition+1:len(line)].strip().strip("\n")
				databaseConnectionList.append(databaseUserName)
				#print(databaseUserName)
			#}
			elif tmpFilepropertyPrefix == propertyPrefix+"password":
			#{
				#print("propertyPrefix:"+propertyPrefix+"password")
				databasePassword = line[tmpPosition+1:len(line)].strip().strip("\n")
				databaseConnectionList.append(databasePassword)
				#print(databasePassword)
			#}
		#}	
		filePtr.close()
	#}
	if checkDatabaseConnectionList in databaseConnectionList:
	#{
		print("Not All Connection Properties have been entered. Please check database-connection properties file and make required changes")
		sys.exit(1)
	#}
	else:
	#{
		return databaseConnectionList
	#}
	#print('Out getDatabaseConnectionDetail:'+str(datetime.datetime.now()))	
#}

