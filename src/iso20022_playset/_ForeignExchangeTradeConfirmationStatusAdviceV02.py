# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalReferences2
from . import Confirmation1
from . import Header23
from . import MessageIdentification1
from . import SupplementaryData1
from . import Trade8
from . import TradePartyIdentification10
from . import TradePartyIdentification9

class ForeignExchangeTradeConfirmationStatusAdviceV02(base_types._BaseFieldType):

	__slots__ = ["_AdvcId", "_ConfInf", "_CtrPtySdId", "_Hdr", "_Ref", "_SplmtryData", "_TradDtl", "_TradgSdId"]
	@property
	def AdvcId(self):
		return self._AdvcId

	@AdvcId.setter
	def AdvcId(self, value):
		self._AdvcId = value if value is not None else base_types.UninitialisedField(self, 'AdvcId', MessageIdentification1, False)

	@AdvcId.deleter
	def AdvcId(self):
		del self._AdvcId
		self._AdvcId = base_types.UninitialisedField(self, 'AdvcId', MessageIdentification1, False)

	@property
	def ConfInf(self):
		return self._ConfInf

	@ConfInf.setter
	def ConfInf(self, value):
		self._ConfInf = value if value is not None else base_types.UninitialisedField(self, 'ConfInf', Confirmation1, False)

	@ConfInf.deleter
	def ConfInf(self):
		del self._ConfInf
		self._ConfInf = base_types.UninitialisedField(self, 'ConfInf', Confirmation1, False)

	@property
	def CtrPtySdId(self):
		return self._CtrPtySdId

	@CtrPtySdId.setter
	def CtrPtySdId(self, value):
		self._CtrPtySdId = value if value is not None else base_types.UninitialisedField(self, 'CtrPtySdId', TradePartyIdentification10, False)

	@CtrPtySdId.deleter
	def CtrPtySdId(self):
		del self._CtrPtySdId
		self._CtrPtySdId = base_types.UninitialisedField(self, 'CtrPtySdId', TradePartyIdentification10, False)

	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if value is not None else base_types.UninitialisedField(self, 'Hdr', Header23, False)

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = base_types.UninitialisedField(self, 'Hdr', Header23, False)

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if value is not None else base_types.UninitialisedField(self, 'Ref', AdditionalReferences2, False)

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = base_types.UninitialisedField(self, 'Ref', AdditionalReferences2, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@property
	def TradDtl(self):
		return self._TradDtl

	@TradDtl.setter
	def TradDtl(self, value):
		self._TradDtl = value if value is not None else base_types.UninitialisedField(self, 'TradDtl', Trade8, False)

	@TradDtl.deleter
	def TradDtl(self):
		del self._TradDtl
		self._TradDtl = base_types.UninitialisedField(self, 'TradDtl', Trade8, False)

	@property
	def TradgSdId(self):
		return self._TradgSdId

	@TradgSdId.setter
	def TradgSdId(self, value):
		self._TradgSdId = value if value is not None else base_types.UninitialisedField(self, 'TradgSdId', TradePartyIdentification9, False)

	@TradgSdId.deleter
	def TradgSdId(self):
		del self._TradgSdId
		self._TradgSdId = base_types.UninitialisedField(self, 'TradgSdId', TradePartyIdentification9, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AdvcId', type=MessageIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConfInf', type=Confirmation1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtySdId', type=TradePartyIdentification10, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header23, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=AdditionalReferences2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TradDtl', type=Trade8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgSdId', type=TradePartyIdentification9, min=1, max=1, mutex_group=None, array=False),
	))