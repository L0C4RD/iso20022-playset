from . import base_types
from .AggregateHoldingBalance3 import AggregateHoldingBalance3
from .PartyIdentification100 import PartyIdentification100
from .AccountSubLevel15 import AccountSubLevel15
from .AggregateHoldingBalance2 import AggregateHoldingBalance2
from .SupplementaryData1 import SupplementaryData1
from .SecuritiesAccount19 import SecuritiesAccount19
from .BeneficialOwner2 import BeneficialOwner2

class AccountSubLevel14(base_types._BaseFieldType):

	__slots__ = ["_AcctSvcr", "_BnfclOwnr", "_SplmtryData", "_AcctOwnr", "_BalDtls", "_AcctId", "_AcctSubLvl5", "_AcctSubLvl5Diff"]
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
	def AcctSubLvl5(self):
		return self._AcctSubLvl5

	@AcctSubLvl5.setter
	def AcctSubLvl5(self, value):
		self._AcctSubLvl5 = value if type(value) != base_types.auto else self.make_default("AcctSubLvl5")

	@AcctSubLvl5.deleter
	def AcctSubLvl5(self):
		del self._AcctSubLvl5
		self._AcctSubLvl5 = None

	@property
	def AcctSubLvl5Diff(self):
		return self._AcctSubLvl5Diff

	@AcctSubLvl5Diff.setter
	def AcctSubLvl5Diff(self, value):
		self._AcctSubLvl5Diff = value if type(value) != base_types.auto else self.make_default("AcctSubLvl5Diff")

	@AcctSubLvl5Diff.deleter
	def AcctSubLvl5Diff(self):
		del self._AcctSubLvl5Diff
		self._AcctSubLvl5Diff = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctSvcr', type=PartyIdentification100, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BnfclOwnr', type=BeneficialOwner2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification100, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalDtls', type=AggregateHoldingBalance3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctId', type=SecuritiesAccount19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSubLvl5', type=AccountSubLevel15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctSubLvl5Diff', type=AggregateHoldingBalance2, min=0, max=None, mutex_group=None, array=True),
	))

