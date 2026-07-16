# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAnd13DecimalAmount
from . import ActiveCurrencyAndAmount
from . import ActiveCurrencyCode
from . import AgreedRate3
from . import DecimalNumber
from . import ISODate
from . import Max70Text
from . import SecurityIdentification18
from . import SettlementDate8Code
from . import TrueFalseIndicator

class Trade10(base_types._BaseFieldType):

	__slots__ = ["_AssoctdTradRef", "_ClctdCtrPtyCcyLastQty", "_DltaInd", "_ExctnPric", "_FwdPts", "_FxgCcy", "_FxgDt", "_LastQty", "_OptnInd", "_RskAmt", "_SctyId", "_SttlmDt", "_SttlmTp", "_ValDt", "_ValtnRate"]
	@property
	def AssoctdTradRef(self):
		return self._AssoctdTradRef

	@AssoctdTradRef.setter
	def AssoctdTradRef(self, value):
		self._AssoctdTradRef = value if value is not None else base_types.UninitialisedField(self, 'AssoctdTradRef', Max70Text, True)

	@AssoctdTradRef.deleter
	def AssoctdTradRef(self):
		del self._AssoctdTradRef
		self._AssoctdTradRef = base_types.UninitialisedField(self, 'AssoctdTradRef', Max70Text, True)

	@property
	def ClctdCtrPtyCcyLastQty(self):
		return self._ClctdCtrPtyCcyLastQty

	@ClctdCtrPtyCcyLastQty.setter
	def ClctdCtrPtyCcyLastQty(self, value):
		self._ClctdCtrPtyCcyLastQty = value if value is not None else base_types.UninitialisedField(self, 'ClctdCtrPtyCcyLastQty', ActiveCurrencyAndAmount, False)

	@ClctdCtrPtyCcyLastQty.deleter
	def ClctdCtrPtyCcyLastQty(self):
		del self._ClctdCtrPtyCcyLastQty
		self._ClctdCtrPtyCcyLastQty = base_types.UninitialisedField(self, 'ClctdCtrPtyCcyLastQty', ActiveCurrencyAndAmount, False)

	@property
	def DltaInd(self):
		return self._DltaInd

	@DltaInd.setter
	def DltaInd(self, value):
		self._DltaInd = value if value is not None else base_types.UninitialisedField(self, 'DltaInd', TrueFalseIndicator, False)

	@DltaInd.deleter
	def DltaInd(self):
		del self._DltaInd
		self._DltaInd = base_types.UninitialisedField(self, 'DltaInd', TrueFalseIndicator, False)

	@property
	def ExctnPric(self):
		return self._ExctnPric

	@ExctnPric.setter
	def ExctnPric(self, value):
		self._ExctnPric = value if value is not None else base_types.UninitialisedField(self, 'ExctnPric', ActiveCurrencyAnd13DecimalAmount, False)

	@ExctnPric.deleter
	def ExctnPric(self):
		del self._ExctnPric
		self._ExctnPric = base_types.UninitialisedField(self, 'ExctnPric', ActiveCurrencyAnd13DecimalAmount, False)

	@property
	def FwdPts(self):
		return self._FwdPts

	@FwdPts.setter
	def FwdPts(self, value):
		self._FwdPts = value if value is not None else base_types.UninitialisedField(self, 'FwdPts', DecimalNumber, False)

	@FwdPts.deleter
	def FwdPts(self):
		del self._FwdPts
		self._FwdPts = base_types.UninitialisedField(self, 'FwdPts', DecimalNumber, False)

	@property
	def FxgCcy(self):
		return self._FxgCcy

	@FxgCcy.setter
	def FxgCcy(self, value):
		self._FxgCcy = value if value is not None else base_types.UninitialisedField(self, 'FxgCcy', ActiveCurrencyCode, False)

	@FxgCcy.deleter
	def FxgCcy(self):
		del self._FxgCcy
		self._FxgCcy = base_types.UninitialisedField(self, 'FxgCcy', ActiveCurrencyCode, False)

	@property
	def FxgDt(self):
		return self._FxgDt

	@FxgDt.setter
	def FxgDt(self, value):
		self._FxgDt = value if value is not None else base_types.UninitialisedField(self, 'FxgDt', ISODate, False)

	@FxgDt.deleter
	def FxgDt(self):
		del self._FxgDt
		self._FxgDt = base_types.UninitialisedField(self, 'FxgDt', ISODate, False)

	@property
	def LastQty(self):
		return self._LastQty

	@LastQty.setter
	def LastQty(self, value):
		self._LastQty = value if value is not None else base_types.UninitialisedField(self, 'LastQty', ActiveCurrencyAndAmount, False)

	@LastQty.deleter
	def LastQty(self):
		del self._LastQty
		self._LastQty = base_types.UninitialisedField(self, 'LastQty', ActiveCurrencyAndAmount, False)

	@property
	def OptnInd(self):
		return self._OptnInd

	@OptnInd.setter
	def OptnInd(self, value):
		self._OptnInd = value if value is not None else base_types.UninitialisedField(self, 'OptnInd', TrueFalseIndicator, False)

	@OptnInd.deleter
	def OptnInd(self):
		del self._OptnInd
		self._OptnInd = base_types.UninitialisedField(self, 'OptnInd', TrueFalseIndicator, False)

	@property
	def RskAmt(self):
		return self._RskAmt

	@RskAmt.setter
	def RskAmt(self, value):
		self._RskAmt = value if value is not None else base_types.UninitialisedField(self, 'RskAmt', ActiveCurrencyAndAmount, False)

	@RskAmt.deleter
	def RskAmt(self):
		del self._RskAmt
		self._RskAmt = base_types.UninitialisedField(self, 'RskAmt', ActiveCurrencyAndAmount, False)

	@property
	def SctyId(self):
		return self._SctyId

	@SctyId.setter
	def SctyId(self, value):
		self._SctyId = value if value is not None else base_types.UninitialisedField(self, 'SctyId', SecurityIdentification18, False)

	@SctyId.deleter
	def SctyId(self):
		del self._SctyId
		self._SctyId = base_types.UninitialisedField(self, 'SctyId', SecurityIdentification18, False)

	@property
	def SttlmDt(self):
		return self._SttlmDt

	@SttlmDt.setter
	def SttlmDt(self, value):
		self._SttlmDt = value if value is not None else base_types.UninitialisedField(self, 'SttlmDt', ISODate, False)

	@SttlmDt.deleter
	def SttlmDt(self):
		del self._SttlmDt
		self._SttlmDt = base_types.UninitialisedField(self, 'SttlmDt', ISODate, False)

	@property
	def SttlmTp(self):
		return self._SttlmTp

	@SttlmTp.setter
	def SttlmTp(self, value):
		self._SttlmTp = value if value is not None else base_types.UninitialisedField(self, 'SttlmTp', SettlementDate8Code, False)

	@SttlmTp.deleter
	def SttlmTp(self):
		del self._SttlmTp
		self._SttlmTp = base_types.UninitialisedField(self, 'SttlmTp', SettlementDate8Code, False)

	@property
	def ValDt(self):
		return self._ValDt

	@ValDt.setter
	def ValDt(self, value):
		self._ValDt = value if value is not None else base_types.UninitialisedField(self, 'ValDt', ISODate, False)

	@ValDt.deleter
	def ValDt(self):
		del self._ValDt
		self._ValDt = base_types.UninitialisedField(self, 'ValDt', ISODate, False)

	@property
	def ValtnRate(self):
		return self._ValtnRate

	@ValtnRate.setter
	def ValtnRate(self, value):
		self._ValtnRate = value if value is not None else base_types.UninitialisedField(self, 'ValtnRate', AgreedRate3, False)

	@ValtnRate.deleter
	def ValtnRate(self):
		del self._ValtnRate
		self._ValtnRate = base_types.UninitialisedField(self, 'ValtnRate', AgreedRate3, False)

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