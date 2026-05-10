from . import base_types
from .AggregateHoldingBalance3 import AggregateHoldingBalance3
from .PartyIdentification100 import PartyIdentification100
from .AggregateHoldingBalance2 import AggregateHoldingBalance2
from .SupplementaryData1 import SupplementaryData1
from .SecuritiesAccount19 import SecuritiesAccount19
from .AccountSubLevel16 import AccountSubLevel16
from .BeneficialOwner2 import BeneficialOwner2

class AccountSubLevel15(base_types._BaseFieldType):

	__slots__ = ["_AcctSvcr", "_BnfclOwnr", "_SplmtryData", "_AcctOwnr", "_AcctSubLvl6Diff", "_BalDtls", "_AcctSubLvl6", "_AcctId"]
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
	def AcctSubLvl6Diff(self):
		return self._AcctSubLvl6Diff

	@AcctSubLvl6Diff.setter
	def AcctSubLvl6Diff(self, value):
		self._AcctSubLvl6Diff = value if type(value) != base_types.auto else self.make_default("AcctSubLvl6Diff")

	@AcctSubLvl6Diff.deleter
	def AcctSubLvl6Diff(self):
		del self._AcctSubLvl6Diff
		self._AcctSubLvl6Diff = None

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
	def AcctSubLvl6(self):
		return self._AcctSubLvl6

	@AcctSubLvl6.setter
	def AcctSubLvl6(self, value):
		self._AcctSubLvl6 = value if type(value) != base_types.auto else self.make_default("AcctSubLvl6")

	@AcctSubLvl6.deleter
	def AcctSubLvl6(self):
		del self._AcctSubLvl6
		self._AcctSubLvl6 = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctSvcr', type=PartyIdentification100, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BnfclOwnr', type=BeneficialOwner2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification100, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSubLvl6Diff', type=AggregateHoldingBalance2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BalDtls', type=AggregateHoldingBalance3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctSubLvl6', type=AccountSubLevel16, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctId', type=SecuritiesAccount19, min=1, max=1, mutex_group=None, array=False),
	))

