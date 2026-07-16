# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CardDataReading8Code
from . import ImpliedCurrencyAndAmount
from . import LanguageCode
from . import Max2NumericText
from . import Max35Text
from . import Max70Text
from . import Organisation26
from . import SaleTokenScope1Code
from . import TrueFalseIndicator

class SaleContext4(base_types._BaseFieldType):

	__slots__ = ["_AddtlSaleData", "_AllwdNtryMd", "_CshrId", "_CshrLang", "_CstmrOrdrReqFlg", "_DlvryNoteNb", "_ForceOnlnFlg", "_InvcNb", "_PurchsOrdrNb", "_ReuseCardDataFlg", "_RmngAmt", "_SaleId", "_SaleRcncltnId", "_SaleRefNb", "_SaleTknScp", "_ShftNb", "_SpltPmt", "_SpnsrdMrchnt"]
	@property
	def AddtlSaleData(self):
		return self._AddtlSaleData

	@AddtlSaleData.setter
	def AddtlSaleData(self, value):
		self._AddtlSaleData = value if value is not None else base_types.UninitialisedField(self, 'AddtlSaleData', Max70Text, False)

	@AddtlSaleData.deleter
	def AddtlSaleData(self):
		del self._AddtlSaleData
		self._AddtlSaleData = base_types.UninitialisedField(self, 'AddtlSaleData', Max70Text, False)

	@property
	def AllwdNtryMd(self):
		return self._AllwdNtryMd

	@AllwdNtryMd.setter
	def AllwdNtryMd(self, value):
		self._AllwdNtryMd = value if value is not None else base_types.UninitialisedField(self, 'AllwdNtryMd', CardDataReading8Code, True)

	@AllwdNtryMd.deleter
	def AllwdNtryMd(self):
		del self._AllwdNtryMd
		self._AllwdNtryMd = base_types.UninitialisedField(self, 'AllwdNtryMd', CardDataReading8Code, True)

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
		self._CshrLang = value if value is not None else base_types.UninitialisedField(self, 'CshrLang', LanguageCode, True)

	@CshrLang.deleter
	def CshrLang(self):
		del self._CshrLang
		self._CshrLang = base_types.UninitialisedField(self, 'CshrLang', LanguageCode, True)

	@property
	def CstmrOrdrReqFlg(self):
		return self._CstmrOrdrReqFlg

	@CstmrOrdrReqFlg.setter
	def CstmrOrdrReqFlg(self, value):
		self._CstmrOrdrReqFlg = value if value is not None else base_types.UninitialisedField(self, 'CstmrOrdrReqFlg', TrueFalseIndicator, False)

	@CstmrOrdrReqFlg.deleter
	def CstmrOrdrReqFlg(self):
		del self._CstmrOrdrReqFlg
		self._CstmrOrdrReqFlg = base_types.UninitialisedField(self, 'CstmrOrdrReqFlg', TrueFalseIndicator, False)

	@property
	def DlvryNoteNb(self):
		return self._DlvryNoteNb

	@DlvryNoteNb.setter
	def DlvryNoteNb(self, value):
		self._DlvryNoteNb = value if value is not None else base_types.UninitialisedField(self, 'DlvryNoteNb', Max35Text, False)

	@DlvryNoteNb.deleter
	def DlvryNoteNb(self):
		del self._DlvryNoteNb
		self._DlvryNoteNb = base_types.UninitialisedField(self, 'DlvryNoteNb', Max35Text, False)

	@property
	def ForceOnlnFlg(self):
		return self._ForceOnlnFlg

	@ForceOnlnFlg.setter
	def ForceOnlnFlg(self, value):
		self._ForceOnlnFlg = value if value is not None else base_types.UninitialisedField(self, 'ForceOnlnFlg', TrueFalseIndicator, False)

	@ForceOnlnFlg.deleter
	def ForceOnlnFlg(self):
		del self._ForceOnlnFlg
		self._ForceOnlnFlg = base_types.UninitialisedField(self, 'ForceOnlnFlg', TrueFalseIndicator, False)

	@property
	def InvcNb(self):
		return self._InvcNb

	@InvcNb.setter
	def InvcNb(self, value):
		self._InvcNb = value if value is not None else base_types.UninitialisedField(self, 'InvcNb', Max35Text, False)

	@InvcNb.deleter
	def InvcNb(self):
		del self._InvcNb
		self._InvcNb = base_types.UninitialisedField(self, 'InvcNb', Max35Text, False)

	@property
	def PurchsOrdrNb(self):
		return self._PurchsOrdrNb

	@PurchsOrdrNb.setter
	def PurchsOrdrNb(self, value):
		self._PurchsOrdrNb = value if value is not None else base_types.UninitialisedField(self, 'PurchsOrdrNb', Max35Text, False)

	@PurchsOrdrNb.deleter
	def PurchsOrdrNb(self):
		del self._PurchsOrdrNb
		self._PurchsOrdrNb = base_types.UninitialisedField(self, 'PurchsOrdrNb', Max35Text, False)

	@property
	def ReuseCardDataFlg(self):
		return self._ReuseCardDataFlg

	@ReuseCardDataFlg.setter
	def ReuseCardDataFlg(self, value):
		self._ReuseCardDataFlg = value if value is not None else base_types.UninitialisedField(self, 'ReuseCardDataFlg', TrueFalseIndicator, False)

	@ReuseCardDataFlg.deleter
	def ReuseCardDataFlg(self):
		del self._ReuseCardDataFlg
		self._ReuseCardDataFlg = base_types.UninitialisedField(self, 'ReuseCardDataFlg', TrueFalseIndicator, False)

	@property
	def RmngAmt(self):
		return self._RmngAmt

	@RmngAmt.setter
	def RmngAmt(self, value):
		self._RmngAmt = value if value is not None else base_types.UninitialisedField(self, 'RmngAmt', ImpliedCurrencyAndAmount, False)

	@RmngAmt.deleter
	def RmngAmt(self):
		del self._RmngAmt
		self._RmngAmt = base_types.UninitialisedField(self, 'RmngAmt', ImpliedCurrencyAndAmount, False)

	@property
	def SaleId(self):
		return self._SaleId

	@SaleId.setter
	def SaleId(self, value):
		self._SaleId = value if value is not None else base_types.UninitialisedField(self, 'SaleId', Max35Text, False)

	@SaleId.deleter
	def SaleId(self):
		del self._SaleId
		self._SaleId = base_types.UninitialisedField(self, 'SaleId', Max35Text, False)

	@property
	def SaleRcncltnId(self):
		return self._SaleRcncltnId

	@SaleRcncltnId.setter
	def SaleRcncltnId(self, value):
		self._SaleRcncltnId = value if value is not None else base_types.UninitialisedField(self, 'SaleRcncltnId', Max35Text, False)

	@SaleRcncltnId.deleter
	def SaleRcncltnId(self):
		del self._SaleRcncltnId
		self._SaleRcncltnId = base_types.UninitialisedField(self, 'SaleRcncltnId', Max35Text, False)

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
	def SaleTknScp(self):
		return self._SaleTknScp

	@SaleTknScp.setter
	def SaleTknScp(self, value):
		self._SaleTknScp = value if value is not None else base_types.UninitialisedField(self, 'SaleTknScp', SaleTokenScope1Code, False)

	@SaleTknScp.deleter
	def SaleTknScp(self):
		del self._SaleTknScp
		self._SaleTknScp = base_types.UninitialisedField(self, 'SaleTknScp', SaleTokenScope1Code, False)

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
	def SpnsrdMrchnt(self):
		return self._SpnsrdMrchnt

	@SpnsrdMrchnt.setter
	def SpnsrdMrchnt(self, value):
		self._SpnsrdMrchnt = value if value is not None else base_types.UninitialisedField(self, 'SpnsrdMrchnt', Organisation26, True)

	@SpnsrdMrchnt.deleter
	def SpnsrdMrchnt(self):
		del self._SpnsrdMrchnt
		self._SpnsrdMrchnt = base_types.UninitialisedField(self, 'SpnsrdMrchnt', Organisation26, True)

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