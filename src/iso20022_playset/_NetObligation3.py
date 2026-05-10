from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._Max10NumericText import Max10NumericText
from ._SettlementParties120 import SettlementParties120
from ._NettingIdentification2Choice import NettingIdentification2Choice
from ._PaymentReceipt1Code import PaymentReceipt1Code
from ._PartyIdentification242Choice import PartyIdentification242Choice
from ._CountryCode import CountryCode
from ._Max35Text import Max35Text

class NetObligation3(base_types._BaseFieldType):

	__slots__ = ["_TxsNb", "_PmtClrCentr", "_OblgtnDrctn", "_Amt", "_CtrPtySttlmInstrs", "_PtcptNetgId", "_NetSvcCtrPtyId", "_CtrPtyNetgId", "_OblgtnId"]
	@property
	def TxsNb(self):
		return self._TxsNb

	@TxsNb.setter
	def TxsNb(self, value):
		self._TxsNb = value if type(value) != base_types.auto else self.make_default("TxsNb")

	@TxsNb.deleter
	def TxsNb(self):
		del self._TxsNb
		self._TxsNb = None

	@property
	def PmtClrCentr(self):
		return self._PmtClrCentr

	@PmtClrCentr.setter
	def PmtClrCentr(self, value):
		self._PmtClrCentr = value if type(value) != base_types.auto else self.make_default("PmtClrCentr")

	@PmtClrCentr.deleter
	def PmtClrCentr(self):
		del self._PmtClrCentr
		self._PmtClrCentr = None

	@property
	def OblgtnDrctn(self):
		return self._OblgtnDrctn

	@OblgtnDrctn.setter
	def OblgtnDrctn(self, value):
		self._OblgtnDrctn = value if type(value) != base_types.auto else self.make_default("OblgtnDrctn")

	@OblgtnDrctn.deleter
	def OblgtnDrctn(self):
		del self._OblgtnDrctn
		self._OblgtnDrctn = None

	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != base_types.auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def CtrPtySttlmInstrs(self):
		return self._CtrPtySttlmInstrs

	@CtrPtySttlmInstrs.setter
	def CtrPtySttlmInstrs(self, value):
		self._CtrPtySttlmInstrs = value if type(value) != base_types.auto else self.make_default("CtrPtySttlmInstrs")

	@CtrPtySttlmInstrs.deleter
	def CtrPtySttlmInstrs(self):
		del self._CtrPtySttlmInstrs
		self._CtrPtySttlmInstrs = None

	@property
	def PtcptNetgId(self):
		return self._PtcptNetgId

	@PtcptNetgId.setter
	def PtcptNetgId(self, value):
		self._PtcptNetgId = value if type(value) != base_types.auto else self.make_default("PtcptNetgId")

	@PtcptNetgId.deleter
	def PtcptNetgId(self):
		del self._PtcptNetgId
		self._PtcptNetgId = None

	@property
	def NetSvcCtrPtyId(self):
		return self._NetSvcCtrPtyId

	@NetSvcCtrPtyId.setter
	def NetSvcCtrPtyId(self, value):
		self._NetSvcCtrPtyId = value if type(value) != base_types.auto else self.make_default("NetSvcCtrPtyId")

	@NetSvcCtrPtyId.deleter
	def NetSvcCtrPtyId(self):
		del self._NetSvcCtrPtyId
		self._NetSvcCtrPtyId = None

	@property
	def CtrPtyNetgId(self):
		return self._CtrPtyNetgId

	@CtrPtyNetgId.setter
	def CtrPtyNetgId(self, value):
		self._CtrPtyNetgId = value if type(value) != base_types.auto else self.make_default("CtrPtyNetgId")

	@CtrPtyNetgId.deleter
	def CtrPtyNetgId(self):
		del self._CtrPtyNetgId
		self._CtrPtyNetgId = None

	@property
	def OblgtnId(self):
		return self._OblgtnId

	@OblgtnId.setter
	def OblgtnId(self, value):
		self._OblgtnId = value if type(value) != base_types.auto else self.make_default("OblgtnId")

	@OblgtnId.deleter
	def OblgtnId(self):
		del self._OblgtnId
		self._OblgtnId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TxsNb', type=Max10NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtClrCentr', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OblgtnDrctn', type=PaymentReceipt1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtySttlmInstrs', type=SettlementParties120, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtcptNetgId', type=NettingIdentification2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetSvcCtrPtyId', type=PartyIdentification242Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyNetgId', type=NettingIdentification2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OblgtnId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

