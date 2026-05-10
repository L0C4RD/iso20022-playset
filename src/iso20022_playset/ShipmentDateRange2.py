from . import base_types
import ISODate
import DecimalNumber

class ShipmentDateRange2(base_types._BaseFieldType):

	__slots__ = ["_EarlstShipmntDt", "_LatstShipmntDt", "_SubQtyVal"]
	@property
	def EarlstShipmntDt(self):
		return self._EarlstShipmntDt

	@EarlstShipmntDt.setter
	def EarlstShipmntDt(self, value):
		self._EarlstShipmntDt = value if type(value) != auto else self.make_default("EarlstShipmntDt")

	@EarlstShipmntDt.deleter
	def EarlstShipmntDt(self):
		del self._EarlstShipmntDt
		self._EarlstShipmntDt = None

	@property
	def LatstShipmntDt(self):
		return self._LatstShipmntDt

	@LatstShipmntDt.setter
	def LatstShipmntDt(self, value):
		self._LatstShipmntDt = value if type(value) != auto else self.make_default("LatstShipmntDt")

	@LatstShipmntDt.deleter
	def LatstShipmntDt(self):
		del self._LatstShipmntDt
		self._LatstShipmntDt = None

	@property
	def SubQtyVal(self):
		return self._SubQtyVal

	@SubQtyVal.setter
	def SubQtyVal(self, value):
		self._SubQtyVal = value if type(value) != auto else self.make_default("SubQtyVal")

	@SubQtyVal.deleter
	def SubQtyVal(self):
		del self._SubQtyVal
		self._SubQtyVal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='EarlstShipmntDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LatstShipmntDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubQtyVal', type=DecimalNumber, min=1, max=1, mutex_group=None, array=False),
	))

