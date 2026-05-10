from . import base_types
from .NetCashForecast4 import NetCashForecast4
from .CashOutForecast5 import CashOutForecast5
from .CountryCode import CountryCode
from .CashInForecast5 import CashInForecast5

class BreakdownByCountry2(base_types._BaseFieldType):

	__slots__ = ["_CshInFcst", "_NetCshFcst", "_Ctry", "_CshOutFcst"]
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
	def NetCshFcst(self):
		return self._NetCshFcst

	@NetCshFcst.setter
	def NetCshFcst(self, value):
		self._NetCshFcst = value if type(value) != base_types.auto else self.make_default("NetCshFcst")

	@NetCshFcst.deleter
	def NetCshFcst(self):
		del self._NetCshFcst
		self._NetCshFcst = None

	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if type(value) != base_types.auto else self.make_default("Ctry")

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshInFcst', type=CashInForecast5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NetCshFcst', type=NetCashForecast4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshOutFcst', type=CashOutForecast5, min=0, max=None, mutex_group=None, array=True),
	))

