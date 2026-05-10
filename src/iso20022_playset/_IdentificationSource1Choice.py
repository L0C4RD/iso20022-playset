from . import base_types
from .Max35Text import Max35Text
from .CountryCode import CountryCode

class IdentificationSource1Choice(base_types._BaseFieldType):

	__slots__ = ["_Dmst", "_Prtry"]
	@property
	def Dmst(self):
		return self._Dmst

	@Dmst.setter
	def Dmst(self, value):
		self._Dmst = value if type(value) != base_types.auto else self.make_default("Dmst")

	@Dmst.deleter
	def Dmst(self):
		del self._Dmst
		self._Dmst = None

	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if type(value) != base_types.auto else self.make_default("Prtry")

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dmst', type=CountryCode, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
	))

