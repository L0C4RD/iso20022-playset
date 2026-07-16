# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActionMessage12
from . import CustomerOrderRequest1Code
from . import ISODateTime
from . import LanguageCode
from . import Max2NumericText
from . import Max35Text
from . import PointOfInteractionComponent18
from . import PointOfInteractionComponentIdentification2
from . import SaleTerminalData1
from . import SaleTokenScope1Code
from . import TrueFalseIndicator

class LoginRequest8(base_types._BaseFieldType):

	__slots__ = ["_CshrId", "_CshrLang", "_CstmrOrdrReq", "_LgnDtTm", "_OutptDisp", "_POIId", "_SaleSftwr", "_SaleTermnlData", "_ShftNb", "_TknReqdTp", "_TrngMdFlg", "_TtlsGrpId"]
	@property
	def CshrId(self):
		return self._CshrId

	@CshrId.setter
	def CshrId(self, value):
		self._CshrId = value if value is not None else base_types.UninitialisedField(self, 'CshrId', Max35Text, False)

	@CshrId.deleter
	def CshrId(self):
		del self._CshrId
		self._CshrId = base_types.UninitialisedField(self, 'CshrId', Max35Text, False)

	@property
	def CshrLang(self):
		return self._CshrLang

	@CshrLang.setter
	def CshrLang(self, value):
		self._CshrLang = value if value is not None else base_types.UninitialisedField(self, 'CshrLang', LanguageCode, False)

	@CshrLang.deleter
	def CshrLang(self):
		del self._CshrLang
		self._CshrLang = base_types.UninitialisedField(self, 'CshrLang', LanguageCode, False)

	@property
	def CstmrOrdrReq(self):
		return self._CstmrOrdrReq

	@CstmrOrdrReq.setter
	def CstmrOrdrReq(self, value):
		self._CstmrOrdrReq = value if value is not None else base_types.UninitialisedField(self, 'CstmrOrdrReq', CustomerOrderRequest1Code, False)

	@CstmrOrdrReq.deleter
	def CstmrOrdrReq(self):
		del self._CstmrOrdrReq
		self._CstmrOrdrReq = base_types.UninitialisedField(self, 'CstmrOrdrReq', CustomerOrderRequest1Code, False)

	@property
	def LgnDtTm(self):
		return self._LgnDtTm

	@LgnDtTm.setter
	def LgnDtTm(self, value):
		self._LgnDtTm = value if value is not None else base_types.UninitialisedField(self, 'LgnDtTm', ISODateTime, False)

	@LgnDtTm.deleter
	def LgnDtTm(self):
		del self._LgnDtTm
		self._LgnDtTm = base_types.UninitialisedField(self, 'LgnDtTm', ISODateTime, False)

	@property
	def OutptDisp(self):
		return self._OutptDisp

	@OutptDisp.setter
	def OutptDisp(self, value):
		self._OutptDisp = value if value is not None else base_types.UninitialisedField(self, 'OutptDisp', ActionMessage12, False)

	@OutptDisp.deleter
	def OutptDisp(self):
		del self._OutptDisp
		self._OutptDisp = base_types.UninitialisedField(self, 'OutptDisp', ActionMessage12, False)

	@property
	def POIId(self):
		return self._POIId

	@POIId.setter
	def POIId(self, value):
		self._POIId = value if value is not None else base_types.UninitialisedField(self, 'POIId', PointOfInteractionComponentIdentification2, False)

	@POIId.deleter
	def POIId(self):
		del self._POIId
		self._POIId = base_types.UninitialisedField(self, 'POIId', PointOfInteractionComponentIdentification2, False)

	@property
	def SaleSftwr(self):
		return self._SaleSftwr

	@SaleSftwr.setter
	def SaleSftwr(self, value):
		self._SaleSftwr = value if value is not None else base_types.UninitialisedField(self, 'SaleSftwr', PointOfInteractionComponent18, True)

	@SaleSftwr.deleter
	def SaleSftwr(self):
		del self._SaleSftwr
		self._SaleSftwr = base_types.UninitialisedField(self, 'SaleSftwr', PointOfInteractionComponent18, True)

	@property
	def SaleTermnlData(self):
		return self._SaleTermnlData

	@SaleTermnlData.setter
	def SaleTermnlData(self, value):
		self._SaleTermnlData = value if value is not None else base_types.UninitialisedField(self, 'SaleTermnlData', SaleTerminalData1, False)

	@SaleTermnlData.deleter
	def SaleTermnlData(self):
		del self._SaleTermnlData
		self._SaleTermnlData = base_types.UninitialisedField(self, 'SaleTermnlData', SaleTerminalData1, False)

	@property
	def ShftNb(self):
		return self._ShftNb

	@ShftNb.setter
	def ShftNb(self, value):
		self._ShftNb = value if value is not None else base_types.UninitialisedField(self, 'ShftNb', Max2NumericText, False)

	@ShftNb.deleter
	def ShftNb(self):
		del self._ShftNb
		self._ShftNb = base_types.UninitialisedField(self, 'ShftNb', Max2NumericText, False)

	@property
	def TknReqdTp(self):
		return self._TknReqdTp

	@TknReqdTp.setter
	def TknReqdTp(self, value):
		self._TknReqdTp = value if value is not None else base_types.UninitialisedField(self, 'TknReqdTp', SaleTokenScope1Code, False)

	@TknReqdTp.deleter
	def TknReqdTp(self):
		del self._TknReqdTp
		self._TknReqdTp = base_types.UninitialisedField(self, 'TknReqdTp', SaleTokenScope1Code, False)

	@property
	def TrngMdFlg(self):
		return self._TrngMdFlg

	@TrngMdFlg.setter
	def TrngMdFlg(self, value):
		self._TrngMdFlg = value if value is not None else base_types.UninitialisedField(self, 'TrngMdFlg', TrueFalseIndicator, False)

	@TrngMdFlg.deleter
	def TrngMdFlg(self):
		del self._TrngMdFlg
		self._TrngMdFlg = base_types.UninitialisedField(self, 'TrngMdFlg', TrueFalseIndicator, False)

	@property
	def TtlsGrpId(self):
		return self._TtlsGrpId

	@TtlsGrpId.setter
	def TtlsGrpId(self, value):
		self._TtlsGrpId = value if value is not None else base_types.UninitialisedField(self, 'TtlsGrpId', Max35Text, False)

	@TtlsGrpId.deleter
	def TtlsGrpId(self):
		del self._TtlsGrpId
		self._TtlsGrpId = base_types.UninitialisedField(self, 'TtlsGrpId', Max35Text, False)

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