from datetime import datetime
import xml.etree.ElementTree as rt

from matplotlib.pyplot import text
class Gen_XML:
    #PACS.009
    @property
    def file_location(self):
        return self.file_location
    def file_location(self,fl):
        self.file_location=fl
    @property
    def debitor_first(self):
        return self.debtor_first
    def debitor_first(self,dfirst):
        self.debitor_first=dfirst
    @property
    def debitor_second(self):
        return self.debitor_second
    def debitor_second(self,dsec):
        self.debitor_second=dsec
    @property
    def business_msg_id(self):
        return self.bus_msg_id
    def business_msg_id(self,bmsgid):
        self.business_msg_id=bmsgid
    @property
    def instruction_id(self):
        return self.instruction_id
    def instruction_id(self,insid):
        self.instruction_id=insid
    @property
    def settlement_amount(self):
        return self.settlement_amount
    def settlement_amount(self,stl_amt):
        self.settlement_amount=stl_amt
    @property
    def initiating_bic(self):
        return self.initiating_bic
    def initiating_bic(self,bic):
        self.initiating_bic=bic
    @property
    def receiving_bic(self):
        return self.receiving_bic
    def receiving_bic(self,bic):
        self.receiving_bic=bic
    @property
    def debitor_branch_routing_no(self):
        return self.debitor_branch_routing_no
    def debitor_branch_routing_no(self,routing_no):
        self.debitor_branch_routing_no=routing_no
    @property
    def creditor_branch_routing_no(self):
        return self.creditor_branch_routing_no
    def creditor_branch_routing_no(self,routing_no):
        self.creditor_branch_routing_no=routing_no
    @property
    def initiating_settlement_acc_no(self):
        return self.initiating_settlement_acc_no
    def initiating_settlement_acc_no(self,acc_no):
        self.initiating_settlement_acc_no=acc_no
    @property
    def receiving_settlement_acc_no(self):
        return self.receiving_settlement_acc_no
    def receiving_settlement_acc_no(self,acc_no):
        self.receiving_settlement_acc_no=acc_no
    @property
    def transaction_reason(self):
        return self.transaction_reason
    def transaction_reason(self,reason):
        self.transaction_reason=reason
    @property
    def return_ref(self):
        return self.return_ref
    def return_ref(self,ref):
        self.return_ref=ref
    @property
    def ret_id(self):
        return self.ret_id
    def ret_id(self,retid):
        self.ret_id=retid
    #CAMT.054
    @property
    def message_id(self):
        return self.message_id
    def message_id(self,id):
        self.message_id=id
    @property
    def account_id(self):
        return self.account_id
    def account_id(self,id):
        self.account_id=id
    @property
    def ntry_ref(self):
        return self.ntry_ref
    def ntry_ref(self,ref):
        self.ntry_ref=ref
    @property
    def transaction_amount(self):
        return self.transaction_amount
    def transaction_amount(self,amount):
        self.transaction_amount=amount

    # PACS_009 : FINANCIAL INSTITUTION CREDIT TRANSFER
    def gen_PACS009(self) :
        root = rt.Element("DataPDU",{'xmlns':'urn:swift:saa:xsd:saa.2.0'})
        Revision=rt.SubElement(root,'Revision')
        Revision.text='2.0.5'
        #Body Segment
        body = rt.SubElement(root,"Body")
        #AppHdr Segment
        AppHdr = rt.SubElement(body,"AppHdr",{'xmlns':'urn:iso:std:iso:20022:tech:xsd:head.001.001.01'})
        Fr = rt.SubElement(AppHdr,'Fr')
        FIId_1 = rt.SubElement(Fr,'FIId')
        FinInstnId_1 = rt.SubElement(FIId_1,'FinInstnId')
        BICFI_1 = rt.SubElement(FinInstnId_1,'BICFI')
        BICFI_1.text=self.initiating_bic
        To=rt.SubElement(AppHdr,'To')
        FIId_2 = rt.SubElement(To,'FIId')
        FinInstnId_2 = rt.SubElement(FIId_2,'FinInstnId')
        BICFI_2 = rt.SubElement(FinInstnId_2,'BICFI')
        BICFI_2.text=self.receiving_bic
        BizMsgIdr = rt.SubElement(AppHdr,'BizMsgIdr')
        BizMsgIdr.text=self.business_msg_id
        MsgDefIdr = rt.SubElement(AppHdr,'MsgDefIdr')
        MsgDefIdr.text='pacs.009.001.04'
        BizSvc=rt.SubElement(AppHdr,'BizSvc')
        BizSvc.text='RTGS_GSMT'
        CreDt=rt.SubElement(AppHdr,'CreDt')
        CreDt.text=datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        #AppHdr Segment End
        #Document Segment
        #GrpHeader
        Document=rt.SubElement(body,'Document',{'xmlns':'urn:iso:std:iso:20022:tech:xsd:pacs.009.001.04'
        ,'xmlns:auto-ns2':'urn:cma:stp:xsd:stp.1.0'})
        FICdtTrf=rt.SubElement(Document,'FICdtTrf')
        GrpHdr=rt.SubElement(FICdtTrf,'GrpHdr')
        MsgId=rt.SubElement(GrpHdr,'MsgId')
        MsgId.text=self.instruction_id
        CreDtTm=rt.SubElement(GrpHdr,'CreDtTm')
        CreDtTm.text=datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        NbOfTxs=rt.SubElement(GrpHdr,'NbOfTxs')
        NbOfTxs.text='1'
        SttlmInf=rt.SubElement(GrpHdr,'SttlmInf')
        SttlmMtd=rt.SubElement(SttlmInf,'SttlmMtd')
        SttlmMtd.text='CLRG'
        #GrpHeader End
        #Credit Transfer Transaction Information Segment
        CdtTrfTxInf=rt.SubElement(FICdtTrf,'CdtTrfTxInf')
        PmtId=rt.SubElement(CdtTrfTxInf,'PmtId')
        InstrId=rt.SubElement(PmtId,'InstrId')
        InstrId.text=self.instruction_id
        EndToEndId=rt.SubElement(PmtId,'EndToEndId')
        EndToEndId.text=self.instruction_id
        TxId=rt.SubElement(PmtId,'TxId')
        TxId.text=self.instruction_id
        PmtTpInf=rt.SubElement(CdtTrfTxInf,'PmtTpInf')
        ClrChanl=rt.SubElement(PmtTpInf,'ClrChanl')
        ClrChanl.text='RTGS'
        SvcLvl=rt.SubElement(PmtTpInf,'SvcLvl')
        Prtry=rt.SubElement(SvcLvl,'Prtry')
        Prtry.text='0040'
        LclInstrm=rt.SubElement(PmtTpInf,'LclInstrm')
        Prtry_2=rt.SubElement(LclInstrm,'Prtry')
        Prtry_2.text='RTGS_FICT'
        CtgyPurp=rt.SubElement(PmtTpInf,'CtgyPurp') # Category Purpose:Category is defined through TTC
        Prtry_3=rt.SubElement(CtgyPurp,'Prtry')
        Prtry_3.text='001'
        IntrBkSttlmAmt=rt.SubElement(CdtTrfTxInf,'IntrBkSttlmAmt',{'Ccy':'BDT'})
        IntrBkSttlmAmt.text=self.settlement_amount

        IntrBkSttlmDt=rt.SubElement(CdtTrfTxInf,'IntrBkSttlmDt')
        IntrBkSttlmDt.text=datetime.now().strftime("%Y-%m-%d")

        Dbtr=rt.SubElement(CdtTrfTxInf,'Dbtr')  # Debitor
        FinInstnId_D=rt.SubElement(Dbtr,'FinInstnId')
        BICFI_D=rt.SubElement(FinInstnId_D,'BICFI')
        BICFI_D.text=self.initiating_bic
        BrnchId_D=rt.SubElement(Dbtr,'BrnchId')
        Id_D=rt.SubElement(BrnchId_D,'Id')
        Id_D.text=self.debitor_branch_routing_no  #Debit Branch ID ( Routing Number)
        #Debitor End
        #Debitor Acc Info
        DbtrAcct=rt.SubElement(CdtTrfTxInf,'DbtrAcct')
        Id_2=rt.SubElement(DbtrAcct,'Id')
        Othr=rt.SubElement(Id_2,'Othr')
        Id_3=rt.SubElement(Othr,'Id')
        Id_3.text=self.initiating_settlement_acc_no
        tree = rt.ElementTree(root)
        #Debitor Acc Info End
        #Creditor Acc Info
        Cdtr=rt.SubElement(CdtTrfTxInf,'Cdtr')
        FinInstnId_C=rt.SubElement(Cdtr,'FinInstnId')
        BICFI_C=rt.SubElement(FinInstnId_C,'BICFI')
        BICFI_C.text=self.receiving_bic
        BrnchId_C=rt.SubElement(Cdtr,'BrnchId')
        Id_C=rt.SubElement(BrnchId_C,'Id')
        Id_C.text=self.creditor_branch_routing_no
        
        CdtrAcct=rt.SubElement(CdtTrfTxInf,'CdtrAcct')
        Id_4=rt.SubElement(CdtrAcct,'Id')
        Othr_2=rt.SubElement(Id_4,'Othr')
        Id_5=rt.SubElement(Othr_2,'Id')
        Id_5.text=self.receiving_settlement_acc_no
        #Creditor Acc Info End
        InstrForNxtAgt=rt.SubElement(CdtTrfTxInf,'InstrForNxtAgt')
        InstrInf=rt.SubElement(InstrForNxtAgt,'InstrInf')
        InstrInf.text=self.transaction_reason
        tree = rt.ElementTree(root) 

        with open (self.file_location, "wb") as files :
            try:
                tree.write(files, xml_declaration=True, encoding='utf-8')
                return 1
            except:
                return 0
    # PACS_009 : FINANCIAL INSTITUTION PAYMENT RETURN
    def gen_PACS009_RET(self) :
        root = rt.Element("Saa:DataPDU",{'xmlns:Saa':'urn:swift:saa:xsd:saa.2.0','xmlns:Sw':'urn:swift:snl:ns.Sw',
        'xmlns:SwGbl':'urn:swift:snl:ns.SwGbl','xmlns:SwInt':'urn:swift:snl:ns.SwInt','xmlns:SwSec':'urn:swift:snl:ns.SwSec'})
        #Body Segment
        body = rt.SubElement(root,"Saa:Body")
        #AppHdr Segment
        AppHdr = rt.SubElement(body,"AppHdr:AppHdr",{'xmlns':'urn:iso:std:iso:20022:tech:xsd:head.001.001.01','xmlns:AppHdr':'urn:iso:std:iso:20022:tech:xsd:head.001.001.01','xmlns:xsi':'http://www.w3.org/2001/XMLSchema-instance'})
        Fr = rt.SubElement(AppHdr,'Fr')
        FIId_1 = rt.SubElement(Fr,'FIId')
        FinInstnId_1 = rt.SubElement(FIId_1,'FinInstnId')
        BICFI_1 = rt.SubElement(FinInstnId_1,'BICFI')
        BICFI_1.text=self.receiving_bic
        To=rt.SubElement(AppHdr,'To')
        FIId_2 = rt.SubElement(To,'FIId')
        FinInstnId_2 = rt.SubElement(FIId_2,'FinInstnId')
        BICFI_2 = rt.SubElement(FinInstnId_2,'BICFI')
        BICFI_2.text=self.initiating_bic
        BizMsgIdr = rt.SubElement(AppHdr,'BizMsgIdr')
        BizMsgIdr.text=self.business_msg_id
        MsgDefIdr = rt.SubElement(AppHdr,'MsgDefIdr')
        MsgDefIdr.text='pacs.009.001.04'
        BizSvc=rt.SubElement(AppHdr,'BizSvc')
        BizSvc.text='RTGS_RETN'
        CreDt=rt.SubElement(AppHdr,'CreDt')
        CreDt.text=datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        #AppHdr Segment End
        #Document Segment
        #GrpHeader
        Document=rt.SubElement(body,'Document',{'xmlns':'urn:iso:std:iso:20022:tech:xsd:pacs.009.001.04'})
        FICdtTrf=rt.SubElement(Document,'FICdtTrf')
        GrpHdr=rt.SubElement(FICdtTrf,'GrpHdr')
        MsgId=rt.SubElement(GrpHdr,'MsgId')
        MsgId.text=self.ret_id
        CreDtTm=rt.SubElement(GrpHdr,'CreDtTm')
        CreDtTm.text=datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        NbOfTxs=rt.SubElement(GrpHdr,'NbOfTxs')
        NbOfTxs.text='1'
        SttlmInf=rt.SubElement(GrpHdr,'SttlmInf')
        SttlmMtd=rt.SubElement(SttlmInf,'SttlmMtd')
        SttlmMtd.text='CLRG'
        #GrpHeader End
        #Credit Transfer Transaction Information Segment
        CdtTrfTxInf=rt.SubElement(FICdtTrf,'CdtTrfTxInf')
        PmtId=rt.SubElement(CdtTrfTxInf,'PmtId')
        InstrId=rt.SubElement(PmtId,'InstrId')
        InstrId.text=self.ret_id
        EndToEndId=rt.SubElement(PmtId,'EndToEndId')
        EndToEndId.text=self.ret_id
        TxId=rt.SubElement(PmtId,'TxId')
        TxId.text=self.ret_id
        PmtTpInf=rt.SubElement(CdtTrfTxInf,'PmtTpInf')
        ClrChanl=rt.SubElement(PmtTpInf,'ClrChanl')
        ClrChanl.text='RTGS'
        SvcLvl=rt.SubElement(PmtTpInf,'SvcLvl')
        Prtry=rt.SubElement(SvcLvl,'Prtry')
        Prtry.text='0040'
        LclInstrm=rt.SubElement(PmtTpInf,'LclInstrm')
        Prtry_2=rt.SubElement(LclInstrm,'Prtry')
        Prtry_2.text='RTGS_RETN'
        CtgyPurp=rt.SubElement(PmtTpInf,'CtgyPurp') # Category Purpose:Category is defined through TTC
        Prtry_3=rt.SubElement(CtgyPurp,'Prtry')
        Prtry_3.text='001'
        IntrBkSttlmAmt=rt.SubElement(CdtTrfTxInf,'IntrBkSttlmAmt',{'Ccy':'BDT'})
        IntrBkSttlmAmt.text=self.settlement_amount

        IntrBkSttlmDt=rt.SubElement(CdtTrfTxInf,'IntrBkSttlmDt')
        IntrBkSttlmDt.text=datetime.now().strftime("%Y-%m-%d")

        InstgAgt=rt.SubElement(CdtTrfTxInf,'InstgAgt')
        FinInstnId_3=rt.SubElement(InstgAgt,'FinInstnId')
        BICFI_3=rt.SubElement(FinInstnId_3,'BICFI')
        BICFI_3.text=self.receiving_bic

        InstgAgt_2=rt.SubElement(CdtTrfTxInf,'InstdAgt')
        FinInstnId_4=rt.SubElement(InstgAgt_2,'FinInstnId')
        BICFI_4=rt.SubElement(FinInstnId_4,'BICFI')
        BICFI_4.text=self.initiating_bic

        Dbtr=rt.SubElement(CdtTrfTxInf,'Dbtr')  # Debitor
        FinInstnId_D=rt.SubElement(Dbtr,'FinInstnId')
        BICFI_D=rt.SubElement(FinInstnId_D,'BICFI')
        BICFI_D.text=self.receiving_bic
        BrnchId_D=rt.SubElement(Dbtr,'BrnchId')
        Id_D=rt.SubElement(BrnchId_D,'Id')
        Id_D.text=self.creditor_branch_routing_no  #Debit Branch ID ( Routing Number)
        #Debitor End
        #Debitor Acc Info
        DbtrAcct=rt.SubElement(CdtTrfTxInf,'DbtrAcct')
        Id_2=rt.SubElement(DbtrAcct,'Id')
        Othr=rt.SubElement(Id_2,'Othr')
        Id_3=rt.SubElement(Othr,'Id')
        Id_3.text=self.receiving_settlement_acc_no
        tree = rt.ElementTree(root)
        #Debitor Acc Info End
        #Creditor Acc Info
        Cdtr=rt.SubElement(CdtTrfTxInf,'Cdtr')
        FinInstnId_C=rt.SubElement(Cdtr,'FinInstnId')
        BICFI_C=rt.SubElement(FinInstnId_C,'BICFI')
        BICFI_C.text=self.initiating_bic
        BrnchId_C=rt.SubElement(Cdtr,'BrnchId')
        Id_C=rt.SubElement(BrnchId_C,'Id')
        Id_C.text=self.debitor_branch_routing_no
        
        CdtrAcct=rt.SubElement(CdtTrfTxInf,'CdtrAcct')
        Id_4=rt.SubElement(CdtrAcct,'Id')
        Othr_2=rt.SubElement(Id_4,'Othr')
        Id_5=rt.SubElement(Othr_2,'Id')
        Id_5.text=self.initiating_settlement_acc_no
        #Creditor Acc Info End
        InstrForNxtAgt=rt.SubElement(CdtTrfTxInf,'InstrForNxtAgt')
        InstrInf=rt.SubElement(InstrForNxtAgt,'InstrInf')
        InstrInf.text=self.transaction_reason

        InstrForNxtAgt2=rt.SubElement(CdtTrfTxInf,'InstrForNxtAgt')
        InstrInf2=rt.SubElement(InstrForNxtAgt2,'InstrInf')
        InstrInf2.text=self.return_ref

        InstrForNxtAgt2=rt.SubElement(CdtTrfTxInf,'InstrForNxtAgt')
        InstrInf2=rt.SubElement(InstrForNxtAgt2,'InstrInf')
        InstrInf2.text='/MREF/'+self.instruction_id

        InstrForNxtAgt3=rt.SubElement(CdtTrfTxInf,'InstrForNxtAgt')
        InstrInf3=rt.SubElement(InstrForNxtAgt3,'InstrInf')
        InstrInf3.text='/TREF/'+self.ret_id
        tree = rt.ElementTree(root) 
        with open (self.file_location, "wb") as files :
            try:
                tree.write(files, xml_declaration=True, encoding='utf-8')
                return 1
            except:
                return 0