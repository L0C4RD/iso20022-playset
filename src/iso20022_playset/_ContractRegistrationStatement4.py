from . import base_types
from ._SupplementaryData1 import SupplementaryData1
from ._GenericValidationRuleIdentification1 import GenericValidationRuleIdentification1
from ._BranchAndFinancialInstitutionIdentification8 import BranchAndFinancialInstitutionIdentification8
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._TradeParty6 import TradeParty6
from ._SupportingDocument4 import SupportingDocument4
from ._RegisteredContract18 import RegisteredContract18
from ._ReportingPeriod4 import ReportingPeriod4
from ._Max35Text import Max35Text
from ._TransactionCertificate4 import TransactionCertificate4

class ContractRegistrationStatement4(base_types._BaseFieldType):

	__slots__ = ["_AddtlSpprtgDocJrnl", "_RegnAgt", "_SpprtgDocJrnl", "_RgltryRuleVldtn", "_RptgPty", "_StmtId", "_RptgPrd", "_TxJrnl", "_SplmtryData", "_TtlCtrctTrnvrSum", "_RegdCtrct"]
	@property
	def AddtlSpprtgDocJrnl(self):
		return self._AddtlSpprtgDocJrnl

	@AddtlSpprtgDocJrnl.setter
	def AddtlSpprtgDocJrnl(self, value):
		self._AddtlSpprtgDocJrnl = value if type(value) != base_types.auto else self.make_default("AddtlSpprtgDocJrnl")

	@AddtlSpprtgDocJrnl.deleter
	def AddtlSpprtgDocJrnl(self):
		del self._AddtlSpprtgDocJrnl
		self._AddtlSpprtgDocJrnl = None

	@property
	def RegdCtrct(self):
		return self._RegdCtrct

	@RegdCtrct.setter
	def RegdCtrct(self, value):
		self._RegdCtrct = value if type(value) != base_types.auto else self.make_default("RegdCtrct")

	@RegdCtrct.deleter
	def RegdCtrct(self):
		del self._RegdCtrct
		self._RegdCtrct = None

	@property
	def RegnAgt(self):
		return self._RegnAgt

	@RegnAgt.setter
	def RegnAgt(self, value):
		self._RegnAgt = value if type(value) != base_types.auto else self.make_default("RegnAgt")

	@RegnAgt.deleter
	def RegnAgt(self):
		del self._RegnAgt
		self._RegnAgt = None

	@property
	def RgltryRuleVldtn(self):
		return self._RgltryRuleVldtn

	@RgltryRuleVldtn.setter
	def RgltryRuleVldtn(self, value):
		self._RgltryRuleVldtn = value if type(value) != base_types.auto else self.make_default("RgltryRuleVldtn")

	@RgltryRuleVldtn.deleter
	def RgltryRuleVldtn(self):
		del self._RgltryRuleVldtn
		self._RgltryRuleVldtn = None

	@property
	def RptgPrd(self):
		return self._RptgPrd

	@RptgPrd.setter
	def RptgPrd(self, value):
		self._RptgPrd = value if type(value) != base_types.auto else self.make_default("RptgPrd")

	@RptgPrd.deleter
	def RptgPrd(self):
		del self._RptgPrd
		self._RptgPrd = None

	@property
	def RptgPty(self):
		return self._RptgPty

	@RptgPty.setter
	def RptgPty(self, value):
		self._RptgPty = value if type(value) != base_types.auto else self.make_default("RptgPty")

	@RptgPty.deleter
	def RptgPty(self):
		del self._RptgPty
		self._RptgPty = None

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
	def SpprtgDocJrnl(self):
		return self._SpprtgDocJrnl

	@SpprtgDocJrnl.setter
	def SpprtgDocJrnl(self, value):
		self._SpprtgDocJrnl = value if type(value) != base_types.auto else self.make_default("SpprtgDocJrnl")

	@SpprtgDocJrnl.deleter
	def SpprtgDocJrnl(self):
		del self._SpprtgDocJrnl
		self._SpprtgDocJrnl = None

	@property
	def StmtId(self):
		return self._StmtId

	@StmtId.setter
	def StmtId(self, value):
		self._StmtId = value if type(value) != base_types.auto else self.make_default("StmtId")

	@StmtId.deleter
	def StmtId(self):
		del self._StmtId
		self._StmtId = None

	@property
	def TtlCtrctTrnvrSum(self):
		return self._TtlCtrctTrnvrSum

	@TtlCtrctTrnvrSum.setter
	def TtlCtrctTrnvrSum(self, value):
		self._TtlCtrctTrnvrSum = value if type(value) != base_types.auto else self.make_default("TtlCtrctTrnvrSum")

	@TtlCtrctTrnvrSum.deleter
	def TtlCtrctTrnvrSum(self):
		del self._TtlCtrctTrnvrSum
		self._TtlCtrctTrnvrSum = None

	@property
	def TxJrnl(self):
		return self._TxJrnl

	@TxJrnl.setter
	def TxJrnl(self, value):
		self._TxJrnl = value if type(value) != base_types.auto else self.make_default("TxJrnl")

	@TxJrnl.deleter
	def TxJrnl(self):
		del self._TxJrnl
		self._TxJrnl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlSpprtgDocJrnl', type=SupportingDocument4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RegdCtrct', type=RegisteredContract18, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnAgt', type=BranchAndFinancialInstitutionIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RgltryRuleVldtn', type=GenericValidationRuleIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RptgPrd', type=ReportingPeriod4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgPty', type=TradeParty6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SpprtgDocJrnl', type=SupportingDocument4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StmtId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlCtrctTrnvrSum', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxJrnl', type=TransactionCertificate4, min=0, max=None, mutex_group=None, array=True),
	))

