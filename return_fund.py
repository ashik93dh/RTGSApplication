from datetime import datetime
from decimal import *
from gen_xml import Gen_XML as gen_xml
from oracle_conn import Oracle_Conn as ora_con
import sys
if __name__ == "__main__":
    connection=ora_con(ip='192.107.2.129',port='1521',db_nm='dbhrac',usr='ashik',passwd='1234')
    trans_id=sys.argv[1]
    #trans_id='202205252000042'
    query="""select * from call_loan.rtgs_trans where status ='C' and trans_typ='RCV' and instr_id = :trans_id"""
    row=connection.c.execute(query,[trans_id])
    for r in row:
        tr=gen_xml()
        tr.initiating_bic=r[0].strip()
        tr.receiving_bic=r[1].strip()
        tr.business_msg_id=r[2].strip()
        tr.instruction_id=trans_id
        tr.settlement_amount="{:.2f}".format(float(r[4].strip()))
        tr.debitor_branch_routing_no=r[5].strip()
        tr.creditor_branch_routing_no=r[6].strip()
        tr.initiating_settlement_acc_no=r[7].strip()
        tr.receiving_settlement_acc_no=r[8].strip()
        tr.transaction_reason='/RETN/'
        tr.ret_id=sys.argv[2]
        tr.return_ref=sys.argv[3]
        tr.return_ref=tr.return_ref.replace("_"," ")
        #tr.file_location="D://STP Adapter/STPAdapterPG_v23_43_CSO/input/"+'RTGS_RET_'+tr.business_msg_id+".xml"
        tr.file_location="D://STP Adapter/clientFiles/input/"+'RTGS_RET_'+tr.business_msg_id+".xml"
        #print(tr.debitor_second)
        result=tr.gen_PACS009_RET()
        if result==1 :
            query="""update call_loan.rtgs_trans set status ='P' where  instr_id = :trans_id"""
            row=connection.c.execute(query,[trans_id])
            connection.conn.commit()
        else:
            query="""update call_loan.rtgs_trans set status ='F' where  instr_id = :trans_id"""
            row=connection.c.execute(query,[trans_id])
            connection.conn.commit()

    



    
    