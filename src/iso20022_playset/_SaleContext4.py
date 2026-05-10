from . import base_types
from ._CardDataReading8Code import CardDataReading8Code
from ._ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from ._LanguageCode import LanguageCode
from ._Max2NumericText import Max2NumericText
from ._Max35Text import Max35Text
from ._Max70Text import Max70Text
from ._Organisation26 import Organisation26
from ._SaleTokenScope1Code import SaleTokenScope1Code
from ._TrueFalseIndicator import TrueFalseIndicator

class SaleContext4(base_types._BaseFieldType):

	__slots__ = ["_AddtlSaleData", "_AllwdNtryMd", "_CshrId", "_CshrLang", "_CstmrOrdrReqFlg", "_DlvryNoteNb", "_ForceOnlnFlg", "_InvcNb", "_PurchsOrdrNb", "_ReuseCardDataFlg", "_RmngAmt", "_SaleId", "_SaleRcncltnId", "_SaleRefNb", "_SaleTknScp", "_ShftNb", "_SpltPmt", "_SpnsrdMrchnt"]
	@property
	def AddtlSaleData(self):
		return self._AddtlSaleData

	@AddtlSaleData.setter
	def AddtlSaleData(self, value):
		self._AddtlSaleData = value if type(value) != base_types.auto else self.make_default("AddtlSaleData")

	@AddtlSaleData.deleter
	def AddtlSaleData(self):
		del self._AddtlSaleData
		self._AddtlSaleData = None

	@property
	def AllwdNtryMd(self):
		return self._AllwdNtryMd

	@AllwdNtryMd.setter
	def AllwdNtryMd(self, value):
		self._AllwdNtryMd = value if type(value) != base_types.auto else self.make_default("AllwdNtryMd")

	@AllwdNtryMd.deleter
	def AllwdNtryMd(self):
		del self._AllwdNtryMd
		self._AllwdNtryMd = None

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
	def CstmrOrdrReqFlg(self):
		return self._CstmrOrdrReqFlg

	@CstmrOrdrReqFlg.setter
	def CstmrOrdrReqFlg(self, value):
		self._CstmrOrdrReqFlg = value if type(value) != base_types.auto else self.make_default("CstmrOrdrReqFlg")

	@CstmrOrdrReqFlg.deleter
	def CstmrOrdrReqFlg(self):
		del self._CstmrOrdrReqFlg
		self._CstmrOrdrReqFlg = None

	@property
	def DlvryNoteNb(self):
		return self._DlvryNoteNb

	@DlvryNoteNb.setter
	def DlvryNoteNb(self, value):
		self._DlvryNoteNb = value if type(value) != base_types.auto else self.make_default("DlvryNoteNb")

	@DlvryNoteNb.deleter
	def DlvryNoteNb(self):
		del self._DlvryNoteNb
		self._DlvryNoteNb = None

	@property
	def ForceOnlnFlg(self):
		return self._ForceOnlnFlg

	@ForceOnlnFlg.setter
	def ForceOnlnFlg(self, value):
		self._ForceOnlnFlg = value if type(value) != base_types.auto else self.make_default("ForceOnlnFlg")

	@ForceOnlnFlg.deleter
	def ForceOnlnFlg(self):
		del self._ForceOnlnFlg
		self._ForceOnlnFlg = None

	@property
	def InvcNb(self):
		return self._InvcNb

	@InvcNb.setter
	def InvcNb(self, value):
		self._InvcNb = value if type(value) != base_types.auto else self.make_default("InvcNb")

	@InvcNb.deleter
	def InvcNb(self):
		del self._InvcNb
		self._InvcNb = None

	@property
	def PurchsOrdrNb(self):
		return self._PurchsOrdrNb

	@PurchsOrdrNb.setter
	def PurchsOrdrNb(self, value):
		self._PurchsOrdrNb = value if type(value) != base_types.auto else self.make_default("PurchsOrdrNb")

	@PurchsOrdrNb.deleter
	def PurchsOrdrNb(self):
		del self._PurchsOrdrNb
		self._PurchsOrdrNb = None

	@property
	def ReuseCardDataFlg(self):
		return self._ReuseCardDataFlg

	@ReuseCardDataFlg.setter
	def ReuseCardDataFlg(self, value):
		self._ReuseCardDataFlg = value if type(value) != base_types.auto else self.make_default("ReuseCardDataFlg")

	@ReuseCardDataFlg.deleter
	def ReuseCardDataFlg(self):
		del self._ReuseCardDataFlg
		self._ReuseCardDataFlg = None

	@property
	def RmngAmt(self):
		return self._RmngAmt

	@RmngAmt.setter
	def RmngAmt(self, value):
		self._RmngAmt = value if type(value) != base_types.auto else self.make_default("RmngAmt")

	@RmngAmt.deleter
	def RmngAmt(self):
		del self._RmngAmt
		self._RmngAmt = None

	@property
	def SaleId(self):
		return self._SaleId

	@SaleId.setter
	def SaleId(self, value):
		self._SaleId = value if type(value) != base_types.auto else self.make_default("SaleId")

	@SaleId.deleter
	def SaleId(self):
		del self._SaleId
		self._SaleId = None

	@property
	def SaleRcncltnId(self):
		return self._SaleRcncltnId

	@SaleRcncltnId.setter
	def SaleRcncltnId(self, value):
		self._SaleRcncltnId = value if type(value) != base_types.auto else self.make_default("SaleRcncltnId")

	@SaleRcncltnId.deleter
	def SaleRcncltnId(self):
		del self._SaleRcncltnId
		self._SaleRcncltnId = None

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
	def SaleTknScp(self):
		return self._SaleTknScp

	@SaleTknScp.setter
	def SaleTknScp(self, value):
		self._SaleTknScp = value if type(value) != base_types.auto else self.make_default("SaleTknScp")

	@SaleTknScp.deleter
	def SaleTknScp(self):
		del self._SaleTknScp
		self._SaleTknScp = None

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
	def SpnsrdMrchnt(self):
		return self._SpnsrdMrchnt

	@SpnsrdMrchnt.setter
	def SpnsrdMrchnt(self, value):
		self._SpnsrdMrchnt = value if type(value) != base_types.auto else self.make_default("SpnsrdMrchnt")

	@SpnsrdMrchnt.deleter
	def SpnsrdMrchnt(self):
		del self._SpnsrdMrchnt
		self._SpnsrdMrchnt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlSaleData', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AllwdNtryMd', type=CardDataReading8Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CshrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshrLang', type=LanguageCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CstmrOrdrReqFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryNoteNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ForceOnlnFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvcNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PurchsOrdrNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReuseCardDataFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmngAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleRcncltnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleRefNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleTknScp', type=SaleTokenScope1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShftNb', type=Max2NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpltPmt', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpnsrdMrchnt', type=Organisation26, min=0, max=None, mutex_group=None, array=True),
	))

