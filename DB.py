import pymysql

conn = pymysql.connect(host='15.164.79.177', user='leaguelugas', password='8426753190', db='remarket', charset='utf8')
curs = conn.cursor(pymysql.cursors.DictCursor)
