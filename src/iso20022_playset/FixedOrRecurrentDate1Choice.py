from . import base_types
import ISODate
import DateInformation1

class FixedOrRecurrentDate1Choice(base_types._BaseFieldType):

	__slots__ = ["_RcrntDt", "_FxdDt"]
	@property
	def RcrntDt(self):
		return self._RcrntDt

	@RcrntDt.setter
	def RcrntDt(self, value):
		self._RcrntDt = value if type(value) != auto else self.make_default("RcrntDt")

	@RcrntDt.deleter
	def RcrntDt(self):
		del self._RcrntDt
		self._RcrntDt = None

	@property
	def FxdDt(self):
		return self._FxdDt

	@FxdDt.setter
	def FxdDt(self, value):
		self._FxdDt = value if type(value) != auto else self.make_default("FxdDt")

	@FxdDt.deleter
	def FxdDt(self):
		del self._FxdDt
		self._FxdDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RcrntDt', type=DateInformation1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FxdDt', type=ISODate, min=0, max=1, mutex_group=1, array=False),
	))

