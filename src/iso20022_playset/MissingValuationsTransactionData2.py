from . import base_types
from .AmountAndDirection106 import AmountAndDirection106
from .DateAndDateTime2Choice import DateAndDateTime2Choice
from .TradeTransactionIdentification24 import TradeTransactionIdentification24

class MissingValuationsTransactionData2(base_types._BaseFieldType):

	__slots__ = ["_ValtnTmStmp", "_TxId", "_ValtnAmt"]
	@property
	def ValtnTmStmp(self):
		return self._ValtnTmStmp

	@ValtnTmStmp.setter
	def ValtnTmStmp(self, value):
		self._ValtnTmStmp = value if type(value) != base_types.auto else self.make_default("ValtnTmStmp")

	@ValtnTmStmp.deleter
	def ValtnTmStmp(self):
		del self._ValtnTmStmp
		self._ValtnTmStmp = None

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

	@property
	def ValtnAmt(self):
		return self._ValtnAmt

	@ValtnAmt.setter
	def ValtnAmt(self, value):
		self._ValtnAmt = value if type(value) != base_types.auto else self.make_default("ValtnAmt")

	@ValtnAmt.deleter
	def ValtnAmt(self):
		del self._ValtnAmt
		self._ValtnAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ValtnTmStmp', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TradeTransactionIdentification24, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnAmt', type=AmountAndDirection106, min=0, max=1, mutex_group=None, array=False),
	))

