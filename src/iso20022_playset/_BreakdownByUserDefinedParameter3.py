# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyCode
from . import CashInForecast5
from . import CashOutForecast5
from . import CountryCode
from . import DataFormat2Choice
from . import InvestmentAccount42
from . import NetCashForecast4

class BreakdownByUserDefinedParameter3(base_types._BaseFieldType):

	__slots__ = ["_Ccy", "_CshInFcst", "_CshOutFcst", "_Ctry", "_NetCshFcst", "_Pty", "_UsrDfnd"]
	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if value is not None else base_types.UninitialisedField(self, 'Ccy', ActiveOrHistoricCurrencyCode, False)

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = base_types.UninitialisedField(self, 'Ccy', ActiveOrHistoricCurrencyCode, False)

	@property
	def CshInFcst(self):
		return self._CshInFcst

	@CshInFcst.setter
	def CshInFcst(self, value):
		self._CshInFcst = value if value is not None else base_types.UninitialisedField(self, 'CshInFcst', CashInForecast5, True)

	@CshInFcst.deleter
	def CshInFcst(self):
		del self._CshInFcst
		self._CshInFcst = base_types.UninitialisedField(self, 'CshInFcst', CashInForecast5, True)

	@property
	def CshOutFcst(self):
		return self._CshOutFcst

	@CshOutFcst.setter
	def CshOutFcst(self, value):
		self._CshOutFcst = value if value is not None else base_types.UninitialisedField(self, 'CshOutFcst', CashOutForecast5, True)

	@CshOutFcst.deleter
	def CshOutFcst(self):
		del self._CshOutFcst
		self._CshOutFcst = base_types.UninitialisedField(self, 'CshOutFcst', CashOutForecast5, True)

	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if value is not None else base_types.UninitialisedField(self, 'Ctry', CountryCode, False)

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = base_types.UninitialisedField(self, 'Ctry', CountryCode, False)

	@property
	def NetCshFcst(self):
		return self._NetCshFcst

	@NetCshFcst.setter
	def NetCshFcst(self, value):
		self._NetCshFcst = value if value is not None else base_types.UninitialisedField(self, 'NetCshFcst', NetCashForecast4, True)

	@NetCshFcst.deleter
	def NetCshFcst(self):
		del self._NetCshFcst
		self._NetCshFcst = base_types.UninitialisedField(self, 'NetCshFcst', NetCashForecast4, True)

	@property
	def Pty(self):
		return self._Pty

	@Pty.setter
	def Pty(self, value):
		self._Pty = value if value is not None else base_types.UninitialisedField(self, 'Pty', InvestmentAccount42, False)

	@Pty.deleter
	def Pty(self):
		del self._Pty
		self._Pty = base_types.UninitialisedField(self, 'Pty', InvestmentAccount42, False)

	@property
	def UsrDfnd(self):
		return self._UsrDfnd

	@UsrDfnd.setter
	def UsrDfnd(self, value):
		self._UsrDfnd = value if value is not None else base_types.UninitialisedField(self, 'UsrDfnd', DataFormat2Choice, False)

	@UsrDfnd.deleter
	def UsrDfnd(self):
		del self._UsrDfnd
		self._UsrDfnd = base_types.UninitialisedField(self, 'UsrDfnd', DataFormat2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ccy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshInFcst', type=CashInForecast5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CshOutFcst', type=CashOutForecast5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetCshFcst', type=NetCashForecast4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Pty', type=InvestmentAccount42, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UsrDfnd', type=DataFormat2Choice, min=0, max=1, mutex_group=None, array=False),
	))