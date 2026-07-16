# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CashInForecast5
from . import CashOutForecast5
from . import CountryCode
from . import NetCashForecast4

class BreakdownByCountry2(base_types._BaseFieldType):

	__slots__ = ["_CshInFcst", "_CshOutFcst", "_Ctry", "_NetCshFcst"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshInFcst', type=CashInForecast5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CshOutFcst', type=CashOutForecast5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetCshFcst', type=NetCashForecast4, min=0, max=None, mutex_group=None, array=True),
	))