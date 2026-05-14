from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._CountryCode import CountryCode
from ._ExternalObligationSettlementMethod1Code import ExternalObligationSettlementMethod1Code
from ._Max10NumericText import Max10NumericText
from ._Max15NumericText import Max15NumericText
from ._Max35Text import Max35Text
from ._NettingIdentification2Choice import NettingIdentification2Choice
from ._PartyIdentification242Choice import PartyIdentification242Choice
from ._PaymentReceipt1Code import PaymentReceipt1Code
from ._SettlementParties120 import SettlementParties120
from ._SplitObligationAttributes1 import SplitObligationAttributes1
from ._TrueFalseIndicator import TrueFalseIndicator

class NetObligation4(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_CtrPtyNetgId", "_CtrPtySttlmInstrs", "_NetSvcCtrPtyId", "_OblgtnDrctn", "_OblgtnId", "_PmtClrCentr", "_PrvsSpltInd", "_PtcptNetgId", "_SpltInd", "_SpltOblgtnData", "_SttlmMtd", "_TtlNbOfSplts", "_TxsNb"]
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
	def OblgtnId(self):
		return self._OblgtnId

	@OblgtnId.setter
	def OblgtnId(self, value):
		self._OblgtnId = value if type(value) != base_types.auto else self.make_default("OblgtnId")

	@OblgtnId.deleter
	def OblgtnId(self):
		del self._OblgtnId
		self._OblgtnId = None

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
	def PrvsSpltInd(self):
		return self._PrvsSpltInd

	@PrvsSpltInd.setter
	def PrvsSpltInd(self, value):
		self._PrvsSpltInd = value if type(value) != base_types.auto else self.make_default("PrvsSpltInd")

	@PrvsSpltInd.deleter
	def PrvsSpltInd(self):
		del self._PrvsSpltInd
		self._PrvsSpltInd = None

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
	def SpltInd(self):
		return self._SpltInd

	@SpltInd.setter
	def SpltInd(self, value):
		self._SpltInd = value if type(value) != base_types.auto else self.make_default("SpltInd")

	@SpltInd.deleter
	def SpltInd(self):
		del self._SpltInd
		self._SpltInd = None

	@property
	def SpltOblgtnData(self):
		return self._SpltOblgtnData

	@SpltOblgtnData.setter
	def SpltOblgtnData(self, value):
		self._SpltOblgtnData = value if type(value) != base_types.auto else self.make_default("SpltOblgtnData")

	@SpltOblgtnData.deleter
	def SpltOblgtnData(self):
		del self._SpltOblgtnData
		self._SpltOblgtnData = None

	@property
	def SttlmMtd(self):
		return self._SttlmMtd

	@SttlmMtd.setter
	def SttlmMtd(self, value):
		self._SttlmMtd = value if type(value) != base_types.auto else self.make_default("SttlmMtd")

	@SttlmMtd.deleter
	def SttlmMtd(self):
		del self._SttlmMtd
		self._SttlmMtd = None

	@property
	def TtlNbOfSplts(self):
		return self._TtlNbOfSplts

	@TtlNbOfSplts.setter
	def TtlNbOfSplts(self, value):
		self._TtlNbOfSplts = value if type(value) != base_types.auto else self.make_default("TtlNbOfSplts")

	@TtlNbOfSplts.deleter
	def TtlNbOfSplts(self):
		del self._TtlNbOfSplts
		self._TtlNbOfSplts = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyNetgId', type=NettingIdentification2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtySttlmInstrs', type=SettlementParties120, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetSvcCtrPtyId', type=PartyIdentification242Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OblgtnDrctn', type=PaymentReceipt1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OblgtnId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtClrCentr', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsSpltInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtcptNetgId', type=NettingIdentification2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpltInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpltOblgtnData', type=SplitObligationAttributes1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmMtd', type=ExternalObligationSettlementMethod1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNbOfSplts', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxsNb', type=Max10NumericText, min=0, max=1, mutex_group=None, array=False),
	))

