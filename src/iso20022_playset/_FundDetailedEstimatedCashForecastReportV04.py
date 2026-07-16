# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalReference3
from . import EstimatedFundCashForecast5
from . import Extension1
from . import Fund3
from . import MessageIdentification1
from . import NetCashForecast3
from . import Pagination

class FundDetailedEstimatedCashForecastReportV04(base_types._BaseFieldType):

	__slots__ = ["_CnsltdNetCshFcst", "_EstmtdFndCshFcstDtls", "_FndOrSubFndDtls", "_MsgId", "_MsgPgntn", "_PoolRef", "_PrvsRef", "_RltdRef", "_Xtnsn"]
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
	def EstmtdFndCshFcstDtls(self):
		return self._EstmtdFndCshFcstDtls

	@EstmtdFndCshFcstDtls.setter
	def EstmtdFndCshFcstDtls(self, value):
		self._EstmtdFndCshFcstDtls = value if value is not None else base_types.UninitialisedField(self, 'EstmtdFndCshFcstDtls', EstimatedFundCashForecast5, True)

	@EstmtdFndCshFcstDtls.deleter
	def EstmtdFndCshFcstDtls(self):
		del self._EstmtdFndCshFcstDtls
		self._EstmtdFndCshFcstDtls = base_types.UninitialisedField(self, 'EstmtdFndCshFcstDtls', EstimatedFundCashForecast5, True)

	@property
	def FndOrSubFndDtls(self):
		return self._FndOrSubFndDtls

	@FndOrSubFndDtls.setter
	def FndOrSubFndDtls(self, value):
		self._FndOrSubFndDtls = value if value is not None else base_types.UninitialisedField(self, 'FndOrSubFndDtls', Fund3, False)

	@FndOrSubFndDtls.deleter
	def FndOrSubFndDtls(self):
		del self._FndOrSubFndDtls
		self._FndOrSubFndDtls = base_types.UninitialisedField(self, 'FndOrSubFndDtls', Fund3, False)

	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if value is not None else base_types.UninitialisedField(self, 'MsgId', MessageIdentification1, False)

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = base_types.UninitialisedField(self, 'MsgId', MessageIdentification1, False)

	@property
	def MsgPgntn(self):
		return self._MsgPgntn

	@MsgPgntn.setter
	def MsgPgntn(self, value):
		self._MsgPgntn = value if value is not None else base_types.UninitialisedField(self, 'MsgPgntn', Pagination, False)

	@MsgPgntn.deleter
	def MsgPgntn(self):
		del self._MsgPgntn
		self._MsgPgntn = base_types.UninitialisedField(self, 'MsgPgntn', Pagination, False)

	@property
	def PoolRef(self):
		return self._PoolRef

	@PoolRef.setter
	def PoolRef(self, value):
		self._PoolRef = value if value is not None else base_types.UninitialisedField(self, 'PoolRef', AdditionalReference3, False)

	@PoolRef.deleter
	def PoolRef(self):
		del self._PoolRef
		self._PoolRef = base_types.UninitialisedField(self, 'PoolRef', AdditionalReference3, False)

	@property
	def PrvsRef(self):
		return self._PrvsRef

	@PrvsRef.setter
	def PrvsRef(self, value):
		self._PrvsRef = value if value is not None else base_types.UninitialisedField(self, 'PrvsRef', AdditionalReference3, True)

	@PrvsRef.deleter
	def PrvsRef(self):
		del self._PrvsRef
		self._PrvsRef = base_types.UninitialisedField(self, 'PrvsRef', AdditionalReference3, True)

	@property
	def RltdRef(self):
		return self._RltdRef

	@RltdRef.setter
	def RltdRef(self, value):
		self._RltdRef = value if value is not None else base_types.UninitialisedField(self, 'RltdRef', AdditionalReference3, True)

	@RltdRef.deleter
	def RltdRef(self):
		del self._RltdRef
		self._RltdRef = base_types.UninitialisedField(self, 'RltdRef', AdditionalReference3, True)

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
		base_types.FieldEntry(name='EstmtdFndCshFcstDtls', type=EstimatedFundCashForecast5, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FndOrSubFndDtls', type=Fund3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgPgntn', type=Pagination, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PoolRef', type=AdditionalReference3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsRef', type=AdditionalReference3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RltdRef', type=AdditionalReference3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Xtnsn', type=Extension1, min=0, max=None, mutex_group=None, array=True),
	))