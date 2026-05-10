from . import base_types
from .Max35Text import Max35Text
from .CountryCode import CountryCode

class ResidenceLocation1Choice(base_types._BaseFieldType):

	__slots__ = ["_Area", "_Ctry"]
	@property
	def Area(self):
		return self._Area

	@Area.setter
	def Area(self, value):
		self._Area = value if type(value) != base_types.auto else self.make_default("Area")

	@Area.deleter
	def Area(self):
		del self._Area
		self._Area = None

	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if type(value) != base_types.auto else self.make_default("Ctry")

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Area', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=0, max=1, mutex_group=1, array=False),
	))

