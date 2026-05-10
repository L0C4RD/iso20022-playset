from . import base_types
from .ReceiptType1Code import ReceiptType1Code
from .ISO18245MerchantCategoryCode import ISO18245MerchantCategoryCode
from .GoodAndServiceDeliveryChannel1Code import GoodAndServiceDeliveryChannel1Code
from .GoodAndServiceDeliverySchedule1Code import GoodAndServiceDeliverySchedule1Code
from .MOTO2Code import MOTO2Code
from .ICCFallbackReason1Code import ICCFallbackReason1Code
from .SecurityCharacteristics1Code import SecurityCharacteristics1Code
from .GoodsAndServicesSubType1Code import GoodsAndServicesSubType1Code
from .Max70Text import Max70Text
from .Max35NumericText import Max35NumericText
from .ECommerceData1 import ECommerceData1
from .CardDataReading10Code import CardDataReading10Code
from .TransactionInitiator1Code import TransactionInitiator1Code
from .ISODate import ISODate
from .QRCodePresentmentMode1Code import QRCodePresentmentMode1Code
from .Max35Text import Max35Text
from .TrueFalseIndicator import TrueFalseIndicator
from .AdditionalData1 import AdditionalData1
from .GoodsAndServices1Code import GoodsAndServices1Code

class Context19(base_types._BaseFieldType):

	__slots__ = ["_EComrc", "_GoodAndSvcDlvryChanl", "_CstmrCnsnt", "_SctyChrtcs", "_SpltPmt", "_GoodAndSvcDlvrySchdl", "_OthrGoodAndSvcDlvrySchdl", "_TempScrCardDataReusd", "_MrchntCtgyCd", "_TxInitr", "_CardDataNtryMd", "_PrtlApprvlSpprtd", "_StorgLctn", "_QRCdPresntmntMd", "_PmtCrdntlMrchntRltsh", "_Attndd", "_SaleRefNb", "_AddtlData", "_EComrcIndPropsd", "_ICCFllbck", "_OthrQRCdPresntmntMd", "_RctDstn", "_DtAntcptd", "_MgntcStrpFllbck", "_DfrrdDlvry", "_GoodAndSvcsSubTp", "_ICCFllbckRsnCd", "_AuthntcnOutg", "_UattnddLvlCtgy", "_MOTOCd", "_PrtlShipmnt", "_TrnspndrInittd", "_OthrMrchntCtgy", "_EComrcData", "_OthrICCFllbckRsnCd", "_CardPres", "_MrchntCtgySpcfcData", "_PINNtryBpss", "_ReSubmissn", "_Reauthstn", "_RctReq", "_NoShow", "_FnlAuthstn", "_Trnst", "_CrdhldrActvtd", "_OthrCardDataNtryMd", "_PINPadInprtv", "_ECRId", "_DelydChrgs", "_EComrcIndApld", "_OthrSctyChrtcs", "_CaptrDt", "_LatePresntmnt", "_GoodAndSvcsOthrSubTp", "_DelydAuthstn", "_CrdhldrPres", "_RctTp", "_OthrGoodAndSvcDlvryChanl", "_GoodsAndSvcsTp"]
	@property
	def EComrc(self):
		return self._EComrc

	@EComrc.setter
	def EComrc(self, value):
		self._EComrc = value if type(value) != base_types.auto else self.make_default("EComrc")

	@EComrc.deleter
	def EComrc(self):
		del self._EComrc
		self._EComrc = None

	@property
	def GoodAndSvcDlvryChanl(self):
		return self._GoodAndSvcDlvryChanl

	@GoodAndSvcDlvryChanl.setter
	def GoodAndSvcDlvryChanl(self, value):
		self._GoodAndSvcDlvryChanl = value if type(value) != base_types.auto else self.make_default("GoodAndSvcDlvryChanl")

	@GoodAndSvcDlvryChanl.deleter
	def GoodAndSvcDlvryChanl(self):
		del self._GoodAndSvcDlvryChanl
		self._GoodAndSvcDlvryChanl = None

	@property
	def CstmrCnsnt(self):
		return self._CstmrCnsnt

	@CstmrCnsnt.setter
	def CstmrCnsnt(self, value):
		self._CstmrCnsnt = value if type(value) != base_types.auto else self.make_default("CstmrCnsnt")

	@CstmrCnsnt.deleter
	def CstmrCnsnt(self):
		del self._CstmrCnsnt
		self._CstmrCnsnt = None

	@property
	def SctyChrtcs(self):
		return self._SctyChrtcs

	@SctyChrtcs.setter
	def SctyChrtcs(self, value):
		self._SctyChrtcs = value if type(value) != base_types.auto else self.make_default("SctyChrtcs")

	@SctyChrtcs.deleter
	def SctyChrtcs(self):
		del self._SctyChrtcs
		self._SctyChrtcs = None

	@property
	def SpltPmt(self):
		return self._SpltPmt

	@SpltPmt.setter
	def SpltPmt(self, value):
		self._SpltPmt = value if type(value) != base_types.auto else self.make_default("SpltPmt")

	@SpltPmt.deleter
	def SpltPmt(self):
		del self._SpltPmt
		self._SpltPmt = None

	@property
	def GoodAndSvcDlvrySchdl(self):
		return self._GoodAndSvcDlvrySchdl

	@GoodAndSvcDlvrySchdl.setter
	def GoodAndSvcDlvrySchdl(self, value):
		self._GoodAndSvcDlvrySchdl = value if type(value) != base_types.auto else self.make_default("GoodAndSvcDlvrySchdl")

	@GoodAndSvcDlvrySchdl.deleter
	def GoodAndSvcDlvrySchdl(self):
		del self._GoodAndSvcDlvrySchdl
		self._GoodAndSvcDlvrySchdl = None

	@property
	def OthrGoodAndSvcDlvrySchdl(self):
		return self._OthrGoodAndSvcDlvrySchdl

	@OthrGoodAndSvcDlvrySchdl.setter
	def OthrGoodAndSvcDlvrySchdl(self, value):
		self._OthrGoodAndSvcDlvrySchdl = value if type(value) != base_types.auto else self.make_default("OthrGoodAndSvcDlvrySchdl")

	@OthrGoodAndSvcDlvrySchdl.deleter
	def OthrGoodAndSvcDlvrySchdl(self):
		del self._OthrGoodAndSvcDlvrySchdl
		self._OthrGoodAndSvcDlvrySchdl = None

	@property
	def TempScrCardDataReusd(self):
		return self._TempScrCardDataReusd

	@TempScrCardDataReusd.setter
	def TempScrCardDataReusd(self, value):
		self._TempScrCardDataReusd = value if type(value) != base_types.auto else self.make_default("TempScrCardDataReusd")

	@TempScrCardDataReusd.deleter
	def TempScrCardDataReusd(self):
		del self._TempScrCardDataReusd
		self._TempScrCardDataReusd = None

	@property
	def MrchntCtgyCd(self):
		return self._MrchntCtgyCd

	@MrchntCtgyCd.setter
	def MrchntCtgyCd(self, value):
		self._MrchntCtgyCd = value if type(value) != base_types.auto else self.make_default("MrchntCtgyCd")

	@MrchntCtgyCd.deleter
	def MrchntCtgyCd(self):
		del self._MrchntCtgyCd
		self._MrchntCtgyCd = None

	@property
	def TxInitr(self):
		return self._TxInitr

	@TxInitr.setter
	def TxInitr(self, value):
		self._TxInitr = value if type(value) != base_types.auto else self.make_default("TxInitr")

	@TxInitr.deleter
	def TxInitr(self):
		del self._TxInitr
		self._TxInitr = None

	@property
	def CardDataNtryMd(self):
		return self._CardDataNtryMd

	@CardDataNtryMd.setter
	def CardDataNtryMd(self, value):
		self._CardDataNtryMd = value if type(value) != base_types.auto else self.make_default("CardDataNtryMd")

	@CardDataNtryMd.deleter
	def CardDataNtryMd(self):
		del self._CardDataNtryMd
		self._CardDataNtryMd = None

	@property
	def PrtlApprvlSpprtd(self):
		return self._PrtlApprvlSpprtd

	@PrtlApprvlSpprtd.setter
	def PrtlApprvlSpprtd(self, value):
		self._PrtlApprvlSpprtd = value if type(value) != base_types.auto else self.make_default("PrtlApprvlSpprtd")

	@PrtlApprvlSpprtd.deleter
	def PrtlApprvlSpprtd(self):
		del self._PrtlApprvlSpprtd
		self._PrtlApprvlSpprtd = None

	@property
	def StorgLctn(self):
		return self._StorgLctn

	@StorgLctn.setter
	def StorgLctn(self, value):
		self._StorgLctn = value if type(value) != base_types.auto else self.make_default("StorgLctn")

	@StorgLctn.deleter
	def StorgLctn(self):
		del self._StorgLctn
		self._StorgLctn = None

	@property
	def QRCdPresntmntMd(self):
		return self._QRCdPresntmntMd

	@QRCdPresntmntMd.setter
	def QRCdPresntmntMd(self, value):
		self._QRCdPresntmntMd = value if type(value) != base_types.auto else self.make_default("QRCdPresntmntMd")

	@QRCdPresntmntMd.deleter
	def QRCdPresntmntMd(self):
		del self._QRCdPresntmntMd
		self._QRCdPresntmntMd = None

	@property
	def PmtCrdntlMrchntRltsh(self):
		return self._PmtCrdntlMrchntRltsh

	@PmtCrdntlMrchntRltsh.setter
	def PmtCrdntlMrchntRltsh(self, value):
		self._PmtCrdntlMrchntRltsh = value if type(value) != base_types.auto else self.make_default("PmtCrdntlMrchntRltsh")

	@PmtCrdntlMrchntRltsh.deleter
	def PmtCrdntlMrchntRltsh(self):
		del self._PmtCrdntlMrchntRltsh
		self._PmtCrdntlMrchntRltsh = None

	@property
	def Attndd(self):
		return self._Attndd

	@Attndd.setter
	def Attndd(self, value):
		self._Attndd = value if type(value) != base_types.auto else self.make_default("Attndd")

	@Attndd.deleter
	def Attndd(self):
		del self._Attndd
		self._Attndd = None

	@property
	def SaleRefNb(self):
		return self._SaleRefNb

	@SaleRefNb.setter
	def SaleRefNb(self, value):
		self._SaleRefNb = value if type(value) != base_types.auto else self.make_default("SaleRefNb")

	@SaleRefNb.deleter
	def SaleRefNb(self):
		del self._SaleRefNb
		self._SaleRefNb = None

	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if type(value) != base_types.auto else self.make_default("AddtlData")

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = None

	@property
	def EComrcIndPropsd(self):
		return self._EComrcIndPropsd

	@EComrcIndPropsd.setter
	def EComrcIndPropsd(self, value):
		self._EComrcIndPropsd = value if type(value) != base_types.auto else self.make_default("EComrcIndPropsd")

	@EComrcIndPropsd.deleter
	def EComrcIndPropsd(self):
		del self._EComrcIndPropsd
		self._EComrcIndPropsd = None

	@property
	def ICCFllbck(self):
		return self._ICCFllbck

	@ICCFllbck.setter
	def ICCFllbck(self, value):
		self._ICCFllbck = value if type(value) != base_types.auto else self.make_default("ICCFllbck")

	@ICCFllbck.deleter
	def ICCFllbck(self):
		del self._ICCFllbck
		self._ICCFllbck = None

	@property
	def OthrQRCdPresntmntMd(self):
		return self._OthrQRCdPresntmntMd

	@OthrQRCdPresntmntMd.setter
	def OthrQRCdPresntmntMd(self, value):
		self._OthrQRCdPresntmntMd = value if type(value) != base_types.auto else self.make_default("OthrQRCdPresntmntMd")

	@OthrQRCdPresntmntMd.deleter
	def OthrQRCdPresntmntMd(self):
		del self._OthrQRCdPresntmntMd
		self._OthrQRCdPresntmntMd = None

	@property
	def RctDstn(self):
		return self._RctDstn

	@RctDstn.setter
	def RctDstn(self, value):
		self._RctDstn = value if type(value) != base_types.auto else self.make_default("RctDstn")

	@RctDstn.deleter
	def RctDstn(self):
		del self._RctDstn
		self._RctDstn = None

	@property
	def DtAntcptd(self):
		return self._DtAntcptd

	@DtAntcptd.setter
	def DtAntcptd(self, value):
		self._DtAntcptd = value if type(value) != base_types.auto else self.make_default("DtAntcptd")

	@DtAntcptd.deleter
	def DtAntcptd(self):
		del self._DtAntcptd
		self._DtAntcptd = None

	@property
	def MgntcStrpFllbck(self):
		return self._MgntcStrpFllbck

	@MgntcStrpFllbck.setter
	def MgntcStrpFllbck(self, value):
		self._MgntcStrpFllbck = value if type(value) != base_types.auto else self.make_default("MgntcStrpFllbck")

	@MgntcStrpFllbck.deleter
	def MgntcStrpFllbck(self):
		del self._MgntcStrpFllbck
		self._MgntcStrpFllbck = None

	@property
	def DfrrdDlvry(self):
		return self._DfrrdDlvry

	@DfrrdDlvry.setter
	def DfrrdDlvry(self, value):
		self._DfrrdDlvry = value if type(value) != base_types.auto else self.make_default("DfrrdDlvry")

	@DfrrdDlvry.deleter
	def DfrrdDlvry(self):
		del self._DfrrdDlvry
		self._DfrrdDlvry = None

	@property
	def GoodAndSvcsSubTp(self):
		return self._GoodAndSvcsSubTp

	@GoodAndSvcsSubTp.setter
	def GoodAndSvcsSubTp(self, value):
		self._GoodAndSvcsSubTp = value if type(value) != base_types.auto else self.make_default("GoodAndSvcsSubTp")

	@GoodAndSvcsSubTp.deleter
	def GoodAndSvcsSubTp(self):
		del self._GoodAndSvcsSubTp
		self._GoodAndSvcsSubTp = None

	@property
	def ICCFllbckRsnCd(self):
		return self._ICCFllbckRsnCd

	@ICCFllbckRsnCd.setter
	def ICCFllbckRsnCd(self, value):
		self._ICCFllbckRsnCd = value if type(value) != base_types.auto else self.make_default("ICCFllbckRsnCd")

	@ICCFllbckRsnCd.deleter
	def ICCFllbckRsnCd(self):
		del self._ICCFllbckRsnCd
		self._ICCFllbckRsnCd = None

	@property
	def AuthntcnOutg(self):
		return self._AuthntcnOutg

	@AuthntcnOutg.setter
	def AuthntcnOutg(self, value):
		self._AuthntcnOutg = value if type(value) != base_types.auto else self.make_default("AuthntcnOutg")

	@AuthntcnOutg.deleter
	def AuthntcnOutg(self):
		del self._AuthntcnOutg
		self._AuthntcnOutg = None

	@property
	def UattnddLvlCtgy(self):
		return self._UattnddLvlCtgy

	@UattnddLvlCtgy.setter
	def UattnddLvlCtgy(self, value):
		self._UattnddLvlCtgy = value if type(value) != base_types.auto else self.make_default("UattnddLvlCtgy")

	@UattnddLvlCtgy.deleter
	def UattnddLvlCtgy(self):
		del self._UattnddLvlCtgy
		self._UattnddLvlCtgy = None

	@property
	def MOTOCd(self):
		return self._MOTOCd

	@MOTOCd.setter
	def MOTOCd(self, value):
		self._MOTOCd = value if type(value) != base_types.auto else self.make_default("MOTOCd")

	@MOTOCd.deleter
	def MOTOCd(self):
		del self._MOTOCd
		self._MOTOCd = None

	@property
	def PrtlShipmnt(self):
		return self._PrtlShipmnt

	@PrtlShipmnt.setter
	def PrtlShipmnt(self, value):
		self._PrtlShipmnt = value if type(value) != base_types.auto else self.make_default("PrtlShipmnt")

	@PrtlShipmnt.deleter
	def PrtlShipmnt(self):
		del self._PrtlShipmnt
		self._PrtlShipmnt = None

	@property
	def TrnspndrInittd(self):
		return self._TrnspndrInittd

	@TrnspndrInittd.setter
	def TrnspndrInittd(self, value):
		self._TrnspndrInittd = value if type(value) != base_types.auto else self.make_default("TrnspndrInittd")

	@TrnspndrInittd.deleter
	def TrnspndrInittd(self):
		del self._TrnspndrInittd
		self._TrnspndrInittd = None

	@property
	def OthrMrchntCtgy(self):
		return self._OthrMrchntCtgy

	@OthrMrchntCtgy.setter
	def OthrMrchntCtgy(self, value):
		self._OthrMrchntCtgy = value if type(value) != base_types.auto else self.make_default("OthrMrchntCtgy")

	@OthrMrchntCtgy.deleter
	def OthrMrchntCtgy(self):
		del self._OthrMrchntCtgy
		self._OthrMrchntCtgy = None

	@property
	def EComrcData(self):
		return self._EComrcData

	@EComrcData.setter
	def EComrcData(self, value):
		self._EComrcData = value if type(value) != base_types.auto else self.make_default("EComrcData")

	@EComrcData.deleter
	def EComrcData(self):
		del self._EComrcData
		self._EComrcData = None

	@property
	def OthrICCFllbckRsnCd(self):
		return self._OthrICCFllbckRsnCd

	@OthrICCFllbckRsnCd.setter
	def OthrICCFllbckRsnCd(self, value):
		self._OthrICCFllbckRsnCd = value if type(value) != base_types.auto else self.make_default("OthrICCFllbckRsnCd")

	@OthrICCFllbckRsnCd.deleter
	def OthrICCFllbckRsnCd(self):
		del self._OthrICCFllbckRsnCd
		self._OthrICCFllbckRsnCd = None

	@property
	def CardPres(self):
		return self._CardPres

	@CardPres.setter
	def CardPres(self, value):
		self._CardPres = value if type(value) != base_types.auto else self.make_default("CardPres")

	@CardPres.deleter
	def CardPres(self):
		del self._CardPres
		self._CardPres = None

	@property
	def MrchntCtgySpcfcData(self):
		return self._MrchntCtgySpcfcData

	@MrchntCtgySpcfcData.setter
	def MrchntCtgySpcfcData(self, value):
		self._MrchntCtgySpcfcData = value if type(value) != base_types.auto else self.make_default("MrchntCtgySpcfcData")

	@MrchntCtgySpcfcData.deleter
	def MrchntCtgySpcfcData(self):
		del self._MrchntCtgySpcfcData
		self._MrchntCtgySpcfcData = None

	@property
	def PINNtryBpss(self):
		return self._PINNtryBpss

	@PINNtryBpss.setter
	def PINNtryBpss(self, value):
		self._PINNtryBpss = value if type(value) != base_types.auto else self.make_default("PINNtryBpss")

	@PINNtryBpss.deleter
	def PINNtryBpss(self):
		del self._PINNtryBpss
		self._PINNtryBpss = None

	@property
	def ReSubmissn(self):
		return self._ReSubmissn

	@ReSubmissn.setter
	def ReSubmissn(self, value):
		self._ReSubmissn = value if type(value) != base_types.auto else self.make_default("ReSubmissn")

	@ReSubmissn.deleter
	def ReSubmissn(self):
		del self._ReSubmissn
		self._ReSubmissn = None

	@property
	def Reauthstn(self):
		return self._Reauthstn

	@Reauthstn.setter
	def Reauthstn(self, value):
		self._Reauthstn = value if type(value) != base_types.auto else self.make_default("Reauthstn")

	@Reauthstn.deleter
	def Reauthstn(self):
		del self._Reauthstn
		self._Reauthstn = None

	@property
	def RctReq(self):
		return self._RctReq

	@RctReq.setter
	def RctReq(self, value):
		self._RctReq = value if type(value) != base_types.auto else self.make_default("RctReq")

	@RctReq.deleter
	def RctReq(self):
		del self._RctReq
		self._RctReq = None

	@property
	def NoShow(self):
		return self._NoShow

	@NoShow.setter
	def NoShow(self, value):
		self._NoShow = value if type(value) != base_types.auto else self.make_default("NoShow")

	@NoShow.deleter
	def NoShow(self):
		del self._NoShow
		self._NoShow = None

	@property
	def FnlAuthstn(self):
		return self._FnlAuthstn

	@FnlAuthstn.setter
	def FnlAuthstn(self, value):
		self._FnlAuthstn = value if type(value) != base_types.auto else self.make_default("FnlAuthstn")

	@FnlAuthstn.deleter
	def FnlAuthstn(self):
		del self._FnlAuthstn
		self._FnlAuthstn = None

	@property
	def Trnst(self):
		return self._Trnst

	@Trnst.setter
	def Trnst(self, value):
		self._Trnst = value if type(value) != base_types.auto else self.make_default("Trnst")

	@Trnst.deleter
	def Trnst(self):
		del self._Trnst
		self._Trnst = None

	@property
	def CrdhldrActvtd(self):
		return self._CrdhldrActvtd

	@CrdhldrActvtd.setter
	def CrdhldrActvtd(self, value):
		self._CrdhldrActvtd = value if type(value) != base_types.auto else self.make_default("CrdhldrActvtd")

	@CrdhldrActvtd.deleter
	def CrdhldrActvtd(self):
		del self._CrdhldrActvtd
		self._CrdhldrActvtd = None

	@property
	def OthrCardDataNtryMd(self):
		return self._OthrCardDataNtryMd

	@OthrCardDataNtryMd.setter
	def OthrCardDataNtryMd(self, value):
		self._OthrCardDataNtryMd = value if type(value) != base_types.auto else self.make_default("OthrCardDataNtryMd")

	@OthrCardDataNtryMd.deleter
	def OthrCardDataNtryMd(self):
		del self._OthrCardDataNtryMd
		self._OthrCardDataNtryMd = None

	@property
	def PINPadInprtv(self):
		return self._PINPadInprtv

	@PINPadInprtv.setter
	def PINPadInprtv(self, value):
		self._PINPadInprtv = value if type(value) != base_types.auto else self.make_default("PINPadInprtv")

	@PINPadInprtv.deleter
	def PINPadInprtv(self):
		del self._PINPadInprtv
		self._PINPadInprtv = None

	@property
	def ECRId(self):
		return self._ECRId

	@ECRId.setter
	def ECRId(self, value):
		self._ECRId = value if type(value) != base_types.auto else self.make_default("ECRId")

	@ECRId.deleter
	def ECRId(self):
		del self._ECRId
		self._ECRId = None

	@property
	def DelydChrgs(self):
		return self._DelydChrgs

	@DelydChrgs.setter
	def DelydChrgs(self, value):
		self._DelydChrgs = value if type(value) != base_types.auto else self.make_default("DelydChrgs")

	@DelydChrgs.deleter
	def DelydChrgs(self):
		del self._DelydChrgs
		self._DelydChrgs = None

	@property
	def EComrcIndApld(self):
		return self._EComrcIndApld

	@EComrcIndApld.setter
	def EComrcIndApld(self, value):
		self._EComrcIndApld = value if type(value) != base_types.auto else self.make_default("EComrcIndApld")

	@EComrcIndApld.deleter
	def EComrcIndApld(self):
		del self._EComrcIndApld
		self._EComrcIndApld = None

	@property
	def OthrSctyChrtcs(self):
		return self._OthrSctyChrtcs

	@OthrSctyChrtcs.setter
	def OthrSctyChrtcs(self, value):
		self._OthrSctyChrtcs = value if type(value) != base_types.auto else self.make_default("OthrSctyChrtcs")

	@OthrSctyChrtcs.deleter
	def OthrSctyChrtcs(self):
		del self._OthrSctyChrtcs
		self._OthrSctyChrtcs = None

	@property
	def CaptrDt(self):
		return self._CaptrDt

	@CaptrDt.setter
	def CaptrDt(self, value):
		self._CaptrDt = value if type(value) != base_types.auto else self.make_default("CaptrDt")

	@CaptrDt.deleter
	def CaptrDt(self):
		del self._CaptrDt
		self._CaptrDt = None

	@property
	def LatePresntmnt(self):
		return self._LatePresntmnt

	@LatePresntmnt.setter
	def LatePresntmnt(self, value):
		self._LatePresntmnt = value if type(value) != base_types.auto else self.make_default("LatePresntmnt")

	@LatePresntmnt.deleter
	def LatePresntmnt(self):
		del self._LatePresntmnt
		self._LatePresntmnt = None

	@property
	def GoodAndSvcsOthrSubTp(self):
		return self._GoodAndSvcsOthrSubTp

	@GoodAndSvcsOthrSubTp.setter
	def GoodAndSvcsOthrSubTp(self, value):
		self._GoodAndSvcsOthrSubTp = value if type(value) != base_types.auto else self.make_default("GoodAndSvcsOthrSubTp")

	@GoodAndSvcsOthrSubTp.deleter
	def GoodAndSvcsOthrSubTp(self):
		del self._GoodAndSvcsOthrSubTp
		self._GoodAndSvcsOthrSubTp = None

	@property
	def DelydAuthstn(self):
		return self._DelydAuthstn

	@DelydAuthstn.setter
	def DelydAuthstn(self, value):
		self._DelydAuthstn = value if type(value) != base_types.auto else self.make_default("DelydAuthstn")

	@DelydAuthstn.deleter
	def DelydAuthstn(self):
		del self._DelydAuthstn
		self._DelydAuthstn = None

	@property
	def CrdhldrPres(self):
		return self._CrdhldrPres

	@CrdhldrPres.setter
	def CrdhldrPres(self, value):
		self._CrdhldrPres = value if type(value) != base_types.auto else self.make_default("CrdhldrPres")

	@CrdhldrPres.deleter
	def CrdhldrPres(self):
		del self._CrdhldrPres
		self._CrdhldrPres = None

	@property
	def RctTp(self):
		return self._RctTp

	@RctTp.setter
	def RctTp(self, value):
		self._RctTp = value if type(value) != base_types.auto else self.make_default("RctTp")

	@RctTp.deleter
	def RctTp(self):
		del self._RctTp
		self._RctTp = None

	@property
	def OthrGoodAndSvcDlvryChanl(self):
		return self._OthrGoodAndSvcDlvryChanl

	@OthrGoodAndSvcDlvryChanl.setter
	def OthrGoodAndSvcDlvryChanl(self, value):
		self._OthrGoodAndSvcDlvryChanl = value if type(value) != base_types.auto else self.make_default("OthrGoodAndSvcDlvryChanl")

	@OthrGoodAndSvcDlvryChanl.deleter
	def OthrGoodAndSvcDlvryChanl(self):
		del self._OthrGoodAndSvcDlvryChanl
		self._OthrGoodAndSvcDlvryChanl = None

	@property
	def GoodsAndSvcsTp(self):
		return self._GoodsAndSvcsTp

	@GoodsAndSvcsTp.setter
	def GoodsAndSvcsTp(self, value):
		self._GoodsAndSvcsTp = value if type(value) != base_types.auto else self.make_default("GoodsAndSvcsTp")

	@GoodsAndSvcsTp.deleter
	def GoodsAndSvcsTp(self):
		del self._GoodsAndSvcsTp
		self._GoodsAndSvcsTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='EComrc', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GoodAndSvcDlvryChanl', type=GoodAndServiceDeliveryChannel1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrCnsnt', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyChrtcs', type=SecurityCharacteristics1Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SpltPmt', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GoodAndSvcDlvrySchdl', type=GoodAndServiceDeliverySchedule1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrGoodAndSvcDlvrySchdl', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TempScrCardDataReusd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrchntCtgyCd', type=ISO18245MerchantCategoryCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxInitr', type=TransactionInitiator1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardDataNtryMd', type=CardDataReading10Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtlApprvlSpprtd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StorgLctn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QRCdPresntmntMd', type=QRCodePresentmentMode1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtCrdntlMrchntRltsh', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Attndd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleRefNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlData', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='EComrcIndPropsd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ICCFllbck', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrQRCdPresntmntMd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RctDstn', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtAntcptd', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MgntcStrpFllbck', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DfrrdDlvry', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GoodAndSvcsSubTp', type=GoodsAndServicesSubType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ICCFllbckRsnCd', type=ICCFallbackReason1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthntcnOutg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UattnddLvlCtgy', type=Max35NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MOTOCd', type=MOTO2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtlShipmnt', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrnspndrInittd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrMrchntCtgy', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EComrcData', type=ECommerceData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OthrICCFllbckRsnCd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardPres', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrchntCtgySpcfcData', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PINNtryBpss', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReSubmissn', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Reauthstn', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RctReq', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NoShow', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FnlAuthstn', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trnst', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrdhldrActvtd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrCardDataNtryMd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PINPadInprtv', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ECRId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DelydChrgs', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EComrcIndApld', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrSctyChrtcs', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CaptrDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LatePresntmnt', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GoodAndSvcsOthrSubTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DelydAuthstn', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrdhldrPres', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RctTp', type=ReceiptType1Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OthrGoodAndSvcDlvryChanl', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GoodsAndSvcsTp', type=GoodsAndServices1Code, min=0, max=1, mutex_group=None, array=False),
	))

