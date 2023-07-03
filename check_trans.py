import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime
from decimal import *
from gen_xml import Gen_XML as gen_xml
from oracle_conn import Oracle_Conn as ora_con
import sys
if __name__ == "__main__":
    connection=ora_con(ip='192.107.2.129',port='1521',db_nm='dbhrac',usr='ashik',passwd='1234')
    connection1=ora_con(ip='192.107.2.129',port='1521',db_nm='dbhrac',usr='ashik',passwd='1234')
    connection2=ora_con(ip='192.107.2.129',port='1521',db_nm='dbhrac',usr='ashik',passwd='1234')
    connection3=ora_con(ip='192.107.2.129',port='1521',db_nm='dbhrac',usr='ashik',passwd='1234')
    connection4=ora_con(ip='192.107.2.129',port='1521',db_nm='dbhrac',usr='ashik',passwd='1234')
    #dir='D://STP Adapter/STPAdapterPG_v23_43_CSO/output/'
    dir='D://STP Adapter/clientFiles/output/'
    pathlist = Path(dir).glob('**/*.xml')
    for path in pathlist:
        path_in_str = str(path)
        tree = ET.parse(path_in_str)
        root = tree.getroot()
        if root[1][0][3].text=='camt.054.001.04' and root[1][1][0][1][3][2].text=='CRDT':
            #print(path_in_str + ' credit ')
            trans_id=root[1][1][0][1][3][6][0][0][2].text
            trans_amt=root[1][1][0][1][3][6][0][1].text
            trans_dt=root[1][1][0][1][3][6][0][4][0].text
            trans_dbtr=root[1][1][0][1][3][6][0][3][0][0][0][0].text
            msg_id=root[1][0][2].text
            #print(trans_id,trans_dt,trans_dbtr,msg_id,trans_amt)
            if (trans_id!='' and trans_amt!='' and trans_dt!='' and trans_dbtr!=''):
                query1="""select count(*) from call_loan.rtgs_trans where  instr_id=:trans_id"""
                row=connection1.c.execute(query1,[trans_id])
                #connection.conn.commit()
                for r in row:
                    #print(r[0])
                    if r[0]>0:
                        continue
                    else:
                        query2="""insert into  call_loan.rtgs_trans(bus_msg_id,instr_id,init_bic,rcv_bic,stl_amt,dr_rt_no,cr_rt_no,init_stl_acc_no,rcv_stl_acc_no,trans_typ,status) 
                                                        values(:msg_id,:trans_id,:trans_dbtr,'DBHLBDDH',:trans_amt,(select rt_no from call_loan.rtgs_fi_det where bic=:trans_dbtr)
                                                        ,(select rt_no from call_loan.rtgs_fi_det where bic='DBHLBDDH'),
                                                        (select stlmnt_acnt from call_loan.rtgs_fi_det where bic=:trans_dbtr),
                                                        (select stlmnt_acnt from call_loan.rtgs_fi_det where bic='DBHLBDDH'),'RCV','C')"""
                        row=connection.c.execute(query2,[msg_id,trans_id,trans_dbtr,trans_amt])
                        connection.conn.commit()
            else:
                continue
        elif root[1][0][3].text=='camt.054.001.04' and root[1][1][0][1][3][2].text=='DBIT':
                #print(path_in_str + ' debit ')
                trans_id=root[1][1][0][1][3][6][0][0][2].text
                query3="""select count(*) from call_loan.rtgs_trans where  instr_id=:trans_id and status='P' and trans_typ='PAY'"""
                row=connection2.c.execute(query3,[trans_id])
                for r in row:
                    if r[0]>0:
                        query4="""update call_loan.rtgs_trans set status ='C' where  instr_id = :trans_id and status='P'"""
                        row=connection3.c.execute(query4,[trans_id])
                        connection3.conn.commit()
                        query6="""select dl_no,cl_no,RCV_STL_ACC_NO from call_loan.rtgs_trans where   instr_id = :trans_id and status='C'"""
                        row1=connection4.c.execute(query6,[trans_id])
                        for r in row1:
                            print(path_in_str+'pay')
                            dl_no=r[0].strip()
                            cl_no=r[1].strip()
                            acc_no=r[2].strip()
                            print(dl_no,cl_no,acc_no)
                            query7="""update call_loan.deal_slip_det set chq_no= :trans_id, chq_ind='Y',chq_by='SYS',chq_dt=trunc(sysdate),b_acc_no=:acc_no,pay_ind='C' where  dl_no = :dl_no and call_loan=:cl_no """
                            row=connection3.c.execute(query7,[trans_id,acc_no,dl_no,cl_no])
                            connection3.conn.commit()  
                    else:
                        continue
                query3="""select count(*) from call_loan.rtgs_trans where  ret_id=:trans_id and status='P' and trans_typ='RCV'"""
                row=connection2.c.execute(query3,[trans_id])
                for r in row:
                    if r[0]>0:
                        query4="""update call_loan.rtgs_trans set status ='R' where  ret_id = :trans_id and status='P'"""
                        row=connection3.c.execute(query4,[trans_id])
                        connection3.conn.commit()
                    else:
                        continue
                
        elif root[1][0][3].text=='pacs.002.001.05' and root[1][1][0][2][3].text=='RJCT':
                #print(path_in_str + ' failed ')
                trans_id=root[1][1][0][2][0].text
                rem=root[1][1][0][1][4][1].text
                msg_id=root[1][0][2].text
                query3="""select count(*) from call_loan.rtgs_trans where  instr_id=:trans_id and status='P'"""
                row=connection4.c.execute(query3,[trans_id])
                for r in row:
                    if r[0]>0:
                        query4="""update call_loan.rtgs_trans set status ='F' where  instr_id = :trans_id and status='P'"""
                        row=connection4.c.execute(query4,[trans_id])
                        query5="""insert into call_loan.rtgs_error(instr_id,remarks,msg_id) values(:trans_id,:rem,:msg_id)"""
                        row2=connection4.c.execute(query5,[trans_id,rem,msg_id])
                        connection4.conn.commit()
                    else:
                        continue
        else:
            continue
        
        
        
         