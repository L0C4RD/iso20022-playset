# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection53
from . import AssetClassCommodity5Choice
from . import Quantity17
from . import SecuritiesTransactionPrice19Choice

class Commodity43(base_types._BaseFieldType):

	__slots__ = ["_Clssfctn", "_MktVal", "_Qty", "_UnitPric"]
	@property
	def Clssfctn(self):
		return self._Clssfctn

	@Clssfctn.setter
	def Clssfctn(self, value):
		self._Clssfctn = value if value is not None else base_types.UninitialisedField(self, 'Clssfctn', AssetClassCommodity5Choice, False)

	@Clssfctn.deleter
	def Clssfctn(self):
		del self._Clssfctn
		self._Clssfctn = base_types.UninitialisedField(self, 'Clssfctn', AssetClassCommodity5Choice, False)

	@property
	def MktVal(self):
		return self._MktVal

	@MktVal.setter
	def MktVal(self, value):
		self._MktVal = value if value is not None else base_types.UninitialisedField(self, 'MktVal', AmountAndDirection53, False)

	@MktVal.deleter
	def MktVal(self):
		del self._MktVal
		self._MktVal = base_types.UninitialisedField(self, 'MktVal', AmountAndDirection53, False)

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if value is not None else base_types.UninitialisedField(self, 'Qty', Quantity17, False)

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = base_types.UninitialisedField(self, 'Qty', Quantity17, False)

	@property
	def UnitPric(self):
		return self._UnitPric

	@UnitPric.setter
	def UnitPric(self, value):
		self._UnitPric = value if value is not None else base_types.UninitialisedField(self, 'UnitPric', SecuritiesTransactionPrice19Choice, False)

	@UnitPric.deleter
	def UnitPric(self):
		del self._UnitPric
		self._UnitPric = base_types.UninitialisedField(self, 'UnitPric', SecuritiesTransactionPrice19Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Clssfctn', type=AssetClassCommodity5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktVal', type=AmountAndDirection53, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=Quantity17, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitPric', type=SecuritiesTransactionPrice19Choice, min=0, max=1, mutex_group=None, array=False),
	))