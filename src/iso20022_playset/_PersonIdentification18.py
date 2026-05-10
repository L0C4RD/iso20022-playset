from . import base_types
from ._DateAndPlaceOfBirth1 import DateAndPlaceOfBirth1
from ._GenericPersonIdentification2 import GenericPersonIdentification2

class PersonIdentification18(base_types._BaseFieldType):

	__slots__ = ["_Othr", "_DtAndPlcOfBirth"]
	@property
	def DtAndPlcOfBirth(self):
		return self._DtAndPlcOfBirth

	@DtAndPlcOfBirth.setter
	def DtAndPlcOfBirth(self, value):
		self._DtAndPlcOfBirth = value if type(value) != base_types.auto else self.make_default("DtAndPlcOfBirth")

	@DtAndPlcOfBirth.deleter
	def DtAndPlcOfBirth(self):
		del self._DtAndPlcOfBirth
		self._DtAndPlcOfBirth = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='DtAndPlcOfBirth', type=DateAndPlaceOfBirth1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Othr', type=GenericPersonIdentification2, min=0, max=None, mutex_group=None, array=True),
	))

