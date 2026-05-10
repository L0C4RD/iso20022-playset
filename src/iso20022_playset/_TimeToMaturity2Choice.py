from . import base_types
from ._TimeToMaturityPeriod2 import TimeToMaturityPeriod2
from ._SpecialPurpose2Code import SpecialPurpose2Code

class TimeToMaturity2Choice(base_types._BaseFieldType):

	__slots__ = ["_Spcl", "_Prd"]
	@property
	def Prd(self):
		return self._Prd

	@Prd.setter
	def Prd(self, value):
		self._Prd = value if type(value) != base_types.auto else self.make_default("Prd")

	@Prd.deleter
	def Prd(self):
		del self._Prd
		self._Prd = None

	@property
	def Spcl(self):
		return self._Spcl

	@Spcl.setter
	def Spcl(self, value):
		self._Spcl = value if type(value) != base_types.auto else self.make_default("Spcl")

	@Spcl.deleter
	def Spcl(self):
		del self._Spcl
		self._Spcl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Prd', type=TimeToMaturityPeriod2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Spcl', type=SpecialPurpose2Code, min=0, max=1, mutex_group=1, array=False),
	))

