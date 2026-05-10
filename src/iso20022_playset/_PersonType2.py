from . import base_types
from ._RequestedIndicator import RequestedIndicator
from ._GenericPersonType1 import GenericPersonType1

class PersonType2(base_types._BaseFieldType):

	__slots__ = ["_Othr", "_DtAndPlcOfBirth", "_EmailAdr"]
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
	def EmailAdr(self):
		return self._EmailAdr

	@EmailAdr.setter
	def EmailAdr(self, value):
		self._EmailAdr = value if type(value) != base_types.auto else self.make_default("EmailAdr")

	@EmailAdr.deleter
	def EmailAdr(self):
		del self._EmailAdr
		self._EmailAdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Othr', type=GenericPersonType1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DtAndPlcOfBirth', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EmailAdr', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
	))

