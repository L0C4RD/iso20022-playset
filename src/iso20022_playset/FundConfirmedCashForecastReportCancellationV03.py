import base_types
import FundConfirmedCashForecastReport3
import MessageIdentification1
import Pagination
import AdditionalReference3

class FundConfirmedCashForecastReportCancellationV03(base_types._BaseFieldType):

	__slots__ = ["_MsgId", "_CshFcstRptToBeCanc", "_PrvsRef", "_MsgPgntn", "_PoolRef", "_RltdRef"]
	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if type(value) != auto else self.make_default("MsgId")

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = None

	@property
	def CshFcstRptToBeCanc(self):
		return self._CshFcstRptToBeCanc

	@CshFcstRptToBeCanc.setter
	def CshFcstRptToBeCanc(self, value):
		self._CshFcstRptToBeCanc = value if type(value) != auto else self.make_default("CshFcstRptToBeCanc")

	@CshFcstRptToBeCanc.deleter
	def CshFcstRptToBeCanc(self):
		del self._CshFcstRptToBeCanc
		self._CshFcstRptToBeCanc = None

	@property
	def PrvsRef(self):
		return self._PrvsRef

	@PrvsRef.setter
	def PrvsRef(self, value):
		self._PrvsRef = value if type(value) != auto else self.make_default("PrvsRef")

	@PrvsRef.deleter
	def PrvsRef(self):
		del self._PrvsRef
		self._PrvsRef = None

	@property
	def MsgPgntn(self):
		return self._MsgPgntn

	@MsgPgntn.setter
	def MsgPgntn(self, value):
		self._MsgPgntn = value if type(value) != auto else self.make_default("MsgPgntn")

	@MsgPgntn.deleter
	def MsgPgntn(self):
		del self._MsgPgntn
		self._MsgPgntn = None

	@property
	def PoolRef(self):
		return self._PoolRef

	@PoolRef.setter
	def PoolRef(self, value):
		self._PoolRef = value if type(value) != auto else self.make_default("PoolRef")

	@PoolRef.deleter
	def PoolRef(self):
		del self._PoolRef
		self._PoolRef = None

	@property
	def RltdRef(self):
		return self._RltdRef

	@RltdRef.setter
	def RltdRef(self, value):
		self._RltdRef = value if type(value) != auto else self.make_default("RltdRef")

	@RltdRef.deleter
	def RltdRef(self):
		del self._RltdRef
		self._RltdRef = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshFcstRptToBeCanc', type=FundConfirmedCashForecastReport3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsRef', type=AdditionalReference3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgPgntn', type=Pagination, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PoolRef', type=AdditionalReference3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdRef', type=AdditionalReference3, min=0, max=None, mutex_group=None, array=True),
	))

