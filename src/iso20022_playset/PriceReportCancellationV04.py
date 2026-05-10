import base_types
import Extension1
import YesNoIndicator
import AdditionalReference3
import PriceReport3
import Max35Text
import Max350Text
import DateAndDateTime1Choice
import MessageIdentification1
import Pagination

class PriceReportCancellationV04(base_types._BaseFieldType):

	__slots__ = ["_MsgId", "_PrvsRef", "_MsgPgntn", "_PoolRef", "_Xtnsn", "_CmpltPricCxl", "_CxlId", "_CancPricValtnDtls", "_XpctdPricCrrctnDt", "_CxlRsn", "_PricRptId"]
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
	def CmpltPricCxl(self):
		return self._CmpltPricCxl

	@CmpltPricCxl.setter
	def CmpltPricCxl(self, value):
		self._CmpltPricCxl = value if type(value) != auto else self.make_default("CmpltPricCxl")

	@CmpltPricCxl.deleter
	def CmpltPricCxl(self):
		del self._CmpltPricCxl
		self._CmpltPricCxl = None

	@property
	def CxlId(self):
		return self._CxlId

	@CxlId.setter
	def CxlId(self, value):
		self._CxlId = value if type(value) != auto else self.make_default("CxlId")

	@CxlId.deleter
	def CxlId(self):
		del self._CxlId
		self._CxlId = None

	@property
	def CancPricValtnDtls(self):
		return self._CancPricValtnDtls

	@CancPricValtnDtls.setter
	def CancPricValtnDtls(self, value):
		self._CancPricValtnDtls = value if type(value) != auto else self.make_default("CancPricValtnDtls")

	@CancPricValtnDtls.deleter
	def CancPricValtnDtls(self):
		del self._CancPricValtnDtls
		self._CancPricValtnDtls = None

	@property
	def XpctdPricCrrctnDt(self):
		return self._XpctdPricCrrctnDt

	@XpctdPricCrrctnDt.setter
	def XpctdPricCrrctnDt(self, value):
		self._XpctdPricCrrctnDt = value if type(value) != auto else self.make_default("XpctdPricCrrctnDt")

	@XpctdPricCrrctnDt.deleter
	def XpctdPricCrrctnDt(self):
		del self._XpctdPricCrrctnDt
		self._XpctdPricCrrctnDt = None

	@property
	def CxlRsn(self):
		return self._CxlRsn

	@CxlRsn.setter
	def CxlRsn(self, value):
		self._CxlRsn = value if type(value) != auto else self.make_default("CxlRsn")

	@CxlRsn.deleter
	def CxlRsn(self):
		del self._CxlRsn
		self._CxlRsn = None

	@property
	def PricRptId(self):
		return self._PricRptId

	@PricRptId.setter
	def PricRptId(self, value):
		self._PricRptId = value if type(value) != auto else self.make_default("PricRptId")

	@PricRptId.deleter
	def PricRptId(self):
		del self._PricRptId
		self._PricRptId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsRef', type=AdditionalReference3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgPgntn', type=Pagination, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PoolRef', type=AdditionalReference3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Xtnsn', type=Extension1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CmpltPricCxl', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CancPricValtnDtls', type=PriceReport3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='XpctdPricCrrctnDt', type=DateAndDateTime1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlRsn', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricRptId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

