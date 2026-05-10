from . import base_types
import DateAndPlaceOfBirth1
import GenericPersonIdentification1

class PersonIdentification13(base_types._BaseFieldType):

	__slots__ = ["_Othr", "_DtAndPlcOfBirth"]
	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if type(value) != auto else self.make_default("Othr")

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = None

	@property
	def DtAndPlcOfBirth(self):
		return self._DtAndPlcOfBirth

	@DtAndPlcOfBirth.setter
	def DtAndPlcOfBirth(self, value):
		self._DtAndPlcOfBirth = value if type(value) != auto else self.make_default("DtAndPlcOfBirth")

	@DtAndPlcOfBirth.deleter
	def DtAndPlcOfBirth(self):
		del self._DtAndPlcOfBirth
		self._DtAndPlcOfBirth = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Othr', type=GenericPersonIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DtAndPlcOfBirth', type=DateAndPlaceOfBirth1, min=0, max=1, mutex_group=None, array=False),
	))

