from . import base_types
from .Max140Text import Max140Text
from .GenericPersonIdentification1 import GenericPersonIdentification1
from .ISODate import ISODate

class PersonIdentification10(base_types._BaseFieldType):

	__slots__ = ["_BirthDt", "_Othr", "_FrstNm", "_Nm"]
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
	def FrstNm(self):
		return self._FrstNm

	@FrstNm.setter
	def FrstNm(self, value):
		self._FrstNm = value if type(value) != base_types.auto else self.make_default("FrstNm")

	@FrstNm.deleter
	def FrstNm(self):
		del self._FrstNm
		self._FrstNm = None

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if type(value) != base_types.auto else self.make_default("Nm")

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BirthDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Othr', type=GenericPersonIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrstNm', type=Max140Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max140Text, min=1, max=1, mutex_group=None, array=False),
	))

