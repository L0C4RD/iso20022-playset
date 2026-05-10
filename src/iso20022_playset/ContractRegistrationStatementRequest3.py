import base_types
import Max35Text
import TradeParty6
import SupplementaryData1
import ReportingPeriod4
import ContractRegistrationStatementCriteria1
import BranchAndFinancialInstitutionIdentification8

class ContractRegistrationStatementRequest3(base_types._BaseFieldType):

	__slots__ = ["_RptgPrd", "_StmtReqId", "_RegnAgt", "_RtrCrit", "_SplmtryData", "_RegdCtrctId", "_RptgPty"]
	@property
	def RptgPrd(self):
		return self._RptgPrd

	@RptgPrd.setter
	def RptgPrd(self, value):
		self._RptgPrd = value if type(value) != auto else self.make_default("RptgPrd")

	@RptgPrd.deleter
	def RptgPrd(self):
		del self._RptgPrd
		self._RptgPrd = None

	@property
	def StmtReqId(self):
		return self._StmtReqId

	@StmtReqId.setter
	def StmtReqId(self, value):
		self._StmtReqId = value if type(value) != auto else self.make_default("StmtReqId")

	@StmtReqId.deleter
	def StmtReqId(self):
		del self._StmtReqId
		self._StmtReqId = None

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
	def RtrCrit(self):
		return self._RtrCrit

	@RtrCrit.setter
	def RtrCrit(self, value):
		self._RtrCrit = value if type(value) != auto else self.make_default("RtrCrit")

	@RtrCrit.deleter
	def RtrCrit(self):
		del self._RtrCrit
		self._RtrCrit = None

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
	def RptgPty(self):
		return self._RptgPty

	@RptgPty.setter
	def RptgPty(self, value):
		self._RptgPty = value if type(value) != auto else self.make_default("RptgPty")

	@RptgPty.deleter
	def RptgPty(self):
		del self._RptgPty
		self._RptgPty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RptgPrd', type=ReportingPeriod4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtReqId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnAgt', type=BranchAndFinancialInstitutionIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrCrit', type=ContractRegistrationStatementCriteria1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RegdCtrctId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgPty', type=TradeParty6, min=1, max=1, mutex_group=None, array=False),
	))

