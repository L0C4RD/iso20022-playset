from . import base_types
from ._AggregateBalanceInformation47 import AggregateBalanceInformation47
from ._SecuritiesAccount19 import SecuritiesAccount19
from ._SubAccountIdentification75 import SubAccountIdentification75
from ._TotalValueInPageAndStatement1 import TotalValueInPageAndStatement1

class Balance30(base_types._BaseFieldType):

	__slots__ = ["_AcctBaseCcyTtlAmts", "_BalForAcct", "_SfkpgAcct", "_SubAcctDtls"]
	@property
	def AcctBaseCcyTtlAmts(self):
		return self._AcctBaseCcyTtlAmts

	@AcctBaseCcyTtlAmts.setter
	def AcctBaseCcyTtlAmts(self, value):
		self._AcctBaseCcyTtlAmts = value if type(value) != base_types.auto else self.make_default("AcctBaseCcyTtlAmts")

	@AcctBaseCcyTtlAmts.deleter
	def AcctBaseCcyTtlAmts(self):
		del self._AcctBaseCcyTtlAmts
		self._AcctBaseCcyTtlAmts = None

	@property
	def BalForAcct(self):
		return self._BalForAcct

	@BalForAcct.setter
	def BalForAcct(self, value):
		self._BalForAcct = value if type(value) != base_types.auto else self.make_default("BalForAcct")

	@BalForAcct.deleter
	def BalForAcct(self):
		del self._BalForAcct
		self._BalForAcct = None

	@property
	def SfkpgAcct(self):
		return self._SfkpgAcct

	@SfkpgAcct.setter
	def SfkpgAcct(self, value):
		self._SfkpgAcct = value if type(value) != base_types.auto else self.make_default("SfkpgAcct")

	@SfkpgAcct.deleter
	def SfkpgAcct(self):
		del self._SfkpgAcct
		self._SfkpgAcct = None

	@property
	def SubAcctDtls(self):
		return self._SubAcctDtls

	@SubAcctDtls.setter
	def SubAcctDtls(self, value):
		self._SubAcctDtls = value if type(value) != base_types.auto else self.make_default("SubAcctDtls")

	@SubAcctDtls.deleter
	def SubAcctDtls(self):
		del self._SubAcctDtls
		self._SubAcctDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctBaseCcyTtlAmts', type=TotalValueInPageAndStatement1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalForAcct', type=AggregateBalanceInformation47, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubAcctDtls', type=SubAccountIdentification75, min=0, max=None, mutex_group=None, array=True),
	))

