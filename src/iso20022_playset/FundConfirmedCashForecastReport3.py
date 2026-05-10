from . import base_types
import FundCashForecast7
import Extension1
import Fund2
import NetCashForecast3

class FundConfirmedCashForecastReport3(base_types._BaseFieldType):

	__slots__ = ["_Xtnsn", "_FndOrSubFndDtls", "_CnsltdNetCshFcst", "_FndCshFcstDtls"]
	@property
	def Xtnsn(self):
		return self._Xtnsn

	@Xtnsn.setter
	def Xtnsn(self, value):
		self._Xtnsn = value if type(value) != auto else self.make_default("Xtnsn")

	@Xtnsn.deleter
	def Xtnsn(self):
		del self._Xtnsn
		self._Xtnsn = None

	@property
	def FndOrSubFndDtls(self):
		return self._FndOrSubFndDtls

	@FndOrSubFndDtls.setter
	def FndOrSubFndDtls(self, value):
		self._FndOrSubFndDtls = value if type(value) != auto else self.make_default("FndOrSubFndDtls")

	@FndOrSubFndDtls.deleter
	def FndOrSubFndDtls(self):
		del self._FndOrSubFndDtls
		self._FndOrSubFndDtls = None

	@property
	def CnsltdNetCshFcst(self):
		return self._CnsltdNetCshFcst

	@CnsltdNetCshFcst.setter
	def CnsltdNetCshFcst(self, value):
		self._CnsltdNetCshFcst = value if type(value) != auto else self.make_default("CnsltdNetCshFcst")

	@CnsltdNetCshFcst.deleter
	def CnsltdNetCshFcst(self):
		del self._CnsltdNetCshFcst
		self._CnsltdNetCshFcst = None

	@property
	def FndCshFcstDtls(self):
		return self._FndCshFcstDtls

	@FndCshFcstDtls.setter
	def FndCshFcstDtls(self, value):
		self._FndCshFcstDtls = value if type(value) != auto else self.make_default("FndCshFcstDtls")

	@FndCshFcstDtls.deleter
	def FndCshFcstDtls(self):
		del self._FndCshFcstDtls
		self._FndCshFcstDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Xtnsn', type=Extension1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FndOrSubFndDtls', type=Fund2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CnsltdNetCshFcst', type=NetCashForecast3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FndCshFcstDtls', type=FundCashForecast7, min=0, max=None, mutex_group=None, array=True),
	))

