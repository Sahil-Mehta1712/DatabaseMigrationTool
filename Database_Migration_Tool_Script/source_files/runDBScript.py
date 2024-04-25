from getDatabaseConnectionDetail import *
import os

def runDBScript(tgtDatabaseType,databaseIdentifier,tableNameList,conn):
#{
	(databaseConnectionList) = getDatabaseConnectionDetail(tgtDatabaseType,databaseIdentifier)
	hostName = databaseConnectionList[0]
	schemaName = databaseConnectionList[1]
	username = databaseConnectionList[2]
	passwordStr = databaseConnectionList[3]
	
	cursor = conn.cursor()
	oldCurrentDirectory = os.path.dirname(os.path.realpath(__file__))
	currentWorkingDirectory = os.getcwd()
	
	if (oldCurrentDirectory != currentWorkingDirectory):
	#{
		raise SystemExit("Python Script invoked from wrong directory. Please change directory to where \"createJARFiles.py\" script is present.")
	#}
	
	currentDirectory = os.path.dirname(os.path.realpath(__file__))
	dbFilePath = os.path.join(currentDirectory, "..")
	dbFilePath = os.path.join(dbFilePath, "..")
	dbFilePath = os.path.join(dbFilePath, "Generated_Scripts")
	dbFilePath = os.path.join(dbFilePath,tgtDatabaseType.lower())
	dbFilePath = os.path.join(dbFilePath,"database_scripts")

	if tableNameList == []:
	#{
		for file in os.listdir(dbFilePath):
			filename = os.fsdecode(file)
			if filename.endswith(".sql"): 
				tablePath = os.path.join(dbFilePath, filename)
				tableName = os.path.splitext(os.path.basename(filename))[0]
				
				dbQuery = "sqlcmd -b -S " + hostName + " -d " + schemaName + " -U " + username + " -P " + passwordStr + " -i " + "\"" + tablePath + "\"" + " -r0"
				print("Executing Database Script for " + tableName.upper())
				os.popen(dbQuery)
				print ('*' * 120)

				continue
			else:
				continue
	#}
	else:
	#{
		for tableName in tableNameList:
		#{
			tablePath = dbFilePath + "\\" + tableName.upper() + "_TMP.sql"
			
			if os.path.exists(tablePath):
			#{
				dbQuery = "sqlcmd -S " + hostName + " -d " + schemaName + " -U " + username + " -P " + passwordStr + " -i " + "\"" + tablePath + "\""
				os.popen(dbQuery)
				print("Executing Database Script for " + tableName.upper())
				print ('*' * 120)
			#}
			else:
			#{
				print("DB script not generated")
			#}
		#}
	#}
	cursor.close()
	conn.commit()
#}