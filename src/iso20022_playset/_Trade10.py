from . import base_types
from ._ActiveCurrencyAnd13DecimalAmount import ActiveCurrencyAnd13DecimalAmount
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._ActiveCurrencyCode import ActiveCurrencyCode
from ._AgreedRate3 import AgreedRate3
from ._DecimalNumber import DecimalNumber
from ._ISODate import ISODate
from ._Max70Text import Max70Text
from ._SecurityIdentification18 import SecurityIdentification18
from ._SettlementDate8Code import SettlementDate8Code
from ._TrueFalseIndicator import TrueFalseIndicator

class Trade10(base_types._BaseFieldType):

	__slots__ = ["_AssoctdTradRef", "_ClctdCtrPtyCcyLastQty", "_DltaInd", "_ExctnPric", "_FwdPts", "_FxgCcy", "_FxgDt", "_LastQty", "_OptnInd", "_RskAmt", "_SctyId", "_SttlmDt", "_SttlmTp", "_ValDt", "_ValtnRate"]
	@property
	def AssoctdTradRef(self):
		return self._AssoctdTradRef

	@AssoctdTradRef.setter
	def AssoctdTradRef(self, value):
		self._AssoctdTradRef = value if type(value) != base_types.auto else self.make_default("AssoctdTradRef")

	@AssoctdTradRef.deleter
	def AssoctdTradRef(self):
		del self._AssoctdTradRef
		self._AssoctdTradRef = None

	@property
	def ClctdCtrPtyCcyLastQty(self):
		return self._ClctdCtrPtyCcyLastQty

	@ClctdCtrPtyCcyLastQty.setter
	def ClctdCtrPtyCcyLastQty(self, value):
		self._ClctdCtrPtyCcyLastQty = value if type(value) != base_types.auto else self.make_default("ClctdCtrPtyCcyLastQty")

	@ClctdCtrPtyCcyLastQty.deleter
	def ClctdCtrPtyCcyLastQty(self):
		del self._ClctdCtrPtyCcyLastQty
		self._ClctdCtrPtyCcyLastQty = None

	@property
	def DltaInd(self):
		return self._DltaInd

	@DltaInd.setter
	def DltaInd(self, value):
		self._DltaInd = value if type(value) != base_types.auto else self.make_default("DltaInd")

	@DltaInd.deleter
	def DltaInd(self):
		del self._DltaInd
		self._DltaInd = None

	@property
	def ExctnPric(self):
		return self._ExctnPric

	@ExctnPric.setter
	def ExctnPric(self, value):
		self._ExctnPric = value if type(value) != base_types.auto else self.make_default("ExctnPric")

	@ExctnPric.deleter
	def ExctnPric(self):
		del self._ExctnPric
		self._ExctnPric = None

	@property
	def FwdPts(self):
		return self._FwdPts

	@FwdPts.setter
	def FwdPts(self, value):
		self._FwdPts = value if type(value) != base_types.auto else self.make_default("FwdPts")

	@FwdPts.deleter
	def FwdPts(self):
		del self._FwdPts
		self._FwdPts = None

	@property
	def FxgCcy(self):
		return self._FxgCcy

	@FxgCcy.setter
	def FxgCcy(self, value):
		self._FxgCcy = value if type(value) != base_types.auto else self.make_default("FxgCcy")

	@FxgCcy.deleter
	def FxgCcy(self):
		del self._FxgCcy
		self._FxgCcy = None

	@property
	def FxgDt(self):
		return self._FxgDt

	@FxgDt.setter
	def FxgDt(self, value):
		self._FxgDt = value if type(value) != base_types.auto else self.make_default("FxgDt")

	@FxgDt.deleter
	def FxgDt(self):
		del self._FxgDt
		self._FxgDt = None

	@property
	def LastQty(self):
		return self._LastQty

	@LastQty.setter
	def LastQty(self, value):
		self._LastQty = value if type(value) != base_types.auto else self.make_default("LastQty")

	@LastQty.deleter
	def LastQty(self):
		del self._LastQty
		self._LastQty = None

	@property
	def OptnInd(self):
		return self._OptnInd

	@OptnInd.setter
	def OptnInd(self, value):
		self._OptnInd = value if type(value) != base_types.auto else self.make_default("OptnInd")

	@OptnInd.deleter
	def OptnInd(self):
		del self._OptnInd
		self._OptnInd = None

	@property
	def RskAmt(self):
		return self._RskAmt

	@RskAmt.setter
	def RskAmt(self, value):
		self._RskAmt = value if type(value) != base_types.auto else self.make_default("RskAmt")

	@RskAmt.deleter
	def RskAmt(self):
		del self._RskAmt
		self._RskAmt = None

	@property
	def SctyId(self):
		return self._SctyId

	@SctyId.setter
	def SctyId(self, value):
		self._SctyId = value if type(value) != base_types.auto else self.make_default("SctyId")

	@SctyId.deleter
	def SctyId(self):
		del self._SctyId
		self._SctyId = None

	@property
	def SttlmDt(self):
		return self._SttlmDt

	@SttlmDt.setter
	def SttlmDt(self, value):
		self._SttlmDt = value if type(value) != base_types.auto else self.make_default("SttlmDt")

	@SttlmDt.deleter
	def SttlmDt(self):
		del self._SttlmDt
		self._SttlmDt = None

	@property
	def SttlmTp(self):
		return self._SttlmTp

	@SttlmTp.setter
	def SttlmTp(self, value):
		self._SttlmTp = value if type(value) != base_types.auto else self.make_default("SttlmTp")

	@SttlmTp.deleter
	def SttlmTp(self):
		del self._SttlmTp
		self._SttlmTp = None

	@property
	def ValDt(self):
		return self._ValDt

	@ValDt.setter
	def ValDt(self, value):
		self._ValDt = value if type(value) != base_types.auto else self.make_default("ValDt")

	@ValDt.deleter
	def ValDt(self):
		del self._ValDt
		self._ValDt = None

	@property
	def ValtnRate(self):
		return self._ValtnRate

	@ValtnRate.setter
	def ValtnRate(self, value):
		self._ValtnRate = value if type(value) != base_types.auto else self.make_default("ValtnRate")

	@ValtnRate.deleter
	def ValtnRate(self):
		del self._ValtnRate
		self._ValtnRate = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AssoctdTradRef', type=Max70Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ClctdCtrPtyCcyLastQty', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DltaInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExctnPric', type=ActiveCurrencyAnd13DecimalAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FwdPts', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FxgCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FxgDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LastQty', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RskAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyId', type=SecurityIdentification18, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmTp', type=SettlementDate8Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnRate', type=AgreedRate3, min=1, max=1, mutex_group=None, array=False),
	))

