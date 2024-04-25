from getDatabaseConnectionDetail import *
import os

def runBCP(tgtDatabaseType,databaseIdentifier,tableNameList):
#{
	(databaseConnectionList) = getDatabaseConnectionDetail(tgtDatabaseType,databaseIdentifier)
	hostName = databaseConnectionList[0]
	schemaName = databaseConnectionList[1]
	username = databaseConnectionList[2]
	passwordStr = databaseConnectionList[3]
	
	oldCurrentDirectory = os.path.dirname(os.path.realpath(__file__))
	currentWorkingDirectory = os.getcwd()
	
	if (oldCurrentDirectory != currentWorkingDirectory):
	#{
		raise SystemExit("Python Script invoked from wrong directory. Please change directory to where \"createJARFiles.py\" script is present.")
	#}
	
	currentDirectory = os.path.dirname(os.path.realpath(__file__))
	csvFilePath = os.path.join(currentDirectory, "..")
	csvFilePath = os.path.join(csvFilePath, "..")
	csvFilePath = os.path.join(csvFilePath, "Generated_Scripts")
	csvFilePath = os.path.join(csvFilePath,tgtDatabaseType.lower())
	csvFilePath = os.path.join(csvFilePath,"csv_scripts")
		
	if tableNameList == []:
	#{
		for file in os.listdir(csvFilePath):
			filename = os.fsdecode(file)
			if filename.endswith(".tsv"): 
				tablePath = os.path.join(csvFilePath, filename)
				tableName = os.path.splitext(os.path.basename(filename))[0]

				bcpQuery = "BCP \"dbo." + tableName.upper() + "\" in " + "\"" + tablePath + "\"" + " -S " + hostName + " -d " + schemaName + " -U " + username + " -P " + passwordStr + " -c "
				os.popen(bcpQuery)
				print("Executing Database Script for " + tableName.upper())
				print ('*' * 120)
				continue
			else:
				continue
	#}
	else:
	#{
		for tableName in tableNameList:
		#{
			tablePath = csvFilePath + "/" + tableName.upper() + "_TMP.tsv"
			
			if os.path.exists(tablePath):
			#{
				bcpQuery = "BCP \"dbo." + tableName.upper() + "_TMP\" in " + "\"" + tablePath + "\"" + " -S " + hostName + " -d " + schemaName + " -U " + username + " -P " + passwordStr + " -c "
				os.popen(bcpQuery)
				print("Executing Database Script for " + tableName.upper())
				print ('*' * 120)
			#}
			else:
			#{
				print("DB script not generated")
			#}
		#}
	#}
#}