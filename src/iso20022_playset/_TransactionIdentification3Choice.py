from . import base_types
from ._TradeTransactionIdentification20 import TradeTransactionIdentification20
from ._TradeTransactionIdentification16 import TradeTransactionIdentification16
from ._TradeTransactionIdentification17 import TradeTransactionIdentification17

class TransactionIdentification3Choice(base_types._BaseFieldType):

	__slots__ = ["_MrgnRptg", "_Tx", "_CollReuse"]
	@property
	def CollReuse(self):
		return self._CollReuse

	@CollReuse.setter
	def CollReuse(self, value):
		self._CollReuse = value if type(value) != base_types.auto else self.make_default("CollReuse")

	@CollReuse.deleter
	def CollReuse(self):
		del self._CollReuse
		self._CollReuse = None

	@property
	def MrgnRptg(self):
		return self._MrgnRptg

	@MrgnRptg.setter
	def MrgnRptg(self, value):
		self._MrgnRptg = value if type(value) != base_types.auto else self.make_default("MrgnRptg")

	@MrgnRptg.deleter
	def MrgnRptg(self):
		del self._MrgnRptg
		self._MrgnRptg = None

	@property
	def Tx(self):
		return self._Tx

	@Tx.setter
	def Tx(self, value):
		self._Tx = value if type(value) != base_types.auto else self.make_default("Tx")

	@Tx.deleter
	def Tx(self):
		del self._Tx
		self._Tx = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollReuse', type=TradeTransactionIdentification17, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MrgnRptg', type=TradeTransactionIdentification16, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Tx', type=TradeTransactionIdentification20, min=0, max=1, mutex_group=1, array=False),
	))

