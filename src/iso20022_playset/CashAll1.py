from . import base_types
from .ActiveCurrencyCode import ActiveCurrencyCode
from .YesNoIndicator import YesNoIndicator

class CashAll1(base_types._BaseFieldType):

	__slots__ = ["_Ccy", "_Ind"]
	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if type(value) != auto else self.make_default("Ccy")

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = None

	@property
	def Ind(self):
		return self._Ind

	@Ind.setter
	def Ind(self, value):
		self._Ind = value if type(value) != auto else self.make_default("Ind")

	@Ind.deleter
	def Ind(self):
		del self._Ind
		self._Ind = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ind', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
	))

