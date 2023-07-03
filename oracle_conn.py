import cx_Oracle 
cx_Oracle.init_oracle_client(lib_dir=r"D:\Oracle\instantclient_21_3")
class Oracle_Conn:
    def __init__(self, ip, port,db_nm,usr,passwd):
        self.dsn_tns = cx_Oracle.makedsn(ip, port, service_name=db_nm) 
        self.conn = cx_Oracle.connect(user=usr, password=passwd, dsn=self.dsn_tns) 
        self.c = self.conn.cursor()

    
