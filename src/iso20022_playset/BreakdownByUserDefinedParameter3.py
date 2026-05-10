from . import base_types
from .CountryCode import CountryCode
from .NetCashForecast4 import NetCashForecast4
from .InvestmentAccount42 import InvestmentAccount42
from .ActiveOrHistoricCurrencyCode import ActiveOrHistoricCurrencyCode
from .DataFormat2Choice import DataFormat2Choice
from .CashInForecast5 import CashInForecast5
from .CashOutForecast5 import CashOutForecast5

class BreakdownByUserDefinedParameter3(base_types._BaseFieldType):

	__slots__ = ["_Ccy", "_CshOutFcst", "_NetCshFcst", "_CshInFcst", "_Ctry", "_UsrDfnd", "_Pty"]
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
	def CshOutFcst(self):
		return self._CshOutFcst

	@CshOutFcst.setter
	def CshOutFcst(self, value):
		self._CshOutFcst = value if type(value) != auto else self.make_default("CshOutFcst")

	@CshOutFcst.deleter
	def CshOutFcst(self):
		del self._CshOutFcst
		self._CshOutFcst = None

	@property
	def NetCshFcst(self):
		return self._NetCshFcst

	@NetCshFcst.setter
	def NetCshFcst(self, value):
		self._NetCshFcst = value if type(value) != auto else self.make_default("NetCshFcst")

	@NetCshFcst.deleter
	def NetCshFcst(self):
		del self._NetCshFcst
		self._NetCshFcst = None

	@property
	def CshInFcst(self):
		return self._CshInFcst

	@CshInFcst.setter
	def CshInFcst(self, value):
		self._CshInFcst = value if type(value) != auto else self.make_default("CshInFcst")

	@CshInFcst.deleter
	def CshInFcst(self):
		del self._CshInFcst
		self._CshInFcst = None

	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if type(value) != auto else self.make_default("Ctry")

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = None

	@property
	def UsrDfnd(self):
		return self._UsrDfnd

	@UsrDfnd.setter
	def UsrDfnd(self, value):
		self._UsrDfnd = value if type(value) != auto else self.make_default("UsrDfnd")

	@UsrDfnd.deleter
	def UsrDfnd(self):
		del self._UsrDfnd
		self._UsrDfnd = None

	@property
	def Pty(self):
		return self._Pty

	@Pty.setter
	def Pty(self, value):
		self._Pty = value if type(value) != auto else self.make_default("Pty")

	@Pty.deleter
	def Pty(self):
		del self._Pty
		self._Pty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ccy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshOutFcst', type=CashOutForecast5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NetCshFcst', type=NetCashForecast4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CshInFcst', type=CashInForecast5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UsrDfnd', type=DataFormat2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pty', type=InvestmentAccount42, min=0, max=1, mutex_group=None, array=False),
	))

