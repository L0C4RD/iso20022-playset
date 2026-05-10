from . import base_types
from .CompareUnitPrice6 import CompareUnitPrice6
from .CompareUnitOfMeasure3 import CompareUnitOfMeasure3
from .CompareDecimalNumber3 import CompareDecimalNumber3
from .CompareCommodityAssetClass3 import CompareCommodityAssetClass3
from .CompareAmountAndDirection2 import CompareAmountAndDirection2

class Commodity42(base_types._BaseFieldType):

	__slots__ = ["_MktVal", "_Clssfctn", "_UnitPric", "_UnitOfMeasr", "_Qty"]
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
	def UnitPric(self):
		return self._UnitPric

	@UnitPric.setter
	def UnitPric(self, value):
		self._UnitPric = value if type(value) != base_types.auto else self.make_default("UnitPric")

	@UnitPric.deleter
	def UnitPric(self):
		del self._UnitPric
		self._UnitPric = None

	@property
	def UnitOfMeasr(self):
		return self._UnitOfMeasr

	@UnitOfMeasr.setter
	def UnitOfMeasr(self, value):
		self._UnitOfMeasr = value if type(value) != base_types.auto else self.make_default("UnitOfMeasr")

	@UnitOfMeasr.deleter
	def UnitOfMeasr(self):
		del self._UnitOfMeasr
		self._UnitOfMeasr = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='MktVal', type=CompareAmountAndDirection2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Clssfctn', type=CompareCommodityAssetClass3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitPric', type=CompareUnitPrice6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitOfMeasr', type=CompareUnitOfMeasure3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=CompareDecimalNumber3, min=0, max=1, mutex_group=None, array=False),
	))

