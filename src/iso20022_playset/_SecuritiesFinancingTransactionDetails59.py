# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AmountAndDirection21 import AmountAndDirection21
from ._AmountAndDirection51 import AmountAndDirection51
from ._BlockChainAddressWallet3 import BlockChainAddressWallet3
from ._DateAndDateTime2Choice import DateAndDateTime2Choice
from ._DeliveryReceiptType2Code import DeliveryReceiptType2Code
from ._DigitalPaymentSettlement2 import DigitalPaymentSettlement2
from ._Max350Text import Max350Text
from ._Max35Text import Max35Text
from ._PartyIdentification144 import PartyIdentification144
from ._PartyIdentification149 import PartyIdentification149
from ._PlaceOfTradeIdentification1 import PlaceOfTradeIdentification1
from ._Quantity51Choice import Quantity51Choice
from ._Rate2 import Rate2
from ._RateName1 import RateName1
from ._RateOrName1Choice import RateOrName1Choice
from ._RateType35Choice import RateType35Choice
from ._ReceiveDelivery1Code import ReceiveDelivery1Code
from ._SafeKeepingPlace5 import SafeKeepingPlace5
from ._SecuritiesAccount19 import SecuritiesAccount19
from ._SecuritiesFinancingTransactionType2Code import SecuritiesFinancingTransactionType2Code
from ._SecurityIdentification19 import SecurityIdentification19
from ._SettlementDate19Choice import SettlementDate19Choice
from ._SettlementDetails227 import SettlementDetails227
from ._SettlementParties127 import SettlementParties127
from ._TerminationDate6Choice import TerminationDate6Choice
from ._TradeDate8Choice import TradeDate8Choice
from ._UTIIdentifier import UTIIdentifier

