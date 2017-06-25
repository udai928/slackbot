import MySQLdb
import yaml


class MySQLClient:
    def __init__(self):
        with open("config.yml") as file:
            config = yaml.load(file)['db']

        self.conn = MySQLdb.connect(
            user=config['user'],
            password=config['password'],
            host=config['host'],
            database=config['database']
        )

        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn = None

    def find(self, table):
        self.cursor.execute("SELECT * FROM " + table)
        return self.cursor.fetchall()


