import base_types
import InstructionForCreditorAgent3
import TrackerRecord8
import EquivalentAmount2
import DateAndDateTime2Choice
import PaymentRejectReturnReason1
import SettlementInstruction9
import TaxInformation8
import RemittanceLocation7
import SettlementDateTimeIndication1
import CreditTransferTransaction46
import BranchAndFinancialInstitutionIdentification6
import TrackerData8
import Max35Text
import TrackerPartyIdentification2
import SettlementTimeRequest2
import TransactionParties8
import ISODate
import CashAccount38
import Max2048Text
import Purpose2Choice
import RelatedTransactionData1
import RegulatoryReporting3
import ActiveOrHistoricCurrencyAndAmount
import ActiveCurrencyAndAmount
import Priority3Code
import BICFIDec2014Identifier
import Charges7
import PaymentIdentification10
import PartyIdentification135
import InstructionForNextAgent1
import ISODateTime
import PaymentTypeInformation28
import RemittanceInformation16
import CurrencyExchange15
import PaymentScenario1Choice
import Party40Choice
import OriginalBusinessInstruction4
import ChargeBearerType1Code

class TrackerPaymentTransaction14(base_types._BaseFieldType):

	__slots__ = ["_ChrgBr", "_RtrChain", "_PmtId", "_UndrlygCstmrCdtTrf", "_TechRcvr", "_SttlmTmReq", "_IntrmyAgt1Acct", "_AccptncDtTm", "_IntrmyAgt2Acct", "_XchgRateData", "_DbtrAgtAcct", "_PrvsInstgAgt2Acct", "_Purp", "_InstrForCdtrAgt", "_Cdtr", "_CdtrAcct", "_TrckrInfrmgPty", "_IntrBkSttlmDt", "_UltmtDbtr", "_Dbtr", "_PrvsInstgAgt2", "_PmtTpInf", "_InitgPty", "_PoolgAdjstmntDt", "_ChrgsInf", "_IntrmyAgt2", "_InstdAmt", "_DbtrAgt", "_RgltryRptg", "_PmtScnro", "_RmtInf", "_CdtrAgtAcct", "_TrckrData", "_IntrmyAgt3Acct", "_InstrForNxtAgt", "_TechSndr", "_CdtrAgt", "_DbtrAcct", "_IntrmyAgt3", "_OrgnlEndToEndId", "_OrgnlInstrId", "_RltdPmtId", "_PrvsInstgAgt3Acct", "_EqvtAmt", "_RltdRmtInf", "_UltmtCdtr", "_IntrBkSttlmAmt", "_IntrmyAgt1", "_RtrdIntrBkSttlmAmt", "_ReqdExctnDt", "_TrckdMsgId", "_SttlmInf", "_PrvsInstgAgt1", "_InstgAgt", "_RtrdInstdAmt", "_PrvsInstgAgt1Acct", "_Tax", "_TrckrInfrmdPty", "_PrvsInstgAgt3", "_SttlmTmIndctn", "_DbtConfURLAdr", "_TrckrRcrd", "_SttlmPrty", "_InstdAgt", "_RjctRtrRsn"]
	@property
	def ChrgBr(self):
		return self._ChrgBr

	@ChrgBr.setter
	def ChrgBr(self, value):
		self._ChrgBr = value if type(value) != auto else self.make_default("ChrgBr")

	@ChrgBr.deleter
	def ChrgBr(self):
		del self._ChrgBr
		self._ChrgBr = None

	@property
	def RtrChain(self):
		return self._RtrChain

	@RtrChain.setter
	def RtrChain(self, value):
		self._RtrChain = value if type(value) != auto else self.make_default("RtrChain")

	@RtrChain.deleter
	def RtrChain(self):
		del self._RtrChain
		self._RtrChain = None

	@property
	def PmtId(self):
		return self._PmtId

	@PmtId.setter
	def PmtId(self, value):
		self._PmtId = value if type(value) != auto else self.make_default("PmtId")

	@PmtId.deleter
	def PmtId(self):
		del self._PmtId
		self._PmtId = None

	@property
	def UndrlygCstmrCdtTrf(self):
		return self._UndrlygCstmrCdtTrf

	@UndrlygCstmrCdtTrf.setter
	def UndrlygCstmrCdtTrf(self, value):
		self._UndrlygCstmrCdtTrf = value if type(value) != auto else self.make_default("UndrlygCstmrCdtTrf")

	@UndrlygCstmrCdtTrf.deleter
	def UndrlygCstmrCdtTrf(self):
		del self._UndrlygCstmrCdtTrf
		self._UndrlygCstmrCdtTrf = None

	@property
	def TechRcvr(self):
		return self._TechRcvr

	@TechRcvr.setter
	def TechRcvr(self, value):
		self._TechRcvr = value if type(value) != auto else self.make_default("TechRcvr")

	@TechRcvr.deleter
	def TechRcvr(self):
		del self._TechRcvr
		self._TechRcvr = None

	@property
	def SttlmTmReq(self):
		return self._SttlmTmReq

	@SttlmTmReq.setter
	def SttlmTmReq(self, value):
		self._SttlmTmReq = value if type(value) != auto else self.make_default("SttlmTmReq")

	@SttlmTmReq.deleter
	def SttlmTmReq(self):
		del self._SttlmTmReq
		self._SttlmTmReq = None

	@property
	def IntrmyAgt1Acct(self):
		return self._IntrmyAgt1Acct

	@IntrmyAgt1Acct.setter
	def IntrmyAgt1Acct(self, value):
		self._IntrmyAgt1Acct = value if type(value) != auto else self.make_default("IntrmyAgt1Acct")

	@IntrmyAgt1Acct.deleter
	def IntrmyAgt1Acct(self):
		del self._IntrmyAgt1Acct
		self._IntrmyAgt1Acct = None

	@property
	def AccptncDtTm(self):
		return self._AccptncDtTm

	@AccptncDtTm.setter
	def AccptncDtTm(self, value):
		self._AccptncDtTm = value if type(value) != auto else self.make_default("AccptncDtTm")

	@AccptncDtTm.deleter
	def AccptncDtTm(self):
		del self._AccptncDtTm
		self._AccptncDtTm = None

	@property
	def IntrmyAgt2Acct(self):
		return self._IntrmyAgt2Acct

	@IntrmyAgt2Acct.setter
	def IntrmyAgt2Acct(self, value):
		self._IntrmyAgt2Acct = value if type(value) != auto else self.make_default("IntrmyAgt2Acct")

	@IntrmyAgt2Acct.deleter
	def IntrmyAgt2Acct(self):
		del self._IntrmyAgt2Acct
		self._IntrmyAgt2Acct = None

	@property
	def XchgRateData(self):
		return self._XchgRateData

	@XchgRateData.setter
	def XchgRateData(self, value):
		self._XchgRateData = value if type(value) != auto else self.make_default("XchgRateData")

	@XchgRateData.deleter
	def XchgRateData(self):
		del self._XchgRateData
		self._XchgRateData = None

	@property
	def DbtrAgtAcct(self):
		return self._DbtrAgtAcct

	@DbtrAgtAcct.setter
	def DbtrAgtAcct(self, value):
		self._DbtrAgtAcct = value if type(value) != auto else self.make_default("DbtrAgtAcct")

	@DbtrAgtAcct.deleter
	def DbtrAgtAcct(self):
		del self._DbtrAgtAcct
		self._DbtrAgtAcct = None

	@property
	def PrvsInstgAgt2Acct(self):
		return self._PrvsInstgAgt2Acct

	@PrvsInstgAgt2Acct.setter
	def PrvsInstgAgt2Acct(self, value):
		self._PrvsInstgAgt2Acct = value if type(value) != auto else self.make_default("PrvsInstgAgt2Acct")

	@PrvsInstgAgt2Acct.deleter
	def PrvsInstgAgt2Acct(self):
		del self._PrvsInstgAgt2Acct
		self._PrvsInstgAgt2Acct = None

	@property
	def Purp(self):
		return self._Purp

	@Purp.setter
	def Purp(self, value):
		self._Purp = value if type(value) != auto else self.make_default("Purp")

	@Purp.deleter
	def Purp(self):
		del self._Purp
		self._Purp = None

	@property
	def InstrForCdtrAgt(self):
		return self._InstrForCdtrAgt

	@InstrForCdtrAgt.setter
	def InstrForCdtrAgt(self, value):
		self._InstrForCdtrAgt = value if type(value) != auto else self.make_default("InstrForCdtrAgt")

	@InstrForCdtrAgt.deleter
	def InstrForCdtrAgt(self):
		del self._InstrForCdtrAgt
		self._InstrForCdtrAgt = None

	@property
	def Cdtr(self):
		return self._Cdtr

	@Cdtr.setter
	def Cdtr(self, value):
		self._Cdtr = value if type(value) != auto else self.make_default("Cdtr")

	@Cdtr.deleter
	def Cdtr(self):
		del self._Cdtr
		self._Cdtr = None

	@property
	def CdtrAcct(self):
		return self._CdtrAcct

	@CdtrAcct.setter
	def CdtrAcct(self, value):
		self._CdtrAcct = value if type(value) != auto else self.make_default("CdtrAcct")

	@CdtrAcct.deleter
	def CdtrAcct(self):
		del self._CdtrAcct
		self._CdtrAcct = None

	@property
	def TrckrInfrmgPty(self):
		return self._TrckrInfrmgPty

	@TrckrInfrmgPty.setter
	def TrckrInfrmgPty(self, value):
		self._TrckrInfrmgPty = value if type(value) != auto else self.make_default("TrckrInfrmgPty")

	@TrckrInfrmgPty.deleter
	def TrckrInfrmgPty(self):
		del self._TrckrInfrmgPty
		self._TrckrInfrmgPty = None

	@property
	def IntrBkSttlmDt(self):
		return self._IntrBkSttlmDt

	@IntrBkSttlmDt.setter
	def IntrBkSttlmDt(self, value):
		self._IntrBkSttlmDt = value if type(value) != auto else self.make_default("IntrBkSttlmDt")

	@IntrBkSttlmDt.deleter
	def IntrBkSttlmDt(self):
		del self._IntrBkSttlmDt
		self._IntrBkSttlmDt = None

	@property
	def UltmtDbtr(self):
		return self._UltmtDbtr

	@UltmtDbtr.setter
	def UltmtDbtr(self, value):
		self._UltmtDbtr = value if type(value) != auto else self.make_default("UltmtDbtr")

	@UltmtDbtr.deleter
	def UltmtDbtr(self):
		del self._UltmtDbtr
		self._UltmtDbtr = None

	@property
	def Dbtr(self):
		return self._Dbtr

	@Dbtr.setter
	def Dbtr(self, value):
		self._Dbtr = value if type(value) != auto else self.make_default("Dbtr")

	@Dbtr.deleter
	def Dbtr(self):
		del self._Dbtr
		self._Dbtr = None

	@property
	def PrvsInstgAgt2(self):
		return self._PrvsInstgAgt2

	@PrvsInstgAgt2.setter
	def PrvsInstgAgt2(self, value):
		self._PrvsInstgAgt2 = value if type(value) != auto else self.make_default("PrvsInstgAgt2")

	@PrvsInstgAgt2.deleter
	def PrvsInstgAgt2(self):
		del self._PrvsInstgAgt2
		self._PrvsInstgAgt2 = None

	@property
	def PmtTpInf(self):
		return self._PmtTpInf

	@PmtTpInf.setter
	def PmtTpInf(self, value):
		self._PmtTpInf = value if type(value) != auto else self.make_default("PmtTpInf")

	@PmtTpInf.deleter
	def PmtTpInf(self):
		del self._PmtTpInf
		self._PmtTpInf = None

	@property
	def InitgPty(self):
		return self._InitgPty

	@InitgPty.setter
	def InitgPty(self, value):
		self._InitgPty = value if type(value) != auto else self.make_default("InitgPty")

	@InitgPty.deleter
	def InitgPty(self):
		del self._InitgPty
		self._InitgPty = None

	@property
	def PoolgAdjstmntDt(self):
		return self._PoolgAdjstmntDt

	@PoolgAdjstmntDt.setter
	def PoolgAdjstmntDt(self, value):
		self._PoolgAdjstmntDt = value if type(value) != auto else self.make_default("PoolgAdjstmntDt")

	@PoolgAdjstmntDt.deleter
	def PoolgAdjstmntDt(self):
		del self._PoolgAdjstmntDt
		self._PoolgAdjstmntDt = None

	@property
	def ChrgsInf(self):
		return self._ChrgsInf

	@ChrgsInf.setter
	def ChrgsInf(self, value):
		self._ChrgsInf = value if type(value) != auto else self.make_default("ChrgsInf")

	@ChrgsInf.deleter
	def ChrgsInf(self):
		del self._ChrgsInf
		self._ChrgsInf = None

	@property
	def IntrmyAgt2(self):
		return self._IntrmyAgt2

	@IntrmyAgt2.setter
	def IntrmyAgt2(self, value):
		self._IntrmyAgt2 = value if type(value) != auto else self.make_default("IntrmyAgt2")

	@IntrmyAgt2.deleter
	def IntrmyAgt2(self):
		del self._IntrmyAgt2
		self._IntrmyAgt2 = None

	@property
	def InstdAmt(self):
		return self._InstdAmt

	@InstdAmt.setter
	def InstdAmt(self, value):
		self._InstdAmt = value if type(value) != auto else self.make_default("InstdAmt")

	@InstdAmt.deleter
	def InstdAmt(self):
		del self._InstdAmt
		self._InstdAmt = None

	@property
	def DbtrAgt(self):
		return self._DbtrAgt

	@DbtrAgt.setter
	def DbtrAgt(self, value):
		self._DbtrAgt = value if type(value) != auto else self.make_default("DbtrAgt")

	@DbtrAgt.deleter
	def DbtrAgt(self):
		del self._DbtrAgt
		self._DbtrAgt = None

	@property
	def RgltryRptg(self):
		return self._RgltryRptg

	@RgltryRptg.setter
	def RgltryRptg(self, value):
		self._RgltryRptg = value if type(value) != auto else self.make_default("RgltryRptg")

	@RgltryRptg.deleter
	def RgltryRptg(self):
		del self._RgltryRptg
		self._RgltryRptg = None

	@property
	def PmtScnro(self):
		return self._PmtScnro

	@PmtScnro.setter
	def PmtScnro(self, value):
		self._PmtScnro = value if type(value) != auto else self.make_default("PmtScnro")

	@PmtScnro.deleter
	def PmtScnro(self):
		del self._PmtScnro
		self._PmtScnro = None

	@property
	def RmtInf(self):
		return self._RmtInf

	@RmtInf.setter
	def RmtInf(self, value):
		self._RmtInf = value if type(value) != auto else self.make_default("RmtInf")

	@RmtInf.deleter
	def RmtInf(self):
		del self._RmtInf
		self._RmtInf = None

	@property
	def CdtrAgtAcct(self):
		return self._CdtrAgtAcct

	@CdtrAgtAcct.setter
	def CdtrAgtAcct(self, value):
		self._CdtrAgtAcct = value if type(value) != auto else self.make_default("CdtrAgtAcct")

	@CdtrAgtAcct.deleter
	def CdtrAgtAcct(self):
		del self._CdtrAgtAcct
		self._CdtrAgtAcct = None

	@property
	def TrckrData(self):
		return self._TrckrData

	@TrckrData.setter
	def TrckrData(self, value):
		self._TrckrData = value if type(value) != auto else self.make_default("TrckrData")

	@TrckrData.deleter
	def TrckrData(self):
		del self._TrckrData
		self._TrckrData = None

	@property
	def IntrmyAgt3Acct(self):
		return self._IntrmyAgt3Acct

	@IntrmyAgt3Acct.setter
	def IntrmyAgt3Acct(self, value):
		self._IntrmyAgt3Acct = value if type(value) != auto else self.make_default("IntrmyAgt3Acct")

	@IntrmyAgt3Acct.deleter
	def IntrmyAgt3Acct(self):
		del self._IntrmyAgt3Acct
		self._IntrmyAgt3Acct = None

	@property
	def InstrForNxtAgt(self):
		return self._InstrForNxtAgt

	@InstrForNxtAgt.setter
	def InstrForNxtAgt(self, value):
		self._InstrForNxtAgt = value if type(value) != auto else self.make_default("InstrForNxtAgt")

	@InstrForNxtAgt.deleter
	def InstrForNxtAgt(self):
		del self._InstrForNxtAgt
		self._InstrForNxtAgt = None

	@property
	def TechSndr(self):
		return self._TechSndr

	@TechSndr.setter
	def TechSndr(self, value):
		self._TechSndr = value if type(value) != auto else self.make_default("TechSndr")

	@TechSndr.deleter
	def TechSndr(self):
		del self._TechSndr
		self._TechSndr = None

	@property
	def CdtrAgt(self):
		return self._CdtrAgt

	@CdtrAgt.setter
	def CdtrAgt(self, value):
		self._CdtrAgt = value if type(value) != auto else self.make_default("CdtrAgt")

	@CdtrAgt.deleter
	def CdtrAgt(self):
		del self._CdtrAgt
		self._CdtrAgt = None

	@property
	def DbtrAcct(self):
		return self._DbtrAcct

	@DbtrAcct.setter
	def DbtrAcct(self, value):
		self._DbtrAcct = value if type(value) != auto else self.make_default("DbtrAcct")

	@DbtrAcct.deleter
	def DbtrAcct(self):
		del self._DbtrAcct
		self._DbtrAcct = None

	@property
	def IntrmyAgt3(self):
		return self._IntrmyAgt3

	@IntrmyAgt3.setter
	def IntrmyAgt3(self, value):
		self._IntrmyAgt3 = value if type(value) != auto else self.make_default("IntrmyAgt3")

	@IntrmyAgt3.deleter
	def IntrmyAgt3(self):
		del self._IntrmyAgt3
		self._IntrmyAgt3 = None

	@property
	def OrgnlEndToEndId(self):
		return self._OrgnlEndToEndId

	@OrgnlEndToEndId.setter
	def OrgnlEndToEndId(self, value):
		self._OrgnlEndToEndId = value if type(value) != auto else self.make_default("OrgnlEndToEndId")

	@OrgnlEndToEndId.deleter
	def OrgnlEndToEndId(self):
		del self._OrgnlEndToEndId
		self._OrgnlEndToEndId = None

	@property
	def OrgnlInstrId(self):
		return self._OrgnlInstrId

	@OrgnlInstrId.setter
	def OrgnlInstrId(self, value):
		self._OrgnlInstrId = value if type(value) != auto else self.make_default("OrgnlInstrId")

	@OrgnlInstrId.deleter
	def OrgnlInstrId(self):
		del self._OrgnlInstrId
		self._OrgnlInstrId = None

	@property
	def RltdPmtId(self):
		return self._RltdPmtId

	@RltdPmtId.setter
	def RltdPmtId(self, value):
		self._RltdPmtId = value if type(value) != auto else self.make_default("RltdPmtId")

	@RltdPmtId.deleter
	def RltdPmtId(self):
		del self._RltdPmtId
		self._RltdPmtId = None

	@property
	def PrvsInstgAgt3Acct(self):
		return self._PrvsInstgAgt3Acct

	@PrvsInstgAgt3Acct.setter
	def PrvsInstgAgt3Acct(self, value):
		self._PrvsInstgAgt3Acct = value if type(value) != auto else self.make_default("PrvsInstgAgt3Acct")

	@PrvsInstgAgt3Acct.deleter
	def PrvsInstgAgt3Acct(self):
		del self._PrvsInstgAgt3Acct
		self._PrvsInstgAgt3Acct = None

	@property
	def EqvtAmt(self):
		return self._EqvtAmt

	@EqvtAmt.setter
	def EqvtAmt(self, value):
		self._EqvtAmt = value if type(value) != auto else self.make_default("EqvtAmt")

	@EqvtAmt.deleter
	def EqvtAmt(self):
		del self._EqvtAmt
		self._EqvtAmt = None

	@property
	def RltdRmtInf(self):
		return self._RltdRmtInf

	@RltdRmtInf.setter
	def RltdRmtInf(self, value):
		self._RltdRmtInf = value if type(value) != auto else self.make_default("RltdRmtInf")

	@RltdRmtInf.deleter
	def RltdRmtInf(self):
		del self._RltdRmtInf
		self._RltdRmtInf = None

	@property
	def UltmtCdtr(self):
		return self._UltmtCdtr

	@UltmtCdtr.setter
	def UltmtCdtr(self, value):
		self._UltmtCdtr = value if type(value) != auto else self.make_default("UltmtCdtr")

	@UltmtCdtr.deleter
	def UltmtCdtr(self):
		del self._UltmtCdtr
		self._UltmtCdtr = None

	@property
	def IntrBkSttlmAmt(self):
		return self._IntrBkSttlmAmt

	@IntrBkSttlmAmt.setter
	def IntrBkSttlmAmt(self, value):
		self._IntrBkSttlmAmt = value if type(value) != auto else self.make_default("IntrBkSttlmAmt")

	@IntrBkSttlmAmt.deleter
	def IntrBkSttlmAmt(self):
		del self._IntrBkSttlmAmt
		self._IntrBkSttlmAmt = None

	@property
	def IntrmyAgt1(self):
		return self._IntrmyAgt1

	@IntrmyAgt1.setter
	def IntrmyAgt1(self, value):
		self._IntrmyAgt1 = value if type(value) != auto else self.make_default("IntrmyAgt1")

	@IntrmyAgt1.deleter
	def IntrmyAgt1(self):
		del self._IntrmyAgt1
		self._IntrmyAgt1 = None

	@property
	def RtrdIntrBkSttlmAmt(self):
		return self._RtrdIntrBkSttlmAmt

	@RtrdIntrBkSttlmAmt.setter
	def RtrdIntrBkSttlmAmt(self, value):
		self._RtrdIntrBkSttlmAmt = value if type(value) != auto else self.make_default("RtrdIntrBkSttlmAmt")

	@RtrdIntrBkSttlmAmt.deleter
	def RtrdIntrBkSttlmAmt(self):
		del self._RtrdIntrBkSttlmAmt
		self._RtrdIntrBkSttlmAmt = None

	@property
	def ReqdExctnDt(self):
		return self._ReqdExctnDt

	@ReqdExctnDt.setter
	def ReqdExctnDt(self, value):
		self._ReqdExctnDt = value if type(value) != auto else self.make_default("ReqdExctnDt")

	@ReqdExctnDt.deleter
	def ReqdExctnDt(self):
		del self._ReqdExctnDt
		self._ReqdExctnDt = None

	@property
	def TrckdMsgId(self):
		return self._TrckdMsgId

	@TrckdMsgId.setter
	def TrckdMsgId(self, value):
		self._TrckdMsgId = value if type(value) != auto else self.make_default("TrckdMsgId")

	@TrckdMsgId.deleter
	def TrckdMsgId(self):
		del self._TrckdMsgId
		self._TrckdMsgId = None

	@property
	def SttlmInf(self):
		return self._SttlmInf

	@SttlmInf.setter
	def SttlmInf(self, value):
		self._SttlmInf = value if type(value) != auto else self.make_default("SttlmInf")

	@SttlmInf.deleter
	def SttlmInf(self):
		del self._SttlmInf
		self._SttlmInf = None

	@property
	def PrvsInstgAgt1(self):
		return self._PrvsInstgAgt1

	@PrvsInstgAgt1.setter
	def PrvsInstgAgt1(self, value):
		self._PrvsInstgAgt1 = value if type(value) != auto else self.make_default("PrvsInstgAgt1")

	@PrvsInstgAgt1.deleter
	def PrvsInstgAgt1(self):
		del self._PrvsInstgAgt1
		self._PrvsInstgAgt1 = None

	@property
	def InstgAgt(self):
		return self._InstgAgt

	@InstgAgt.setter
	def InstgAgt(self, value):
		self._InstgAgt = value if type(value) != auto else self.make_default("InstgAgt")

	@InstgAgt.deleter
	def InstgAgt(self):
		del self._InstgAgt
		self._InstgAgt = None

	@property
	def RtrdInstdAmt(self):
		return self._RtrdInstdAmt

	@RtrdInstdAmt.setter
	def RtrdInstdAmt(self, value):
		self._RtrdInstdAmt = value if type(value) != auto else self.make_default("RtrdInstdAmt")

	@RtrdInstdAmt.deleter
	def RtrdInstdAmt(self):
		del self._RtrdInstdAmt
		self._RtrdInstdAmt = None

	@property
	def PrvsInstgAgt1Acct(self):
		return self._PrvsInstgAgt1Acct

	@PrvsInstgAgt1Acct.setter
	def PrvsInstgAgt1Acct(self, value):
		self._PrvsInstgAgt1Acct = value if type(value) != auto else self.make_default("PrvsInstgAgt1Acct")

	@PrvsInstgAgt1Acct.deleter
	def PrvsInstgAgt1Acct(self):
		del self._PrvsInstgAgt1Acct
		self._PrvsInstgAgt1Acct = None

	@property
	def Tax(self):
		return self._Tax

	@Tax.setter
	def Tax(self, value):
		self._Tax = value if type(value) != auto else self.make_default("Tax")

	@Tax.deleter
	def Tax(self):
		del self._Tax
		self._Tax = None

	@property
	def TrckrInfrmdPty(self):
		return self._TrckrInfrmdPty

	@TrckrInfrmdPty.setter
	def TrckrInfrmdPty(self, value):
		self._TrckrInfrmdPty = value if type(value) != auto else self.make_default("TrckrInfrmdPty")

	@TrckrInfrmdPty.deleter
	def TrckrInfrmdPty(self):
		del self._TrckrInfrmdPty
		self._TrckrInfrmdPty = None

	@property
	def PrvsInstgAgt3(self):
		return self._PrvsInstgAgt3

	@PrvsInstgAgt3.setter
	def PrvsInstgAgt3(self, value):
		self._PrvsInstgAgt3 = value if type(value) != auto else self.make_default("PrvsInstgAgt3")

	@PrvsInstgAgt3.deleter
	def PrvsInstgAgt3(self):
		del self._PrvsInstgAgt3
		self._PrvsInstgAgt3 = None

	@property
	def SttlmTmIndctn(self):
		return self._SttlmTmIndctn

	@SttlmTmIndctn.setter
	def SttlmTmIndctn(self, value):
		self._SttlmTmIndctn = value if type(value) != auto else self.make_default("SttlmTmIndctn")

	@SttlmTmIndctn.deleter
	def SttlmTmIndctn(self):
		del self._SttlmTmIndctn
		self._SttlmTmIndctn = None

	@property
	def DbtConfURLAdr(self):
		return self._DbtConfURLAdr

	@DbtConfURLAdr.setter
	def DbtConfURLAdr(self, value):
		self._DbtConfURLAdr = value if type(value) != auto else self.make_default("DbtConfURLAdr")

	@DbtConfURLAdr.deleter
	def DbtConfURLAdr(self):
		del self._DbtConfURLAdr
		self._DbtConfURLAdr = None

	@property
	def TrckrRcrd(self):
		return self._TrckrRcrd

	@TrckrRcrd.setter
	def TrckrRcrd(self, value):
		self._TrckrRcrd = value if type(value) != auto else self.make_default("TrckrRcrd")

	@TrckrRcrd.deleter
	def TrckrRcrd(self):
		del self._TrckrRcrd
		self._TrckrRcrd = None

	@property
	def SttlmPrty(self):
		return self._SttlmPrty

	@SttlmPrty.setter
	def SttlmPrty(self, value):
		self._SttlmPrty = value if type(value) != auto else self.make_default("SttlmPrty")

	@SttlmPrty.deleter
	def SttlmPrty(self):
		del self._SttlmPrty
		self._SttlmPrty = None

	@property
	def InstdAgt(self):
		return self._InstdAgt

	@InstdAgt.setter
	def InstdAgt(self, value):
		self._InstdAgt = value if type(value) != auto else self.make_default("InstdAgt")

	@InstdAgt.deleter
	def InstdAgt(self):
		del self._InstdAgt
		self._InstdAgt = None

	@property
	def RjctRtrRsn(self):
		return self._RjctRtrRsn

	@RjctRtrRsn.setter
	def RjctRtrRsn(self, value):
		self._RjctRtrRsn = value if type(value) != auto else self.make_default("RjctRtrRsn")

	@RjctRtrRsn.deleter
	def RjctRtrRsn(self):
		del self._RjctRtrRsn
		self._RjctRtrRsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ChrgBr', type=ChargeBearerType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrChain', type=TransactionParties8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtId', type=PaymentIdentification10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygCstmrCdtTrf', type=CreditTransferTransaction46, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TechRcvr', type=BICFIDec2014Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmTmReq', type=SettlementTimeRequest2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyAgt1Acct', type=CashAccount38, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AccptncDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyAgt2Acct', type=CashAccount38, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgRateData', type=CurrencyExchange15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAgtAcct', type=CashAccount38, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsInstgAgt2Acct', type=CashAccount38, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Purp', type=Purpose2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrForCdtrAgt', type=InstructionForCreditorAgent3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Cdtr', type=Party40Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAcct', type=CashAccount38, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrckrInfrmgPty', type=TrackerPartyIdentification2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrBkSttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UltmtDbtr', type=PartyIdentification135, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dbtr', type=Party40Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsInstgAgt2', type=BranchAndFinancialInstitutionIdentification6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtTpInf', type=PaymentTypeInformation28, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitgPty', type=PartyIdentification135, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PoolgAdjstmntDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsInf', type=Charges7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IntrmyAgt2', type=BranchAndFinancialInstitutionIdentification6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstdAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAgt', type=BranchAndFinancialInstitutionIdentification6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RgltryRptg', type=RegulatoryReporting3, min=0, max=10, mutex_group=None, array=True),
		base_types.FieldEntry(name='PmtScnro', type=PaymentScenario1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmtInf', type=RemittanceInformation16, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAgtAcct', type=CashAccount38, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrckrData', type=TrackerData8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyAgt3Acct', type=CashAccount38, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrForNxtAgt', type=InstructionForNextAgent1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TechSndr', type=BICFIDec2014Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAgt', type=BranchAndFinancialInstitutionIdentification6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAcct', type=CashAccount38, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyAgt3', type=BranchAndFinancialInstitutionIdentification6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlEndToEndId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlInstrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdPmtId', type=RelatedTransactionData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsInstgAgt3Acct', type=CashAccount38, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EqvtAmt', type=EquivalentAmount2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdRmtInf', type=RemittanceLocation7, min=0, max=10, mutex_group=None, array=True),
		base_types.FieldEntry(name='UltmtCdtr', type=PartyIdentification135, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrBkSttlmAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyAgt1', type=BranchAndFinancialInstitutionIdentification6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrdIntrBkSttlmAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdExctnDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrckdMsgId', type=OriginalBusinessInstruction4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmInf', type=SettlementInstruction9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsInstgAgt1', type=BranchAndFinancialInstitutionIdentification6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstgAgt', type=BranchAndFinancialInstitutionIdentification6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrdInstdAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsInstgAgt1Acct', type=CashAccount38, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tax', type=TaxInformation8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrckrInfrmdPty', type=TrackerPartyIdentification2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsInstgAgt3', type=BranchAndFinancialInstitutionIdentification6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmTmIndctn', type=SettlementDateTimeIndication1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtConfURLAdr', type=Max2048Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrckrRcrd', type=TrackerRecord8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmPrty', type=Priority3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstdAgt', type=BranchAndFinancialInstitutionIdentification6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctRtrRsn', type=PaymentRejectReturnReason1, min=0, max=None, mutex_group=None, array=True),
	))

