import mysql.connector

mydb = mysql.connector.connect(
    host='192.168.137.1',
    user='hoadi',
    password='Coffee99',
    auth_plugin='mysql_native_password'  # Explicitly specifying the plugin
)


mycur = mydb.cursor()
mycur.execute("USE club")

recipnet=input