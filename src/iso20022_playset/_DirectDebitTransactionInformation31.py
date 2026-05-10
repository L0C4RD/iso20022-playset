from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount
from ._BaseOneRate import BaseOneRate
from ._BranchAndFinancialInstitutionIdentification8 import BranchAndFinancialInstitutionIdentification8
from ._CashAccount40 import CashAccount40
from ._ChargeBearerType1Code import ChargeBearerType1Code
from ._Charges16 import Charges16
from ._DirectDebitTransaction12 import DirectDebitTransaction12
from ._ISODate import ISODate
from ._PartyIdentification272 import PartyIdentification272
from ._PaymentIdentification13 import PaymentIdentification13
from ._PaymentTypeInformation27 import PaymentTypeInformation27
from ._Priority3Code import Priority3Code
from ._Purpose2Choice import Purpose2Choice
from ._RegulatoryReporting3 import RegulatoryReporting3
from ._RemittanceInformation22 import RemittanceInformation22
from ._RemittanceLocation8 import RemittanceLocation8
from ._SettlementDateTimeIndication1 import SettlementDateTimeIndication1
from ._SupplementaryData1 import SupplementaryData1

class DirectDebitTransactionInformation31(base_types._BaseFieldType):

	__slots__ = ["_Cdtr", "_CdtrAcct", "_CdtrAgt", "_CdtrAgtAcct", "_ChrgBr", "_ChrgsInf", "_Dbtr", "_DbtrAcct", "_DbtrAgt", "_DbtrAgtAcct", "_DrctDbtTx", "_InitgPty", "_InstdAgt", "_InstdAmt", "_InstgAgt", "_IntrBkSttlmAmt", "_IntrBkSttlmDt", "_IntrmyAgt1", "_IntrmyAgt1Acct", "_IntrmyAgt2", "_IntrmyAgt2Acct", "_IntrmyAgt3", "_IntrmyAgt3Acct", "_PmtId", "_PmtTpInf", "_Purp", "_ReqdColltnDt", "_RgltryRptg", "_RltdRmtInf", "_RmtInf", "_SplmtryData", "_SttlmPrty", "_SttlmTmIndctn", "_UltmtCdtr", "_UltmtDbtr", "_XchgRate"]
	@property
	def Cdtr(self):
		return self._Cdtr

	@Cdtr.setter
	def Cdtr(self, value):
		self._Cdtr = value if type(value) != base_types.auto else self.make_default("Cdtr")

	@Cdtr.deleter
	def Cdtr(self):
		del self._Cdtr
		self._Cdtr = None

	@property
	def CdtrAcct(self):
		return self._CdtrAcct

	@CdtrAcct.setter
	def CdtrAcct(self, value):
		self._CdtrAcct = value if type(value) != base_types.auto else self.make_default("CdtrAcct")

	@CdtrAcct.deleter
	def CdtrAcct(self):
		del self._CdtrAcct
		self._CdtrAcct = None

	@property
	def CdtrAgt(self):
		return self._CdtrAgt

	@CdtrAgt.setter
	def CdtrAgt(self, value):
		self._CdtrAgt = value if type(value) != base_types.auto else self.make_default("CdtrAgt")

	@CdtrAgt.deleter
	def CdtrAgt(self):
		del self._CdtrAgt
		self._CdtrAgt = None

	@property
	def CdtrAgtAcct(self):
		return self._CdtrAgtAcct

	@CdtrAgtAcct.setter
	def CdtrAgtAcct(self, value):
		self._CdtrAgtAcct = value if type(value) != base_types.auto else self.make_default("CdtrAgtAcct")

	@CdtrAgtAcct.deleter
	def CdtrAgtAcct(self):
		del self._CdtrAgtAcct
		self._CdtrAgtAcct = None

	@property
	def ChrgBr(self):
		return self._ChrgBr

	@ChrgBr.setter
	def ChrgBr(self, value):
		self._ChrgBr = value if type(value) != base_types.auto else self.make_default("ChrgBr")

	@ChrgBr.deleter
	def ChrgBr(self):
		del self._ChrgBr
		self._ChrgBr = None

	@property
	def ChrgsInf(self):
		return self._ChrgsInf

	@ChrgsInf.setter
	def ChrgsInf(self, value):
		self._ChrgsInf = value if type(value) != base_types.auto else self.make_default("ChrgsInf")

	@ChrgsInf.deleter
	def ChrgsInf(self):
		del self._ChrgsInf
		self._ChrgsInf = None

	@property
	def Dbtr(self):
		return self._Dbtr

	@Dbtr.setter
	def Dbtr(self, value):
		self._Dbtr = value if type(value) != base_types.auto else self.make_default("Dbtr")

	@Dbtr.deleter
	def Dbtr(self):
		del self._Dbtr
		self._Dbtr = None

	@property
	def DbtrAcct(self):
		return self._DbtrAcct

	@DbtrAcct.setter
	def DbtrAcct(self, value):
		self._DbtrAcct = value if type(value) != base_types.auto else self.make_default("DbtrAcct")

	@DbtrAcct.deleter
	def DbtrAcct(self):
		del self._DbtrAcct
		self._DbtrAcct = None

	@property
	def DbtrAgt(self):
		return self._DbtrAgt

	@DbtrAgt.setter
	def DbtrAgt(self, value):
		self._DbtrAgt = value if type(value) != base_types.auto else self.make_default("DbtrAgt")

	@DbtrAgt.deleter
	def DbtrAgt(self):
		del self._DbtrAgt
		self._DbtrAgt = None

	@property
	def DbtrAgtAcct(self):
		return self._DbtrAgtAcct

	@DbtrAgtAcct.setter
	def DbtrAgtAcct(self, value):
		self._DbtrAgtAcct = value if type(value) != base_types.auto else self.make_default("DbtrAgtAcct")

	@DbtrAgtAcct.deleter
	def DbtrAgtAcct(self):
		del self._DbtrAgtAcct
		self._DbtrAgtAcct = None

	@property
	def DrctDbtTx(self):
		return self._DrctDbtTx

	@DrctDbtTx.setter
	def DrctDbtTx(self, value):
		self._DrctDbtTx = value if type(value) != base_types.auto else self.make_default("DrctDbtTx")

	@DrctDbtTx.deleter
	def DrctDbtTx(self):
		del self._DrctDbtTx
		self._DrctDbtTx = None

	@property
	def InitgPty(self):
		return self._InitgPty

	@InitgPty.setter
	def InitgPty(self, value):
		self._InitgPty = value if type(value) != base_types.auto else self.make_default("InitgPty")

	@InitgPty.deleter
	def InitgPty(self):
		del self._InitgPty
		self._InitgPty = None

	@property
	def InstdAgt(self):
		return self._InstdAgt

	@InstdAgt.setter
	def InstdAgt(self, value):
		self._InstdAgt = value if type(value) != base_types.auto else self.make_default("InstdAgt")

	@InstdAgt.deleter
	def InstdAgt(self):
		del self._InstdAgt
		self._InstdAgt = None

	@property
	def InstdAmt(self):
		return self._InstdAmt

	@InstdAmt.setter
	def InstdAmt(self, value):
		self._InstdAmt = value if type(value) != base_types.auto else self.make_default("InstdAmt")

	@InstdAmt.deleter
	def InstdAmt(self):
		del self._InstdAmt
		self._InstdAmt = None

	@property
	def InstgAgt(self):
		return self._InstgAgt

	@InstgAgt.setter
	def InstgAgt(self, value):
		self._InstgAgt = value if type(value) != base_types.auto else self.make_default("InstgAgt")

	@InstgAgt.deleter
	def InstgAgt(self):
		del self._InstgAgt
		self._InstgAgt = None

	@property
	def IntrBkSttlmAmt(self):
		return self._IntrBkSttlmAmt

	@IntrBkSttlmAmt.setter
	def IntrBkSttlmAmt(self, value):
		self._IntrBkSttlmAmt = value if type(value) != base_types.auto else self.make_default("IntrBkSttlmAmt")

	@IntrBkSttlmAmt.deleter
	def IntrBkSttlmAmt(self):
		del self._IntrBkSttlmAmt
		self._IntrBkSttlmAmt = None

	@property
	def IntrBkSttlmDt(self):
		return self._IntrBkSttlmDt

	@IntrBkSttlmDt.setter
	def IntrBkSttlmDt(self, value):
		self._IntrBkSttlmDt = value if type(value) != base_types.auto else self.make_default("IntrBkSttlmDt")

	@IntrBkSttlmDt.deleter
	def IntrBkSttlmDt(self):
		del self._IntrBkSttlmDt
		self._IntrBkSttlmDt = None

	@property
	def IntrmyAgt1(self):
		return self._IntrmyAgt1

	@IntrmyAgt1.setter
	def IntrmyAgt1(self, value):
		self._IntrmyAgt1 = value if type(value) != base_types.auto else self.make_default("IntrmyAgt1")

	@IntrmyAgt1.deleter
	def IntrmyAgt1(self):
		del self._IntrmyAgt1
		self._IntrmyAgt1 = None

	@property
	def IntrmyAgt1Acct(self):
		return self._IntrmyAgt1Acct

	@IntrmyAgt1Acct.setter
	def IntrmyAgt1Acct(self, value):
		self._IntrmyAgt1Acct = value if type(value) != base_types.auto else self.make_default("IntrmyAgt1Acct")

	@IntrmyAgt1Acct.deleter
	def IntrmyAgt1Acct(self):
		del self._IntrmyAgt1Acct
		self._IntrmyAgt1Acct = None

	@property
	def IntrmyAgt2(self):
		return self._IntrmyAgt2

	@IntrmyAgt2.setter
	def IntrmyAgt2(self, value):
		self._IntrmyAgt2 = value if type(value) != base_types.auto else self.make_default("IntrmyAgt2")

	@IntrmyAgt2.deleter
	def IntrmyAgt2(self):
		del self._IntrmyAgt2
		self._IntrmyAgt2 = None

	@property
	def IntrmyAgt2Acct(self):
		return self._IntrmyAgt2Acct

	@IntrmyAgt2Acct.setter
	def IntrmyAgt2Acct(self, value):
		self._IntrmyAgt2Acct = value if type(value) != base_types.auto else self.make_default("IntrmyAgt2Acct")

	@IntrmyAgt2Acct.deleter
	def IntrmyAgt2Acct(self):
		del self._IntrmyAgt2Acct
		self._IntrmyAgt2Acct = None

	@property
	def IntrmyAgt3(self):
		return self._IntrmyAgt3

	@IntrmyAgt3.setter
	def IntrmyAgt3(self, value):
		self._IntrmyAgt3 = value if type(value) != base_types.auto else self.make_default("IntrmyAgt3")

	@IntrmyAgt3.deleter
	def IntrmyAgt3(self):
		del self._IntrmyAgt3
		self._IntrmyAgt3 = None

	@property
	def IntrmyAgt3Acct(self):
		return self._IntrmyAgt3Acct

	@IntrmyAgt3Acct.setter
	def IntrmyAgt3Acct(self, value):
		self._IntrmyAgt3Acct = value if type(value) != base_types.auto else self.make_default("IntrmyAgt3Acct")

	@IntrmyAgt3Acct.deleter
	def IntrmyAgt3Acct(self):
		del self._IntrmyAgt3Acct
		self._IntrmyAgt3Acct = None

	@property
	def PmtId(self):
		return self._PmtId

	@PmtId.setter
	def PmtId(self, value):
		self._PmtId = value if type(value) != base_types.auto else self.make_default("PmtId")

	@PmtId.deleter
	def PmtId(self):
		del self._PmtId
		self._PmtId = None

	@property
	def PmtTpInf(self):
		return self._PmtTpInf

	@PmtTpInf.setter
	def PmtTpInf(self, value):
		self._PmtTpInf = value if type(value) != base_types.auto else self.make_default("PmtTpInf")

	@PmtTpInf.deleter
	def PmtTpInf(self):
		del self._PmtTpInf
		self._PmtTpInf = None

	@property
	def Purp(self):
		return self._Purp

	@Purp.setter
	def Purp(self, value):
		self._Purp = value if type(value) != base_types.auto else self.make_default("Purp")

	@Purp.deleter
	def Purp(self):
		del self._Purp
		self._Purp = None

	@property
	def ReqdColltnDt(self):
		return self._ReqdColltnDt

	@ReqdColltnDt.setter
	def ReqdColltnDt(self, value):
		self._ReqdColltnDt = value if type(value) != base_types.auto else self.make_default("ReqdColltnDt")

	@ReqdColltnDt.deleter
	def ReqdColltnDt(self):
		del self._ReqdColltnDt
		self._ReqdColltnDt = None

	@property
	def RgltryRptg(self):
		return self._RgltryRptg

	@RgltryRptg.setter
	def RgltryRptg(self, value):
		self._RgltryRptg = value if type(value) != base_types.auto else self.make_default("RgltryRptg")

	@RgltryRptg.deleter
	def RgltryRptg(self):
		del self._RgltryRptg
		self._RgltryRptg = None

	@property
	def RltdRmtInf(self):
		return self._RltdRmtInf

	@RltdRmtInf.setter
	def RltdRmtInf(self, value):
		self._RltdRmtInf = value if type(value) != base_types.auto else self.make_default("RltdRmtInf")

	@RltdRmtInf.deleter
	def RltdRmtInf(self):
		del self._RltdRmtInf
		self._RltdRmtInf = None

	@property
	def RmtInf(self):
		return self._RmtInf

	@RmtInf.setter
	def RmtInf(self, value):
		self._RmtInf = value if type(value) != base_types.auto else self.make_default("RmtInf")

	@RmtInf.deleter
	def RmtInf(self):
		del self._RmtInf
		self._RmtInf = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def SttlmPrty(self):
		return self._SttlmPrty

	@SttlmPrty.setter
	def SttlmPrty(self, value):
		self._SttlmPrty = value if type(value) != base_types.auto else self.make_default("SttlmPrty")

	@SttlmPrty.deleter
	def SttlmPrty(self):
		del self._SttlmPrty
		self._SttlmPrty = None

	@property
	def SttlmTmIndctn(self):
		return self._SttlmTmIndctn

	@SttlmTmIndctn.setter
	def SttlmTmIndctn(self, value):
		self._SttlmTmIndctn = value if type(value) != base_types.auto else self.make_default("SttlmTmIndctn")

	@SttlmTmIndctn.deleter
	def SttlmTmIndctn(self):
		del self._SttlmTmIndctn
		self._SttlmTmIndctn = None

	@property
	def UltmtCdtr(self):
		return self._UltmtCdtr

	@UltmtCdtr.setter
	def UltmtCdtr(self, value):
		self._UltmtCdtr = value if type(value) != base_types.auto else self.make_default("UltmtCdtr")

	@UltmtCdtr.deleter
	def UltmtCdtr(self):
		del self._UltmtCdtr
		self._UltmtCdtr = None

	@property
	def UltmtDbtr(self):
		return self._UltmtDbtr

	@UltmtDbtr.setter
	def UltmtDbtr(self, value):
		self._UltmtDbtr = value if type(value) != base_types.auto else self.make_default("UltmtDbtr")

	@UltmtDbtr.deleter
	def UltmtDbtr(self):
		del self._UltmtDbtr
		self._UltmtDbtr = None

	@property
	def XchgRate(self):
		return self._XchgRate

	@XchgRate.setter
	def XchgRate(self, value):
		self._XchgRate = value if type(value) != base_types.auto else self.make_default("XchgRate")

	@XchgRate.deleter
	def XchgRate(self):
		del self._XchgRate
		self._XchgRate = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cdtr', type=PartyIdentification272, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAgt', type=BranchAndFinancialInstitutionIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAgtAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgBr', type=ChargeBearerType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsInf', type=Charges16, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Dbtr', type=PartyIdentification272, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAcct', type=CashAccount40, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAgt', type=BranchAndFinancialInstitutionIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAgtAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrctDbtTx', type=DirectDebitTransaction12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitgPty', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstdAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstdAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstgAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrBkSttlmAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrBkSttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyAgt1', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyAgt1Acct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyAgt2', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyAgt2Acct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyAgt3', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyAgt3Acct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtId', type=PaymentIdentification13, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtTpInf', type=PaymentTypeInformation27, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Purp', type=Purpose2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdColltnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RgltryRptg', type=RegulatoryReporting3, min=0, max=10, mutex_group=None, array=True),
		base_types.FieldEntry(name='RltdRmtInf', type=RemittanceLocation8, min=0, max=10, mutex_group=None, array=True),
		base_types.FieldEntry(name='RmtInf', type=RemittanceInformation22, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmPrty', type=Priority3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmTmIndctn', type=SettlementDateTimeIndication1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UltmtCdtr', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UltmtDbtr', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgRate', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
	))

