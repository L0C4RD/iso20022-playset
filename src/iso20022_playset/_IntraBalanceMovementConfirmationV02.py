from . import base_types
from .SupplementaryData1 import SupplementaryData1
from .AdditionalParameters16 import AdditionalParameters16
from .BranchAndFinancialInstitutionIdentification8 import BranchAndFinancialInstitutionIdentification8
from .CashAccount40 import CashAccount40
from .DocumentIdentification51 import DocumentIdentification51
from .IntraBalance6 import IntraBalance6
from .SystemPartyIdentification8 import SystemPartyIdentification8

class IntraBalanceMovementConfirmationV02(base_types._BaseFieldType):

	__slots__ = ["_AddtlParams", "_CshAcctSvcr", "_CshAcct", "_CshAcctOwnr", "_SplmtryData", "_IntraBal", "_Id"]
	@property
	def AddtlParams(self):
		return self._AddtlParams

	@AddtlParams.setter
	def AddtlParams(self, value):
		self._AddtlParams = value if type(value) != base_types.auto else self.make_default("AddtlParams")

	@AddtlParams.deleter
	def AddtlParams(self):
		del self._AddtlParams
		self._AddtlParams = None

	@property
	def CshAcctSvcr(self):
		return self._CshAcctSvcr

	@CshAcctSvcr.setter
	def CshAcctSvcr(self, value):
		self._CshAcctSvcr = value if type(value) != base_types.auto else self.make_default("CshAcctSvcr")

	@CshAcctSvcr.deleter
	def CshAcctSvcr(self):
		del self._CshAcctSvcr
		self._CshAcctSvcr = None

	@property
	def CshAcct(self):
		return self._CshAcct

	@CshAcct.setter
	def CshAcct(self, value):
		self._CshAcct = value if type(value) != base_types.auto else self.make_default("CshAcct")

	@CshAcct.deleter
	def CshAcct(self):
		del self._CshAcct
		self._CshAcct = None

	@property
	def CshAcctOwnr(self):
		return self._CshAcctOwnr

	@CshAcctOwnr.setter
	def CshAcctOwnr(self, value):
		self._CshAcctOwnr = value if type(value) != base_types.auto else self.make_default("CshAcctOwnr")

	@CshAcctOwnr.deleter
	def CshAcctOwnr(self):
		del self._CshAcctOwnr
		self._CshAcctOwnr = None

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
	def IntraBal(self):
		return self._IntraBal

	@IntraBal.setter
	def IntraBal(self, value):
		self._IntraBal = value if type(value) != base_types.auto else self.make_default("IntraBal")

	@IntraBal.deleter
	def IntraBal(self):
		del self._IntraBal
		self._IntraBal = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlParams', type=AdditionalParameters16, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcctSvcr', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcct', type=CashAccount40, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcctOwnr', type=SystemPartyIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IntraBal', type=IntraBalance6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=DocumentIdentification51, min=0, max=1, mutex_group=None, array=False),
	))

