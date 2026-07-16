# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CompareAmountAndDirection2
from . import CompareCommodityAssetClass3
from . import CompareDecimalNumber3
from . import CompareUnitOfMeasure3
from . import CompareUnitPrice6

class Commodity42(base_types._BaseFieldType):

	__slots__ = ["_Clssfctn", "_MktVal", "_Qty", "_UnitOfMeasr", "_UnitPric"]
	@property
	def Clssfctn(self):
		return self._Clssfctn

	@Clssfctn.setter
	def Clssfctn(self, value):
		self._Clssfctn = value if value is not None else base_types.UninitialisedField(self, 'Clssfctn', CompareCommodityAssetClass3, False)

	@Clssfctn.deleter
	def Clssfctn(self):
		del self._Clssfctn
		self._Clssfctn = base_types.UninitialisedField(self, 'Clssfctn', CompareCommodityAssetClass3, False)

	@property
	def MktVal(self):
		return self._MktVal

	@MktVal.setter
	def MktVal(self, value):
		self._MktVal = value if value is not None else base_types.UninitialisedField(self, 'MktVal', CompareAmountAndDirection2, False)

	@MktVal.deleter
	def MktVal(self):
		del self._MktVal
		self._MktVal = base_types.UninitialisedField(self, 'MktVal', CompareAmountAndDirection2, False)

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if value is not None else base_types.UninitialisedField(self, 'Qty', CompareDecimalNumber3, False)

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = base_types.UninitialisedField(self, 'Qty', CompareDecimalNumber3, False)

	@property
	def UnitOfMeasr(self):
		return self._UnitOfMeasr

	@UnitOfMeasr.setter
	def UnitOfMeasr(self, value):
		self._UnitOfMeasr = value if value is not None else base_types.UninitialisedField(self, 'UnitOfMeasr', CompareUnitOfMeasure3, False)

	@UnitOfMeasr.deleter
	def UnitOfMeasr(self):
		del self._UnitOfMeasr
		self._UnitOfMeasr = base_types.UninitialisedField(self, 'UnitOfMeasr', CompareUnitOfMeasure3, False)

	@property
	def UnitPric(self):
		return self._UnitPric

	@UnitPric.setter
	def UnitPric(self, value):
		self._UnitPric = value if value is not None else base_types.UninitialisedField(self, 'UnitPric', CompareUnitPrice6, False)

	@UnitPric.deleter
	def UnitPric(self):
		del self._UnitPric
		self._UnitPric = base_types.UninitialisedField(self, 'UnitPric', CompareUnitPrice6, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Clssfctn', type=CompareCommodityAssetClass3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktVal', type=CompareAmountAndDirection2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=CompareDecimalNumber3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitOfMeasr', type=CompareUnitOfMeasure3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitPric', type=CompareUnitPrice6, min=0, max=1, mutex_group=None, array=False),
	))