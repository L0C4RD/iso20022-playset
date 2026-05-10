from . import base_types
from .PercentageRate import PercentageRate
from .Rates3 import Rates3

class PriceMetrics3(base_types._BaseFieldType):

	__slots__ = ["_LndgFee", "_Rates"]
	@property
	def LndgFee(self):
		return self._LndgFee

	@LndgFee.setter
	def LndgFee(self, value):
		self._LndgFee = value if type(value) != auto else self.make_default("LndgFee")

	@LndgFee.deleter
	def LndgFee(self):
		del self._LndgFee
		self._LndgFee = None

	@property
	def Rates(self):
		return self._Rates

	@Rates.setter
	def Rates(self, value):
		self._Rates = value if type(value) != auto else self.make_default("Rates")

	@Rates.deleter
	def Rates(self):
		del self._Rates
		self._Rates = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LndgFee', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rates', type=Rates3, min=0, max=1, mutex_group=None, array=False),
	))

