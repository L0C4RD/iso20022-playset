import base_types
import PercentageRate

class InternalisationDataRate1(base_types._BaseFieldType):

	__slots__ = ["_Val", "_VolPctg"]
	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if type(value) != auto else self.make_default("Val")

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = None

	@property
	def VolPctg(self):
		return self._VolPctg

	@VolPctg.setter
	def VolPctg(self, value):
		self._VolPctg = value if type(value) != auto else self.make_default("VolPctg")

	@VolPctg.deleter
	def VolPctg(self):
		del self._VolPctg
		self._VolPctg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Val', type=PercentageRate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VolPctg', type=PercentageRate, min=1, max=1, mutex_group=None, array=False),
	))

