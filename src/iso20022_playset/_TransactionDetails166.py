from . import base_types
from ._AmountAndDirection51 import AmountAndDirection51
from ._BlockChainAddressWallet3 import BlockChainAddressWallet3
from ._DateAndDateTime2Choice import DateAndDateTime2Choice
from ._DeliveryReceiptType2Code import DeliveryReceiptType2Code
from ._ISODateTime import ISODateTime
from ._Max350Text import Max350Text
from ._Max35Text import Max35Text
from ._PartyIdentification136 import PartyIdentification136
from ._PartyIdentification144 import PartyIdentification144
from ._PartyIdentification149 import PartyIdentification149
from ._PlaceOfClearingIdentification2 import PlaceOfClearingIdentification2
from ._PlaceOfTradeIdentification1 import PlaceOfTradeIdentification1
from ._Quantity51Choice import Quantity51Choice
from ._ReceiveDelivery1Code import ReceiveDelivery1Code
from ._SafeKeepingPlace5 import SafeKeepingPlace5
from ._SecuritiesAccount19 import SecuritiesAccount19
from ._SecurityIdentification19 import SecurityIdentification19
from ._SettlementDate19Choice import SettlementDate19Choice
from ._SettlementDetails216 import SettlementDetails216
from ._SettlementParties125 import SettlementParties125
from ._TradeDate8Choice import TradeDate8Choice
from ._UTIIdentifier import UTIIdentifier

