# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import CountryCode
from . import Max10NumericText
from . import Max35Text
from . import NettingIdentification2Choice
from . import PartyIdentification242Choice
from . import PaymentReceipt1Code
from . import SettlementParties120

class NetObligation3(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_CtrPtyNetgId", "_CtrPtySttlmInstrs", "_NetSvcCtrPtyId", "_OblgtnDrctn", "_OblgtnId", "_PmtClrCentr", "_PtcptNetgId", "_TxsNb"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@property
	def CtrPtyNetgId(self):
		return self._CtrPtyNetgId

	@CtrPtyNetgId.setter
	def CtrPtyNetgId(self, value):
		self._CtrPtyNetgId = value if value is not None else base_types.UninitialisedField(self, 'CtrPtyNetgId', NettingIdentification2Choice, False)

	@CtrPtyNetgId.deleter
	def CtrPtyNetgId(self):
		del self._CtrPtyNetgId
		self._CtrPtyNetgId = base_types.UninitialisedField(self, 'CtrPtyNetgId', NettingIdentification2Choice, False)

	@property
	def CtrPtySttlmInstrs(self):
		return self._CtrPtySttlmInstrs

	@CtrPtySttlmInstrs.setter
	def CtrPtySttlmInstrs(self, value):
		self._CtrPtySttlmInstrs = value if value is not None else base_types.UninitialisedField(self, 'CtrPtySttlmInstrs', SettlementParties120, False)

	@CtrPtySttlmInstrs.deleter
	def CtrPtySttlmInstrs(self):
		del self._CtrPtySttlmInstrs
		self._CtrPtySttlmInstrs = base_types.UninitialisedField(self, 'CtrPtySttlmInstrs', SettlementParties120, False)

	@property
	def NetSvcCtrPtyId(self):
		return self._NetSvcCtrPtyId

	@NetSvcCtrPtyId.setter
	def NetSvcCtrPtyId(self, value):
		self._NetSvcCtrPtyId = value if value is not None else base_types.UninitialisedField(self, 'NetSvcCtrPtyId', PartyIdentification242Choice, False)

	@NetSvcCtrPtyId.deleter
	def NetSvcCtrPtyId(self):
		del self._NetSvcCtrPtyId
		self._NetSvcCtrPtyId = base_types.UninitialisedField(self, 'NetSvcCtrPtyId', PartyIdentification242Choice, False)

	@property
	def OblgtnDrctn(self):
		return self._OblgtnDrctn

	@OblgtnDrctn.setter
	def OblgtnDrctn(self, value):
		self._OblgtnDrctn = value if value is not None else base_types.UninitialisedField(self, 'OblgtnDrctn', PaymentReceipt1Code, False)

	@OblgtnDrctn.deleter
	def OblgtnDrctn(self):
		del self._OblgtnDrctn
		self._OblgtnDrctn = base_types.UninitialisedField(self, 'OblgtnDrctn', PaymentReceipt1Code, False)

	@property
	def OblgtnId(self):
		return self._OblgtnId

	@OblgtnId.setter
	def OblgtnId(self, value):
		self._OblgtnId = value if value is not None else base_types.UninitialisedField(self, 'OblgtnId', Max35Text, False)

	@OblgtnId.deleter
	def OblgtnId(self):
		del self._OblgtnId
		self._OblgtnId = base_types.UninitialisedField(self, 'OblgtnId', Max35Text, False)

	@property
	def PmtClrCentr(self):
		return self._PmtClrCentr

	@PmtClrCentr.setter
	def PmtClrCentr(self, value):
		self._PmtClrCentr = value if value is not None else base_types.UninitialisedField(self, 'PmtClrCentr', CountryCode, False)

	@PmtClrCentr.deleter
	def PmtClrCentr(self):
		del self._PmtClrCentr
		self._PmtClrCentr = base_types.UninitialisedField(self, 'PmtClrCentr', CountryCode, False)

	@property
	def PtcptNetgId(self):
		return self._PtcptNetgId

	@PtcptNetgId.setter
	def PtcptNetgId(self, value):
		self._PtcptNetgId = value if value is not None else base_types.UninitialisedField(self, 'PtcptNetgId', NettingIdentification2Choice, False)

	@PtcptNetgId.deleter
	def PtcptNetgId(self):
		del self._PtcptNetgId
		self._PtcptNetgId = base_types.UninitialisedField(self, 'PtcptNetgId', NettingIdentification2Choice, False)

	@property
	def TxsNb(self):
		return self._TxsNb

	@TxsNb.setter
	def TxsNb(self, value):
		self._TxsNb = value if value is not None else base_types.UninitialisedField(self, 'TxsNb', Max10NumericText, False)

	@TxsNb.deleter
	def TxsNb(self):
		del self._TxsNb
		self._TxsNb = base_types.UninitialisedField(self, 'TxsNb', Max10NumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyNetgId', type=NettingIdentification2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtySttlmInstrs', type=SettlementParties120, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetSvcCtrPtyId', type=PartyIdentification242Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OblgtnDrctn', type=PaymentReceipt1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OblgtnId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtClrCentr', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtcptNetgId', type=NettingIdentification2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxsNb', type=Max10NumericText, min=0, max=1, mutex_group=None, array=False),
	))