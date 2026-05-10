from . import base_types
from .NetCashForecast4 import NetCashForecast4
from .CashInForecast5 import CashInForecast5
from .InvestmentAccount42 import InvestmentAccount42
from .AdditionalParameters1 import AdditionalParameters1
from .CashOutForecast5 import CashOutForecast5

class BreakdownByParty3(base_types._BaseFieldType):

	__slots__ = ["_AddtlParams", "_CshOutFcst", "_CshInFcst", "_NetCshFcst", "_Pty"]
	@property
	def AddtlParams(self):
		return self._AddtlParams

	@AddtlParams.setter
	def AddtlParams(self, value):
		self._AddtlParams = value if type(value) != base_types.auto else self.make_default("AddtlParams")

	@AddtlParams.deleter
	def AddtlParams(self):
		del self._AddtlParams
		self._AddtlParams = None

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
	def Pty(self):
		return self._Pty

	@Pty.setter
	def Pty(self, value):
		self._Pty = value if type(value) != base_types.auto else self.make_default("Pty")

	@Pty.deleter
	def Pty(self):
		del self._Pty
		self._Pty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlParams', type=AdditionalParameters1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshOutFcst', type=CashOutForecast5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CshInFcst', type=CashInForecast5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NetCshFcst', type=NetCashForecast4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Pty', type=InvestmentAccount42, min=1, max=1, mutex_group=None, array=False),
	))

