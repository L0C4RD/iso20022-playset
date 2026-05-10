from . import base_types
from ._PlusOrMinusIndicator import PlusOrMinusIndicator
from ._PercentageRate import PercentageRate

class Rate2(base_types._BaseFieldType):

	__slots__ = ["_Rate", "_Sgn"]
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
	def Sgn(self):
		return self._Sgn

	@Sgn.setter
	def Sgn(self, value):
		self._Sgn = value if type(value) != base_types.auto else self.make_default("Sgn")

	@Sgn.deleter
	def Sgn(self):
		del self._Sgn
		self._Sgn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rate', type=PercentageRate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sgn', type=PlusOrMinusIndicator, min=0, max=1, mutex_group=None, array=False),
	))

