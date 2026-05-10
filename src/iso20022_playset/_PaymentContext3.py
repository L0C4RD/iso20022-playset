from . import base_types
from .TrueFalseIndicator import TrueFalseIndicator
from .AttendanceContext1Code import AttendanceContext1Code
from .CardDataReading1Code import CardDataReading1Code
from .CardholderAuthentication2 import CardholderAuthentication2
from .ISO2ALanguageCode import ISO2ALanguageCode
from .TransactionChannel1Code import TransactionChannel1Code
from .TransactionEnvironment1Code import TransactionEnvironment1Code

class PaymentContext3(base_types._BaseFieldType):

	__slots__ = ["_OnLineCntxt", "_FllbckInd", "_CardPres", "_AttndncCntxt", "_AuthntcnMtd", "_TxEnvt", "_CardDataNtryMd", "_CrdhldrPres", "_TxChanl", "_AttndntMsgCpbl", "_AttndntLang"]
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
	def FllbckInd(self):
		return self._FllbckInd

	@FllbckInd.setter
	def FllbckInd(self, value):
		self._FllbckInd = value if type(value) != base_types.auto else self.make_default("FllbckInd")

	@FllbckInd.deleter
	def FllbckInd(self):
		del self._FllbckInd
		self._FllbckInd = None

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
	def AuthntcnMtd(self):
		return self._AuthntcnMtd

	@AuthntcnMtd.setter
	def AuthntcnMtd(self, value):
		self._AuthntcnMtd = value if type(value) != base_types.auto else self.make_default("AuthntcnMtd")

	@AuthntcnMtd.deleter
	def AuthntcnMtd(self):
		del self._AuthntcnMtd
		self._AuthntcnMtd = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='OnLineCntxt', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FllbckInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardPres', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AttndncCntxt', type=AttendanceContext1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthntcnMtd', type=CardholderAuthentication2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxEnvt', type=TransactionEnvironment1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardDataNtryMd', type=CardDataReading1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrdhldrPres', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxChanl', type=TransactionChannel1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AttndntMsgCpbl', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AttndntLang', type=ISO2ALanguageCode, min=0, max=1, mutex_group=None, array=False),
	))

