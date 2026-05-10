import base_types
import VariableInterest1Rate
import PercentageRate

class InterestRate1Choice(base_types._BaseFieldType):

	__slots__ = ["_FxdIntrstRate", "_VarblIntrstRate"]
	@property
	def FxdIntrstRate(self):
		return self._FxdIntrstRate

	@FxdIntrstRate.setter
	def FxdIntrstRate(self, value):
		self._FxdIntrstRate = value if type(value) != auto else self.make_default("FxdIntrstRate")

	@FxdIntrstRate.deleter
	def FxdIntrstRate(self):
		del self._FxdIntrstRate
		self._FxdIntrstRate = None

	@property
	def VarblIntrstRate(self):
		return self._VarblIntrstRate

	@VarblIntrstRate.setter
	def VarblIntrstRate(self, value):
		self._VarblIntrstRate = value if type(value) != auto else self.make_default("VarblIntrstRate")

	@VarblIntrstRate.deleter
	def VarblIntrstRate(self):
		del self._VarblIntrstRate
		self._VarblIntrstRate = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FxdIntrstRate', type=PercentageRate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='VarblIntrstRate', type=VariableInterest1Rate, min=0, max=1, mutex_group=1, array=False),
	))

