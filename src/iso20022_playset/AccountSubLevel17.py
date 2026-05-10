from . import base_types
import AccountSubLevel18
import AggregateHoldingBalance2
import PartyIdentification100
import BeneficialOwner2
import SupplementaryData1
import AggregateHoldingBalance3
import SecuritiesAccount19

class AccountSubLevel17(base_types._BaseFieldType):

	__slots__ = ["_BalDtls", "_SplmtryData", "_AcctSubLvl8", "_BnfclOwnr", "_AcctSvcr", "_AcctSubLvl8Diff", "_AcctOwnr", "_AcctId"]
	@property
	def BalDtls(self):
		return self._BalDtls

	@BalDtls.setter
	def BalDtls(self, value):
		self._BalDtls = value if type(value) != auto else self.make_default("BalDtls")

	@BalDtls.deleter
	def BalDtls(self):
		del self._BalDtls
		self._BalDtls = None

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
	def AcctSubLvl8(self):
		return self._AcctSubLvl8

	@AcctSubLvl8.setter
	def AcctSubLvl8(self, value):
		self._AcctSubLvl8 = value if type(value) != auto else self.make_default("AcctSubLvl8")

	@AcctSubLvl8.deleter
	def AcctSubLvl8(self):
		del self._AcctSubLvl8
		self._AcctSubLvl8 = None

	@property
	def BnfclOwnr(self):
		return self._BnfclOwnr

	@BnfclOwnr.setter
	def BnfclOwnr(self, value):
		self._BnfclOwnr = value if type(value) != auto else self.make_default("BnfclOwnr")

	@BnfclOwnr.deleter
	def BnfclOwnr(self):
		del self._BnfclOwnr
		self._BnfclOwnr = None

	@property
	def AcctSvcr(self):
		return self._AcctSvcr

	@AcctSvcr.setter
	def AcctSvcr(self, value):
		self._AcctSvcr = value if type(value) != auto else self.make_default("AcctSvcr")

	@AcctSvcr.deleter
	def AcctSvcr(self):
		del self._AcctSvcr
		self._AcctSvcr = None

	@property
	def AcctSubLvl8Diff(self):
		return self._AcctSubLvl8Diff

	@AcctSubLvl8Diff.setter
	def AcctSubLvl8Diff(self, value):
		self._AcctSubLvl8Diff = value if type(value) != auto else self.make_default("AcctSubLvl8Diff")

	@AcctSubLvl8Diff.deleter
	def AcctSubLvl8Diff(self):
		del self._AcctSubLvl8Diff
		self._AcctSubLvl8Diff = None

	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if type(value) != auto else self.make_default("AcctOwnr")

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = None

	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if type(value) != auto else self.make_default("AcctId")

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BalDtls', type=AggregateHoldingBalance3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctSubLvl8', type=AccountSubLevel18, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BnfclOwnr', type=BeneficialOwner2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctSvcr', type=PartyIdentification100, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSubLvl8Diff', type=AggregateHoldingBalance2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification100, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctId', type=SecuritiesAccount19, min=1, max=1, mutex_group=None, array=False),
	))

