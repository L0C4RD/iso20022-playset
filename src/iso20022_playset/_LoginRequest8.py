from . import base_types
from ._ActionMessage12 import ActionMessage12
from ._CustomerOrderRequest1Code import CustomerOrderRequest1Code
from ._ISODateTime import ISODateTime
from ._LanguageCode import LanguageCode
from ._Max2NumericText import Max2NumericText
from ._Max35Text import Max35Text
from ._PointOfInteractionComponent18 import PointOfInteractionComponent18
from ._PointOfInteractionComponentIdentification2 import PointOfInteractionComponentIdentification2
from ._SaleTerminalData1 import SaleTerminalData1
from ._SaleTokenScope1Code import SaleTokenScope1Code
from ._TrueFalseIndicator import TrueFalseIndicator

class LoginRequest8(base_types._BaseFieldType):

	__slots__ = ["_CshrId", "_CshrLang", "_CstmrOrdrReq", "_LgnDtTm", "_OutptDisp", "_POIId", "_SaleSftwr", "_SaleTermnlData", "_ShftNb", "_TknReqdTp", "_TrngMdFlg", "_TtlsGrpId"]
	@property
	def CshrId(self):
		return self._CshrId

	@CshrId.setter
	def CshrId(self, value):
		self._CshrId = value if type(value) != base_types.auto else self.make_default("CshrId")

	@CshrId.deleter
	def CshrId(self):
		del self._CshrId
		self._CshrId = None

	@property
	def CshrLang(self):
		return self._CshrLang

	@CshrLang.setter
	def CshrLang(self, value):
		self._CshrLang = value if type(value) != base_types.auto else self.make_default("CshrLang")

	@CshrLang.deleter
	def CshrLang(self):
		del self._CshrLang
		self._CshrLang = None

	@property
	def CstmrOrdrReq(self):
		return self._CstmrOrdrReq

	@CstmrOrdrReq.setter
	def CstmrOrdrReq(self, value):
		self._CstmrOrdrReq = value if type(value) != base_types.auto else self.make_default("CstmrOrdrReq")

	@CstmrOrdrReq.deleter
	def CstmrOrdrReq(self):
		del self._CstmrOrdrReq
		self._CstmrOrdrReq = None

	@property
	def LgnDtTm(self):
		return self._LgnDtTm

	@LgnDtTm.setter
	def LgnDtTm(self, value):
		self._LgnDtTm = value if type(value) != base_types.auto else self.make_default("LgnDtTm")

	@LgnDtTm.deleter
	def LgnDtTm(self):
		del self._LgnDtTm
		self._LgnDtTm = None

	@property
	def OutptDisp(self):
		return self._OutptDisp

	@OutptDisp.setter
	def OutptDisp(self, value):
		self._OutptDisp = value if type(value) != base_types.auto else self.make_default("OutptDisp")

	@OutptDisp.deleter
	def OutptDisp(self):
		del self._OutptDisp
		self._OutptDisp = None

	@property
	def POIId(self):
		return self._POIId

	@POIId.setter
	def POIId(self, value):
		self._POIId = value if type(value) != base_types.auto else self.make_default("POIId")

	@POIId.deleter
	def POIId(self):
		del self._POIId
		self._POIId = None

	@property
	def SaleSftwr(self):
		return self._SaleSftwr

	@SaleSftwr.setter
	def SaleSftwr(self, value):
		self._SaleSftwr = value if type(value) != base_types.auto else self.make_default("SaleSftwr")

	@SaleSftwr.deleter
	def SaleSftwr(self):
		del self._SaleSftwr
		self._SaleSftwr = None

	@property
	def SaleTermnlData(self):
		return self._SaleTermnlData

	@SaleTermnlData.setter
	def SaleTermnlData(self, value):
		self._SaleTermnlData = value if type(value) != base_types.auto else self.make_default("SaleTermnlData")

	@SaleTermnlData.deleter
	def SaleTermnlData(self):
		del self._SaleTermnlData
		self._SaleTermnlData = None

	@property
	def ShftNb(self):
		return self._ShftNb

	@ShftNb.setter
	def ShftNb(self, value):
		self._ShftNb = value if type(value) != base_types.auto else self.make_default("ShftNb")

	@ShftNb.deleter
	def ShftNb(self):
		del self._ShftNb
		self._ShftNb = None

	@property
	def TknReqdTp(self):
		return self._TknReqdTp

	@TknReqdTp.setter
	def TknReqdTp(self, value):
		self._TknReqdTp = value if type(value) != base_types.auto else self.make_default("TknReqdTp")

	@TknReqdTp.deleter
	def TknReqdTp(self):
		del self._TknReqdTp
		self._TknReqdTp = None

	@property
	def TrngMdFlg(self):
		return self._TrngMdFlg

	@TrngMdFlg.setter
	def TrngMdFlg(self, value):
		self._TrngMdFlg = value if type(value) != base_types.auto else self.make_default("TrngMdFlg")

	@TrngMdFlg.deleter
	def TrngMdFlg(self):
		del self._TrngMdFlg
		self._TrngMdFlg = None

	@property
	def TtlsGrpId(self):
		return self._TtlsGrpId

	@TtlsGrpId.setter
	def TtlsGrpId(self, value):
		self._TtlsGrpId = value if type(value) != base_types.auto else self.make_default("TtlsGrpId")

	@TtlsGrpId.deleter
	def TtlsGrpId(self):
		del self._TtlsGrpId
		self._TtlsGrpId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshrLang', type=LanguageCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrOrdrReq', type=CustomerOrderRequest1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LgnDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OutptDisp', type=ActionMessage12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POIId', type=PointOfInteractionComponentIdentification2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleSftwr', type=PointOfInteractionComponent18, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SaleTermnlData', type=SaleTerminalData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShftNb', type=Max2NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TknReqdTp', type=SaleTokenScope1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrngMdFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlsGrpId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

