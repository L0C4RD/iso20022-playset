# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection106
from . import DateAndDateTime2Choice
from . import TradeTransactionIdentification24

class MissingValuationsTransactionData2(base_types._BaseFieldType):

	__slots__ = ["_TxId", "_ValtnAmt", "_ValtnTmStmp"]
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

	@property
	def ValtnAmt(self):
		return self._ValtnAmt

	@ValtnAmt.setter
	def ValtnAmt(self, value):
		self._ValtnAmt = value if value is not None else base_types.UninitialisedField(self, 'ValtnAmt', AmountAndDirection106, False)

	@ValtnAmt.deleter
	def ValtnAmt(self):
		del self._ValtnAmt
		self._ValtnAmt = base_types.UninitialisedField(self, 'ValtnAmt', AmountAndDirection106, False)

	@property
	def ValtnTmStmp(self):
		return self._ValtnTmStmp

	@ValtnTmStmp.setter
	def ValtnTmStmp(self, value):
		self._ValtnTmStmp = value if value is not None else base_types.UninitialisedField(self, 'ValtnTmStmp', DateAndDateTime2Choice, False)

	@ValtnTmStmp.deleter
	def ValtnTmStmp(self):
		del self._ValtnTmStmp
		self._ValtnTmStmp = base_types.UninitialisedField(self, 'ValtnTmStmp', DateAndDateTime2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='TxId', type=TradeTransactionIdentification24, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnAmt', type=AmountAndDirection106, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnTmStmp', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
	))