# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._MatchingCriteria17 import MatchingCriteria17
from ._TradeTransactionIdentification24 import TradeTransactionIdentification24

class ReconciliationReport15(base_types._BaseFieldType):

	__slots__ = ["_MtchgCrit", "_TxId"]
	@property
	def MtchgCrit(self):
		return self._MtchgCrit

	@MtchgCrit.setter
	def MtchgCrit(self, value):
		self._MtchgCrit = value if type(value) != base_types.auto else self.make_default("MtchgCrit")

	@MtchgCrit.deleter
	def MtchgCrit(self):
		del self._MtchgCrit
		self._MtchgCrit = None

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if type(value) != base_types.auto else self.make_default("TxId")

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MtchgCrit', type=MatchingCriteria17, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TradeTransactionIdentification24, min=1, max=1, mutex_group=None, array=False),
	))