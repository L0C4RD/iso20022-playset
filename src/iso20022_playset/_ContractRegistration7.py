from . import base_types
from ._BranchAndFinancialInstitutionIdentification8 import BranchAndFinancialInstitutionIdentification8
from ._ContractRegistration8 import ContractRegistration8
from ._Max35Text import Max35Text
from ._SupplementaryData1 import SupplementaryData1
from ._TradeParty6 import TradeParty6

class ContractRegistration7(base_types._BaseFieldType):

	__slots__ = ["_CtrctRegnId", "_CtrctRegnOpng", "_RegnAgt", "_RptgPty", "_SplmtryData"]
	@property
	def CtrctRegnId(self):
		return self._CtrctRegnId

	@CtrctRegnId.setter
	def CtrctRegnId(self, value):
		self._CtrctRegnId = value if type(value) != base_types.auto else self.make_default("CtrctRegnId")

	@CtrctRegnId.deleter
	def CtrctRegnId(self):
		del self._CtrctRegnId
		self._CtrctRegnId = None

	@property
	def CtrctRegnOpng(self):
		return self._CtrctRegnOpng

	@CtrctRegnOpng.setter
	def CtrctRegnOpng(self, value):
		self._CtrctRegnOpng = value if type(value) != base_types.auto else self.make_default("CtrctRegnOpng")

	@CtrctRegnOpng.deleter
	def CtrctRegnOpng(self):
		del self._CtrctRegnOpng
		self._CtrctRegnOpng = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtrctRegnId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctRegnOpng', type=ContractRegistration8, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RegnAgt', type=BranchAndFinancialInstitutionIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgPty', type=TradeParty6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

