import os

def supportedDatabases():
#{
	oldCurrentDirectory = os.path.dirname(os.path.realpath(__file__))
	currentWorkingDirectory = os.getcwd()
	
	if (oldCurrentDirectory != currentWorkingDirectory):
	#{
		raise SystemExit("Python Script invoked from wrong directory. Please change directory to where \"createJARFiles.py\" script is present.")
	#}
	
	currentDirectory = os.path.dirname(os.path.realpath(__file__))
	supportedDatabasePath = os.path.join(currentDirectory, "..")
	supportedDatabasePath = os.path.join(supportedDatabasePath, "common_properties")
	supportedDatabasePath = os.path.join(supportedDatabasePath,"supported-database.properties")
	
	filePtr=open(supportedDatabasePath, "r")
	srcDatabaseList = []
	tgtDatabaseList = []
	
	for line in filePtr:
	#{
		tmpPosition = line.find("|")
		tmpFilepropertyPrefix = line[0:tmpPosition]
		tmpFilepropertyPrefix = tmpFilepropertyPrefix.lower()
		tmpFilepropertySuffix = line[tmpPosition+1:len(line)].lower().strip().strip("\n")
		tmpFilepropertySuffix = tmpFilepropertySuffix.lower()
		if tmpFilepropertyPrefix == 'source':
		#{
			srcDatabase = tmpFilepropertySuffix.lower()
			srcDatabaseList.append(srcDatabase)
		#}
		elif tmpFilepropertyPrefix == 'target':
		#{
			tgtDatabase = tmpFilepropertySuffix.lower()
			tgtDatabaseList.append(tgtDatabase)
		#}
		else:
		#{
			print("Error in supported-database.properties file")
		#}
	#}
	return srcDatabaseList, tgtDatabaseList
#}


