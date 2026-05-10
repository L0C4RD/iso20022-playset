from . import base_types
from .ISODateTime import ISODateTime
from .TradeTransactionIdentification24 import TradeTransactionIdentification24

class MissingMarginTransactionData2(base_types._BaseFieldType):

	__slots__ = ["_CollTmStmp", "_TxId"]
	@property
	def CollTmStmp(self):
		return self._CollTmStmp

	@CollTmStmp.setter
	def CollTmStmp(self, value):
		self._CollTmStmp = value if type(value) != base_types.auto else self.make_default("CollTmStmp")

	@CollTmStmp.deleter
	def CollTmStmp(self):
		del self._CollTmStmp
		self._CollTmStmp = None

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
		base_types.FieldEntry(name='CollTmStmp', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TradeTransactionIdentification24, min=1, max=1, mutex_group=None, array=False),
	))

