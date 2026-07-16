# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Extension1
from . import Fund4
from . import FundCashForecast6
from . import NetCashForecast3

class FundDetailedConfirmedCashForecastReport3(base_types._BaseFieldType):

	__slots__ = ["_CnsltdNetCshFcst", "_FndCshFcstDtls", "_FndOrSubFndDtls", "_Xtnsn"]
	@property
	def CnsltdNetCshFcst(self):
		return self._CnsltdNetCshFcst

	@CnsltdNetCshFcst.setter
	def CnsltdNetCshFcst(self, value):
		self._CnsltdNetCshFcst = value if value is not None else base_types.UninitialisedField(self, 'CnsltdNetCshFcst', NetCashForecast3, False)

	@CnsltdNetCshFcst.deleter
	def CnsltdNetCshFcst(self):
		del self._CnsltdNetCshFcst
		self._CnsltdNetCshFcst = base_types.UninitialisedField(self, 'CnsltdNetCshFcst', NetCashForecast3, False)

	@property
	def FndCshFcstDtls(self):
		return self._FndCshFcstDtls

	@FndCshFcstDtls.setter
	def FndCshFcstDtls(self, value):
		self._FndCshFcstDtls = value if value is not None else base_types.UninitialisedField(self, 'FndCshFcstDtls', FundCashForecast6, True)

	@FndCshFcstDtls.deleter
	def FndCshFcstDtls(self):
		del self._FndCshFcstDtls
		self._FndCshFcstDtls = base_types.UninitialisedField(self, 'FndCshFcstDtls', FundCashForecast6, True)

	@property
	def FndOrSubFndDtls(self):
		return self._FndOrSubFndDtls

	@FndOrSubFndDtls.setter
	def FndOrSubFndDtls(self, value):
		self._FndOrSubFndDtls = value if value is not None else base_types.UninitialisedField(self, 'FndOrSubFndDtls', Fund4, False)

	@FndOrSubFndDtls.deleter
	def FndOrSubFndDtls(self):
		del self._FndOrSubFndDtls
		self._FndOrSubFndDtls = base_types.UninitialisedField(self, 'FndOrSubFndDtls', Fund4, False)

	@property
	def Xtnsn(self):
		return self._Xtnsn

	@Xtnsn.setter
	def Xtnsn(self, value):
		self._Xtnsn = value if value is not None else base_types.UninitialisedField(self, 'Xtnsn', Extension1, True)

	@Xtnsn.deleter
	def Xtnsn(self):
		del self._Xtnsn
		self._Xtnsn = base_types.UninitialisedField(self, 'Xtnsn', Extension1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CnsltdNetCshFcst', type=NetCashForecast3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FndCshFcstDtls', type=FundCashForecast6, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FndOrSubFndDtls', type=Fund4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Xtnsn', type=Extension1, min=0, max=None, mutex_group=None, array=True),
	))