class TransactionDetails166(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnr", "_AckdStsTmStmp", "_BlckChainAdrOrWllt", "_ClntCollInstrId", "_ClntTrptyCollTxId", "_CorpActnEvtId", "_DlvrgSttlmPties", "_FinInstrmId", "_Invstr", "_LateDlvryDt", "_MtchdStsTmStmp", "_NonceId", "_PlcOfClr", "_PlcOfTrad", "_Pmt", "_PoolId", "_PrtlyRlsdQty", "_QlfdFrgnIntrmy", "_RcvgSttlmPties", "_SctiesMvmntTp", "_SfkpgAcct", "_SfkpgPlc", "_SttlmAmt", "_SttlmDt", "_SttlmInstrPrcgAddtlDtls", "_SttlmParams", "_SttlmQty", "_TradDt", "_TradId", "_TrptyAgtSvcPrvdrCollInstrId", "_TrptyAgtSvcPrvdrCollTxId", "_UnqTxIdr", "_XpctdSttlmDt", "_XpctdValDt"]
	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if type(value) != base_types.auto else self.make_default("AcctOwnr")

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = None

	@property
	def AckdStsTmStmp(self):
		return self._AckdStsTmStmp

	@AckdStsTmStmp.setter
	def AckdStsTmStmp(self, value):
		self._AckdStsTmStmp = value if type(value) != base_types.auto else self.make_default("AckdStsTmStmp")

	@AckdStsTmStmp.deleter
	def AckdStsTmStmp(self):
		del self._AckdStsTmStmp
		self._AckdStsTmStmp = None

	@property
	def BlckChainAdrOrWllt(self):
		return self._BlckChainAdrOrWllt

	@BlckChainAdrOrWllt.setter
	def BlckChainAdrOrWllt(self, value):
		self._BlckChainAdrOrWllt = value if type(value) != base_types.auto else self.make_default("BlckChainAdrOrWllt")

	@BlckChainAdrOrWllt.deleter
	def BlckChainAdrOrWllt(self):
		del self._BlckChainAdrOrWllt
		self._BlckChainAdrOrWllt = None

	@property
	def ClntCollInstrId(self):
		return self._ClntCollInstrId

	@ClntCollInstrId.setter
	def ClntCollInstrId(self, value):
		self._ClntCollInstrId = value if type(value) != base_types.auto else self.make_default("ClntCollInstrId")

	@ClntCollInstrId.deleter
	def ClntCollInstrId(self):
		del self._ClntCollInstrId
		self._ClntCollInstrId = None

	@property
	def ClntTrptyCollTxId(self):
		return self._ClntTrptyCollTxId

	@ClntTrptyCollTxId.setter
	def ClntTrptyCollTxId(self, value):
		self._ClntTrptyCollTxId = value if type(value) != base_types.auto else self.make_default("ClntTrptyCollTxId")

	@ClntTrptyCollTxId.deleter
	def ClntTrptyCollTxId(self):
		del self._ClntTrptyCollTxId
		self._ClntTrptyCollTxId = None

	@property
	def CorpActnEvtId(self):
		return self._CorpActnEvtId

	@CorpActnEvtId.setter
	def CorpActnEvtId(self, value):
		self._CorpActnEvtId = value if type(value) != base_types.auto else self.make_default("CorpActnEvtId")

	@CorpActnEvtId.deleter
	def CorpActnEvtId(self):
		del self._CorpActnEvtId
		self._CorpActnEvtId = None

	@property
	def DlvrgSttlmPties(self):
		return self._DlvrgSttlmPties

	@DlvrgSttlmPties.setter
	def DlvrgSttlmPties(self, value):
		self._DlvrgSttlmPties = value if type(value) != base_types.auto else self.make_default("DlvrgSttlmPties")

	@DlvrgSttlmPties.deleter
	def DlvrgSttlmPties(self):
		del self._DlvrgSttlmPties
		self._DlvrgSttlmPties = None

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if type(value) != base_types.auto else self.make_default("FinInstrmId")

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = None

	@property
	def Invstr(self):
		return self._Invstr

	@Invstr.setter
	def Invstr(self, value):
		self._Invstr = value if type(value) != base_types.auto else self.make_default("Invstr")

	@Invstr.deleter
	def Invstr(self):
		del self._Invstr
		self._Invstr = None

	@property
	def LateDlvryDt(self):
		return self._LateDlvryDt

	@LateDlvryDt.setter
	def LateDlvryDt(self, value):
		self._LateDlvryDt = value if type(value) != base_types.auto else self.make_default("LateDlvryDt")

	@LateDlvryDt.deleter
	def LateDlvryDt(self):
		del self._LateDlvryDt
		self._LateDlvryDt = None

	@property
	def MtchdStsTmStmp(self):
		return self._MtchdStsTmStmp

	@MtchdStsTmStmp.setter
	def MtchdStsTmStmp(self, value):
		self._MtchdStsTmStmp = value if type(value) != base_types.auto else self.make_default("MtchdStsTmStmp")

	@MtchdStsTmStmp.deleter
	def MtchdStsTmStmp(self):
		del self._MtchdStsTmStmp
		self._MtchdStsTmStmp = None

	@property
	def NonceId(self):
		return self._NonceId

	@NonceId.setter
	def NonceId(self, value):
		self._NonceId = value if type(value) != base_types.auto else self.make_default("NonceId")

	@NonceId.deleter
	def NonceId(self):
		del self._NonceId
		self._NonceId = None

	@property
	def PlcOfClr(self):
		return self._PlcOfClr

	@PlcOfClr.setter
	def PlcOfClr(self, value):
		self._PlcOfClr = value if type(value) != base_types.auto else self.make_default("PlcOfClr")

	@PlcOfClr.deleter
	def PlcOfClr(self):
		del self._PlcOfClr
		self._PlcOfClr = None

	@property
	def PlcOfTrad(self):
		return self._PlcOfTrad

	@PlcOfTrad.setter
	def PlcOfTrad(self, value):
		self._PlcOfTrad = value if type(value) != base_types.auto else self.make_default("PlcOfTrad")

	@PlcOfTrad.deleter
	def PlcOfTrad(self):
		del self._PlcOfTrad
		self._PlcOfTrad = None

	@property
	def Pmt(self):
		return self._Pmt

	@Pmt.setter
	def Pmt(self, value):
		self._Pmt = value if type(value) != base_types.auto else self.make_default("Pmt")

	@Pmt.deleter
	def Pmt(self):
		del self._Pmt
		self._Pmt = None

	@property
	def PoolId(self):
		return self._PoolId

	@PoolId.setter
	def PoolId(self, value):
		self._PoolId = value if type(value) != base_types.auto else self.make_default("PoolId")

	@PoolId.deleter
	def PoolId(self):
		del self._PoolId
		self._PoolId = None

	@property
	def PrtlyRlsdQty(self):
		return self._PrtlyRlsdQty

	@PrtlyRlsdQty.setter
	def PrtlyRlsdQty(self, value):
		self._PrtlyRlsdQty = value if type(value) != base_types.auto else self.make_default("PrtlyRlsdQty")

	@PrtlyRlsdQty.deleter
	def PrtlyRlsdQty(self):
		del self._PrtlyRlsdQty
		self._PrtlyRlsdQty = None

	@property
	def QlfdFrgnIntrmy(self):
		return self._QlfdFrgnIntrmy

	@QlfdFrgnIntrmy.setter
	def QlfdFrgnIntrmy(self, value):
		self._QlfdFrgnIntrmy = value if type(value) != base_types.auto else self.make_default("QlfdFrgnIntrmy")

	@QlfdFrgnIntrmy.deleter
	def QlfdFrgnIntrmy(self):
		del self._QlfdFrgnIntrmy
		self._QlfdFrgnIntrmy = None

	@property
	def RcvgSttlmPties(self):
		return self._RcvgSttlmPties

	@RcvgSttlmPties.setter
	def RcvgSttlmPties(self, value):
		self._RcvgSttlmPties = value if type(value) != base_types.auto else self.make_default("RcvgSttlmPties")

	@RcvgSttlmPties.deleter
	def RcvgSttlmPties(self):
		del self._RcvgSttlmPties
		self._RcvgSttlmPties = None

	@property
	def SctiesMvmntTp(self):
		return self._SctiesMvmntTp

	@SctiesMvmntTp.setter
	def SctiesMvmntTp(self, value):
		self._SctiesMvmntTp = value if type(value) != base_types.auto else self.make_default("SctiesMvmntTp")

	@SctiesMvmntTp.deleter
	def SctiesMvmntTp(self):
		del self._SctiesMvmntTp
		self._SctiesMvmntTp = None

	@property
	def SfkpgAcct(self):
		return self._SfkpgAcct

	@SfkpgAcct.setter
	def SfkpgAcct(self, value):
		self._SfkpgAcct = value if type(value) != base_types.auto else self.make_default("SfkpgAcct")

	@SfkpgAcct.deleter
	def SfkpgAcct(self):
		del self._SfkpgAcct
		self._SfkpgAcct = None

	@property
	def SfkpgPlc(self):
		return self._SfkpgPlc

	@SfkpgPlc.setter
	def SfkpgPlc(self, value):
		self._SfkpgPlc = value if type(value) != base_types.auto else self.make_default("SfkpgPlc")

	@SfkpgPlc.deleter
	def SfkpgPlc(self):
		del self._SfkpgPlc
		self._SfkpgPlc = None

	@property
	def SttlmAmt(self):
		return self._SttlmAmt

	@SttlmAmt.setter
	def SttlmAmt(self, value):
		self._SttlmAmt = value if type(value) != base_types.auto else self.make_default("SttlmAmt")

	@SttlmAmt.deleter
	def SttlmAmt(self):
		del self._SttlmAmt
		self._SttlmAmt = None

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
	def SttlmInstrPrcgAddtlDtls(self):
		return self._SttlmInstrPrcgAddtlDtls

	@SttlmInstrPrcgAddtlDtls.setter
	def SttlmInstrPrcgAddtlDtls(self, value):
		self._SttlmInstrPrcgAddtlDtls = value if type(value) != base_types.auto else self.make_default("SttlmInstrPrcgAddtlDtls")

	@SttlmInstrPrcgAddtlDtls.deleter
	def SttlmInstrPrcgAddtlDtls(self):
		del self._SttlmInstrPrcgAddtlDtls
		self._SttlmInstrPrcgAddtlDtls = None

	@property
	def SttlmParams(self):
		return self._SttlmParams

	@SttlmParams.setter
	def SttlmParams(self, value):
		self._SttlmParams = value if type(value) != base_types.auto else self.make_default("SttlmParams")

	@SttlmParams.deleter
	def SttlmParams(self):
		del self._SttlmParams
		self._SttlmParams = None

	@property
	def SttlmQty(self):
		return self._SttlmQty

	@SttlmQty.setter
	def SttlmQty(self, value):
		self._SttlmQty = value if type(value) != base_types.auto else self.make_default("SttlmQty")

	@SttlmQty.deleter
	def SttlmQty(self):
		del self._SttlmQty
		self._SttlmQty = None

	@property
	def TradDt(self):
		return self._TradDt

	@TradDt.setter
	def TradDt(self, value):
		self._TradDt = value if type(value) != base_types.auto else self.make_default("TradDt")

	@TradDt.deleter
	def TradDt(self):
		del self._TradDt
		self._TradDt = None

	@property
	def TradId(self):
		return self._TradId

	@TradId.setter
	def TradId(self, value):
		self._TradId = value if type(value) != base_types.auto else self.make_default("TradId")

	@TradId.deleter
	def TradId(self):
		del self._TradId
		self._TradId = None

	@property
	def TrptyAgtSvcPrvdrCollInstrId(self):
		return self._TrptyAgtSvcPrvdrCollInstrId

	@TrptyAgtSvcPrvdrCollInstrId.setter
	def TrptyAgtSvcPrvdrCollInstrId(self, value):
		self._TrptyAgtSvcPrvdrCollInstrId = value if type(value) != base_types.auto else self.make_default("TrptyAgtSvcPrvdrCollInstrId")

	@TrptyAgtSvcPrvdrCollInstrId.deleter
	def TrptyAgtSvcPrvdrCollInstrId(self):
		del self._TrptyAgtSvcPrvdrCollInstrId
		self._TrptyAgtSvcPrvdrCollInstrId = None

	@property
	def TrptyAgtSvcPrvdrCollTxId(self):
		return self._TrptyAgtSvcPrvdrCollTxId

	@TrptyAgtSvcPrvdrCollTxId.setter
	def TrptyAgtSvcPrvdrCollTxId(self, value):
		self._TrptyAgtSvcPrvdrCollTxId = value if type(value) != base_types.auto else self.make_default("TrptyAgtSvcPrvdrCollTxId")

	@TrptyAgtSvcPrvdrCollTxId.deleter
	def TrptyAgtSvcPrvdrCollTxId(self):
		del self._TrptyAgtSvcPrvdrCollTxId
		self._TrptyAgtSvcPrvdrCollTxId = None

	@property
	def UnqTxIdr(self):
		return self._UnqTxIdr

	@UnqTxIdr.setter
	def UnqTxIdr(self, value):
		self._UnqTxIdr = value if type(value) != base_types.auto else self.make_default("UnqTxIdr")

	@UnqTxIdr.deleter
	def UnqTxIdr(self):
		del self._UnqTxIdr
		self._UnqTxIdr = None

	@property
	def XpctdSttlmDt(self):
		return self._XpctdSttlmDt

	@XpctdSttlmDt.setter
	def XpctdSttlmDt(self, value):
		self._XpctdSttlmDt = value if type(value) != base_types.auto else self.make_default("XpctdSttlmDt")

	@XpctdSttlmDt.deleter
	def XpctdSttlmDt(self):
		del self._XpctdSttlmDt
		self._XpctdSttlmDt = None

	@property
	def XpctdValDt(self):
		return self._XpctdValDt

	@XpctdValDt.setter
	def XpctdValDt(self, value):
		self._XpctdValDt = value if type(value) != base_types.auto else self.make_default("XpctdValDt")

	@XpctdValDt.deleter
	def XpctdValDt(self):
		del self._XpctdValDt
		self._XpctdValDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification144, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AckdStsTmStmp', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=BlockChainAddressWallet3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntCollInstrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntTrptyCollTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnEvtId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvrgSttlmPties', type=SettlementParties125, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Invstr', type=PartyIdentification149, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LateDlvryDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtchdStsTmStmp', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonceId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfClr', type=PlaceOfClearingIdentification2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfTrad', type=PlaceOfTradeIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pmt', type=DeliveryReceiptType2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PoolId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtlyRlsdQty', type=Quantity51Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QlfdFrgnIntrmy', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvgSttlmPties', type=SettlementParties125, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesMvmntTp', type=ReceiveDelivery1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgPlc', type=SafeKeepingPlace5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAmt', type=AmountAndDirection51, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmDt', type=SettlementDate19Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmInstrPrcgAddtlDtls', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmParams', type=SettlementDetails216, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmQty', type=Quantity51Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDt', type=TradeDate8Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrptyAgtSvcPrvdrCollInstrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrptyAgtSvcPrvdrCollTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnqTxIdr', type=UTIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpctdSttlmDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpctdValDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
	))

