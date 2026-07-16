# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DecimalNumber
from . import ISODate

class ShipmentDateRange2(base_types._BaseFieldType):

	__slots__ = ["_EarlstShipmntDt", "_LatstShipmntDt", "_SubQtyVal"]
	@property
	def EarlstShipmntDt(self):
		return self._EarlstShipmntDt

	@EarlstShipmntDt.setter
	def EarlstShipmntDt(self, value):
		self._EarlstShipmntDt = value if value is not None else base_types.UninitialisedField(self, 'EarlstShipmntDt', ISODate, False)

	@EarlstShipmntDt.deleter
	def EarlstShipmntDt(self):
		del self._EarlstShipmntDt
		self._EarlstShipmntDt = base_types.UninitialisedField(self, 'EarlstShipmntDt', ISODate, False)

	@property
	def LatstShipmntDt(self):
		return self._LatstShipmntDt

	@LatstShipmntDt.setter
	def LatstShipmntDt(self, value):
		self._LatstShipmntDt = value if value is not None else base_types.UninitialisedField(self, 'LatstShipmntDt', ISODate, False)

	@LatstShipmntDt.deleter
	def LatstShipmntDt(self):
		del self._LatstShipmntDt
		self._LatstShipmntDt = base_types.UninitialisedField(self, 'LatstShipmntDt', ISODate, False)

	@property
	def SubQtyVal(self):
		return self._SubQtyVal

	@SubQtyVal.setter
	def SubQtyVal(self, value):
		self._SubQtyVal = value if value is not None else base_types.UninitialisedField(self, 'SubQtyVal', DecimalNumber, False)

	@SubQtyVal.deleter
	def SubQtyVal(self):
		del self._SubQtyVal
		self._SubQtyVal = base_types.UninitialisedField(self, 'SubQtyVal', DecimalNumber, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='EarlstShipmntDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LatstShipmntDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubQtyVal', type=DecimalNumber, min=1, max=1, mutex_group=None, array=False),
	))