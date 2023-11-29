import pymysql

class BD:
    _instancia = None
    conn = ""
    cursor = ""
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(BD, cls).__new__(cls)
        return cls._instancia

    def connect(self):
        try:
            self.conn=pymysql.connect(host='localhost',
                                    port=3306,
                                    user='root',
                                    password='',
                                    db='limpieza'
                                    )
            self.cursor=self.conn.cursor()
        except  Exception as e:
            print(e)

if __name__ == "__main__":
    bd = BD()