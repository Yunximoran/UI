from pymysql import connect
from .load_config import CONF

HOST = CONF['host']
PORT = CONF['port']
USER = CONF['user']
PASS = CONF['pass']
DB = CONF['database']


class DBManager:
    def __init__(self):
        self.conn = connect(
            host=HOST,
            port=PORT,
            user=USER,
            password=PASS,
            database=DB,
        )
        self.cursor = self.conn.cursor()

    def setAppInfo(self, an, ap):
        SQL = """
            insert into app_info(appName, appPath) value ('%s', '%s')
        """
        self.__execute(SQL % (an, ap))

    def getAppInfo(self):
        SQL = """
            select * from app_info;
        """
        self.__execute(SQL)
        return self.cursor.fetchall()

    def delAppInfo(self, an):
        SQL = """
            delete from app_info where appName = '%s'
        """
        self.__execute(SQL % an)

    def __execute(self, SQL):
        # print(SQL)
        try:
            self.cursor.execute(SQL)
            self.conn.commit()
        except ImportError:
            self.conn.rollback()


if __name__ == '__main__':
    pass
