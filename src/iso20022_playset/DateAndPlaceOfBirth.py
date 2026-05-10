from . import base_types
from .CountryCode import CountryCode
from .ISODate import ISODate
from .Max35Text import Max35Text

class DateAndPlaceOfBirth(base_types._BaseFieldType):

	__slots__ = ["_CityOfBirth", "_BirthDt", "_PrvcOfBirth", "_CtryOfBirth"]
	@property
	def CityOfBirth(self):
		return self._CityOfBirth

	@CityOfBirth.setter
	def CityOfBirth(self, value):
		self._CityOfBirth = value if type(value) != base_types.auto else self.make_default("CityOfBirth")

	@CityOfBirth.deleter
	def CityOfBirth(self):
		del self._CityOfBirth
		self._CityOfBirth = None

	@property
	def BirthDt(self):
		return self._BirthDt

	@BirthDt.setter
	def BirthDt(self, value):
		self._BirthDt = value if type(value) != base_types.auto else self.make_default("BirthDt")

	@BirthDt.deleter
	def BirthDt(self):
		del self._BirthDt
		self._BirthDt = None

	@property
	def PrvcOfBirth(self):
		return self._PrvcOfBirth

	@PrvcOfBirth.setter
	def PrvcOfBirth(self, value):
		self._PrvcOfBirth = value if type(value) != base_types.auto else self.make_default("PrvcOfBirth")

	@PrvcOfBirth.deleter
	def PrvcOfBirth(self):
		del self._PrvcOfBirth
		self._PrvcOfBirth = None

	@property
	def CtryOfBirth(self):
		return self._CtryOfBirth

	@CtryOfBirth.setter
	def CtryOfBirth(self, value):
		self._CtryOfBirth = value if type(value) != base_types.auto else self.make_default("CtryOfBirth")

	@CtryOfBirth.deleter
	def CtryOfBirth(self):
		del self._CtryOfBirth
		self._CtryOfBirth = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CityOfBirth', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BirthDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvcOfBirth', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryOfBirth', type=CountryCode, min=1, max=1, mutex_group=None, array=False),
	))

