from . import base_types
from .PercentageRate import PercentageRate

class PercentageTolerance1(base_types._BaseFieldType):

	__slots__ = ["_MnsPct", "_PlusPct"]
	@property
	def MnsPct(self):
		return self._MnsPct

	@MnsPct.setter
	def MnsPct(self, value):
		self._MnsPct = value if type(value) != auto else self.make_default("MnsPct")

	@MnsPct.deleter
	def MnsPct(self):
		del self._MnsPct
		self._MnsPct = None

	@property
	def PlusPct(self):
		return self._PlusPct

	@PlusPct.setter
	def PlusPct(self, value):
		self._PlusPct = value if type(value) != auto else self.make_default("PlusPct")

	@PlusPct.deleter
	def PlusPct(self):
		del self._PlusPct
		self._PlusPct = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MnsPct', type=PercentageRate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlusPct', type=PercentageRate, min=1, max=1, mutex_group=None, array=False),
	))

