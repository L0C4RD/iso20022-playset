# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ATICALaxProcessing import ATICALaxProcessing
from ._Exact14NumericText import Exact14NumericText
from ._Exact1AlphaText import Exact1AlphaText
from ._Exact1Text import Exact1Text
from ._Exact20Binary import Exact20Binary
from ._Exact2NumericText import Exact2NumericText
from ._Exact3AlphaNumericText import Exact3AlphaNumericText
from ._ISO3NumericCurrencyCode import ISO3NumericCurrencyCode
from ._ISO8583ShippingIndicatorCode import ISO8583ShippingIndicatorCode
from ._Max10KText import Max10KText
from ._Max10Text import Max10Text
from ._Max16Binary import Max16Binary
from ._Max35Text import Max35Text
from ._Max36Text import Max36Text
from ._Max37Text import Max37Text
from ._Max40Text import Max40Text
from ._Max45Text import Max45Text
from ._Max48Text import Max48Text
from ._Max50Text import Max50Text
from ._Max64Text import Max64Text
from ._Min5Max8Text import Min5Max8Text
from ._TrueFalseIndicator import TrueFalseIndicator

class CardAuthenticationData1(base_types._BaseFieldType):

	__slots__ = ["_AccptrCertSrlNb", "_AcctBasedDgtlSgntr", "_AdrMtchInd", "_ApplIPAdr", "_AuthntcnCd", "_AuthntcnMrchntNm", "_AuthntcnSts", "_AuthntcnSvrTxIdr", "_AuthntcnVal", "_BrwsrIPAdr", "_CrdhldrCertSrlNb", "_DataQlty", "_DvcId", "_DvcIdVlctyCnt", "_DvcInf", "_DvcTp", "_IPAdrVlctyCnt", "_IntrmyTxIdr", "_MsgCtgy", "_MsgVrsn", "_NtlData", "_Prgrmm", "_PrvtData", "_PurchsAmt", "_PurchsCcy", "_PurchsDtTm", "_RcrngTxSetp", "_SDKApplId", "_ShppgInd", "_SsnId", "_ThrdPtyId", "_ThrdPtyRskScore", "_XID"]
	@property
	def AccptrCertSrlNb(self):
		return self._AccptrCertSrlNb

	@AccptrCertSrlNb.setter
	def AccptrCertSrlNb(self, value):
		self._AccptrCertSrlNb = value if type(value) != base_types.auto else self.make_default("AccptrCertSrlNb")

	@AccptrCertSrlNb.deleter
	def AccptrCertSrlNb(self):
		del self._AccptrCertSrlNb
		self._AccptrCertSrlNb = None

	@property
	def AcctBasedDgtlSgntr(self):
		return self._AcctBasedDgtlSgntr

	@AcctBasedDgtlSgntr.setter
	def AcctBasedDgtlSgntr(self, value):
		self._AcctBasedDgtlSgntr = value if type(value) != base_types.auto else self.make_default("AcctBasedDgtlSgntr")

	@AcctBasedDgtlSgntr.deleter
	def AcctBasedDgtlSgntr(self):
		del self._AcctBasedDgtlSgntr
		self._AcctBasedDgtlSgntr = None

	@property
	def AdrMtchInd(self):
		return self._AdrMtchInd

	@AdrMtchInd.setter
	def AdrMtchInd(self, value):
		self._AdrMtchInd = value if type(value) != base_types.auto else self.make_default("AdrMtchInd")

	@AdrMtchInd.deleter
	def AdrMtchInd(self):
		del self._AdrMtchInd
		self._AdrMtchInd = None

	@property
	def ApplIPAdr(self):
		return self._ApplIPAdr

	@ApplIPAdr.setter
	def ApplIPAdr(self, value):
		self._ApplIPAdr = value if type(value) != base_types.auto else self.make_default("ApplIPAdr")

	@ApplIPAdr.deleter
	def ApplIPAdr(self):
		del self._ApplIPAdr
		self._ApplIPAdr = None

	@property
	def AuthntcnCd(self):
		return self._AuthntcnCd

	@AuthntcnCd.setter
	def AuthntcnCd(self, value):
		self._AuthntcnCd = value if type(value) != base_types.auto else self.make_default("AuthntcnCd")

	@AuthntcnCd.deleter
	def AuthntcnCd(self):
		del self._AuthntcnCd
		self._AuthntcnCd = None

	@property
	def AuthntcnMrchntNm(self):
		return self._AuthntcnMrchntNm

	@AuthntcnMrchntNm.setter
	def AuthntcnMrchntNm(self, value):
		self._AuthntcnMrchntNm = value if type(value) != base_types.auto else self.make_default("AuthntcnMrchntNm")

	@AuthntcnMrchntNm.deleter
	def AuthntcnMrchntNm(self):
		del self._AuthntcnMrchntNm
		self._AuthntcnMrchntNm = None

	@property
	def AuthntcnSts(self):
		return self._AuthntcnSts

	@AuthntcnSts.setter
	def AuthntcnSts(self, value):
		self._AuthntcnSts = value if type(value) != base_types.auto else self.make_default("AuthntcnSts")

	@AuthntcnSts.deleter
	def AuthntcnSts(self):
		del self._AuthntcnSts
		self._AuthntcnSts = None

	@property
	def AuthntcnSvrTxIdr(self):
		return self._AuthntcnSvrTxIdr

	@AuthntcnSvrTxIdr.setter
	def AuthntcnSvrTxIdr(self, value):
		self._AuthntcnSvrTxIdr = value if type(value) != base_types.auto else self.make_default("AuthntcnSvrTxIdr")

	@AuthntcnSvrTxIdr.deleter
	def AuthntcnSvrTxIdr(self):
		del self._AuthntcnSvrTxIdr
		self._AuthntcnSvrTxIdr = None

	@property
	def AuthntcnVal(self):
		return self._AuthntcnVal

	@AuthntcnVal.setter
	def AuthntcnVal(self, value):
		self._AuthntcnVal = value if type(value) != base_types.auto else self.make_default("AuthntcnVal")

	@AuthntcnVal.deleter
	def AuthntcnVal(self):
		del self._AuthntcnVal
		self._AuthntcnVal = None

	@property
	def BrwsrIPAdr(self):
		return self._BrwsrIPAdr

	@BrwsrIPAdr.setter
	def BrwsrIPAdr(self, value):
		self._BrwsrIPAdr = value if type(value) != base_types.auto else self.make_default("BrwsrIPAdr")

	@BrwsrIPAdr.deleter
	def BrwsrIPAdr(self):
		del self._BrwsrIPAdr
		self._BrwsrIPAdr = None

	@property
	def CrdhldrCertSrlNb(self):
		return self._CrdhldrCertSrlNb

	@CrdhldrCertSrlNb.setter
	def CrdhldrCertSrlNb(self, value):
		self._CrdhldrCertSrlNb = value if type(value) != base_types.auto else self.make_default("CrdhldrCertSrlNb")

	@CrdhldrCertSrlNb.deleter
	def CrdhldrCertSrlNb(self):
		del self._CrdhldrCertSrlNb
		self._CrdhldrCertSrlNb = None

	@property
	def DataQlty(self):
		return self._DataQlty

	@DataQlty.setter
	def DataQlty(self, value):
		self._DataQlty = value if type(value) != base_types.auto else self.make_default("DataQlty")

	@DataQlty.deleter
	def DataQlty(self):
		del self._DataQlty
		self._DataQlty = None

	@property
	def DvcId(self):
		return self._DvcId

	@DvcId.setter
	def DvcId(self, value):
		self._DvcId = value if type(value) != base_types.auto else self.make_default("DvcId")

	@DvcId.deleter
	def DvcId(self):
		del self._DvcId
		self._DvcId = None

	@property
	def DvcIdVlctyCnt(self):
		return self._DvcIdVlctyCnt

	@DvcIdVlctyCnt.setter
	def DvcIdVlctyCnt(self, value):
		self._DvcIdVlctyCnt = value if type(value) != base_types.auto else self.make_default("DvcIdVlctyCnt")

	@DvcIdVlctyCnt.deleter
	def DvcIdVlctyCnt(self):
		del self._DvcIdVlctyCnt
		self._DvcIdVlctyCnt = None

	@property
	def DvcInf(self):
		return self._DvcInf

	@DvcInf.setter
	def DvcInf(self, value):
		self._DvcInf = value if type(value) != base_types.auto else self.make_default("DvcInf")

	@DvcInf.deleter
	def DvcInf(self):
		del self._DvcInf
		self._DvcInf = None

	@property
	def DvcTp(self):
		return self._DvcTp

	@DvcTp.setter
	def DvcTp(self, value):
		self._DvcTp = value if type(value) != base_types.auto else self.make_default("DvcTp")

	@DvcTp.deleter
	def DvcTp(self):
		del self._DvcTp
		self._DvcTp = None

	@property
	def IPAdrVlctyCnt(self):
		return self._IPAdrVlctyCnt

	@IPAdrVlctyCnt.setter
	def IPAdrVlctyCnt(self, value):
		self._IPAdrVlctyCnt = value if type(value) != base_types.auto else self.make_default("IPAdrVlctyCnt")

	@IPAdrVlctyCnt.deleter
	def IPAdrVlctyCnt(self):
		del self._IPAdrVlctyCnt
		self._IPAdrVlctyCnt = None

	@property
	def IntrmyTxIdr(self):
		return self._IntrmyTxIdr

	@IntrmyTxIdr.setter
	def IntrmyTxIdr(self, value):
		self._IntrmyTxIdr = value if type(value) != base_types.auto else self.make_default("IntrmyTxIdr")

	@IntrmyTxIdr.deleter
	def IntrmyTxIdr(self):
		del self._IntrmyTxIdr
		self._IntrmyTxIdr = None

	@property
	def MsgCtgy(self):
		return self._MsgCtgy

	@MsgCtgy.setter
	def MsgCtgy(self, value):
		self._MsgCtgy = value if type(value) != base_types.auto else self.make_default("MsgCtgy")

	@MsgCtgy.deleter
	def MsgCtgy(self):
		del self._MsgCtgy
		self._MsgCtgy = None

	@property
	def MsgVrsn(self):
		return self._MsgVrsn

	@MsgVrsn.setter
	def MsgVrsn(self, value):
		self._MsgVrsn = value if type(value) != base_types.auto else self.make_default("MsgVrsn")

	@MsgVrsn.deleter
	def MsgVrsn(self):
		del self._MsgVrsn
		self._MsgVrsn = None

	@property
	def NtlData(self):
		return self._NtlData

	@NtlData.setter
	def NtlData(self, value):
		self._NtlData = value if type(value) != base_types.auto else self.make_default("NtlData")

	@NtlData.deleter
	def NtlData(self):
		del self._NtlData
		self._NtlData = None

	@property
	def Prgrmm(self):
		return self._Prgrmm

	@Prgrmm.setter
	def Prgrmm(self, value):
		self._Prgrmm = value if type(value) != base_types.auto else self.make_default("Prgrmm")

	@Prgrmm.deleter
	def Prgrmm(self):
		del self._Prgrmm
		self._Prgrmm = None

	@property
	def PrvtData(self):
		return self._PrvtData

	@PrvtData.setter
	def PrvtData(self, value):
		self._PrvtData = value if type(value) != base_types.auto else self.make_default("PrvtData")

	@PrvtData.deleter
	def PrvtData(self):
		del self._PrvtData
		self._PrvtData = None

	@property
	def PurchsAmt(self):
		return self._PurchsAmt

	@PurchsAmt.setter
	def PurchsAmt(self, value):
		self._PurchsAmt = value if type(value) != base_types.auto else self.make_default("PurchsAmt")

	@PurchsAmt.deleter
	def PurchsAmt(self):
		del self._PurchsAmt
		self._PurchsAmt = None

	@property
	def PurchsCcy(self):
		return self._PurchsCcy

	@PurchsCcy.setter
	def PurchsCcy(self, value):
		self._PurchsCcy = value if type(value) != base_types.auto else self.make_default("PurchsCcy")

	@PurchsCcy.deleter
	def PurchsCcy(self):
		del self._PurchsCcy
		self._PurchsCcy = None

	@property
	def PurchsDtTm(self):
		return self._PurchsDtTm

	@PurchsDtTm.setter
	def PurchsDtTm(self, value):
		self._PurchsDtTm = value if type(value) != base_types.auto else self.make_default("PurchsDtTm")

	@PurchsDtTm.deleter
	def PurchsDtTm(self):
		del self._PurchsDtTm
		self._PurchsDtTm = None

	@property
	def RcrngTxSetp(self):
		return self._RcrngTxSetp

	@RcrngTxSetp.setter
	def RcrngTxSetp(self, value):
		self._RcrngTxSetp = value if type(value) != base_types.auto else self.make_default("RcrngTxSetp")

	@RcrngTxSetp.deleter
	def RcrngTxSetp(self):
		del self._RcrngTxSetp
		self._RcrngTxSetp = None

	@property
	def SDKApplId(self):
		return self._SDKApplId

	@SDKApplId.setter
	def SDKApplId(self, value):
		self._SDKApplId = value if type(value) != base_types.auto else self.make_default("SDKApplId")

	@SDKApplId.deleter
	def SDKApplId(self):
		del self._SDKApplId
		self._SDKApplId = None

	@property
	def ShppgInd(self):
		return self._ShppgInd

	@ShppgInd.setter
	def ShppgInd(self, value):
		self._ShppgInd = value if type(value) != base_types.auto else self.make_default("ShppgInd")

	@ShppgInd.deleter
	def ShppgInd(self):
		del self._ShppgInd
		self._ShppgInd = None

	@property
	def SsnId(self):
		return self._SsnId

	@SsnId.setter
	def SsnId(self, value):
		self._SsnId = value if type(value) != base_types.auto else self.make_default("SsnId")

	@SsnId.deleter
	def SsnId(self):
		del self._SsnId
		self._SsnId = None

	@property
	def ThrdPtyId(self):
		return self._ThrdPtyId

	@ThrdPtyId.setter
	def ThrdPtyId(self, value):
		self._ThrdPtyId = value if type(value) != base_types.auto else self.make_default("ThrdPtyId")

	@ThrdPtyId.deleter
	def ThrdPtyId(self):
		del self._ThrdPtyId
		self._ThrdPtyId = None

	@property
	def ThrdPtyRskScore(self):
		return self._ThrdPtyRskScore

	@ThrdPtyRskScore.setter
	def ThrdPtyRskScore(self, value):
		self._ThrdPtyRskScore = value if type(value) != base_types.auto else self.make_default("ThrdPtyRskScore")

	@ThrdPtyRskScore.deleter
	def ThrdPtyRskScore(self):
		del self._ThrdPtyRskScore
		self._ThrdPtyRskScore = None

	@property
	def XID(self):
		return self._XID

	@XID.setter
	def XID(self, value):
		self._XID = value if type(value) != base_types.auto else self.make_default("XID")

	@XID.deleter
	def XID(self):
		del self._XID
		self._XID = None

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