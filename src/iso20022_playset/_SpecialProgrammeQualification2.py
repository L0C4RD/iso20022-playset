from . import base_types
from .Max35Text import Max35Text
from .SpecialProgrammeDetails2 import SpecialProgrammeDetails2

class SpecialProgrammeQualification2(base_types._BaseFieldType):

	__slots__ = ["_Dtl", "_Prgrmm"]
	@property
	def Dtl(self):
		return self._Dtl

	@Dtl.setter
	def Dtl(self, value):
		self._Dtl = value if type(value) != base_types.auto else self.make_default("Dtl")

	@Dtl.deleter
	def Dtl(self):
		del self._Dtl
		self._Dtl = None

	@property
	def Prgrmm(self):
		return self._Prgrmm

	@Prgrmm.setter
	def Prgrmm(self, value):
		self._Prgrmm = value if type(value) != base_types.auto else self.make_default("Prgrmm")

	@Prgrmm.deleter
	def Prgrmm(self):
		del self._Prgrmm
		self._Prgrmm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dtl', type=SpecialProgrammeDetails2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Prgrmm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

