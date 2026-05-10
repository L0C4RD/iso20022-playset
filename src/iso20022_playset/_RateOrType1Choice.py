from . import base_types
from ._GenericIdentification1 import GenericIdentification1
from ._PercentageRate import PercentageRate

class RateOrType1Choice(base_types._BaseFieldType):

	__slots__ = ["_Rate", "_Tp"]
	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if type(value) != base_types.auto else self.make_default("Rate")

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = None

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
		base_types.FieldEntry(name='Rate', type=PercentageRate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Tp', type=GenericIdentification1, min=0, max=1, mutex_group=1, array=False),
	))

