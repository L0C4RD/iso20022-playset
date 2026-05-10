from . import base_types
import TradeParty6
import DocumentIdentification29
import ContractBalance1
import SupplementaryData1
import Max35Text
import UnderlyingContract4Choice
import BranchAndFinancialInstitutionIdentification8
import ActiveCurrencyAndAmount
import Max1025Text
import RegisteredContractCommunication1
import TrueFalseIndicator
import RegisteredContractJournal3
import DocumentIdentification22
import PaymentScheduleType2Choice
import RegisteredContractAmendment1

class RegisteredContract20(base_types._BaseFieldType):

	__slots__ = ["_RegdCtrctId", "_EstmtdDtInd", "_IntrCpnyLn", "_Amdmnt", "_OrgnlCtrctRegnReq", "_RptgPty", "_CtrctBal", "_SplmtryData", "_PrvsRegdCtrctId", "_Ctrct", "_RegdCtrctJrnl", "_Submissn", "_IssrFI", "_LnPrncplAmt", "_AddtlInf", "_RegnAgt", "_Dlvry", "_PmtSchdlTp"]
	@property
	def RegdCtrctId(self):
		return self._RegdCtrctId

	@RegdCtrctId.setter
	def RegdCtrctId(self, value):
		self._RegdCtrctId = value if type(value) != auto else self.make_default("RegdCtrctId")

	@RegdCtrctId.deleter
	def RegdCtrctId(self):
		del self._RegdCtrctId
		self._RegdCtrctId = None

	@property
	def EstmtdDtInd(self):
		return self._EstmtdDtInd

	@EstmtdDtInd.setter
	def EstmtdDtInd(self, value):
		self._EstmtdDtInd = value if type(value) != auto else self.make_default("EstmtdDtInd")

	@EstmtdDtInd.deleter
	def EstmtdDtInd(self):
		del self._EstmtdDtInd
		self._EstmtdDtInd = None

	@property
	def IntrCpnyLn(self):
		return self._IntrCpnyLn

	@IntrCpnyLn.setter
	def IntrCpnyLn(self, value):
		self._IntrCpnyLn = value if type(value) != auto else self.make_default("IntrCpnyLn")

	@IntrCpnyLn.deleter
	def IntrCpnyLn(self):
		del self._IntrCpnyLn
		self._IntrCpnyLn = None

	@property
	def Amdmnt(self):
		return self._Amdmnt

	@Amdmnt.setter
	def Amdmnt(self, value):
		self._Amdmnt = value if type(value) != auto else self.make_default("Amdmnt")

	@Amdmnt.deleter
	def Amdmnt(self):
		del self._Amdmnt
		self._Amdmnt = None

	@property
	def OrgnlCtrctRegnReq(self):
		return self._OrgnlCtrctRegnReq

	@OrgnlCtrctRegnReq.setter
	def OrgnlCtrctRegnReq(self, value):
		self._OrgnlCtrctRegnReq = value if type(value) != auto else self.make_default("OrgnlCtrctRegnReq")

	@OrgnlCtrctRegnReq.deleter
	def OrgnlCtrctRegnReq(self):
		del self._OrgnlCtrctRegnReq
		self._OrgnlCtrctRegnReq = None

	@property
	def RptgPty(self):
		return self._RptgPty

	@RptgPty.setter
	def RptgPty(self, value):
		self._RptgPty = value if type(value) != auto else self.make_default("RptgPty")

	@RptgPty.deleter
	def RptgPty(self):
		del self._RptgPty
		self._RptgPty = None

	@property
	def CtrctBal(self):
		return self._CtrctBal

	@CtrctBal.setter
	def CtrctBal(self, value):
		self._CtrctBal = value if type(value) != auto else self.make_default("CtrctBal")

	@CtrctBal.deleter
	def CtrctBal(self):
		del self._CtrctBal
		self._CtrctBal = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def PrvsRegdCtrctId(self):
		return self._PrvsRegdCtrctId

	@PrvsRegdCtrctId.setter
	def PrvsRegdCtrctId(self, value):
		self._PrvsRegdCtrctId = value if type(value) != auto else self.make_default("PrvsRegdCtrctId")

	@PrvsRegdCtrctId.deleter
	def PrvsRegdCtrctId(self):
		del self._PrvsRegdCtrctId
		self._PrvsRegdCtrctId = None

	@property
	def Ctrct(self):
		return self._Ctrct

	@Ctrct.setter
	def Ctrct(self, value):
		self._Ctrct = value if type(value) != auto else self.make_default("Ctrct")

	@Ctrct.deleter
	def Ctrct(self):
		del self._Ctrct
		self._Ctrct = None

	@property
	def RegdCtrctJrnl(self):
		return self._RegdCtrctJrnl

	@RegdCtrctJrnl.setter
	def RegdCtrctJrnl(self, value):
		self._RegdCtrctJrnl = value if type(value) != auto else self.make_default("RegdCtrctJrnl")

	@RegdCtrctJrnl.deleter
	def RegdCtrctJrnl(self):
		del self._RegdCtrctJrnl
		self._RegdCtrctJrnl = None

	@property
	def Submissn(self):
		return self._Submissn

	@Submissn.setter
	def Submissn(self, value):
		self._Submissn = value if type(value) != auto else self.make_default("Submissn")

	@Submissn.deleter
	def Submissn(self):
		del self._Submissn
		self._Submissn = None

	@property
	def IssrFI(self):
		return self._IssrFI

	@IssrFI.setter
	def IssrFI(self, value):
		self._IssrFI = value if type(value) != auto else self.make_default("IssrFI")

	@IssrFI.deleter
	def IssrFI(self):
		del self._IssrFI
		self._IssrFI = None

	@property
	def LnPrncplAmt(self):
		return self._LnPrncplAmt

	@LnPrncplAmt.setter
	def LnPrncplAmt(self, value):
		self._LnPrncplAmt = value if type(value) != auto else self.make_default("LnPrncplAmt")

	@LnPrncplAmt.deleter
	def LnPrncplAmt(self):
		del self._LnPrncplAmt
		self._LnPrncplAmt = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def RegnAgt(self):
		return self._RegnAgt

	@RegnAgt.setter
	def RegnAgt(self, value):
		self._RegnAgt = value if type(value) != auto else self.make_default("RegnAgt")

	@RegnAgt.deleter
	def RegnAgt(self):
		del self._RegnAgt
		self._RegnAgt = None

	@property
	def Dlvry(self):
		return self._Dlvry

	@Dlvry.setter
	def Dlvry(self, value):
		self._Dlvry = value if type(value) != auto else self.make_default("Dlvry")

	@Dlvry.deleter
	def Dlvry(self):
		del self._Dlvry
		self._Dlvry = None

	@property
	def PmtSchdlTp(self):
		return self._PmtSchdlTp

	@PmtSchdlTp.setter
	def PmtSchdlTp(self, value):
		self._PmtSchdlTp = value if type(value) != auto else self.make_default("PmtSchdlTp")

	@PmtSchdlTp.deleter
	def PmtSchdlTp(self):
		del self._PmtSchdlTp
		self._PmtSchdlTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RegdCtrctId', type=DocumentIdentification29, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EstmtdDtInd', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrCpnyLn', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amdmnt', type=RegisteredContractAmendment1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlCtrctRegnReq', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgPty', type=TradeParty6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctBal', type=ContractBalance1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrvsRegdCtrctId', type=DocumentIdentification22, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctrct', type=UnderlyingContract4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegdCtrctJrnl', type=RegisteredContractJournal3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Submissn', type=RegisteredContractCommunication1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrFI', type=BranchAndFinancialInstitutionIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LnPrncplAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=Max1025Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnAgt', type=BranchAndFinancialInstitutionIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dlvry', type=RegisteredContractCommunication1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtSchdlTp', type=PaymentScheduleType2Choice, min=0, max=1, mutex_group=None, array=False),
	))

