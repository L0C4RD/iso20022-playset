from . import base_types
from ._AggregateHoldingBalance3 import AggregateHoldingBalance3
from ._AccountSubLevel19 import AccountSubLevel19
from ._PartyIdentification100 import PartyIdentification100
from ._AggregateHoldingBalance2 import AggregateHoldingBalance2
from ._BeneficialOwner2 import BeneficialOwner2
from ._SupplementaryData1 import SupplementaryData1
from ._SecuritiesAccount19 import SecuritiesAccount19

class AccountSubLevel18(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnr", "_AcctSubLvl9Diff", "_AcctId", "_AcctSvcr", "_BalDtls", "_BnfclOwnr", "_AcctSubLvl9", "_SplmtryData"]
	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if type(value) != base_types.auto else self.make_default("AcctOwnr")

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = None

	@property
	def AcctSubLvl9Diff(self):
		return self._AcctSubLvl9Diff

	@AcctSubLvl9Diff.setter
	def AcctSubLvl9Diff(self, value):
		self._AcctSubLvl9Diff = value if type(value) != base_types.auto else self.make_default("AcctSubLvl9Diff")

	@AcctSubLvl9Diff.deleter
	def AcctSubLvl9Diff(self):
		del self._AcctSubLvl9Diff
		self._AcctSubLvl9Diff = None

	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if type(value) != base_types.auto else self.make_default("AcctId")

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = None

	@property
	def AcctSvcr(self):
		return self._AcctSvcr

	@AcctSvcr.setter
	def AcctSvcr(self, value):
		self._AcctSvcr = value if type(value) != base_types.auto else self.make_default("AcctSvcr")

	@AcctSvcr.deleter
	def AcctSvcr(self):
		del self._AcctSvcr
		self._AcctSvcr = None

	@property
	def BalDtls(self):
		return self._BalDtls

	@BalDtls.setter
	def BalDtls(self, value):
		self._BalDtls = value if type(value) != base_types.auto else self.make_default("BalDtls")

	@BalDtls.deleter
	def BalDtls(self):
		del self._BalDtls
		self._BalDtls = None

	@property
	def BnfclOwnr(self):
		return self._BnfclOwnr

	@BnfclOwnr.setter
	def BnfclOwnr(self, value):
		self._BnfclOwnr = value if type(value) != base_types.auto else self.make_default("BnfclOwnr")

	@BnfclOwnr.deleter
	def BnfclOwnr(self):
		del self._BnfclOwnr
		self._BnfclOwnr = None

	@property
	def AcctSubLvl9(self):
		return self._AcctSubLvl9

	@AcctSubLvl9.setter
	def AcctSubLvl9(self, value):
		self._AcctSubLvl9 = value if type(value) != base_types.auto else self.make_default("AcctSubLvl9")

	@AcctSubLvl9.deleter
	def AcctSubLvl9(self):
		del self._AcctSubLvl9
		self._AcctSubLvl9 = None

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
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification100, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSubLvl9Diff', type=AggregateHoldingBalance2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctId', type=SecuritiesAccount19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcr', type=PartyIdentification100, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalDtls', type=AggregateHoldingBalance3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BnfclOwnr', type=BeneficialOwner2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctSubLvl9', type=AccountSubLevel19, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