class SecuritiesFinancingTransactionDetails59(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnr", "_BlckChainAdrOrWllt", "_ClntTrptyCollTxId", "_ClsgLegId", "_CorpActnEvtId", "_DgtlPmtSttlm", "_DlvrgSttlmPties", "_FinInstrmId", "_Invstr", "_LateDlvryDt", "_OpngSttlmAmt", "_OpngSttlmDt", "_PlcOfTrad", "_Pmt", "_PoolId", "_PricgRate", "_RateChngDt", "_RateTp", "_RcvgSttlmPties", "_RpRate", "_SctiesFincgTradId", "_SctiesFincgTxTp", "_SctiesFincgUnqTxIdr", "_SctiesHrcut", "_SctiesMvmntTp", "_SfkpgAcct", "_SfkpgPlc", "_Sprd", "_StockLnMrgn", "_SttlmInstrPrcgAddtlDtls", "_SttlmParams", "_SttlmQty", "_TermntnDt", "_TermntnTxAmt", "_TradDt", "_TrptyAgtSvcPrvdrCollTxId", "_VarblRateSpprt", "_XpctdSttlmDt", "_XpctdValDt"]
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
	def ClsgLegId(self):
		return self._ClsgLegId

	@ClsgLegId.setter
	def ClsgLegId(self, value):
		self._ClsgLegId = value if type(value) != base_types.auto else self.make_default("ClsgLegId")

	@ClsgLegId.deleter
	def ClsgLegId(self):
		del self._ClsgLegId
		self._ClsgLegId = None

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
	def DgtlPmtSttlm(self):
		return self._DgtlPmtSttlm

	@DgtlPmtSttlm.setter
	def DgtlPmtSttlm(self, value):
		self._DgtlPmtSttlm = value if type(value) != base_types.auto else self.make_default("DgtlPmtSttlm")

	@DgtlPmtSttlm.deleter
	def DgtlPmtSttlm(self):
		del self._DgtlPmtSttlm
		self._DgtlPmtSttlm = None

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
	def OpngSttlmAmt(self):
		return self._OpngSttlmAmt

	@OpngSttlmAmt.setter
	def OpngSttlmAmt(self, value):
		self._OpngSttlmAmt = value if type(value) != base_types.auto else self.make_default("OpngSttlmAmt")

	@OpngSttlmAmt.deleter
	def OpngSttlmAmt(self):
		del self._OpngSttlmAmt
		self._OpngSttlmAmt = None

	@property
	def OpngSttlmDt(self):
		return self._OpngSttlmDt

	@OpngSttlmDt.setter
	def OpngSttlmDt(self, value):
		self._OpngSttlmDt = value if type(value) != base_types.auto else self.make_default("OpngSttlmDt")

	@OpngSttlmDt.deleter
	def OpngSttlmDt(self):
		del self._OpngSttlmDt
		self._OpngSttlmDt = None

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
	def PricgRate(self):
		return self._PricgRate

	@PricgRate.setter
	def PricgRate(self, value):
		self._PricgRate = value if type(value) != base_types.auto else self.make_default("PricgRate")

	@PricgRate.deleter
	def PricgRate(self):
		del self._PricgRate
		self._PricgRate = None

	@property
	def RateChngDt(self):
		return self._RateChngDt

	@RateChngDt.setter
	def RateChngDt(self, value):
		self._RateChngDt = value if type(value) != base_types.auto else self.make_default("RateChngDt")

	@RateChngDt.deleter
	def RateChngDt(self):
		del self._RateChngDt
		self._RateChngDt = None

	@property
	def RateTp(self):
		return self._RateTp

	@RateTp.setter
	def RateTp(self, value):
		self._RateTp = value if type(value) != base_types.auto else self.make_default("RateTp")

	@RateTp.deleter
	def RateTp(self):
		del self._RateTp
		self._RateTp = None

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
	def RpRate(self):
		return self._RpRate

	@RpRate.setter
	def RpRate(self, value):
		self._RpRate = value if type(value) != base_types.auto else self.make_default("RpRate")

	@RpRate.deleter
	def RpRate(self):
		del self._RpRate
		self._RpRate = None

	@property
	def SctiesFincgTradId(self):
		return self._SctiesFincgTradId

	@SctiesFincgTradId.setter
	def SctiesFincgTradId(self, value):
		self._SctiesFincgTradId = value if type(value) != base_types.auto else self.make_default("SctiesFincgTradId")

	@SctiesFincgTradId.deleter
	def SctiesFincgTradId(self):
		del self._SctiesFincgTradId
		self._SctiesFincgTradId = None

	@property
	def SctiesFincgTxTp(self):
		return self._SctiesFincgTxTp

	@SctiesFincgTxTp.setter
	def SctiesFincgTxTp(self, value):
		self._SctiesFincgTxTp = value if type(value) != base_types.auto else self.make_default("SctiesFincgTxTp")

	@SctiesFincgTxTp.deleter
	def SctiesFincgTxTp(self):
		del self._SctiesFincgTxTp
		self._SctiesFincgTxTp = None

	@property
	def SctiesFincgUnqTxIdr(self):
		return self._SctiesFincgUnqTxIdr

	@SctiesFincgUnqTxIdr.setter
	def SctiesFincgUnqTxIdr(self, value):
		self._SctiesFincgUnqTxIdr = value if type(value) != base_types.auto else self.make_default("SctiesFincgUnqTxIdr")

	@SctiesFincgUnqTxIdr.deleter
	def SctiesFincgUnqTxIdr(self):
		del self._SctiesFincgUnqTxIdr
		self._SctiesFincgUnqTxIdr = None

	@property
	def SctiesHrcut(self):
		return self._SctiesHrcut

	@SctiesHrcut.setter
	def SctiesHrcut(self, value):
		self._SctiesHrcut = value if type(value) != base_types.auto else self.make_default("SctiesHrcut")

	@SctiesHrcut.deleter
	def SctiesHrcut(self):
		del self._SctiesHrcut
		self._SctiesHrcut = None

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
	def Sprd(self):
		return self._Sprd

	@Sprd.setter
	def Sprd(self, value):
		self._Sprd = value if type(value) != base_types.auto else self.make_default("Sprd")

	@Sprd.deleter
	def Sprd(self):
		del self._Sprd
		self._Sprd = None

	@property
	def StockLnMrgn(self):
		return self._StockLnMrgn

	@StockLnMrgn.setter
	def StockLnMrgn(self, value):
		self._StockLnMrgn = value if type(value) != base_types.auto else self.make_default("StockLnMrgn")

	@StockLnMrgn.deleter
	def StockLnMrgn(self):
		del self._StockLnMrgn
		self._StockLnMrgn = None

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
	def TermntnDt(self):
		return self._TermntnDt

	@TermntnDt.setter
	def TermntnDt(self, value):
		self._TermntnDt = value if type(value) != base_types.auto else self.make_default("TermntnDt")

	@TermntnDt.deleter
	def TermntnDt(self):
		del self._TermntnDt
		self._TermntnDt = None

	@property
	def TermntnTxAmt(self):
		return self._TermntnTxAmt

	@TermntnTxAmt.setter
	def TermntnTxAmt(self, value):
		self._TermntnTxAmt = value if type(value) != base_types.auto else self.make_default("TermntnTxAmt")

	@TermntnTxAmt.deleter
	def TermntnTxAmt(self):
		del self._TermntnTxAmt
		self._TermntnTxAmt = None

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
	def VarblRateSpprt(self):
		return self._VarblRateSpprt

	@VarblRateSpprt.setter
	def VarblRateSpprt(self, value):
		self._VarblRateSpprt = value if type(value) != base_types.auto else self.make_default("VarblRateSpprt")

	@VarblRateSpprt.deleter
	def VarblRateSpprt(self):
		del self._VarblRateSpprt
		self._VarblRateSpprt = None

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
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=BlockChainAddressWallet3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntTrptyCollTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClsgLegId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnEvtId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DgtlPmtSttlm', type=DigitalPaymentSettlement2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvrgSttlmPties', type=SettlementParties127, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Invstr', type=PartyIdentification149, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LateDlvryDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OpngSttlmAmt', type=AmountAndDirection51, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OpngSttlmDt', type=SettlementDate19Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfTrad', type=PlaceOfTradeIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pmt', type=DeliveryReceiptType2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PoolId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricgRate', type=RateOrName1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateChngDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateTp', type=RateType35Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvgSttlmPties', type=SettlementParties127, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RpRate', type=Rate2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesFincgTradId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesFincgTxTp', type=SecuritiesFinancingTransactionType2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesFincgUnqTxIdr', type=UTIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesHrcut', type=Rate2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesMvmntTp', type=ReceiveDelivery1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgPlc', type=SafeKeepingPlace5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sprd', type=Rate2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StockLnMrgn', type=Rate2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmInstrPrcgAddtlDtls', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmParams', type=SettlementDetails227, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmQty', type=Quantity51Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TermntnDt', type=TerminationDate6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TermntnTxAmt', type=AmountAndDirection21, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDt', type=TradeDate8Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrptyAgtSvcPrvdrCollTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VarblRateSpprt', type=RateName1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpctdSttlmDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpctdValDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
	))