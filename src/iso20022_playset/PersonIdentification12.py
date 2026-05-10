from . import base_types
from .GenericPersonIdentification1 import GenericPersonIdentification1
from .CountryCode import CountryCode

class PersonIdentification12(base_types._BaseFieldType):

	__slots__ = ["_Othr", "_CtryOfBrnch"]
	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if type(value) != base_types.auto else self.make_default("Othr")

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = None

	@property
	def CtryOfBrnch(self):
		return self._CtryOfBrnch

	@CtryOfBrnch.setter
	def CtryOfBrnch(self, value):
		self._CtryOfBrnch = value if type(value) != base_types.auto else self.make_default("CtryOfBrnch")

	@CtryOfBrnch.deleter
	def CtryOfBrnch(self):
		del self._CtryOfBrnch
		self._CtryOfBrnch = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Othr', type=GenericPersonIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryOfBrnch', type=CountryCode, min=1, max=1, mutex_group=None, array=False),
	))

