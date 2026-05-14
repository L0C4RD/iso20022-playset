# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ATICALaxProcessing import ATICALaxProcessing
from ._CardDataReading11Code import CardDataReading11Code
from ._ISO18245MerchantCategoryCode import ISO18245MerchantCategoryCode
from ._ISO8583POSConditionCode import ISO8583POSConditionCode
from ._ISODate import ISODate
from ._JulianDate import JulianDate
from ._MOTO2Code import MOTO2Code
from ._Max10Text import Max10Text
from ._Max35NumericText import Max35NumericText
from ._Max35Text import Max35Text
from ._QRCodePresentmentMode2Code import QRCodePresentmentMode2Code
from ._SecurityCharacteristics2Code import SecurityCharacteristics2Code
from ._TransactionInitiator1Code import TransactionInitiator1Code
from ._TrueFalseIndicator import TrueFalseIndicator

class Context27(base_types._BaseFieldType):

	__slots__ = ["_Attndd", "_CardDataNtryMd", "_CardPres", "_CrdhldrActvtd", "_CrdhldrPres", "_DelydAuthstn", "_DelydChrgs", "_DtAntcptd", "_EComrc", "_EComrcData", "_EComrcIndApld", "_EComrcIndPropsd", "_MOTOCd", "_MaxPrcgDt", "_MrchntCtgyCd", "_MrchntCtgySpcfcData", "_NoShow", "_NtlData", "_OthrMrchntCtgy", "_POSCondCd", "_PmtCrdntlMrchntRltsh", "_PrtlApprvlSpprtd", "_PrtlShipmnt", "_PrvtData", "_QRCdPresntmntMd", "_ReSubmissn", "_Reauthstn", "_SctyChrtcs", "_StorgLctn", "_TempScrCardDataReusd", "_TrnspndrInittd", "_Trnst", "_TxInitr", "_UattnddLvlCtgy", "_VATDcmnttnReq", "_VATDcmnttnRspn"]
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
	def MaxPrcgDt(self):
		return self._MaxPrcgDt

	@MaxPrcgDt.setter
	def MaxPrcgDt(self, value):
		self._MaxPrcgDt = value if type(value) != base_types.auto else self.make_default("MaxPrcgDt")

	@MaxPrcgDt.deleter
	def MaxPrcgDt(self):
		del self._MaxPrcgDt
		self._MaxPrcgDt = None

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
	def POSCondCd(self):
		return self._POSCondCd

	@POSCondCd.setter
	def POSCondCd(self, value):
		self._POSCondCd = value if type(value) != base_types.auto else self.make_default("POSCondCd")

	@POSCondCd.deleter
	def POSCondCd(self):
		del self._POSCondCd
		self._POSCondCd = None

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
	def VATDcmnttnReq(self):
		return self._VATDcmnttnReq

	@VATDcmnttnReq.setter
	def VATDcmnttnReq(self, value):
		self._VATDcmnttnReq = value if type(value) != base_types.auto else self.make_default("VATDcmnttnReq")

	@VATDcmnttnReq.deleter
	def VATDcmnttnReq(self):
		del self._VATDcmnttnReq
		self._VATDcmnttnReq = None

	@property
	def VATDcmnttnRspn(self):
		return self._VATDcmnttnRspn

	@VATDcmnttnRspn.setter
	def VATDcmnttnRspn(self, value):
		self._VATDcmnttnRspn = value if type(value) != base_types.auto else self.make_default("VATDcmnttnRspn")

	@VATDcmnttnRspn.deleter
	def VATDcmnttnRspn(self):
		del self._VATDcmnttnRspn
		self._VATDcmnttnRspn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Attndd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardDataNtryMd', type=CardDataReading11Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardPres', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrdhldrActvtd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrdhldrPres', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DelydAuthstn', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DelydChrgs', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtAntcptd', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EComrc', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EComrcData', type=ATICALaxProcessing, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EComrcIndApld', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EComrcIndPropsd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MOTOCd', type=MOTO2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxPrcgDt', type=JulianDate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrchntCtgyCd', type=ISO18245MerchantCategoryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrchntCtgySpcfcData', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NoShow', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtlData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OthrMrchntCtgy', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POSCondCd', type=ISO8583POSConditionCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtCrdntlMrchntRltsh', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtlApprvlSpprtd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtlShipmnt', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvtData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='QRCdPresntmntMd', type=QRCodePresentmentMode2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReSubmissn', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Reauthstn', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyChrtcs', type=SecurityCharacteristics2Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StorgLctn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TempScrCardDataReusd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrnspndrInittd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trnst', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxInitr', type=TransactionInitiator1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UattnddLvlCtgy', type=Max35NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VATDcmnttnReq', type=Max10Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VATDcmnttnRspn', type=Max10Text, min=0, max=1, mutex_group=None, array=False),
	))