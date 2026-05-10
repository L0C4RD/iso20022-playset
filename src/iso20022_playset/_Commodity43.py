from . import base_types
from ._SecuritiesTransactionPrice19Choice import SecuritiesTransactionPrice19Choice
from ._Quantity17 import Quantity17
from ._AmountAndDirection53 import AmountAndDirection53
from ._AssetClassCommodity5Choice import AssetClassCommodity5Choice

class Commodity43(base_types._BaseFieldType):

	__slots__ = ["_MktVal", "_Qty", "_UnitPric", "_Clssfctn"]
	@property
	def Clssfctn(self):
		return self._Clssfctn

	@Clssfctn.setter
	def Clssfctn(self, value):
		self._Clssfctn = value if type(value) != base_types.auto else self.make_default("Clssfctn")

	@Clssfctn.deleter
	def Clssfctn(self):
		del self._Clssfctn
		self._Clssfctn = None

	@property
	def MktVal(self):
		return self._MktVal

	@MktVal.setter
	def MktVal(self, value):
		self._MktVal = value if type(value) != base_types.auto else self.make_default("MktVal")

	@MktVal.deleter
	def MktVal(self):
		del self._MktVal
		self._MktVal = None

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if type(value) != base_types.auto else self.make_default("Qty")

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = None

	@property
	def UnitPric(self):
		return self._UnitPric

	@UnitPric.setter
	def UnitPric(self, value):
		self._UnitPric = value if type(value) != base_types.auto else self.make_default("UnitPric")

	@UnitPric.deleter
	def UnitPric(self):
		del self._UnitPric
		self._UnitPric = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Clssfctn', type=AssetClassCommodity5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktVal', type=AmountAndDirection53, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=Quantity17, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitPric', type=SecuritiesTransactionPrice19Choice, min=0, max=1, mutex_group=None, array=False),
	))

