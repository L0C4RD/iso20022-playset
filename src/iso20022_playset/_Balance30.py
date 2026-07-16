# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AggregateBalanceInformation47
from . import SecuritiesAccount19
from . import SubAccountIdentification75
from . import TotalValueInPageAndStatement1

class Balance30(base_types._BaseFieldType):

	__slots__ = ["_AcctBaseCcyTtlAmts", "_BalForAcct", "_SfkpgAcct", "_SubAcctDtls"]
	@property
	def AcctBaseCcyTtlAmts(self):
		return self._AcctBaseCcyTtlAmts

	@AcctBaseCcyTtlAmts.setter
	def AcctBaseCcyTtlAmts(self, value):
		self._AcctBaseCcyTtlAmts = value if value is not None else base_types.UninitialisedField(self, 'AcctBaseCcyTtlAmts', TotalValueInPageAndStatement1, False)

	@AcctBaseCcyTtlAmts.deleter
	def AcctBaseCcyTtlAmts(self):
		del self._AcctBaseCcyTtlAmts
		self._AcctBaseCcyTtlAmts = base_types.UninitialisedField(self, 'AcctBaseCcyTtlAmts', TotalValueInPageAndStatement1, False)

	@property
	def BalForAcct(self):
		return self._BalForAcct

	@BalForAcct.setter
	def BalForAcct(self, value):
		self._BalForAcct = value if value is not None else base_types.UninitialisedField(self, 'BalForAcct', AggregateBalanceInformation47, True)

	@BalForAcct.deleter
	def BalForAcct(self):
		del self._BalForAcct
		self._BalForAcct = base_types.UninitialisedField(self, 'BalForAcct', AggregateBalanceInformation47, True)

	@property
	def SfkpgAcct(self):
		return self._SfkpgAcct

	@SfkpgAcct.setter
	def SfkpgAcct(self, value):
		self._SfkpgAcct = value if value is not None else base_types.UninitialisedField(self, 'SfkpgAcct', SecuritiesAccount19, False)

	@SfkpgAcct.deleter
	def SfkpgAcct(self):
		del self._SfkpgAcct
		self._SfkpgAcct = base_types.UninitialisedField(self, 'SfkpgAcct', SecuritiesAccount19, False)

	@property
	def SubAcctDtls(self):
		return self._SubAcctDtls

	@SubAcctDtls.setter
	def SubAcctDtls(self, value):
		self._SubAcctDtls = value if value is not None else base_types.UninitialisedField(self, 'SubAcctDtls', SubAccountIdentification75, True)

	@SubAcctDtls.deleter
	def SubAcctDtls(self):
		del self._SubAcctDtls
		self._SubAcctDtls = base_types.UninitialisedField(self, 'SubAcctDtls', SubAccountIdentification75, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctBaseCcyTtlAmts', type=TotalValueInPageAndStatement1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalForAcct', type=AggregateBalanceInformation47, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubAcctDtls', type=SubAccountIdentification75, min=0, max=None, mutex_group=None, array=True),
	))