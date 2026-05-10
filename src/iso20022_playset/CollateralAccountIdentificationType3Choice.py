from . import base_types
from .CollateralAccountType1Code import CollateralAccountType1Code
from .GenericIdentification36 import GenericIdentification36

class CollateralAccountIdentificationType3Choice(base_types._BaseFieldType):

	__slots__ = ["_Prtry", "_Tp"]
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

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Prtry', type=GenericIdentification36, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Tp', type=CollateralAccountType1Code, min=0, max=1, mutex_group=1, array=False),
	))

