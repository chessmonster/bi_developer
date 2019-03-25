import sqlite3
from datetime import datetime

def main():
	database = 'db.sqlite3'

	con = sqlite3.connect(database)
	cur = con.cursor()

	# get the packages
	cur.execute('SELECT * FROM EXAM_APP_PACKAGE')
	packages = cur.fetchall()

	# get the region
	cur.execute('SELECT * FROM EXAM_APP_REGION')
	regions = cur.fetchall()

	for package in packages:

		# identify major region
		for region in regions:	
			if (region[1] in package[1]):
				match_major_region = region[2]
				cur.execute(''' UPDATE EXAM_APP_PACKAGE SET major_region = ? WHERE ID = ? ''', (match_major_region, package[0]))
				break	

		# identify lead time
		shipped_at = datetime.strptime(package[4], '%Y-%m-%d %H:%M:%S')
		delivered_at = datetime.strptime(package[5], '%Y-%m-%d %H:%M:%S')
		diff = delivered_at - shipped_at
		diff_computed = str(round(((diff.total_seconds() / 3600) / 24), 3))

		cur.execute(''' UPDATE EXAM_APP_PACKAGE SET leadtime = ? WHERE ID = ? ''', (str(diff_computed), package[0]))

		print(type(diff))


	con.commit()

	# for region in regions:
	# 	print(region)

if __name__ == '__main__':
	main()