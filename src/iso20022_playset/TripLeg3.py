from . import base_types
from .LoyaltyProgramme4 import LoyaltyProgramme4
from .AmountDetails3 import AmountDetails3
from .Max140Text import Max140Text
from .Max4Text import Max4Text
from .AdditionalData1 import AdditionalData1
from .DocumentReference1 import DocumentReference1
from .TransportType1Code import TransportType1Code
from .Max35Text import Max35Text
from .Max4NumericText import Max4NumericText
from .Max70Text import Max70Text
from .ISODate import ISODate
from .TrueFalseIndicator import TrueFalseIndicator
from .DepartureOrArrival1 import DepartureOrArrival1
from .Max35NumericText import Max35NumericText

class TripLeg3(base_types._BaseFieldType):

	__slots__ = ["_XchgdTcktNb", "_XchgdTckt", "_TrnsprtTp", "_RouteNb", "_CnjnctnTcktNb", "_TcktIsseDt", "_RsvatnNb", "_OpnTckt", "_Drtn", "_NonDrctRouteCd", "_LltyPrgrmm", "_TcktRstrctns", "_Insrnc", "_OrgnlRsvatnSys", "_OrgnlRsvatnNb", "_RstrctdTckt", "_IATACd", "_Amt", "_SeqNb", "_StopOver", "_CmmdtyCd", "_PrcdrId", "_Arrvl", "_TcktIssr", "_SvcClss", "_CdtRsnCd", "_Dprture", "_OthrTrnsprtTp", "_FairBsisCd", "_CrrierNm", "_AddtlData", "_Doc", "_RcrdLctrNb", "_RsvatnSys", "_TcktNb", "_TcktIsseLctn", "_CrrierCd"]
	@property
	def XchgdTcktNb(self):
		return self._XchgdTcktNb

	@XchgdTcktNb.setter
	def XchgdTcktNb(self, value):
		self._XchgdTcktNb = value if type(value) != base_types.auto else self.make_default("XchgdTcktNb")

	@XchgdTcktNb.deleter
	def XchgdTcktNb(self):
		del self._XchgdTcktNb
		self._XchgdTcktNb = None

	@property
	def XchgdTckt(self):
		return self._XchgdTckt

	@XchgdTckt.setter
	def XchgdTckt(self, value):
		self._XchgdTckt = value if type(value) != base_types.auto else self.make_default("XchgdTckt")

	@XchgdTckt.deleter
	def XchgdTckt(self):
		del self._XchgdTckt
		self._XchgdTckt = None

	@property
	def TrnsprtTp(self):
		return self._TrnsprtTp

	@TrnsprtTp.setter
	def TrnsprtTp(self, value):
		self._TrnsprtTp = value if type(value) != base_types.auto else self.make_default("TrnsprtTp")

	@TrnsprtTp.deleter
	def TrnsprtTp(self):
		del self._TrnsprtTp
		self._TrnsprtTp = None

	@property
	def RouteNb(self):
		return self._RouteNb

	@RouteNb.setter
	def RouteNb(self, value):
		self._RouteNb = value if type(value) != base_types.auto else self.make_default("RouteNb")

	@RouteNb.deleter
	def RouteNb(self):
		del self._RouteNb
		self._RouteNb = None

	@property
	def CnjnctnTcktNb(self):
		return self._CnjnctnTcktNb

	@CnjnctnTcktNb.setter
	def CnjnctnTcktNb(self, value):
		self._CnjnctnTcktNb = value if type(value) != base_types.auto else self.make_default("CnjnctnTcktNb")

	@CnjnctnTcktNb.deleter
	def CnjnctnTcktNb(self):
		del self._CnjnctnTcktNb
		self._CnjnctnTcktNb = None

	@property
	def TcktIsseDt(self):
		return self._TcktIsseDt

	@TcktIsseDt.setter
	def TcktIsseDt(self, value):
		self._TcktIsseDt = value if type(value) != base_types.auto else self.make_default("TcktIsseDt")

	@TcktIsseDt.deleter
	def TcktIsseDt(self):
		del self._TcktIsseDt
		self._TcktIsseDt = None

	@property
	def RsvatnNb(self):
		return self._RsvatnNb

	@RsvatnNb.setter
	def RsvatnNb(self, value):
		self._RsvatnNb = value if type(value) != base_types.auto else self.make_default("RsvatnNb")

	@RsvatnNb.deleter
	def RsvatnNb(self):
		del self._RsvatnNb
		self._RsvatnNb = None

	@property
	def OpnTckt(self):
		return self._OpnTckt

	@OpnTckt.setter
	def OpnTckt(self, value):
		self._OpnTckt = value if type(value) != base_types.auto else self.make_default("OpnTckt")

	@OpnTckt.deleter
	def OpnTckt(self):
		del self._OpnTckt
		self._OpnTckt = None

	@property
	def Drtn(self):
		return self._Drtn

	@Drtn.setter
	def Drtn(self, value):
		self._Drtn = value if type(value) != base_types.auto else self.make_default("Drtn")

	@Drtn.deleter
	def Drtn(self):
		del self._Drtn
		self._Drtn = None

	@property
	def NonDrctRouteCd(self):
		return self._NonDrctRouteCd

	@NonDrctRouteCd.setter
	def NonDrctRouteCd(self, value):
		self._NonDrctRouteCd = value if type(value) != base_types.auto else self.make_default("NonDrctRouteCd")

	@NonDrctRouteCd.deleter
	def NonDrctRouteCd(self):
		del self._NonDrctRouteCd
		self._NonDrctRouteCd = None

	@property
	def LltyPrgrmm(self):
		return self._LltyPrgrmm

	@LltyPrgrmm.setter
	def LltyPrgrmm(self, value):
		self._LltyPrgrmm = value if type(value) != base_types.auto else self.make_default("LltyPrgrmm")

	@LltyPrgrmm.deleter
	def LltyPrgrmm(self):
		del self._LltyPrgrmm
		self._LltyPrgrmm = None

	@property
	def TcktRstrctns(self):
		return self._TcktRstrctns

	@TcktRstrctns.setter
	def TcktRstrctns(self, value):
		self._TcktRstrctns = value if type(value) != base_types.auto else self.make_default("TcktRstrctns")

	@TcktRstrctns.deleter
	def TcktRstrctns(self):
		del self._TcktRstrctns
		self._TcktRstrctns = None

	@property
	def Insrnc(self):
		return self._Insrnc

	@Insrnc.setter
	def Insrnc(self, value):
		self._Insrnc = value if type(value) != base_types.auto else self.make_default("Insrnc")

	@Insrnc.deleter
	def Insrnc(self):
		del self._Insrnc
		self._Insrnc = None

	@property
	def OrgnlRsvatnSys(self):
		return self._OrgnlRsvatnSys

	@OrgnlRsvatnSys.setter
	def OrgnlRsvatnSys(self, value):
		self._OrgnlRsvatnSys = value if type(value) != base_types.auto else self.make_default("OrgnlRsvatnSys")

	@OrgnlRsvatnSys.deleter
	def OrgnlRsvatnSys(self):
		del self._OrgnlRsvatnSys
		self._OrgnlRsvatnSys = None

	@property
	def OrgnlRsvatnNb(self):
		return self._OrgnlRsvatnNb

	@OrgnlRsvatnNb.setter
	def OrgnlRsvatnNb(self, value):
		self._OrgnlRsvatnNb = value if type(value) != base_types.auto else self.make_default("OrgnlRsvatnNb")

	@OrgnlRsvatnNb.deleter
	def OrgnlRsvatnNb(self):
		del self._OrgnlRsvatnNb
		self._OrgnlRsvatnNb = None

	@property
	def RstrctdTckt(self):
		return self._RstrctdTckt

	@RstrctdTckt.setter
	def RstrctdTckt(self, value):
		self._RstrctdTckt = value if type(value) != base_types.auto else self.make_default("RstrctdTckt")

	@RstrctdTckt.deleter
	def RstrctdTckt(self):
		del self._RstrctdTckt
		self._RstrctdTckt = None

	@property
	def IATACd(self):
		return self._IATACd

	@IATACd.setter
	def IATACd(self, value):
		self._IATACd = value if type(value) != base_types.auto else self.make_default("IATACd")

	@IATACd.deleter
	def IATACd(self):
		del self._IATACd
		self._IATACd = None

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
	def SeqNb(self):
		return self._SeqNb

	@SeqNb.setter
	def SeqNb(self, value):
		self._SeqNb = value if type(value) != base_types.auto else self.make_default("SeqNb")

	@SeqNb.deleter
	def SeqNb(self):
		del self._SeqNb
		self._SeqNb = None

	@property
	def StopOver(self):
		return self._StopOver

	@StopOver.setter
	def StopOver(self, value):
		self._StopOver = value if type(value) != base_types.auto else self.make_default("StopOver")

	@StopOver.deleter
	def StopOver(self):
		del self._StopOver
		self._StopOver = None

	@property
	def CmmdtyCd(self):
		return self._CmmdtyCd

	@CmmdtyCd.setter
	def CmmdtyCd(self, value):
		self._CmmdtyCd = value if type(value) != base_types.auto else self.make_default("CmmdtyCd")

	@CmmdtyCd.deleter
	def CmmdtyCd(self):
		del self._CmmdtyCd
		self._CmmdtyCd = None

	@property
	def PrcdrId(self):
		return self._PrcdrId

	@PrcdrId.setter
	def PrcdrId(self, value):
		self._PrcdrId = value if type(value) != base_types.auto else self.make_default("PrcdrId")

	@PrcdrId.deleter
	def PrcdrId(self):
		del self._PrcdrId
		self._PrcdrId = None

	@property
	def Arrvl(self):
		return self._Arrvl

	@Arrvl.setter
	def Arrvl(self, value):
		self._Arrvl = value if type(value) != base_types.auto else self.make_default("Arrvl")

	@Arrvl.deleter
	def Arrvl(self):
		del self._Arrvl
		self._Arrvl = None

	@property
	def TcktIssr(self):
		return self._TcktIssr

	@TcktIssr.setter
	def TcktIssr(self, value):
		self._TcktIssr = value if type(value) != base_types.auto else self.make_default("TcktIssr")

	@TcktIssr.deleter
	def TcktIssr(self):
		del self._TcktIssr
		self._TcktIssr = None

	@property
	def SvcClss(self):
		return self._SvcClss

	@SvcClss.setter
	def SvcClss(self, value):
		self._SvcClss = value if type(value) != base_types.auto else self.make_default("SvcClss")

	@SvcClss.deleter
	def SvcClss(self):
		del self._SvcClss
		self._SvcClss = None

	@property
	def CdtRsnCd(self):
		return self._CdtRsnCd

	@CdtRsnCd.setter
	def CdtRsnCd(self, value):
		self._CdtRsnCd = value if type(value) != base_types.auto else self.make_default("CdtRsnCd")

	@CdtRsnCd.deleter
	def CdtRsnCd(self):
		del self._CdtRsnCd
		self._CdtRsnCd = None

	@property
	def Dprture(self):
		return self._Dprture

	@Dprture.setter
	def Dprture(self, value):
		self._Dprture = value if type(value) != base_types.auto else self.make_default("Dprture")

	@Dprture.deleter
	def Dprture(self):
		del self._Dprture
		self._Dprture = None

	@property
	def OthrTrnsprtTp(self):
		return self._OthrTrnsprtTp

	@OthrTrnsprtTp.setter
	def OthrTrnsprtTp(self, value):
		self._OthrTrnsprtTp = value if type(value) != base_types.auto else self.make_default("OthrTrnsprtTp")

	@OthrTrnsprtTp.deleter
	def OthrTrnsprtTp(self):
		del self._OthrTrnsprtTp
		self._OthrTrnsprtTp = None

	@property
	def FairBsisCd(self):
		return self._FairBsisCd

	@FairBsisCd.setter
	def FairBsisCd(self, value):
		self._FairBsisCd = value if type(value) != base_types.auto else self.make_default("FairBsisCd")

	@FairBsisCd.deleter
	def FairBsisCd(self):
		del self._FairBsisCd
		self._FairBsisCd = None

	@property
	def CrrierNm(self):
		return self._CrrierNm

	@CrrierNm.setter
	def CrrierNm(self, value):
		self._CrrierNm = value if type(value) != base_types.auto else self.make_default("CrrierNm")

	@CrrierNm.deleter
	def CrrierNm(self):
		del self._CrrierNm
		self._CrrierNm = None

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
	def Doc(self):
		return self._Doc

	@Doc.setter
	def Doc(self, value):
		self._Doc = value if type(value) != base_types.auto else self.make_default("Doc")

	@Doc.deleter
	def Doc(self):
		del self._Doc
		self._Doc = None

	@property
	def RcrdLctrNb(self):
		return self._RcrdLctrNb

	@RcrdLctrNb.setter
	def RcrdLctrNb(self, value):
		self._RcrdLctrNb = value if type(value) != base_types.auto else self.make_default("RcrdLctrNb")

	@RcrdLctrNb.deleter
	def RcrdLctrNb(self):
		del self._RcrdLctrNb
		self._RcrdLctrNb = None

	@property
	def RsvatnSys(self):
		return self._RsvatnSys

	@RsvatnSys.setter
	def RsvatnSys(self, value):
		self._RsvatnSys = value if type(value) != base_types.auto else self.make_default("RsvatnSys")

	@RsvatnSys.deleter
	def RsvatnSys(self):
		del self._RsvatnSys
		self._RsvatnSys = None

	@property
	def TcktNb(self):
		return self._TcktNb

	@TcktNb.setter
	def TcktNb(self, value):
		self._TcktNb = value if type(value) != base_types.auto else self.make_default("TcktNb")

	@TcktNb.deleter
	def TcktNb(self):
		del self._TcktNb
		self._TcktNb = None

	@property
	def TcktIsseLctn(self):
		return self._TcktIsseLctn

	@TcktIsseLctn.setter
	def TcktIsseLctn(self, value):
		self._TcktIsseLctn = value if type(value) != base_types.auto else self.make_default("TcktIsseLctn")

	@TcktIsseLctn.deleter
	def TcktIsseLctn(self):
		del self._TcktIsseLctn
		self._TcktIsseLctn = None

	@property
	def CrrierCd(self):
		return self._CrrierCd

	@CrrierCd.setter
	def CrrierCd(self, value):
		self._CrrierCd = value if type(value) != base_types.auto else self.make_default("CrrierCd")

	@CrrierCd.deleter
	def CrrierCd(self):
		del self._CrrierCd
		self._CrrierCd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='XchgdTcktNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgdTckt', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrnsprtTp', type=TransportType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RouteNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CnjnctnTcktNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TcktIsseDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsvatnNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OpnTckt', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Drtn', type=Max4NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonDrctRouteCd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LltyPrgrmm', type=LoyaltyProgramme4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TcktRstrctns', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Insrnc', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlRsvatnSys', type=Max4Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlRsvatnNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RstrctdTckt', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IATACd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=AmountDetails3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SeqNb', type=Max35NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StopOver', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmmdtyCd', type=Max4Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcdrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Arrvl', type=DepartureOrArrival1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TcktIssr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcClss', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtRsnCd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dprture', type=DepartureOrArrival1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrTrnsprtTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FairBsisCd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrrierNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlData', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Doc', type=DocumentReference1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RcrdLctrNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsvatnSys', type=Max4Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TcktNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TcktIsseLctn', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrrierCd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

