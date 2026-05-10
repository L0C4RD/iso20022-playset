import base_types
import AggregateHoldingBalance2
import SecuritiesAccount19
import AccountSubLevel17
import AggregateHoldingBalance3
import PartyIdentification100
import SupplementaryData1
import BeneficialOwner2

class AccountSubLevel16(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_BalDtls", "_AcctSubLvl7Diff", "_AcctId", "_BnfclOwnr", "_AcctOwnr", "_AcctSvcr", "_AcctSubLvl7"]
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
	def AcctSubLvl7Diff(self):
		return self._AcctSubLvl7Diff

	@AcctSubLvl7Diff.setter
	def AcctSubLvl7Diff(self, value):
		self._AcctSubLvl7Diff = value if type(value) != auto else self.make_default("AcctSubLvl7Diff")

	@AcctSubLvl7Diff.deleter
	def AcctSubLvl7Diff(self):
		del self._AcctSubLvl7Diff
		self._AcctSubLvl7Diff = None

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
	def AcctSubLvl7(self):
		return self._AcctSubLvl7

	@AcctSubLvl7.setter
	def AcctSubLvl7(self, value):
		self._AcctSubLvl7 = value if type(value) != auto else self.make_default("AcctSubLvl7")

	@AcctSubLvl7.deleter
	def AcctSubLvl7(self):
		del self._AcctSubLvl7
		self._AcctSubLvl7 = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BalDtls', type=AggregateHoldingBalance3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctSubLvl7Diff', type=AggregateHoldingBalance2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctId', type=SecuritiesAccount19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BnfclOwnr', type=BeneficialOwner2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification100, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcr', type=PartyIdentification100, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSubLvl7', type=AccountSubLevel17, min=0, max=None, mutex_group=None, array=True),
	))

