# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalData1
from . import AmountDetails3
from . import DepartureOrArrival1
from . import DocumentReference1
from . import ISODate
from . import LoyaltyProgramme4
from . import Max140Text
from . import Max35NumericText
from . import Max35Text
from . import Max4NumericText
from . import Max4Text
from . import Max70Text
from . import TransportType1Code
from . import TrueFalseIndicator

class TripLeg3(base_types._BaseFieldType):

	__slots__ = ["_AddtlData", "_Amt", "_Arrvl", "_CdtRsnCd", "_CmmdtyCd", "_CnjnctnTcktNb", "_CrrierCd", "_CrrierNm", "_Doc", "_Dprture", "_Drtn", "_FairBsisCd", "_IATACd", "_Insrnc", "_LltyPrgrmm", "_NonDrctRouteCd", "_OpnTckt", "_OrgnlRsvatnNb", "_OrgnlRsvatnSys", "_OthrTrnsprtTp", "_PrcdrId", "_RcrdLctrNb", "_RouteNb", "_RstrctdTckt", "_RsvatnNb", "_RsvatnSys", "_SeqNb", "_StopOver", "_SvcClss", "_TcktIsseDt", "_TcktIsseLctn", "_TcktIssr", "_TcktNb", "_TcktRstrctns", "_TrnsprtTp", "_XchgdTckt", "_XchgdTcktNb"]
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
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', AmountDetails3, True)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', AmountDetails3, True)

	@property
	def Arrvl(self):
		return self._Arrvl

	@Arrvl.setter
	def Arrvl(self, value):
		self._Arrvl = value if value is not None else base_types.UninitialisedField(self, 'Arrvl', DepartureOrArrival1, False)

	@Arrvl.deleter
	def Arrvl(self):
		del self._Arrvl
		self._Arrvl = base_types.UninitialisedField(self, 'Arrvl', DepartureOrArrival1, False)

	@property
	def CdtRsnCd(self):
		return self._CdtRsnCd

	@CdtRsnCd.setter
	def CdtRsnCd(self, value):
		self._CdtRsnCd = value if value is not None else base_types.UninitialisedField(self, 'CdtRsnCd', Max35Text, False)

	@CdtRsnCd.deleter
	def CdtRsnCd(self):
		del self._CdtRsnCd
		self._CdtRsnCd = base_types.UninitialisedField(self, 'CdtRsnCd', Max35Text, False)

	@property
	def CmmdtyCd(self):
		return self._CmmdtyCd

	@CmmdtyCd.setter
	def CmmdtyCd(self, value):
		self._CmmdtyCd = value if value is not None else base_types.UninitialisedField(self, 'CmmdtyCd', Max4Text, False)

	@CmmdtyCd.deleter
	def CmmdtyCd(self):
		del self._CmmdtyCd
		self._CmmdtyCd = base_types.UninitialisedField(self, 'CmmdtyCd', Max4Text, False)

	@property
	def CnjnctnTcktNb(self):
		return self._CnjnctnTcktNb

	@CnjnctnTcktNb.setter
	def CnjnctnTcktNb(self, value):
		self._CnjnctnTcktNb = value if value is not None else base_types.UninitialisedField(self, 'CnjnctnTcktNb', Max35Text, False)

	@CnjnctnTcktNb.deleter
	def CnjnctnTcktNb(self):
		del self._CnjnctnTcktNb
		self._CnjnctnTcktNb = base_types.UninitialisedField(self, 'CnjnctnTcktNb', Max35Text, False)

	@property
	def CrrierCd(self):
		return self._CrrierCd

	@CrrierCd.setter
	def CrrierCd(self, value):
		self._CrrierCd = value if value is not None else base_types.UninitialisedField(self, 'CrrierCd', Max35Text, False)

	@CrrierCd.deleter
	def CrrierCd(self):
		del self._CrrierCd
		self._CrrierCd = base_types.UninitialisedField(self, 'CrrierCd', Max35Text, False)

	@property
	def CrrierNm(self):
		return self._CrrierNm

	@CrrierNm.setter
	def CrrierNm(self, value):
		self._CrrierNm = value if value is not None else base_types.UninitialisedField(self, 'CrrierNm', Max70Text, False)

	@CrrierNm.deleter
	def CrrierNm(self):
		del self._CrrierNm
		self._CrrierNm = base_types.UninitialisedField(self, 'CrrierNm', Max70Text, False)

	@property
	def Doc(self):
		return self._Doc

	@Doc.setter
	def Doc(self, value):
		self._Doc = value if value is not None else base_types.UninitialisedField(self, 'Doc', DocumentReference1, True)

	@Doc.deleter
	def Doc(self):
		del self._Doc
		self._Doc = base_types.UninitialisedField(self, 'Doc', DocumentReference1, True)

	@property
	def Dprture(self):
		return self._Dprture

	@Dprture.setter
	def Dprture(self, value):
		self._Dprture = value if value is not None else base_types.UninitialisedField(self, 'Dprture', DepartureOrArrival1, False)

	@Dprture.deleter
	def Dprture(self):
		del self._Dprture
		self._Dprture = base_types.UninitialisedField(self, 'Dprture', DepartureOrArrival1, False)

	@property
	def Drtn(self):
		return self._Drtn

	@Drtn.setter
	def Drtn(self, value):
		self._Drtn = value if value is not None else base_types.UninitialisedField(self, 'Drtn', Max4NumericText, False)

	@Drtn.deleter
	def Drtn(self):
		del self._Drtn
		self._Drtn = base_types.UninitialisedField(self, 'Drtn', Max4NumericText, False)

	@property
	def FairBsisCd(self):
		return self._FairBsisCd

	@FairBsisCd.setter
	def FairBsisCd(self, value):
		self._FairBsisCd = value if value is not None else base_types.UninitialisedField(self, 'FairBsisCd', Max35Text, False)

	@FairBsisCd.deleter
	def FairBsisCd(self):
		del self._FairBsisCd
		self._FairBsisCd = base_types.UninitialisedField(self, 'FairBsisCd', Max35Text, False)

	@property
	def IATACd(self):
		return self._IATACd

	@IATACd.setter
	def IATACd(self, value):
		self._IATACd = value if value is not None else base_types.UninitialisedField(self, 'IATACd', Max35Text, False)

	@IATACd.deleter
	def IATACd(self):
		del self._IATACd
		self._IATACd = base_types.UninitialisedField(self, 'IATACd', Max35Text, False)

	@property
	def Insrnc(self):
		return self._Insrnc

	@Insrnc.setter
	def Insrnc(self, value):
		self._Insrnc = value if value is not None else base_types.UninitialisedField(self, 'Insrnc', TrueFalseIndicator, False)

	@Insrnc.deleter
	def Insrnc(self):
		del self._Insrnc
		self._Insrnc = base_types.UninitialisedField(self, 'Insrnc', TrueFalseIndicator, False)

	@property
	def LltyPrgrmm(self):
		return self._LltyPrgrmm

	@LltyPrgrmm.setter
	def LltyPrgrmm(self, value):
		self._LltyPrgrmm = value if value is not None else base_types.UninitialisedField(self, 'LltyPrgrmm', LoyaltyProgramme4, False)

	@LltyPrgrmm.deleter
	def LltyPrgrmm(self):
		del self._LltyPrgrmm
		self._LltyPrgrmm = base_types.UninitialisedField(self, 'LltyPrgrmm', LoyaltyProgramme4, False)

	@property
	def NonDrctRouteCd(self):
		return self._NonDrctRouteCd

	@NonDrctRouteCd.setter
	def NonDrctRouteCd(self, value):
		self._NonDrctRouteCd = value if value is not None else base_types.UninitialisedField(self, 'NonDrctRouteCd', Max35Text, False)

	@NonDrctRouteCd.deleter
	def NonDrctRouteCd(self):
		del self._NonDrctRouteCd
		self._NonDrctRouteCd = base_types.UninitialisedField(self, 'NonDrctRouteCd', Max35Text, False)

	@property
	def OpnTckt(self):
		return self._OpnTckt

	@OpnTckt.setter
	def OpnTckt(self, value):
		self._OpnTckt = value if value is not None else base_types.UninitialisedField(self, 'OpnTckt', TrueFalseIndicator, False)

	@OpnTckt.deleter
	def OpnTckt(self):
		del self._OpnTckt
		self._OpnTckt = base_types.UninitialisedField(self, 'OpnTckt', TrueFalseIndicator, False)

	@property
	def OrgnlRsvatnNb(self):
		return self._OrgnlRsvatnNb

	@OrgnlRsvatnNb.setter
	def OrgnlRsvatnNb(self, value):
		self._OrgnlRsvatnNb = value if value is not None else base_types.UninitialisedField(self, 'OrgnlRsvatnNb', Max35Text, False)

	@OrgnlRsvatnNb.deleter
	def OrgnlRsvatnNb(self):
		del self._OrgnlRsvatnNb
		self._OrgnlRsvatnNb = base_types.UninitialisedField(self, 'OrgnlRsvatnNb', Max35Text, False)

	@property
	def OrgnlRsvatnSys(self):
		return self._OrgnlRsvatnSys

	@OrgnlRsvatnSys.setter
	def OrgnlRsvatnSys(self, value):
		self._OrgnlRsvatnSys = value if value is not None else base_types.UninitialisedField(self, 'OrgnlRsvatnSys', Max4Text, False)

	@OrgnlRsvatnSys.deleter
	def OrgnlRsvatnSys(self):
		del self._OrgnlRsvatnSys
		self._OrgnlRsvatnSys = base_types.UninitialisedField(self, 'OrgnlRsvatnSys', Max4Text, False)

	@property
	def OthrTrnsprtTp(self):
		return self._OthrTrnsprtTp

	@OthrTrnsprtTp.setter
	def OthrTrnsprtTp(self, value):
		self._OthrTrnsprtTp = value if value is not None else base_types.UninitialisedField(self, 'OthrTrnsprtTp', Max35Text, False)

	@OthrTrnsprtTp.deleter
	def OthrTrnsprtTp(self):
		del self._OthrTrnsprtTp
		self._OthrTrnsprtTp = base_types.UninitialisedField(self, 'OthrTrnsprtTp', Max35Text, False)

	@property
	def PrcdrId(self):
		return self._PrcdrId

	@PrcdrId.setter
	def PrcdrId(self, value):
		self._PrcdrId = value if value is not None else base_types.UninitialisedField(self, 'PrcdrId', Max35Text, False)

	@PrcdrId.deleter
	def PrcdrId(self):
		del self._PrcdrId
		self._PrcdrId = base_types.UninitialisedField(self, 'PrcdrId', Max35Text, False)

	@property
	def RcrdLctrNb(self):
		return self._RcrdLctrNb

	@RcrdLctrNb.setter
	def RcrdLctrNb(self, value):
		self._RcrdLctrNb = value if value is not None else base_types.UninitialisedField(self, 'RcrdLctrNb', Max35Text, False)

	@RcrdLctrNb.deleter
	def RcrdLctrNb(self):
		del self._RcrdLctrNb
		self._RcrdLctrNb = base_types.UninitialisedField(self, 'RcrdLctrNb', Max35Text, False)

	@property
	def RouteNb(self):
		return self._RouteNb

	@RouteNb.setter
	def RouteNb(self, value):
		self._RouteNb = value if value is not None else base_types.UninitialisedField(self, 'RouteNb', Max35Text, False)

	@RouteNb.deleter
	def RouteNb(self):
		del self._RouteNb
		self._RouteNb = base_types.UninitialisedField(self, 'RouteNb', Max35Text, False)

	@property
	def RstrctdTckt(self):
		return self._RstrctdTckt

	@RstrctdTckt.setter
	def RstrctdTckt(self, value):
		self._RstrctdTckt = value if value is not None else base_types.UninitialisedField(self, 'RstrctdTckt', TrueFalseIndicator, False)

	@RstrctdTckt.deleter
	def RstrctdTckt(self):
		del self._RstrctdTckt
		self._RstrctdTckt = base_types.UninitialisedField(self, 'RstrctdTckt', TrueFalseIndicator, False)

	@property
	def RsvatnNb(self):
		return self._RsvatnNb

	@RsvatnNb.setter
	def RsvatnNb(self, value):
		self._RsvatnNb = value if value is not None else base_types.UninitialisedField(self, 'RsvatnNb', Max35Text, False)

	@RsvatnNb.deleter
	def RsvatnNb(self):
		del self._RsvatnNb
		self._RsvatnNb = base_types.UninitialisedField(self, 'RsvatnNb', Max35Text, False)

	@property
	def RsvatnSys(self):
		return self._RsvatnSys

	@RsvatnSys.setter
	def RsvatnSys(self, value):
		self._RsvatnSys = value if value is not None else base_types.UninitialisedField(self, 'RsvatnSys', Max4Text, False)

	@RsvatnSys.deleter
	def RsvatnSys(self):
		del self._RsvatnSys
		self._RsvatnSys = base_types.UninitialisedField(self, 'RsvatnSys', Max4Text, False)

	@property
	def SeqNb(self):
		return self._SeqNb

	@SeqNb.setter
	def SeqNb(self, value):
		self._SeqNb = value if value is not None else base_types.UninitialisedField(self, 'SeqNb', Max35NumericText, False)

	@SeqNb.deleter
	def SeqNb(self):
		del self._SeqNb
		self._SeqNb = base_types.UninitialisedField(self, 'SeqNb', Max35NumericText, False)

	@property
	def StopOver(self):
		return self._StopOver

	@StopOver.setter
	def StopOver(self, value):
		self._StopOver = value if value is not None else base_types.UninitialisedField(self, 'StopOver', TrueFalseIndicator, False)

	@StopOver.deleter
	def StopOver(self):
		del self._StopOver
		self._StopOver = base_types.UninitialisedField(self, 'StopOver', TrueFalseIndicator, False)

	@property
	def SvcClss(self):
		return self._SvcClss

	@SvcClss.setter
	def SvcClss(self, value):
		self._SvcClss = value if value is not None else base_types.UninitialisedField(self, 'SvcClss', Max35Text, False)

	@SvcClss.deleter
	def SvcClss(self):
		del self._SvcClss
		self._SvcClss = base_types.UninitialisedField(self, 'SvcClss', Max35Text, False)

	@property
	def TcktIsseDt(self):
		return self._TcktIsseDt

	@TcktIsseDt.setter
	def TcktIsseDt(self, value):
		self._TcktIsseDt = value if value is not None else base_types.UninitialisedField(self, 'TcktIsseDt', ISODate, False)

	@TcktIsseDt.deleter
	def TcktIsseDt(self):
		del self._TcktIsseDt
		self._TcktIsseDt = base_types.UninitialisedField(self, 'TcktIsseDt', ISODate, False)

	@property
	def TcktIsseLctn(self):
		return self._TcktIsseLctn

	@TcktIsseLctn.setter
	def TcktIsseLctn(self, value):
		self._TcktIsseLctn = value if value is not None else base_types.UninitialisedField(self, 'TcktIsseLctn', Max140Text, False)

	@TcktIsseLctn.deleter
	def TcktIsseLctn(self):
		del self._TcktIsseLctn
		self._TcktIsseLctn = base_types.UninitialisedField(self, 'TcktIsseLctn', Max140Text, False)

	@property
	def TcktIssr(self):
		return self._TcktIssr

	@TcktIssr.setter
	def TcktIssr(self, value):
		self._TcktIssr = value if value is not None else base_types.UninitialisedField(self, 'TcktIssr', Max35Text, False)

	@TcktIssr.deleter
	def TcktIssr(self):
		del self._TcktIssr
		self._TcktIssr = base_types.UninitialisedField(self, 'TcktIssr', Max35Text, False)

	@property
	def TcktNb(self):
		return self._TcktNb

	@TcktNb.setter
	def TcktNb(self, value):
		self._TcktNb = value if value is not None else base_types.UninitialisedField(self, 'TcktNb', Max35Text, False)

	@TcktNb.deleter
	def TcktNb(self):
		del self._TcktNb
		self._TcktNb = base_types.UninitialisedField(self, 'TcktNb', Max35Text, False)

	@property
	def TcktRstrctns(self):
		return self._TcktRstrctns

	@TcktRstrctns.setter
	def TcktRstrctns(self, value):
		self._TcktRstrctns = value if value is not None else base_types.UninitialisedField(self, 'TcktRstrctns', Max70Text, False)

	@TcktRstrctns.deleter
	def TcktRstrctns(self):
		del self._TcktRstrctns
		self._TcktRstrctns = base_types.UninitialisedField(self, 'TcktRstrctns', Max70Text, False)

	@property
	def TrnsprtTp(self):
		return self._TrnsprtTp

	@TrnsprtTp.setter
	def TrnsprtTp(self, value):
		self._TrnsprtTp = value if value is not None else base_types.UninitialisedField(self, 'TrnsprtTp', TransportType1Code, False)

	@TrnsprtTp.deleter
	def TrnsprtTp(self):
		del self._TrnsprtTp
		self._TrnsprtTp = base_types.UninitialisedField(self, 'TrnsprtTp', TransportType1Code, False)

	@property
	def XchgdTckt(self):
		return self._XchgdTckt

	@XchgdTckt.setter
	def XchgdTckt(self, value):
		self._XchgdTckt = value if value is not None else base_types.UninitialisedField(self, 'XchgdTckt', TrueFalseIndicator, False)

	@XchgdTckt.deleter
	def XchgdTckt(self):
		del self._XchgdTckt
		self._XchgdTckt = base_types.UninitialisedField(self, 'XchgdTckt', TrueFalseIndicator, False)

	@property
	def XchgdTcktNb(self):
		return self._XchgdTcktNb

	@XchgdTcktNb.setter
	def XchgdTcktNb(self, value):
		self._XchgdTcktNb = value if value is not None else base_types.UninitialisedField(self, 'XchgdTcktNb', Max35Text, False)

	@XchgdTcktNb.deleter
	def XchgdTcktNb(self):
		del self._XchgdTcktNb
		self._XchgdTcktNb = base_types.UninitialisedField(self, 'XchgdTcktNb', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlData', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Amt', type=AmountDetails3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Arrvl', type=DepartureOrArrival1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtRsnCd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmmdtyCd', type=Max4Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CnjnctnTcktNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrrierCd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrrierNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Doc', type=DocumentReference1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Dprture', type=DepartureOrArrival1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Drtn', type=Max4NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FairBsisCd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IATACd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Insrnc', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LltyPrgrmm', type=LoyaltyProgramme4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonDrctRouteCd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OpnTckt', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlRsvatnNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlRsvatnSys', type=Max4Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrTrnsprtTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcdrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcrdLctrNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RouteNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RstrctdTckt', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsvatnNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsvatnSys', type=Max4Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SeqNb', type=Max35NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StopOver', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcClss', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TcktIsseDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TcktIsseLctn', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TcktIssr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TcktNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TcktRstrctns', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrnsprtTp', type=TransportType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgdTckt', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgdTcktNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))