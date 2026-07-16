# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalReference3
from . import DateAndDateTime1Choice
from . import Extension1
from . import Max350Text
from . import Max35Text
from . import MessageIdentification1
from . import Pagination
from . import PriceReport3
from . import YesNoIndicator

class PriceReportCancellationV04(base_types._BaseFieldType):

	__slots__ = ["_CancPricValtnDtls", "_CmpltPricCxl", "_CxlId", "_CxlRsn", "_MsgId", "_MsgPgntn", "_PoolRef", "_PricRptId", "_PrvsRef", "_XpctdPricCrrctnDt", "_Xtnsn"]
	@property
	def CancPricValtnDtls(self):
		return self._CancPricValtnDtls

	@CancPricValtnDtls.setter
	def CancPricValtnDtls(self, value):
		self._CancPricValtnDtls = value if value is not None else base_types.UninitialisedField(self, 'CancPricValtnDtls', PriceReport3, True)

	@CancPricValtnDtls.deleter
	def CancPricValtnDtls(self):
		del self._CancPricValtnDtls
		self._CancPricValtnDtls = base_types.UninitialisedField(self, 'CancPricValtnDtls', PriceReport3, True)

	@property
	def CmpltPricCxl(self):
		return self._CmpltPricCxl

	@CmpltPricCxl.setter
	def CmpltPricCxl(self, value):
		self._CmpltPricCxl = value if value is not None else base_types.UninitialisedField(self, 'CmpltPricCxl', YesNoIndicator, False)

	@CmpltPricCxl.deleter
	def CmpltPricCxl(self):
		del self._CmpltPricCxl
		self._CmpltPricCxl = base_types.UninitialisedField(self, 'CmpltPricCxl', YesNoIndicator, False)

	@property
	def CxlId(self):
		return self._CxlId

	@CxlId.setter
	def CxlId(self, value):
		self._CxlId = value if value is not None else base_types.UninitialisedField(self, 'CxlId', Max35Text, False)

	@CxlId.deleter
	def CxlId(self):
		del self._CxlId
		self._CxlId = base_types.UninitialisedField(self, 'CxlId', Max35Text, False)

	@property
	def CxlRsn(self):
		return self._CxlRsn

	@CxlRsn.setter
	def CxlRsn(self, value):
		self._CxlRsn = value if value is not None else base_types.UninitialisedField(self, 'CxlRsn', Max350Text, False)

	@CxlRsn.deleter
	def CxlRsn(self):
		del self._CxlRsn
		self._CxlRsn = base_types.UninitialisedField(self, 'CxlRsn', Max350Text, False)

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
	def PricRptId(self):
		return self._PricRptId

	@PricRptId.setter
	def PricRptId(self, value):
		self._PricRptId = value if value is not None else base_types.UninitialisedField(self, 'PricRptId', Max35Text, False)

	@PricRptId.deleter
	def PricRptId(self):
		del self._PricRptId
		self._PricRptId = base_types.UninitialisedField(self, 'PricRptId', Max35Text, False)

	@property
	def PrvsRef(self):
		return self._PrvsRef

	@PrvsRef.setter
	def PrvsRef(self, value):
		self._PrvsRef = value if value is not None else base_types.UninitialisedField(self, 'PrvsRef', AdditionalReference3, False)

	@PrvsRef.deleter
	def PrvsRef(self):
		del self._PrvsRef
		self._PrvsRef = base_types.UninitialisedField(self, 'PrvsRef', AdditionalReference3, False)

	@property
	def XpctdPricCrrctnDt(self):
		return self._XpctdPricCrrctnDt

	@XpctdPricCrrctnDt.setter
	def XpctdPricCrrctnDt(self, value):
		self._XpctdPricCrrctnDt = value if value is not None else base_types.UninitialisedField(self, 'XpctdPricCrrctnDt', DateAndDateTime1Choice, False)

	@XpctdPricCrrctnDt.deleter
	def XpctdPricCrrctnDt(self):
		del self._XpctdPricCrrctnDt
		self._XpctdPricCrrctnDt = base_types.UninitialisedField(self, 'XpctdPricCrrctnDt', DateAndDateTime1Choice, False)

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
		base_types.FieldEntry(name='CancPricValtnDtls', type=PriceReport3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CmpltPricCxl', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlRsn', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgPgntn', type=Pagination, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PoolRef', type=AdditionalReference3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricRptId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsRef', type=AdditionalReference3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpctdPricCrrctnDt', type=DateAndDateTime1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Xtnsn', type=Extension1, min=0, max=None, mutex_group=None, array=True),
	))