from . import base_types
from ._BaseOneRate import BaseOneRate
from ._PercentageRate import PercentageRate

class ExchangeRateOrPercentage1Choice(base_types._BaseFieldType):

	__slots__ = ["_Rate", "_Pctg"]
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
	def Pctg(self):
		return self._Pctg

	@Pctg.setter
	def Pctg(self, value):
		self._Pctg = value if type(value) != base_types.auto else self.make_default("Pctg")

	@Pctg.deleter
	def Pctg(self):
		del self._Pctg
		self._Pctg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rate', type=BaseOneRate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Pctg', type=PercentageRate, min=0, max=1, mutex_group=1, array=False),
	))

