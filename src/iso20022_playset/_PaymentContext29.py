from . import base_types
from ._TransactionChannel5Code import TransactionChannel5Code
from ._CardDataReading8Code import CardDataReading8Code
from ._TransactionEnvironment1Code import TransactionEnvironment1Code
from ._BusinessArea2Code import BusinessArea2Code
from ._SupportedPaymentOption2Code import SupportedPaymentOption2Code
from ._CardFallback1Code import CardFallback1Code
from ._TrueFalseIndicator import TrueFalseIndicator
from ._LanguageCode import LanguageCode
from ._AttendanceContext1Code import AttendanceContext1Code

class PaymentContext29(base_types._BaseFieldType):

	__slots__ = ["_OnLineCntxt", "_CrdhldrPres", "_BizArea", "_TxEnvt", "_SpprtdOptn", "_CardDataNtryMd", "_AttndntMsgCpbl", "_AttndntLang", "_TxChanl", "_CardPres", "_AttndncCntxt", "_FllbckInd"]
	@property
	def OnLineCntxt(self):
		return self._OnLineCntxt

	@OnLineCntxt.setter
	def OnLineCntxt(self, value):
		self._OnLineCntxt = value if type(value) != base_types.auto else self.make_default("OnLineCntxt")

	@OnLineCntxt.deleter
	def OnLineCntxt(self):
		del self._OnLineCntxt
		self._OnLineCntxt = None

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
	def BizArea(self):
		return self._BizArea

	@BizArea.setter
	def BizArea(self, value):
		self._BizArea = value if type(value) != base_types.auto else self.make_default("BizArea")

	@BizArea.deleter
	def BizArea(self):
		del self._BizArea
		self._BizArea = None

	@property
	def TxEnvt(self):
		return self._TxEnvt

	@TxEnvt.setter
	def TxEnvt(self, value):
		self._TxEnvt = value if type(value) != base_types.auto else self.make_default("TxEnvt")

	@TxEnvt.deleter
	def TxEnvt(self):
		del self._TxEnvt
		self._TxEnvt = None

	@property
	def SpprtdOptn(self):
		return self._SpprtdOptn

	@SpprtdOptn.setter
	def SpprtdOptn(self, value):
		self._SpprtdOptn = value if type(value) != base_types.auto else self.make_default("SpprtdOptn")

	@SpprtdOptn.deleter
	def SpprtdOptn(self):
		del self._SpprtdOptn
		self._SpprtdOptn = None

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
	def AttndntMsgCpbl(self):
		return self._AttndntMsgCpbl

	@AttndntMsgCpbl.setter
	def AttndntMsgCpbl(self, value):
		self._AttndntMsgCpbl = value if type(value) != base_types.auto else self.make_default("AttndntMsgCpbl")

	@AttndntMsgCpbl.deleter
	def AttndntMsgCpbl(self):
		del self._AttndntMsgCpbl
		self._AttndntMsgCpbl = None

	@property
	def AttndntLang(self):
		return self._AttndntLang

	@AttndntLang.setter
	def AttndntLang(self, value):
		self._AttndntLang = value if type(value) != base_types.auto else self.make_default("AttndntLang")

	@AttndntLang.deleter
	def AttndntLang(self):
		del self._AttndntLang
		self._AttndntLang = None

	@property
	def TxChanl(self):
		return self._TxChanl

	@TxChanl.setter
	def TxChanl(self, value):
		self._TxChanl = value if type(value) != base_types.auto else self.make_default("TxChanl")

	@TxChanl.deleter
	def TxChanl(self):
		del self._TxChanl
		self._TxChanl = None

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
	def AttndncCntxt(self):
		return self._AttndncCntxt

	@AttndncCntxt.setter
	def AttndncCntxt(self, value):
		self._AttndncCntxt = value if type(value) != base_types.auto else self.make_default("AttndncCntxt")

	@AttndncCntxt.deleter
	def AttndncCntxt(self):
		del self._AttndncCntxt
		self._AttndncCntxt = None

	@property
	def FllbckInd(self):
		return self._FllbckInd

	@FllbckInd.setter
	def FllbckInd(self, value):
		self._FllbckInd = value if type(value) != base_types.auto else self.make_default("FllbckInd")

	@FllbckInd.deleter
	def FllbckInd(self):
		del self._FllbckInd
		self._FllbckInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OnLineCntxt', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrdhldrPres', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BizArea', type=BusinessArea2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxEnvt', type=TransactionEnvironment1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpprtdOptn', type=SupportedPaymentOption2Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CardDataNtryMd', type=CardDataReading8Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AttndntMsgCpbl', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AttndntLang', type=LanguageCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxChanl', type=TransactionChannel5Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardPres', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AttndncCntxt', type=AttendanceContext1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FllbckInd', type=CardFallback1Code, min=0, max=1, mutex_group=None, array=False),
	))

