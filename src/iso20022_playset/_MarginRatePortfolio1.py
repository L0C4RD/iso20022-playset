from . import base_types
from ._ActiveCurrencyAnd24Amount import ActiveCurrencyAnd24Amount
from ._Max2000Text import Max2000Text

class MarginRatePortfolio1(base_types._BaseFieldType):

	__slots__ = ["_Desc", "_LngMrgnRate", "_ShrtMrgnRate"]
	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if type(value) != base_types.auto else self.make_default("Desc")

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = None

	@property
	def LngMrgnRate(self):
		return self._LngMrgnRate

	@LngMrgnRate.setter
	def LngMrgnRate(self, value):
		self._LngMrgnRate = value if type(value) != base_types.auto else self.make_default("LngMrgnRate")

	@LngMrgnRate.deleter
	def LngMrgnRate(self):
		del self._LngMrgnRate
		self._LngMrgnRate = None

	@property
	def ShrtMrgnRate(self):
		return self._ShrtMrgnRate

	@ShrtMrgnRate.setter
	def ShrtMrgnRate(self, value):
		self._ShrtMrgnRate = value if type(value) != base_types.auto else self.make_default("ShrtMrgnRate")

	@ShrtMrgnRate.deleter
	def ShrtMrgnRate(self):
		del self._ShrtMrgnRate
		self._ShrtMrgnRate = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Desc', type=Max2000Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LngMrgnRate', type=ActiveCurrencyAnd24Amount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrtMrgnRate', type=ActiveCurrencyAnd24Amount, min=1, max=1, mutex_group=None, array=False),
	))

