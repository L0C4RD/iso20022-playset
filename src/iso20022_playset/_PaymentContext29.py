# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AttendanceContext1Code
from . import BusinessArea2Code
from . import CardDataReading8Code
from . import CardFallback1Code
from . import LanguageCode
from . import SupportedPaymentOption2Code
from . import TransactionChannel5Code
from . import TransactionEnvironment1Code
from . import TrueFalseIndicator

class PaymentContext29(base_types._BaseFieldType):

	__slots__ = ["_AttndncCntxt", "_AttndntLang", "_AttndntMsgCpbl", "_BizArea", "_CardDataNtryMd", "_CardPres", "_CrdhldrPres", "_FllbckInd", "_OnLineCntxt", "_SpprtdOptn", "_TxChanl", "_TxEnvt"]
	@property
	def AttndncCntxt(self):
		return self._AttndncCntxt

	@AttndncCntxt.setter
	def AttndncCntxt(self, value):
		self._AttndncCntxt = value if value is not None else base_types.UninitialisedField(self, 'AttndncCntxt', AttendanceContext1Code, False)

	@AttndncCntxt.deleter
	def AttndncCntxt(self):
		del self._AttndncCntxt
		self._AttndncCntxt = base_types.UninitialisedField(self, 'AttndncCntxt', AttendanceContext1Code, False)

	@property
	def AttndntLang(self):
		return self._AttndntLang

	@AttndntLang.setter
	def AttndntLang(self, value):
		self._AttndntLang = value if value is not None else base_types.UninitialisedField(self, 'AttndntLang', LanguageCode, False)

	@AttndntLang.deleter
	def AttndntLang(self):
		del self._AttndntLang
		self._AttndntLang = base_types.UninitialisedField(self, 'AttndntLang', LanguageCode, False)

	@property
	def AttndntMsgCpbl(self):
		return self._AttndntMsgCpbl

	@AttndntMsgCpbl.setter
	def AttndntMsgCpbl(self, value):
		self._AttndntMsgCpbl = value if value is not None else base_types.UninitialisedField(self, 'AttndntMsgCpbl', TrueFalseIndicator, False)

	@AttndntMsgCpbl.deleter
	def AttndntMsgCpbl(self):
		del self._AttndntMsgCpbl
		self._AttndntMsgCpbl = base_types.UninitialisedField(self, 'AttndntMsgCpbl', TrueFalseIndicator, False)

	@property
	def BizArea(self):
		return self._BizArea

	@BizArea.setter
	def BizArea(self, value):
		self._BizArea = value if value is not None else base_types.UninitialisedField(self, 'BizArea', BusinessArea2Code, False)

	@BizArea.deleter
	def BizArea(self):
		del self._BizArea
		self._BizArea = base_types.UninitialisedField(self, 'BizArea', BusinessArea2Code, False)

	@property
	def CardDataNtryMd(self):
		return self._CardDataNtryMd

	@CardDataNtryMd.setter
	def CardDataNtryMd(self, value):
		self._CardDataNtryMd = value if value is not None else base_types.UninitialisedField(self, 'CardDataNtryMd', CardDataReading8Code, False)

	@CardDataNtryMd.deleter
	def CardDataNtryMd(self):
		del self._CardDataNtryMd
		self._CardDataNtryMd = base_types.UninitialisedField(self, 'CardDataNtryMd', CardDataReading8Code, False)

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
	def FllbckInd(self):
		return self._FllbckInd

	@FllbckInd.setter
	def FllbckInd(self, value):
		self._FllbckInd = value if value is not None else base_types.UninitialisedField(self, 'FllbckInd', CardFallback1Code, False)

	@FllbckInd.deleter
	def FllbckInd(self):
		del self._FllbckInd
		self._FllbckInd = base_types.UninitialisedField(self, 'FllbckInd', CardFallback1Code, False)

	@property
	def OnLineCntxt(self):
		return self._OnLineCntxt

	@OnLineCntxt.setter
	def OnLineCntxt(self, value):
		self._OnLineCntxt = value if value is not None else base_types.UninitialisedField(self, 'OnLineCntxt', TrueFalseIndicator, False)

	@OnLineCntxt.deleter
	def OnLineCntxt(self):
		del self._OnLineCntxt
		self._OnLineCntxt = base_types.UninitialisedField(self, 'OnLineCntxt', TrueFalseIndicator, False)

	@property
	def SpprtdOptn(self):
		return self._SpprtdOptn

	@SpprtdOptn.setter
	def SpprtdOptn(self, value):
		self._SpprtdOptn = value if value is not None else base_types.UninitialisedField(self, 'SpprtdOptn', SupportedPaymentOption2Code, True)

	@SpprtdOptn.deleter
	def SpprtdOptn(self):
		del self._SpprtdOptn
		self._SpprtdOptn = base_types.UninitialisedField(self, 'SpprtdOptn', SupportedPaymentOption2Code, True)

	@property
	def TxChanl(self):
		return self._TxChanl

	@TxChanl.setter
	def TxChanl(self, value):
		self._TxChanl = value if value is not None else base_types.UninitialisedField(self, 'TxChanl', TransactionChannel5Code, False)

	@TxChanl.deleter
	def TxChanl(self):
		del self._TxChanl
		self._TxChanl = base_types.UninitialisedField(self, 'TxChanl', TransactionChannel5Code, False)

	@property
	def TxEnvt(self):
		return self._TxEnvt

	@TxEnvt.setter
	def TxEnvt(self, value):
		self._TxEnvt = value if value is not None else base_types.UninitialisedField(self, 'TxEnvt', TransactionEnvironment1Code, False)

	@TxEnvt.deleter
	def TxEnvt(self):
		del self._TxEnvt
		self._TxEnvt = base_types.UninitialisedField(self, 'TxEnvt', TransactionEnvironment1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AttndncCntxt', type=AttendanceContext1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AttndntLang', type=LanguageCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AttndntMsgCpbl', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BizArea', type=BusinessArea2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardDataNtryMd', type=CardDataReading8Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardPres', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrdhldrPres', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FllbckInd', type=CardFallback1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OnLineCntxt', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpprtdOptn', type=SupportedPaymentOption2Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxChanl', type=TransactionChannel5Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxEnvt', type=TransactionEnvironment1Code, min=0, max=1, mutex_group=None, array=False),
	))