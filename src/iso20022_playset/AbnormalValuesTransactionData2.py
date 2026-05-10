from . import base_types
from .TradeTransactionIdentification24 import TradeTransactionIdentification24
from .NotionalAmountLegs5 import NotionalAmountLegs5
from .NotionalQuantityLegs5 import NotionalQuantityLegs5

class AbnormalValuesTransactionData2(base_types._BaseFieldType):

	__slots__ = ["_NtnlAmt", "_TxId", "_NtnlQty"]
	@property
	def NtnlAmt(self):
		return self._NtnlAmt

	@NtnlAmt.setter
	def NtnlAmt(self, value):
		self._NtnlAmt = value if type(value) != base_types.auto else self.make_default("NtnlAmt")

	@NtnlAmt.deleter
	def NtnlAmt(self):
		del self._NtnlAmt
		self._NtnlAmt = None

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
	def NtnlQty(self):
		return self._NtnlQty

	@NtnlQty.setter
	def NtnlQty(self, value):
		self._NtnlQty = value if type(value) != base_types.auto else self.make_default("NtnlQty")

	@NtnlQty.deleter
	def NtnlQty(self):
		del self._NtnlQty
		self._NtnlQty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NtnlAmt', type=NotionalAmountLegs5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TradeTransactionIdentification24, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtnlQty', type=NotionalQuantityLegs5, min=0, max=1, mutex_group=None, array=False),
	))

