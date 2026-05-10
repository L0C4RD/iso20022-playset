import base_types
import ISODate

class ShipmentDateRange1(base_types._BaseFieldType):

	__slots__ = ["_EarlstShipmntDt", "_LatstShipmntDt"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='EarlstShipmntDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LatstShipmntDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))

