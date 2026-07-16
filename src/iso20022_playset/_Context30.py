# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATICALaxProcessing
from . import CardDataReading11Code
from . import ECommerceData1
from . import GoodAndServiceDeliveryChannel2Code
from . import GoodAndServiceDeliverySchedule2Code
from . import GoodsAndServices1Code
from . import GoodsAndServicesSubType2Code
from . import ISO18245MerchantCategoryCode
from . import ISODate
from . import MOTO2Code
from . import Max35NumericText
from . import Max35Text
from . import Max70Text
from . import QRCodePresentmentMode2Code
from . import ReceiptType1Code
from . import SecurityCharacteristics2Code
from . import TransactionInitiator1Code
from . import TrueFalseIndicator

class Context30(base_types._BaseFieldType):

	__slots__ = ["_Attndd", "_AuthntcnOutg", "_CaptrDt", "_CardDataNtryMd", "_CardPres", "_CrdhldrActvtd", "_CrdhldrPres", "_DelydAuthstn", "_DelydChrgs", "_DfrrdDlvry", "_DtAntcptd", "_EComrc", "_EComrcData", "_EComrcIndApld", "_EComrcIndPropsd", "_GoodAndSvcDlvryChanl", "_GoodAndSvcDlvrySchdl", "_GoodsAndSvcsSubTp", "_GoodsAndSvcsTp", "_LatePresntmnt", "_MOTOCd", "_MrchntCtgyCd", "_MrchntCtgySpcfcData", "_NoShow", "_NtlData", "_OthrMrchntCtgy", "_PmtCrdntlMrchntRltsh", "_PrtlApprvlSpprtd", "_PrtlShipmnt", "_PrvtData", "_QRCdPresntmntMd", "_RctDstn", "_RctReq", "_RctTp", "_ReSubmissn", "_Reauthstn", "_SaleRefNb", "_SctyChrtcs", "_SpltPmt", "_StorgLctn", "_TrnspndrInittd", "_Trnst", "_TxInitr", "_UattnddLvlCtgy"]
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
		self._CardDataNtryMd = value if value is not None else base_types.UninitialisedField(self, 'CardDataNtryMd', CardDataReading11Code, False)

	@CardDataNtryMd.deleter
	def CardDataNtryMd(self):
		del self._CardDataNtryMd
		self._CardDataNtryMd = base_types.UninitialisedField(self, 'CardDataNtryMd', CardDataReading11Code, False)

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
	def GoodAndSvcDlvryChanl(self):
		return self._GoodAndSvcDlvryChanl

	@GoodAndSvcDlvryChanl.setter
	def GoodAndSvcDlvryChanl(self, value):
		self._GoodAndSvcDlvryChanl = value if value is not None else base_types.UninitialisedField(self, 'GoodAndSvcDlvryChanl', GoodAndServiceDeliveryChannel2Code, False)

	@GoodAndSvcDlvryChanl.deleter
	def GoodAndSvcDlvryChanl(self):
		del self._GoodAndSvcDlvryChanl
		self._GoodAndSvcDlvryChanl = base_types.UninitialisedField(self, 'GoodAndSvcDlvryChanl', GoodAndServiceDeliveryChannel2Code, False)

	@property
	def GoodAndSvcDlvrySchdl(self):
		return self._GoodAndSvcDlvrySchdl

	@GoodAndSvcDlvrySchdl.setter
	def GoodAndSvcDlvrySchdl(self, value):
		self._GoodAndSvcDlvrySchdl = value if value is not None else base_types.UninitialisedField(self, 'GoodAndSvcDlvrySchdl', GoodAndServiceDeliverySchedule2Code, False)

	@GoodAndSvcDlvrySchdl.deleter
	def GoodAndSvcDlvrySchdl(self):
		del self._GoodAndSvcDlvrySchdl
		self._GoodAndSvcDlvrySchdl = base_types.UninitialisedField(self, 'GoodAndSvcDlvrySchdl', GoodAndServiceDeliverySchedule2Code, False)

	@property
	def GoodsAndSvcsSubTp(self):
		return self._GoodsAndSvcsSubTp

	@GoodsAndSvcsSubTp.setter
	def GoodsAndSvcsSubTp(self, value):
		self._GoodsAndSvcsSubTp = value if value is not None else base_types.UninitialisedField(self, 'GoodsAndSvcsSubTp', GoodsAndServicesSubType2Code, False)

	@GoodsAndSvcsSubTp.deleter
	def GoodsAndSvcsSubTp(self):
		del self._GoodsAndSvcsSubTp
		self._GoodsAndSvcsSubTp = base_types.UninitialisedField(self, 'GoodsAndSvcsSubTp', GoodsAndServicesSubType2Code, False)

	@property
	def GoodsAndSvcsTp(self):
		return self._GoodsAndSvcsTp

	@GoodsAndSvcsTp.setter
	def GoodsAndSvcsTp(self, value):
		self._GoodsAndSvcsTp = value if value is not None else base_types.UninitialisedField(self, 'GoodsAndSvcsTp', GoodsAndServices1Code, False)

	@GoodsAndSvcsTp.deleter
	def GoodsAndSvcsTp(self):
		del self._GoodsAndSvcsTp
		self._GoodsAndSvcsTp = base_types.UninitialisedField(self, 'GoodsAndSvcsTp', GoodsAndServices1Code, False)

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
	def QRCdPresntmntMd(self):
		return self._QRCdPresntmntMd

	@QRCdPresntmntMd.setter
	def QRCdPresntmntMd(self, value):
		self._QRCdPresntmntMd = value if value is not None else base_types.UninitialisedField(self, 'QRCdPresntmntMd', QRCodePresentmentMode2Code, False)

	@QRCdPresntmntMd.deleter
	def QRCdPresntmntMd(self):
		del self._QRCdPresntmntMd
		self._QRCdPresntmntMd = base_types.UninitialisedField(self, 'QRCdPresntmntMd', QRCodePresentmentMode2Code, False)

	@property
	def RctDstn(self):
		return self._RctDstn

	@RctDstn.setter
	def RctDstn(self, value):
		self._RctDstn = value if value is not None else base_types.UninitialisedField(self, 'RctDstn', Max70Text, False)

	@RctDstn.deleter
	def RctDstn(self):
		del self._RctDstn
		self._RctDstn = base_types.UninitialisedField(self, 'RctDstn', Max70Text, False)

	@property
	def RctReq(self):
		return self._RctReq

	@RctReq.setter
	def RctReq(self, value):
		self._RctReq = value if value is not None else base_types.UninitialisedField(self, 'RctReq', TrueFalseIndicator, False)

	@RctReq.deleter
	def RctReq(self):
		del self._RctReq
		self._RctReq = base_types.UninitialisedField(self, 'RctReq', TrueFalseIndicator, False)

	@property
	def RctTp(self):
		return self._RctTp

	@RctTp.setter
	def RctTp(self, value):
		self._RctTp = value if value is not None else base_types.UninitialisedField(self, 'RctTp', ReceiptType1Code, True)

	@RctTp.deleter
	def RctTp(self):
		del self._RctTp
		self._RctTp = base_types.UninitialisedField(self, 'RctTp', ReceiptType1Code, True)

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
	def SaleRefNb(self):
		return self._SaleRefNb

	@SaleRefNb.setter
	def SaleRefNb(self, value):
		self._SaleRefNb = value if value is not None else base_types.UninitialisedField(self, 'SaleRefNb', Max35Text, False)

	@SaleRefNb.deleter
	def SaleRefNb(self):
		del self._SaleRefNb
		self._SaleRefNb = base_types.UninitialisedField(self, 'SaleRefNb', Max35Text, False)

	@property
	def SctyChrtcs(self):
		return self._SctyChrtcs

	@SctyChrtcs.setter
	def SctyChrtcs(self, value):
		self._SctyChrtcs = value if value is not None else base_types.UninitialisedField(self, 'SctyChrtcs', SecurityCharacteristics2Code, True)

	@SctyChrtcs.deleter
	def SctyChrtcs(self):
		del self._SctyChrtcs
		self._SctyChrtcs = base_types.UninitialisedField(self, 'SctyChrtcs', SecurityCharacteristics2Code, True)

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
		base_types.FieldEntry(name='Attndd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthntcnOutg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CaptrDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardDataNtryMd', type=CardDataReading11Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardPres', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrdhldrActvtd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrdhldrPres', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DelydAuthstn', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DelydChrgs', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DfrrdDlvry', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtAntcptd', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EComrc', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EComrcData', type=ECommerceData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='EComrcIndApld', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EComrcIndPropsd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GoodAndSvcDlvryChanl', type=GoodAndServiceDeliveryChannel2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GoodAndSvcDlvrySchdl', type=GoodAndServiceDeliverySchedule2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GoodsAndSvcsSubTp', type=GoodsAndServicesSubType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GoodsAndSvcsTp', type=GoodsAndServices1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LatePresntmnt', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MOTOCd', type=MOTO2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrchntCtgyCd', type=ISO18245MerchantCategoryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrchntCtgySpcfcData', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NoShow', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtlData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OthrMrchntCtgy', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtCrdntlMrchntRltsh', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtlApprvlSpprtd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtlShipmnt', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvtData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='QRCdPresntmntMd', type=QRCodePresentmentMode2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RctDstn', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RctReq', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RctTp', type=ReceiptType1Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ReSubmissn', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Reauthstn', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleRefNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyChrtcs', type=SecurityCharacteristics2Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SpltPmt', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StorgLctn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrnspndrInittd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trnst', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxInitr', type=TransactionInitiator1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UattnddLvlCtgy', type=Max35NumericText, min=0, max=1, mutex_group=None, array=False),
	))