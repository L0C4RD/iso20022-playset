from . import base_types
from ._AggregateHoldingBalance3 import AggregateHoldingBalance3
from ._AccountSubLevel13 import AccountSubLevel13
from ._PartyIdentification100 import PartyIdentification100
from ._AggregateHoldingBalance2 import AggregateHoldingBalance2
from ._BeneficialOwner2 import BeneficialOwner2
from ._SupplementaryData1 import SupplementaryData1
from ._SecuritiesAccount19 import SecuritiesAccount19

class AccountSubLevel12(base_types._BaseFieldType):

	__slots__ = ["_AcctSubLvl3Diff", "_AcctOwnr", "_AcctId", "_AcctSubLvl3", "_AcctSvcr", "_BalDtls", "_BnfclOwnr", "_SplmtryData"]
	@property
	def AcctSubLvl3Diff(self):
		return self._AcctSubLvl3Diff

	@AcctSubLvl3Diff.setter
	def AcctSubLvl3Diff(self, value):
		self._AcctSubLvl3Diff = value if type(value) != base_types.auto else self.make_default("AcctSubLvl3Diff")

	@AcctSubLvl3Diff.deleter
	def AcctSubLvl3Diff(self):
		del self._AcctSubLvl3Diff
		self._AcctSubLvl3Diff = None

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
	def AcctSubLvl3(self):
		return self._AcctSubLvl3

	@AcctSubLvl3.setter
	def AcctSubLvl3(self, value):
		self._AcctSubLvl3 = value if type(value) != base_types.auto else self.make_default("AcctSubLvl3")

	@AcctSubLvl3.deleter
	def AcctSubLvl3(self):
		del self._AcctSubLvl3
		self._AcctSubLvl3 = None

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
		base_types.FieldEntry(name='AcctSubLvl3Diff', type=AggregateHoldingBalance2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification100, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctId', type=SecuritiesAccount19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSubLvl3', type=AccountSubLevel13, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctSvcr', type=PartyIdentification100, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalDtls', type=AggregateHoldingBalance3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BnfclOwnr', type=BeneficialOwner2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

