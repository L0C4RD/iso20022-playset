# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATICALaxProcessing
from . import Exact14NumericText
from . import Exact1AlphaText
from . import Exact1Text
from . import Exact20Binary
from . import Exact2NumericText
from . import Exact3AlphaNumericText
from . import ISO3NumericCurrencyCode
from . import ISO8583ShippingIndicatorCode
from . import Max10KText
from . import Max10Text
from . import Max16Binary
from . import Max35Text
from . import Max36Text
from . import Max37Text
from . import Max40Text
from . import Max45Text
from . import Max48Text
from . import Max50Text
from . import Max64Text
from . import Min5Max8Text
from . import TrueFalseIndicator

class CardAuthenticationData1(base_types._BaseFieldType):

	__slots__ = ["_AccptrCertSrlNb", "_AcctBasedDgtlSgntr", "_AdrMtchInd", "_ApplIPAdr", "_AuthntcnCd", "_AuthntcnMrchntNm", "_AuthntcnSts", "_AuthntcnSvrTxIdr", "_AuthntcnVal", "_BrwsrIPAdr", "_CrdhldrCertSrlNb", "_DataQlty", "_DvcId", "_DvcIdVlctyCnt", "_DvcInf", "_DvcTp", "_IPAdrVlctyCnt", "_IntrmyTxIdr", "_MsgCtgy", "_MsgVrsn", "_NtlData", "_Prgrmm", "_PrvtData", "_PurchsAmt", "_PurchsCcy", "_PurchsDtTm", "_RcrngTxSetp", "_SDKApplId", "_ShppgInd", "_SsnId", "_ThrdPtyId", "_ThrdPtyRskScore", "_XID"]
	@property
	def AccptrCertSrlNb(self):
		return self._AccptrCertSrlNb

	@AccptrCertSrlNb.setter
	def AccptrCertSrlNb(self, value):
		self._AccptrCertSrlNb = value if value is not None else base_types.UninitialisedField(self, 'AccptrCertSrlNb', Max16Binary, False)

	@AccptrCertSrlNb.deleter
	def AccptrCertSrlNb(self):
		del self._AccptrCertSrlNb
		self._AccptrCertSrlNb = base_types.UninitialisedField(self, 'AccptrCertSrlNb', Max16Binary, False)

	@property
	def AcctBasedDgtlSgntr(self):
		return self._AcctBasedDgtlSgntr

	@AcctBasedDgtlSgntr.setter
	def AcctBasedDgtlSgntr(self, value):
		self._AcctBasedDgtlSgntr = value if value is not None else base_types.UninitialisedField(self, 'AcctBasedDgtlSgntr', Exact2NumericText, False)

	@AcctBasedDgtlSgntr.deleter
	def AcctBasedDgtlSgntr(self):
		del self._AcctBasedDgtlSgntr
		self._AcctBasedDgtlSgntr = base_types.UninitialisedField(self, 'AcctBasedDgtlSgntr', Exact2NumericText, False)

	@property
	def AdrMtchInd(self):
		return self._AdrMtchInd

	@AdrMtchInd.setter
	def AdrMtchInd(self, value):
		self._AdrMtchInd = value if value is not None else base_types.UninitialisedField(self, 'AdrMtchInd', Exact1Text, False)

	@AdrMtchInd.deleter
	def AdrMtchInd(self):
		del self._AdrMtchInd
		self._AdrMtchInd = base_types.UninitialisedField(self, 'AdrMtchInd', Exact1Text, False)

	@property
	def ApplIPAdr(self):
		return self._ApplIPAdr

	@ApplIPAdr.setter
	def ApplIPAdr(self, value):
		self._ApplIPAdr = value if value is not None else base_types.UninitialisedField(self, 'ApplIPAdr', Max45Text, False)

	@ApplIPAdr.deleter
	def ApplIPAdr(self):
		del self._ApplIPAdr
		self._ApplIPAdr = base_types.UninitialisedField(self, 'ApplIPAdr', Max45Text, False)

	@property
	def AuthntcnCd(self):
		return self._AuthntcnCd

	@AuthntcnCd.setter
	def AuthntcnCd(self, value):
		self._AuthntcnCd = value if value is not None else base_types.UninitialisedField(self, 'AuthntcnCd', Max50Text, False)

	@AuthntcnCd.deleter
	def AuthntcnCd(self):
		del self._AuthntcnCd
		self._AuthntcnCd = base_types.UninitialisedField(self, 'AuthntcnCd', Max50Text, False)

	@property
	def AuthntcnMrchntNm(self):
		return self._AuthntcnMrchntNm

	@AuthntcnMrchntNm.setter
	def AuthntcnMrchntNm(self, value):
		self._AuthntcnMrchntNm = value if value is not None else base_types.UninitialisedField(self, 'AuthntcnMrchntNm', Max40Text, False)

	@AuthntcnMrchntNm.deleter
	def AuthntcnMrchntNm(self):
		del self._AuthntcnMrchntNm
		self._AuthntcnMrchntNm = base_types.UninitialisedField(self, 'AuthntcnMrchntNm', Max40Text, False)

	@property
	def AuthntcnSts(self):
		return self._AuthntcnSts

	@AuthntcnSts.setter
	def AuthntcnSts(self, value):
		self._AuthntcnSts = value if value is not None else base_types.UninitialisedField(self, 'AuthntcnSts', Exact1AlphaText, False)

	@AuthntcnSts.deleter
	def AuthntcnSts(self):
		del self._AuthntcnSts
		self._AuthntcnSts = base_types.UninitialisedField(self, 'AuthntcnSts', Exact1AlphaText, False)

	@property
	def AuthntcnSvrTxIdr(self):
		return self._AuthntcnSvrTxIdr

	@AuthntcnSvrTxIdr.setter
	def AuthntcnSvrTxIdr(self, value):
		self._AuthntcnSvrTxIdr = value if value is not None else base_types.UninitialisedField(self, 'AuthntcnSvrTxIdr', Max36Text, False)

	@AuthntcnSvrTxIdr.deleter
	def AuthntcnSvrTxIdr(self):
		del self._AuthntcnSvrTxIdr
		self._AuthntcnSvrTxIdr = base_types.UninitialisedField(self, 'AuthntcnSvrTxIdr', Max36Text, False)

	@property
	def AuthntcnVal(self):
		return self._AuthntcnVal

	@AuthntcnVal.setter
	def AuthntcnVal(self, value):
		self._AuthntcnVal = value if value is not None else base_types.UninitialisedField(self, 'AuthntcnVal', Exact20Binary, False)

	@AuthntcnVal.deleter
	def AuthntcnVal(self):
		del self._AuthntcnVal
		self._AuthntcnVal = base_types.UninitialisedField(self, 'AuthntcnVal', Exact20Binary, False)

	@property
	def BrwsrIPAdr(self):
		return self._BrwsrIPAdr

	@BrwsrIPAdr.setter
	def BrwsrIPAdr(self, value):
		self._BrwsrIPAdr = value if value is not None else base_types.UninitialisedField(self, 'BrwsrIPAdr', Max45Text, False)

	@BrwsrIPAdr.deleter
	def BrwsrIPAdr(self):
		del self._BrwsrIPAdr
		self._BrwsrIPAdr = base_types.UninitialisedField(self, 'BrwsrIPAdr', Max45Text, False)

	@property
	def CrdhldrCertSrlNb(self):
		return self._CrdhldrCertSrlNb

	@CrdhldrCertSrlNb.setter
	def CrdhldrCertSrlNb(self, value):
		self._CrdhldrCertSrlNb = value if value is not None else base_types.UninitialisedField(self, 'CrdhldrCertSrlNb', Max16Binary, False)

	@CrdhldrCertSrlNb.deleter
	def CrdhldrCertSrlNb(self):
		del self._CrdhldrCertSrlNb
		self._CrdhldrCertSrlNb = base_types.UninitialisedField(self, 'CrdhldrCertSrlNb', Max16Binary, False)

	@property
	def DataQlty(self):
		return self._DataQlty

	@DataQlty.setter
	def DataQlty(self, value):
		self._DataQlty = value if value is not None else base_types.UninitialisedField(self, 'DataQlty', TrueFalseIndicator, False)

	@DataQlty.deleter
	def DataQlty(self):
		del self._DataQlty
		self._DataQlty = base_types.UninitialisedField(self, 'DataQlty', TrueFalseIndicator, False)

	@property
	def DvcId(self):
		return self._DvcId

	@DvcId.setter
	def DvcId(self, value):
		self._DvcId = value if value is not None else base_types.UninitialisedField(self, 'DvcId', Max64Text, True)

	@DvcId.deleter
	def DvcId(self):
		del self._DvcId
		self._DvcId = base_types.UninitialisedField(self, 'DvcId', Max64Text, True)

	@property
	def DvcIdVlctyCnt(self):
		return self._DvcIdVlctyCnt

	@DvcIdVlctyCnt.setter
	def DvcIdVlctyCnt(self, value):
		self._DvcIdVlctyCnt = value if value is not None else base_types.UninitialisedField(self, 'DvcIdVlctyCnt', Exact2NumericText, False)

	@DvcIdVlctyCnt.deleter
	def DvcIdVlctyCnt(self):
		del self._DvcIdVlctyCnt
		self._DvcIdVlctyCnt = base_types.UninitialisedField(self, 'DvcIdVlctyCnt', Exact2NumericText, False)

	@property
	def DvcInf(self):
		return self._DvcInf

	@DvcInf.setter
	def DvcInf(self, value):
		self._DvcInf = value if value is not None else base_types.UninitialisedField(self, 'DvcInf', Max10KText, False)

	@DvcInf.deleter
	def DvcInf(self):
		del self._DvcInf
		self._DvcInf = base_types.UninitialisedField(self, 'DvcInf', Max10KText, False)

	@property
	def DvcTp(self):
		return self._DvcTp

	@DvcTp.setter
	def DvcTp(self, value):
		self._DvcTp = value if value is not None else base_types.UninitialisedField(self, 'DvcTp', Exact2NumericText, True)

	@DvcTp.deleter
	def DvcTp(self):
		del self._DvcTp
		self._DvcTp = base_types.UninitialisedField(self, 'DvcTp', Exact2NumericText, True)

	@property
	def IPAdrVlctyCnt(self):
		return self._IPAdrVlctyCnt

	@IPAdrVlctyCnt.setter
	def IPAdrVlctyCnt(self, value):
		self._IPAdrVlctyCnt = value if value is not None else base_types.UninitialisedField(self, 'IPAdrVlctyCnt', Exact2NumericText, False)

	@IPAdrVlctyCnt.deleter
	def IPAdrVlctyCnt(self):
		del self._IPAdrVlctyCnt
		self._IPAdrVlctyCnt = base_types.UninitialisedField(self, 'IPAdrVlctyCnt', Exact2NumericText, False)

	@property
	def IntrmyTxIdr(self):
		return self._IntrmyTxIdr

	@IntrmyTxIdr.setter
	def IntrmyTxIdr(self, value):
		self._IntrmyTxIdr = value if value is not None else base_types.UninitialisedField(self, 'IntrmyTxIdr', Max36Text, False)

	@IntrmyTxIdr.deleter
	def IntrmyTxIdr(self):
		del self._IntrmyTxIdr
		self._IntrmyTxIdr = base_types.UninitialisedField(self, 'IntrmyTxIdr', Max36Text, False)

	@property
	def MsgCtgy(self):
		return self._MsgCtgy

	@MsgCtgy.setter
	def MsgCtgy(self, value):
		self._MsgCtgy = value if value is not None else base_types.UninitialisedField(self, 'MsgCtgy', Exact2NumericText, False)

	@MsgCtgy.deleter
	def MsgCtgy(self):
		del self._MsgCtgy
		self._MsgCtgy = base_types.UninitialisedField(self, 'MsgCtgy', Exact2NumericText, False)

	@property
	def MsgVrsn(self):
		return self._MsgVrsn

	@MsgVrsn.setter
	def MsgVrsn(self, value):
		self._MsgVrsn = value if value is not None else base_types.UninitialisedField(self, 'MsgVrsn', Min5Max8Text, False)

	@MsgVrsn.deleter
	def MsgVrsn(self):
		del self._MsgVrsn
		self._MsgVrsn = base_types.UninitialisedField(self, 'MsgVrsn', Min5Max8Text, False)

	@property
	def NtlData(self):
		return self._NtlData

	@NtlData.setter
	def NtlData(self, value):
		self._NtlData = value if value is not None else base_types.UninitialisedField(self, 'NtlData', ATICALaxProcessing, True)

	@NtlData.deleter
	def NtlData(self):
		del self._NtlData
		self._NtlData = base_types.UninitialisedField(self, 'NtlData', ATICALaxProcessing, True)

	@property
	def Prgrmm(self):
		return self._Prgrmm

	@Prgrmm.setter
	def Prgrmm(self, value):
		self._Prgrmm = value if value is not None else base_types.UninitialisedField(self, 'Prgrmm', Max10Text, False)

	@Prgrmm.deleter
	def Prgrmm(self):
		del self._Prgrmm
		self._Prgrmm = base_types.UninitialisedField(self, 'Prgrmm', Max10Text, False)

	@property
	def PrvtData(self):
		return self._PrvtData

	@PrvtData.setter
	def PrvtData(self, value):
		self._PrvtData = value if value is not None else base_types.UninitialisedField(self, 'PrvtData', ATICALaxProcessing, True)

	@PrvtData.deleter
	def PrvtData(self):
		del self._PrvtData
		self._PrvtData = base_types.UninitialisedField(self, 'PrvtData', ATICALaxProcessing, True)

	@property
	def PurchsAmt(self):
		return self._PurchsAmt

	@PurchsAmt.setter
	def PurchsAmt(self, value):
		self._PurchsAmt = value if value is not None else base_types.UninitialisedField(self, 'PurchsAmt', Max48Text, False)

	@PurchsAmt.deleter
	def PurchsAmt(self):
		del self._PurchsAmt
		self._PurchsAmt = base_types.UninitialisedField(self, 'PurchsAmt', Max48Text, False)

	@property
	def PurchsCcy(self):
		return self._PurchsCcy

	@PurchsCcy.setter
	def PurchsCcy(self, value):
		self._PurchsCcy = value if value is not None else base_types.UninitialisedField(self, 'PurchsCcy', ISO3NumericCurrencyCode, False)

	@PurchsCcy.deleter
	def PurchsCcy(self):
		del self._PurchsCcy
		self._PurchsCcy = base_types.UninitialisedField(self, 'PurchsCcy', ISO3NumericCurrencyCode, False)

	@property
	def PurchsDtTm(self):
		return self._PurchsDtTm

	@PurchsDtTm.setter
	def PurchsDtTm(self, value):
		self._PurchsDtTm = value if value is not None else base_types.UninitialisedField(self, 'PurchsDtTm', Exact14NumericText, False)

	@PurchsDtTm.deleter
	def PurchsDtTm(self):
		del self._PurchsDtTm
		self._PurchsDtTm = base_types.UninitialisedField(self, 'PurchsDtTm', Exact14NumericText, False)

	@property
	def RcrngTxSetp(self):
		return self._RcrngTxSetp

	@RcrngTxSetp.setter
	def RcrngTxSetp(self, value):
		self._RcrngTxSetp = value if value is not None else base_types.UninitialisedField(self, 'RcrngTxSetp', Exact3AlphaNumericText, False)

	@RcrngTxSetp.deleter
	def RcrngTxSetp(self):
		del self._RcrngTxSetp
		self._RcrngTxSetp = base_types.UninitialisedField(self, 'RcrngTxSetp', Exact3AlphaNumericText, False)

	@property
	def SDKApplId(self):
		return self._SDKApplId

	@SDKApplId.setter
	def SDKApplId(self, value):
		self._SDKApplId = value if value is not None else base_types.UninitialisedField(self, 'SDKApplId', Max37Text, False)

	@SDKApplId.deleter
	def SDKApplId(self):
		del self._SDKApplId
		self._SDKApplId = base_types.UninitialisedField(self, 'SDKApplId', Max37Text, False)

	@property
	def ShppgInd(self):
		return self._ShppgInd

	@ShppgInd.setter
	def ShppgInd(self, value):
		self._ShppgInd = value if value is not None else base_types.UninitialisedField(self, 'ShppgInd', ISO8583ShippingIndicatorCode, False)

	@ShppgInd.deleter
	def ShppgInd(self):
		del self._ShppgInd
		self._ShppgInd = base_types.UninitialisedField(self, 'ShppgInd', ISO8583ShippingIndicatorCode, False)

	@property
	def SsnId(self):
		return self._SsnId

	@SsnId.setter
	def SsnId(self, value):
		self._SsnId = value if value is not None else base_types.UninitialisedField(self, 'SsnId', Max35Text, False)

	@SsnId.deleter
	def SsnId(self):
		del self._SsnId
		self._SsnId = base_types.UninitialisedField(self, 'SsnId', Max35Text, False)

	@property
	def ThrdPtyId(self):
		return self._ThrdPtyId

	@ThrdPtyId.setter
	def ThrdPtyId(self, value):
		self._ThrdPtyId = value if value is not None else base_types.UninitialisedField(self, 'ThrdPtyId', Max64Text, False)

	@ThrdPtyId.deleter
	def ThrdPtyId(self):
		del self._ThrdPtyId
		self._ThrdPtyId = base_types.UninitialisedField(self, 'ThrdPtyId', Max64Text, False)

	@property
	def ThrdPtyRskScore(self):
		return self._ThrdPtyRskScore

	@ThrdPtyRskScore.setter
	def ThrdPtyRskScore(self, value):
		self._ThrdPtyRskScore = value if value is not None else base_types.UninitialisedField(self, 'ThrdPtyRskScore', Exact2NumericText, False)

	@ThrdPtyRskScore.deleter
	def ThrdPtyRskScore(self):
		del self._ThrdPtyRskScore
		self._ThrdPtyRskScore = base_types.UninitialisedField(self, 'ThrdPtyRskScore', Exact2NumericText, False)

	@property
	def XID(self):
		return self._XID

	@XID.setter
	def XID(self, value):
		self._XID = value if value is not None else base_types.UninitialisedField(self, 'XID', Exact20Binary, False)

	@XID.deleter
	def XID(self):
		del self._XID
		self._XID = base_types.UninitialisedField(self, 'XID', Exact20Binary, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AccptrCertSrlNb', type=Max16Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctBasedDgtlSgntr', type=Exact2NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AdrMtchInd', type=Exact1Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ApplIPAdr', type=Max45Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthntcnCd', type=Max50Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthntcnMrchntNm', type=Max40Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthntcnSts', type=Exact1AlphaText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthntcnSvrTxIdr', type=Max36Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthntcnVal', type=Exact20Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BrwsrIPAdr', type=Max45Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrdhldrCertSrlNb', type=Max16Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DataQlty', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DvcId', type=Max64Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DvcIdVlctyCnt', type=Exact2NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DvcInf', type=Max10KText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DvcTp', type=Exact2NumericText, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IPAdrVlctyCnt', type=Exact2NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyTxIdr', type=Max36Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgCtgy', type=Exact2NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgVrsn', type=Min5Max8Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtlData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Prgrmm', type=Max10Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvtData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PurchsAmt', type=Max48Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PurchsCcy', type=ISO3NumericCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PurchsDtTm', type=Exact14NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcrngTxSetp', type=Exact3AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SDKApplId', type=Max37Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShppgInd', type=ISO8583ShippingIndicatorCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SsnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ThrdPtyId', type=Max64Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ThrdPtyRskScore', type=Exact2NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XID', type=Exact20Binary, min=0, max=1, mutex_group=None, array=False),
	))