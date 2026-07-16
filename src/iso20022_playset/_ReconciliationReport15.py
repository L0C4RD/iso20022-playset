# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MatchingCriteria17
from . import TradeTransactionIdentification24

class ReconciliationReport15(base_types._BaseFieldType):

	__slots__ = ["_MtchgCrit", "_TxId"]
	@property
	def MtchgCrit(self):
		return self._MtchgCrit

	@MtchgCrit.setter
	def MtchgCrit(self, value):
		self._MtchgCrit = value if value is not None else base_types.UninitialisedField(self, 'MtchgCrit', MatchingCriteria17, False)

	@MtchgCrit.deleter
	def MtchgCrit(self):
		del self._MtchgCrit
		self._MtchgCrit = base_types.UninitialisedField(self, 'MtchgCrit', MatchingCriteria17, False)

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if value is not None else base_types.UninitialisedField(self, 'TxId', TradeTransactionIdentification24, False)

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = base_types.UninitialisedField(self, 'TxId', TradeTransactionIdentification24, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MtchgCrit', type=MatchingCriteria17, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TradeTransactionIdentification24, min=1, max=1, mutex_group=None, array=False),
	))