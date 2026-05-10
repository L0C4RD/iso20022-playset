from . import base_types
from ._CashOutForecast5 import CashOutForecast5
from ._NetCashForecast4 import NetCashForecast4
from ._ActiveOrHistoricCurrencyCode import ActiveOrHistoricCurrencyCode
from ._CashInForecast5 import CashInForecast5

class BreakdownByCurrency2(base_types._BaseFieldType):

	__slots__ = ["_CshOutFcst", "_NetCshFcst", "_Ccy", "_CshInFcst"]
	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if type(value) != base_types.auto else self.make_default("Ccy")

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = None

	@property
	def CshInFcst(self):
		return self._CshInFcst

	@CshInFcst.setter
	def CshInFcst(self, value):
		self._CshInFcst = value if type(value) != base_types.auto else self.make_default("CshInFcst")

	@CshInFcst.deleter
	def CshInFcst(self):
		del self._CshInFcst
		self._CshInFcst = None

	@property
	def CshOutFcst(self):
		return self._CshOutFcst

	@CshOutFcst.setter
	def CshOutFcst(self, value):
		self._CshOutFcst = value if type(value) != base_types.auto else self.make_default("CshOutFcst")

	@CshOutFcst.deleter
	def CshOutFcst(self):
		del self._CshOutFcst
		self._CshOutFcst = None

	@property
	def NetCshFcst(self):
		return self._NetCshFcst

	@NetCshFcst.setter
	def NetCshFcst(self, value):
		self._NetCshFcst = value if type(value) != base_types.auto else self.make_default("NetCshFcst")

	@NetCshFcst.deleter
	def NetCshFcst(self):
		del self._NetCshFcst
		self._NetCshFcst = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ccy', type=ActiveOrHistoricCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshInFcst', type=CashInForecast5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CshOutFcst', type=CashOutForecast5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NetCshFcst', type=NetCashForecast4, min=0, max=None, mutex_group=None, array=True),
	))

