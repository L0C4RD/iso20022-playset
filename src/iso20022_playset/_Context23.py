# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalData1
from . import CardDataReading10Code
from . import ECommerceData1
from . import ICCFallbackReason1Code
from . import ISO18245MerchantCategoryCode
from . import ISODate
from . import MOTO2Code
from . import Max35NumericText
from . import Max35Text
from . import QRCodePresentmentMode1Code
from . import SecurityCharacteristics1Code
from . import TransactionInitiator1Code
from . import TrueFalseIndicator

class Context23(base_types._BaseFieldType):

	__slots__ = ["_AddtlData", "_Attndd", "_AuthntcnOutg", "_CaptrDt", "_CardDataNtryMd", "_CardPres", "_CrdhldrActvtd", "_CrdhldrPres", "_CstmrCnsnt", "_DelydAuthstn", "_DelydChrgs", "_DfrrdDlvry", "_DtAntcptd", "_EComrc", "_EComrcData", "_EComrcIndApld", "_EComrcIndPropsd", "_FnlAuthstn", "_ICCFllbck", "_ICCFllbckRsnCd", "_LatePresntmnt", "_MOTOCd", "_MgntcStrpFllbck", "_MrchntCtgyCd", "_MrchntCtgySpcfcData", "_NoShow", "_OthrCardDataNtryMd", "_OthrICCFllbckRsnCd", "_OthrMrchntCtgy", "_OthrQRCdPresntmntMd", "_OthrSctyChrtcs", "_PINNtryBpss", "_PINPadInprtv", "_PmtCrdntlMrchntRltsh", "_PrtlApprvlSpprtd", "_PrtlShipmnt", "_QRCdPresntmntMd", "_ReSubmissn", "_Reauthstn", "_SctyChrtcs", "_SpltPmt", "_StorgLctn", "_TempScrCardDataReusd", "_TrnspndrInittd", "_Trnst", "_TxInitr", "_UattnddLvlCtgy"]
	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if value is not None else base_types.UninitialisedField(self, 'AddtlData', AdditionalData1, True)

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = base_types.UninitialisedField(self, 'AddtlData', AdditionalData1, True)

	@property
	def Attndd(self):
		return self._Attndd

	@Attndd.setter
	def Attndd(self, value):
		self._Attndd = value if value is not None else base_types.UninitialisedField(self, 'Attndd', TrueFalseIndicator, False)

	@Attndd.deleter
	def Attndd(self):
		del self._Attndd
		self._Attndd = base_types.UninitialisedField(self, 'Attndd', TrueFalseIndicator, False)

	@property
	def AuthntcnOutg(self):
		return self._AuthntcnOutg

	@AuthntcnOutg.setter
	def AuthntcnOutg(self, value):
		self._AuthntcnOutg = value if value is not None else base_types.UninitialisedField(self, 'AuthntcnOutg', TrueFalseIndicator, False)

	@AuthntcnOutg.deleter
	def AuthntcnOutg(self):
		del self._AuthntcnOutg
		self._AuthntcnOutg = base_types.UninitialisedField(self, 'AuthntcnOutg', TrueFalseIndicator, False)

	@property
	def CaptrDt(self):
		return self._CaptrDt

	@CaptrDt.setter
	def CaptrDt(self, value):
		self._CaptrDt = value if value is not None else base_types.UninitialisedField(self, 'CaptrDt', ISODate, False)

	@CaptrDt.deleter
	def CaptrDt(self):
		del self._CaptrDt
		self._CaptrDt = base_types.UninitialisedField(self, 'CaptrDt', ISODate, False)

	@property
	def CardDataNtryMd(self):
		return self._CardDataNtryMd

	@CardDataNtryMd.setter
	def CardDataNtryMd(self, value):
		self._CardDataNtryMd = value if value is not None else base_types.UninitialisedField(self, 'CardDataNtryMd', CardDataReading10Code, False)

	@CardDataNtryMd.deleter
	def CardDataNtryMd(self):
		del self._CardDataNtryMd
		self._CardDataNtryMd = base_types.UninitialisedField(self, 'CardDataNtryMd', CardDataReading10Code, False)

	@property
	def CardPres(self):
		return self._CardPres

	@CardPres.setter
	def CardPres(self, value):
		self._CardPres = value if value is not None else base_types.UninitialisedField(self, 'CardPres', TrueFalseIndicator, False)

	@CardPres.deleter
	def CardPres(self):
		del self._CardPres
		self._CardPres = base_types.UninitialisedField(self, 'CardPres', TrueFalseIndicator, False)

	@property
	def CrdhldrActvtd(self):
		return self._CrdhldrActvtd

	@CrdhldrActvtd.setter
	def CrdhldrActvtd(self, value):
		self._CrdhldrActvtd = value if value is not None else base_types.UninitialisedField(self, 'CrdhldrActvtd', TrueFalseIndicator, False)

	@CrdhldrActvtd.deleter
	def CrdhldrActvtd(self):
		del self._CrdhldrActvtd
		self._CrdhldrActvtd = base_types.UninitialisedField(self, 'CrdhldrActvtd', TrueFalseIndicator, False)

	@property
	def CrdhldrPres(self):
		return self._CrdhldrPres

	@CrdhldrPres.setter
	def CrdhldrPres(self, value):
		self._CrdhldrPres = value if value is not None else base_types.UninitialisedField(self, 'CrdhldrPres', TrueFalseIndicator, False)

	@CrdhldrPres.deleter
	def CrdhldrPres(self):
		del self._CrdhldrPres
		self._CrdhldrPres = base_types.UninitialisedField(self, 'CrdhldrPres', TrueFalseIndicator, False)

	@property
	def CstmrCnsnt(self):
		return self._CstmrCnsnt

	@CstmrCnsnt.setter
	def CstmrCnsnt(self, value):
		self._CstmrCnsnt = value if value is not None else base_types.UninitialisedField(self, 'CstmrCnsnt', TrueFalseIndicator, False)

	@CstmrCnsnt.deleter
	def CstmrCnsnt(self):
		del self._CstmrCnsnt
		self._CstmrCnsnt = base_types.UninitialisedField(self, 'CstmrCnsnt', TrueFalseIndicator, False)

	@property
	def DelydAuthstn(self):
		return self._DelydAuthstn

	@DelydAuthstn.setter
	def DelydAuthstn(self, value):
		self._DelydAuthstn = value if value is not None else base_types.UninitialisedField(self, 'DelydAuthstn', TrueFalseIndicator, False)

	@DelydAuthstn.deleter
	def DelydAuthstn(self):
		del self._DelydAuthstn
		self._DelydAuthstn = base_types.UninitialisedField(self, 'DelydAuthstn', TrueFalseIndicator, False)

	@property
	def DelydChrgs(self):
		return self._DelydChrgs

	@DelydChrgs.setter
	def DelydChrgs(self, value):
		self._DelydChrgs = value if value is not None else base_types.UninitialisedField(self, 'DelydChrgs', TrueFalseIndicator, False)

	@DelydChrgs.deleter
	def DelydChrgs(self):
		del self._DelydChrgs
		self._DelydChrgs = base_types.UninitialisedField(self, 'DelydChrgs', TrueFalseIndicator, False)

	@property
	def DfrrdDlvry(self):
		return self._DfrrdDlvry

	@DfrrdDlvry.setter
	def DfrrdDlvry(self, value):
		self._DfrrdDlvry = value if value is not None else base_types.UninitialisedField(self, 'DfrrdDlvry', TrueFalseIndicator, False)

	@DfrrdDlvry.deleter
	def DfrrdDlvry(self):
		del self._DfrrdDlvry
		self._DfrrdDlvry = base_types.UninitialisedField(self, 'DfrrdDlvry', TrueFalseIndicator, False)

	@property
	def DtAntcptd(self):
		return self._DtAntcptd

	@DtAntcptd.setter
	def DtAntcptd(self, value):
		self._DtAntcptd = value if value is not None else base_types.UninitialisedField(self, 'DtAntcptd', ISODate, False)

	@DtAntcptd.deleter
	def DtAntcptd(self):
		del self._DtAntcptd
		self._DtAntcptd = base_types.UninitialisedField(self, 'DtAntcptd', ISODate, False)

	@property
	def EComrc(self):
		return self._EComrc

	@EComrc.setter
	def EComrc(self, value):
		self._EComrc = value if value is not None else base_types.UninitialisedField(self, 'EComrc', TrueFalseIndicator, False)

	@EComrc.deleter
	def EComrc(self):
		del self._EComrc
		self._EComrc = base_types.UninitialisedField(self, 'EComrc', TrueFalseIndicator, False)

	@property
	def EComrcData(self):
		return self._EComrcData

	@EComrcData.setter
	def EComrcData(self, value):
		self._EComrcData = value if value is not None else base_types.UninitialisedField(self, 'EComrcData', ECommerceData1, True)

	@EComrcData.deleter
	def EComrcData(self):
		del self._EComrcData
		self._EComrcData = base_types.UninitialisedField(self, 'EComrcData', ECommerceData1, True)

	@property
	def EComrcIndApld(self):
		return self._EComrcIndApld

	@EComrcIndApld.setter
	def EComrcIndApld(self, value):
		self._EComrcIndApld = value if value is not None else base_types.UninitialisedField(self, 'EComrcIndApld', Max35Text, False)

	@EComrcIndApld.deleter
	def EComrcIndApld(self):
		del self._EComrcIndApld
		self._EComrcIndApld = base_types.UninitialisedField(self, 'EComrcIndApld', Max35Text, False)

	@property
	def EComrcIndPropsd(self):
		return self._EComrcIndPropsd

	@EComrcIndPropsd.setter
	def EComrcIndPropsd(self, value):
		self._EComrcIndPropsd = value if value is not None else base_types.UninitialisedField(self, 'EComrcIndPropsd', Max35Text, False)

	@EComrcIndPropsd.deleter
	def EComrcIndPropsd(self):
		del self._EComrcIndPropsd
		self._EComrcIndPropsd = base_types.UninitialisedField(self, 'EComrcIndPropsd', Max35Text, False)

	@property
	def FnlAuthstn(self):
		return self._FnlAuthstn

	@FnlAuthstn.setter
	def FnlAuthstn(self, value):
		self._FnlAuthstn = value if value is not None else base_types.UninitialisedField(self, 'FnlAuthstn', TrueFalseIndicator, False)

	@FnlAuthstn.deleter
	def FnlAuthstn(self):
		del self._FnlAuthstn
		self._FnlAuthstn = base_types.UninitialisedField(self, 'FnlAuthstn', TrueFalseIndicator, False)

	@property
	def ICCFllbck(self):
		return self._ICCFllbck

	@ICCFllbck.setter
	def ICCFllbck(self, value):
		self._ICCFllbck = value if value is not None else base_types.UninitialisedField(self, 'ICCFllbck', TrueFalseIndicator, False)

	@ICCFllbck.deleter
	def ICCFllbck(self):
		del self._ICCFllbck
		self._ICCFllbck = base_types.UninitialisedField(self, 'ICCFllbck', TrueFalseIndicator, False)

	@property
	def ICCFllbckRsnCd(self):
		return self._ICCFllbckRsnCd

	@ICCFllbckRsnCd.setter
	def ICCFllbckRsnCd(self, value):
		self._ICCFllbckRsnCd = value if value is not None else base_types.UninitialisedField(self, 'ICCFllbckRsnCd', ICCFallbackReason1Code, False)

	@ICCFllbckRsnCd.deleter
	def ICCFllbckRsnCd(self):
		del self._ICCFllbckRsnCd
		self._ICCFllbckRsnCd = base_types.UninitialisedField(self, 'ICCFllbckRsnCd', ICCFallbackReason1Code, False)

	@property
	def LatePresntmnt(self):
		return self._LatePresntmnt

	@LatePresntmnt.setter
	def LatePresntmnt(self, value):
		self._LatePresntmnt = value if value is not None else base_types.UninitialisedField(self, 'LatePresntmnt', TrueFalseIndicator, False)

	@LatePresntmnt.deleter
	def LatePresntmnt(self):
		del self._LatePresntmnt
		self._LatePresntmnt = base_types.UninitialisedField(self, 'LatePresntmnt', TrueFalseIndicator, False)

	@property
	def MOTOCd(self):
		return self._MOTOCd

	@MOTOCd.setter
	def MOTOCd(self, value):
		self._MOTOCd = value if value is not None else base_types.UninitialisedField(self, 'MOTOCd', MOTO2Code, False)

	@MOTOCd.deleter
	def MOTOCd(self):
		del self._MOTOCd
		self._MOTOCd = base_types.UninitialisedField(self, 'MOTOCd', MOTO2Code, False)

	@property
	def MgntcStrpFllbck(self):
		return self._MgntcStrpFllbck

	@MgntcStrpFllbck.setter
	def MgntcStrpFllbck(self, value):
		self._MgntcStrpFllbck = value if value is not None else base_types.UninitialisedField(self, 'MgntcStrpFllbck', TrueFalseIndicator, False)

	@MgntcStrpFllbck.deleter
	def MgntcStrpFllbck(self):
		del self._MgntcStrpFllbck
		self._MgntcStrpFllbck = base_types.UninitialisedField(self, 'MgntcStrpFllbck', TrueFalseIndicator, False)

	@property
	def MrchntCtgyCd(self):
		return self._MrchntCtgyCd

	@MrchntCtgyCd.setter
	def MrchntCtgyCd(self, value):
		self._MrchntCtgyCd = value if value is not None else base_types.UninitialisedField(self, 'MrchntCtgyCd', ISO18245MerchantCategoryCode, False)

	@MrchntCtgyCd.deleter
	def MrchntCtgyCd(self):
		del self._MrchntCtgyCd
		self._MrchntCtgyCd = base_types.UninitialisedField(self, 'MrchntCtgyCd', ISO18245MerchantCategoryCode, False)

	@property
	def MrchntCtgySpcfcData(self):
		return self._MrchntCtgySpcfcData

	@MrchntCtgySpcfcData.setter
	def MrchntCtgySpcfcData(self, value):
		self._MrchntCtgySpcfcData = value if value is not None else base_types.UninitialisedField(self, 'MrchntCtgySpcfcData', Max35Text, False)

	@MrchntCtgySpcfcData.deleter
	def MrchntCtgySpcfcData(self):
		del self._MrchntCtgySpcfcData
		self._MrchntCtgySpcfcData = base_types.UninitialisedField(self, 'MrchntCtgySpcfcData', Max35Text, False)

	@property
	def NoShow(self):
		return self._NoShow

	@NoShow.setter
	def NoShow(self, value):
		self._NoShow = value if value is not None else base_types.UninitialisedField(self, 'NoShow', TrueFalseIndicator, False)

	@NoShow.deleter
	def NoShow(self):
		del self._NoShow
		self._NoShow = base_types.UninitialisedField(self, 'NoShow', TrueFalseIndicator, False)

	@property
	def OthrCardDataNtryMd(self):
		return self._OthrCardDataNtryMd

	@OthrCardDataNtryMd.setter
	def OthrCardDataNtryMd(self, value):
		self._OthrCardDataNtryMd = value if value is not None else base_types.UninitialisedField(self, 'OthrCardDataNtryMd', Max35Text, False)

	@OthrCardDataNtryMd.deleter
	def OthrCardDataNtryMd(self):
		del self._OthrCardDataNtryMd
		self._OthrCardDataNtryMd = base_types.UninitialisedField(self, 'OthrCardDataNtryMd', Max35Text, False)

	@property
	def OthrICCFllbckRsnCd(self):
		return self._OthrICCFllbckRsnCd

	@OthrICCFllbckRsnCd.setter
	def OthrICCFllbckRsnCd(self, value):
		self._OthrICCFllbckRsnCd = value if value is not None else base_types.UninitialisedField(self, 'OthrICCFllbckRsnCd', Max35Text, False)

	@OthrICCFllbckRsnCd.deleter
	def OthrICCFllbckRsnCd(self):
		del self._OthrICCFllbckRsnCd
		self._OthrICCFllbckRsnCd = base_types.UninitialisedField(self, 'OthrICCFllbckRsnCd', Max35Text, False)

	@property
	def OthrMrchntCtgy(self):
		return self._OthrMrchntCtgy

	@OthrMrchntCtgy.setter
	def OthrMrchntCtgy(self, value):
		self._OthrMrchntCtgy = value if value is not None else base_types.UninitialisedField(self, 'OthrMrchntCtgy', Max35Text, False)

	@OthrMrchntCtgy.deleter
	def OthrMrchntCtgy(self):
		del self._OthrMrchntCtgy
		self._OthrMrchntCtgy = base_types.UninitialisedField(self, 'OthrMrchntCtgy', Max35Text, False)

	@property
	def OthrQRCdPresntmntMd(self):
		return self._OthrQRCdPresntmntMd

	@OthrQRCdPresntmntMd.setter
	def OthrQRCdPresntmntMd(self, value):
		self._OthrQRCdPresntmntMd = value if value is not None else base_types.UninitialisedField(self, 'OthrQRCdPresntmntMd', Max35Text, False)

	@OthrQRCdPresntmntMd.deleter
	def OthrQRCdPresntmntMd(self):
		del self._OthrQRCdPresntmntMd
		self._OthrQRCdPresntmntMd = base_types.UninitialisedField(self, 'OthrQRCdPresntmntMd', Max35Text, False)

	@property
	def OthrSctyChrtcs(self):
		return self._OthrSctyChrtcs

	@OthrSctyChrtcs.setter
	def OthrSctyChrtcs(self, value):
		self._OthrSctyChrtcs = value if value is not None else base_types.UninitialisedField(self, 'OthrSctyChrtcs', Max35Text, False)

	@OthrSctyChrtcs.deleter
	def OthrSctyChrtcs(self):
		del self._OthrSctyChrtcs
		self._OthrSctyChrtcs = base_types.UninitialisedField(self, 'OthrSctyChrtcs', Max35Text, False)

	@property
	def PINNtryBpss(self):
		return self._PINNtryBpss

	@PINNtryBpss.setter
	def PINNtryBpss(self, value):
		self._PINNtryBpss = value if value is not None else base_types.UninitialisedField(self, 'PINNtryBpss', TrueFalseIndicator, False)

	@PINNtryBpss.deleter
	def PINNtryBpss(self):
		del self._PINNtryBpss
		self._PINNtryBpss = base_types.UninitialisedField(self, 'PINNtryBpss', TrueFalseIndicator, False)

	@property
	def PINPadInprtv(self):
		return self._PINPadInprtv

	@PINPadInprtv.setter
	def PINPadInprtv(self, value):
		self._PINPadInprtv = value if value is not None else base_types.UninitialisedField(self, 'PINPadInprtv', TrueFalseIndicator, False)

	@PINPadInprtv.deleter
	def PINPadInprtv(self):
		del self._PINPadInprtv
		self._PINPadInprtv = base_types.UninitialisedField(self, 'PINPadInprtv', TrueFalseIndicator, False)

	@property
	def PmtCrdntlMrchntRltsh(self):
		return self._PmtCrdntlMrchntRltsh

	@PmtCrdntlMrchntRltsh.setter
	def PmtCrdntlMrchntRltsh(self, value):
		self._PmtCrdntlMrchntRltsh = value if value is not None else base_types.UninitialisedField(self, 'PmtCrdntlMrchntRltsh', TrueFalseIndicator, False)

	@PmtCrdntlMrchntRltsh.deleter
	def PmtCrdntlMrchntRltsh(self):
		del self._PmtCrdntlMrchntRltsh
		self._PmtCrdntlMrchntRltsh = base_types.UninitialisedField(self, 'PmtCrdntlMrchntRltsh', TrueFalseIndicator, False)

	@property
	def PrtlApprvlSpprtd(self):
		return self._PrtlApprvlSpprtd

	@PrtlApprvlSpprtd.setter
	def PrtlApprvlSpprtd(self, value):
		self._PrtlApprvlSpprtd = value if value is not None else base_types.UninitialisedField(self, 'PrtlApprvlSpprtd', TrueFalseIndicator, False)

	@PrtlApprvlSpprtd.deleter
	def PrtlApprvlSpprtd(self):
		del self._PrtlApprvlSpprtd
		self._PrtlApprvlSpprtd = base_types.UninitialisedField(self, 'PrtlApprvlSpprtd', TrueFalseIndicator, False)

	@property
	def PrtlShipmnt(self):
		return self._PrtlShipmnt

	@PrtlShipmnt.setter
	def PrtlShipmnt(self, value):
		self._PrtlShipmnt = value if value is not None else base_types.UninitialisedField(self, 'PrtlShipmnt', TrueFalseIndicator, False)

	@PrtlShipmnt.deleter
	def PrtlShipmnt(self):
		del self._PrtlShipmnt
		self._PrtlShipmnt = base_types.UninitialisedField(self, 'PrtlShipmnt', TrueFalseIndicator, False)

	@property
	def QRCdPresntmntMd(self):
		return self._QRCdPresntmntMd

	@QRCdPresntmntMd.setter
	def QRCdPresntmntMd(self, value):
		self._QRCdPresntmntMd = value if value is not None else base_types.UninitialisedField(self, 'QRCdPresntmntMd', QRCodePresentmentMode1Code, False)

	@QRCdPresntmntMd.deleter
	def QRCdPresntmntMd(self):
		del self._QRCdPresntmntMd
		self._QRCdPresntmntMd = base_types.UninitialisedField(self, 'QRCdPresntmntMd', QRCodePresentmentMode1Code, False)

	@property
	def ReSubmissn(self):
		return self._ReSubmissn

	@ReSubmissn.setter
	def ReSubmissn(self, value):
		self._ReSubmissn = value if value is not None else base_types.UninitialisedField(self, 'ReSubmissn', TrueFalseIndicator, False)

	@ReSubmissn.deleter
	def ReSubmissn(self):
		del self._ReSubmissn
		self._ReSubmissn = base_types.UninitialisedField(self, 'ReSubmissn', TrueFalseIndicator, False)

	@property
	def Reauthstn(self):
		return self._Reauthstn

	@Reauthstn.setter
	def Reauthstn(self, value):
		self._Reauthstn = value if value is not None else base_types.UninitialisedField(self, 'Reauthstn', TrueFalseIndicator, False)

	@Reauthstn.deleter
	def Reauthstn(self):
		del self._Reauthstn
		self._Reauthstn = base_types.UninitialisedField(self, 'Reauthstn', TrueFalseIndicator, False)

	@property
	def SctyChrtcs(self):
		return self._SctyChrtcs

	@SctyChrtcs.setter
	def SctyChrtcs(self, value):
		self._SctyChrtcs = value if value is not None else base_types.UninitialisedField(self, 'SctyChrtcs', SecurityCharacteristics1Code, True)

	@SctyChrtcs.deleter
	def SctyChrtcs(self):
		del self._SctyChrtcs
		self._SctyChrtcs = base_types.UninitialisedField(self, 'SctyChrtcs', SecurityCharacteristics1Code, True)

	@property
	def SpltPmt(self):
		return self._SpltPmt

	@SpltPmt.setter
	def SpltPmt(self, value):
		self._SpltPmt = value if value is not None else base_types.UninitialisedField(self, 'SpltPmt', TrueFalseIndicator, False)

	@SpltPmt.deleter
	def SpltPmt(self):
		del self._SpltPmt
		self._SpltPmt = base_types.UninitialisedField(self, 'SpltPmt', TrueFalseIndicator, False)

	@property
	def StorgLctn(self):
		return self._StorgLctn

	@StorgLctn.setter
	def StorgLctn(self, value):
		self._StorgLctn = value if value is not None else base_types.UninitialisedField(self, 'StorgLctn', Max35Text, False)

	@StorgLctn.deleter
	def StorgLctn(self):
		del self._StorgLctn
		self._StorgLctn = base_types.UninitialisedField(self, 'StorgLctn', Max35Text, False)

	@property
	def TempScrCardDataReusd(self):
		return self._TempScrCardDataReusd

	@TempScrCardDataReusd.setter
	def TempScrCardDataReusd(self, value):
		self._TempScrCardDataReusd = value if value is not None else base_types.UninitialisedField(self, 'TempScrCardDataReusd', TrueFalseIndicator, False)

	@TempScrCardDataReusd.deleter
	def TempScrCardDataReusd(self):
		del self._TempScrCardDataReusd
		self._TempScrCardDataReusd = base_types.UninitialisedField(self, 'TempScrCardDataReusd', TrueFalseIndicator, False)

	@property
	def TrnspndrInittd(self):
		return self._TrnspndrInittd

	@TrnspndrInittd.setter
	def TrnspndrInittd(self, value):
		self._TrnspndrInittd = value if value is not None else base_types.UninitialisedField(self, 'TrnspndrInittd', TrueFalseIndicator, False)

	@TrnspndrInittd.deleter
	def TrnspndrInittd(self):
		del self._TrnspndrInittd
		self._TrnspndrInittd = base_types.UninitialisedField(self, 'TrnspndrInittd', TrueFalseIndicator, False)

	@property
	def Trnst(self):
		return self._Trnst

	@Trnst.setter
	def Trnst(self, value):
		self._Trnst = value if value is not None else base_types.UninitialisedField(self, 'Trnst', TrueFalseIndicator, False)

	@Trnst.deleter
	def Trnst(self):
		del self._Trnst
		self._Trnst = base_types.UninitialisedField(self, 'Trnst', TrueFalseIndicator, False)

	@property
	def TxInitr(self):
		return self._TxInitr

	@TxInitr.setter
	def TxInitr(self, value):
		self._TxInitr = value if value is not None else base_types.UninitialisedField(self, 'TxInitr', TransactionInitiator1Code, False)

	@TxInitr.deleter
	def TxInitr(self):
		del self._TxInitr
		self._TxInitr = base_types.UninitialisedField(self, 'TxInitr', TransactionInitiator1Code, False)

	@property
	def UattnddLvlCtgy(self):
		return self._UattnddLvlCtgy

	@UattnddLvlCtgy.setter
	def UattnddLvlCtgy(self, value):
		self._UattnddLvlCtgy = value if value is not None else base_types.UninitialisedField(self, 'UattnddLvlCtgy', Max35NumericText, False)

	@UattnddLvlCtgy.deleter
	def UattnddLvlCtgy(self):
		del self._UattnddLvlCtgy
		self._UattnddLvlCtgy = base_types.UninitialisedField(self, 'UattnddLvlCtgy', Max35NumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlData', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Attndd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthntcnOutg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CaptrDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardDataNtryMd', type=CardDataReading10Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardPres', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrdhldrActvtd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrdhldrPres', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrCnsnt', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DelydAuthstn', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DelydChrgs', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DfrrdDlvry', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtAntcptd', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EComrc', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EComrcData', type=ECommerceData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='EComrcIndApld', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EComrcIndPropsd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FnlAuthstn', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ICCFllbck', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ICCFllbckRsnCd', type=ICCFallbackReason1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LatePresntmnt', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MOTOCd', type=MOTO2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MgntcStrpFllbck', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrchntCtgyCd', type=ISO18245MerchantCategoryCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrchntCtgySpcfcData', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NoShow', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrCardDataNtryMd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrICCFllbckRsnCd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrMrchntCtgy', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrQRCdPresntmntMd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrSctyChrtcs', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PINNtryBpss', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PINPadInprtv', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtCrdntlMrchntRltsh', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtlApprvlSpprtd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtlShipmnt', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QRCdPresntmntMd', type=QRCodePresentmentMode1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReSubmissn', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Reauthstn', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyChrtcs', type=SecurityCharacteristics1Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SpltPmt', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StorgLctn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TempScrCardDataReusd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrnspndrInittd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trnst', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxInitr', type=TransactionInitiator1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UattnddLvlCtgy', type=Max35NumericText, min=0, max=1, mutex_group=None, array=False),
	))