from . import base_types
from ._Pagination import Pagination
from ._EstimatedFundCashForecast6 import EstimatedFundCashForecast6
from ._Fund1 import Fund1
from ._MessageIdentification1 import MessageIdentification1
from ._Extension1 import Extension1
from ._AdditionalReference3 import AdditionalReference3
from ._NetCashForecast3 import NetCashForecast3

class FundEstimatedCashForecastReportV04(base_types._BaseFieldType):

	__slots__ = ["_CnsltdNetCshFcst", "_FndOrSubFndDtls", "_MsgId", "_EstmtdFndCshFcstDtls", "_PrvsRef", "_PoolRef", "_RltdRef", "_MsgPgntn", "_Xtnsn"]
	@property
	def CnsltdNetCshFcst(self):
		return self._CnsltdNetCshFcst

	@CnsltdNetCshFcst.setter
	def CnsltdNetCshFcst(self, value):
		self._CnsltdNetCshFcst = value if type(value) != base_types.auto else self.make_default("CnsltdNetCshFcst")

	@CnsltdNetCshFcst.deleter
	def CnsltdNetCshFcst(self):
		del self._CnsltdNetCshFcst
		self._CnsltdNetCshFcst = None

	@property
	def EstmtdFndCshFcstDtls(self):
		return self._EstmtdFndCshFcstDtls

	@EstmtdFndCshFcstDtls.setter
	def EstmtdFndCshFcstDtls(self, value):
		self._EstmtdFndCshFcstDtls = value if type(value) != base_types.auto else self.make_default("EstmtdFndCshFcstDtls")

	@EstmtdFndCshFcstDtls.deleter
	def EstmtdFndCshFcstDtls(self):
		del self._EstmtdFndCshFcstDtls
		self._EstmtdFndCshFcstDtls = None

	@property
	def FndOrSubFndDtls(self):
		return self._FndOrSubFndDtls

	@FndOrSubFndDtls.setter
	def FndOrSubFndDtls(self, value):
		self._FndOrSubFndDtls = value if type(value) != base_types.auto else self.make_default("FndOrSubFndDtls")

	@FndOrSubFndDtls.deleter
	def FndOrSubFndDtls(self):
		del self._FndOrSubFndDtls
		self._FndOrSubFndDtls = None

	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if type(value) != base_types.auto else self.make_default("MsgId")

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = None

	@property
	def MsgPgntn(self):
		return self._MsgPgntn

	@MsgPgntn.setter
	def MsgPgntn(self, value):
		self._MsgPgntn = value if type(value) != base_types.auto else self.make_default("MsgPgntn")

	@MsgPgntn.deleter
	def MsgPgntn(self):
		del self._MsgPgntn
		self._MsgPgntn = None

	@property
	def PoolRef(self):
		return self._PoolRef

	@PoolRef.setter
	def PoolRef(self, value):
		self._PoolRef = value if type(value) != base_types.auto else self.make_default("PoolRef")

	@PoolRef.deleter
	def PoolRef(self):
		del self._PoolRef
		self._PoolRef = None

	@property
	def PrvsRef(self):
		return self._PrvsRef

	@PrvsRef.setter
	def PrvsRef(self, value):
		self._PrvsRef = value if type(value) != base_types.auto else self.make_default("PrvsRef")

	@PrvsRef.deleter
	def PrvsRef(self):
		del self._PrvsRef
		self._PrvsRef = None

	@property
	def RltdRef(self):
		return self._RltdRef

	@RltdRef.setter
	def RltdRef(self, value):
		self._RltdRef = value if type(value) != base_types.auto else self.make_default("RltdRef")

	@RltdRef.deleter
	def RltdRef(self):
		del self._RltdRef
		self._RltdRef = None

	@property
	def Xtnsn(self):
		return self._Xtnsn

	@Xtnsn.setter
	def Xtnsn(self, value):
		self._Xtnsn = value if type(value) != base_types.auto else self.make_default("Xtnsn")

	@Xtnsn.deleter
	def Xtnsn(self):
		del self._Xtnsn
		self._Xtnsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CnsltdNetCshFcst', type=NetCashForecast3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EstmtdFndCshFcstDtls', type=EstimatedFundCashForecast6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FndOrSubFndDtls', type=Fund1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgPgntn', type=Pagination, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PoolRef', type=AdditionalReference3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsRef', type=AdditionalReference3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RltdRef', type=AdditionalReference3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Xtnsn', type=Extension1, min=0, max=None, mutex_group=None, array=True),
	))

