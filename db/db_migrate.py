import mysql.connector

DB_CONFIG = {}
DB_CONFIG["host"] = ""
DB_CONFIG["database"] = ""
DB_CONFIG["user"] = ""
DB_CONFIG["password"] = ""

NO_OF_LINES_AT_ONE_TIME = 40000
NAME_OF_FILE = ''

fObj = open(NAME_OF_FILE)
fObjw = open('error', 'w')

def create_values_part(line):
	line = line.strip()
	line = line.replace("\"", "")
	lineArr = line.split(",")
	return "({}, {}, {}, {}, {})\n".format("\"" + lineArr[0] + "\""
	, "\"" + lineArr[1] + "\"", "\"" + lineArr[3] + "\"", "\"" + lineArr[4] + "\"", "\"" + lineArr[5] + "\"")

def create_query(arr):
	print("creating query")
	final_query = "insert into ip_info(start_ip_number, end_ip_number, country, state, region) values"
	final_query += create_values_part(arr[0])
	for line in arr[1:]:
		final_query += "," + create_values_part(line)

	return final_query

def fire_query(final_query):
	print("firing query")
	cnx = mysql.connector.connect(**DB_CONFIG)
	cursor = cnx.cursor()
	try:
		cursor.execute(final_query)
	except Exception as e:
		print(e)
		fObjw.write(final_query)

	cnx.commit()
	cursor.close()
	cnx.close()

def file_iter():
	arr = []
	count = 0
	for line in fObj:
		if count == NO_OF_LINES_AT_ONE_TIME:
			final_query = create_query(arr)
			arr = []
			count = 0
			fire_query(final_query)

		arr.append(line)
		count += 1
	if count > 0:
		final_query = create_query(arr)
		fire_query(final_query)

file_iter()
