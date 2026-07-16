# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AttendanceContext1Code
from . import CardDataReading1Code
from . import CardholderAuthentication2
from . import ISO2ALanguageCode
from . import TransactionChannel1Code
from . import TransactionEnvironment1Code
from . import TrueFalseIndicator

class PaymentContext3(base_types._BaseFieldType):

	__slots__ = ["_AttndncCntxt", "_AttndntLang", "_AttndntMsgCpbl", "_AuthntcnMtd", "_CardDataNtryMd", "_CardPres", "_CrdhldrPres", "_FllbckInd", "_OnLineCntxt", "_TxChanl", "_TxEnvt"]
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
		self._AttndntLang = value if value is not None else base_types.UninitialisedField(self, 'AttndntLang', ISO2ALanguageCode, False)

	@AttndntLang.deleter
	def AttndntLang(self):
		del self._AttndntLang
		self._AttndntLang = base_types.UninitialisedField(self, 'AttndntLang', ISO2ALanguageCode, False)

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
	def AuthntcnMtd(self):
		return self._AuthntcnMtd

	@AuthntcnMtd.setter
	def AuthntcnMtd(self, value):
		self._AuthntcnMtd = value if value is not None else base_types.UninitialisedField(self, 'AuthntcnMtd', CardholderAuthentication2, False)

	@AuthntcnMtd.deleter
	def AuthntcnMtd(self):
		del self._AuthntcnMtd
		self._AuthntcnMtd = base_types.UninitialisedField(self, 'AuthntcnMtd', CardholderAuthentication2, False)

	@property
	def CardDataNtryMd(self):
		return self._CardDataNtryMd

	@CardDataNtryMd.setter
	def CardDataNtryMd(self, value):
		self._CardDataNtryMd = value if value is not None else base_types.UninitialisedField(self, 'CardDataNtryMd', CardDataReading1Code, False)

	@CardDataNtryMd.deleter
	def CardDataNtryMd(self):
		del self._CardDataNtryMd
		self._CardDataNtryMd = base_types.UninitialisedField(self, 'CardDataNtryMd', CardDataReading1Code, False)

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
		self._FllbckInd = value if value is not None else base_types.UninitialisedField(self, 'FllbckInd', TrueFalseIndicator, False)

	@FllbckInd.deleter
	def FllbckInd(self):
		del self._FllbckInd
		self._FllbckInd = base_types.UninitialisedField(self, 'FllbckInd', TrueFalseIndicator, False)

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
	def TxChanl(self):
		return self._TxChanl

	@TxChanl.setter
	def TxChanl(self, value):
		self._TxChanl = value if value is not None else base_types.UninitialisedField(self, 'TxChanl', TransactionChannel1Code, False)

	@TxChanl.deleter
	def TxChanl(self):
		del self._TxChanl
		self._TxChanl = base_types.UninitialisedField(self, 'TxChanl', TransactionChannel1Code, False)

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
		base_types.FieldEntry(name='AttndntLang', type=ISO2ALanguageCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AttndntMsgCpbl', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthntcnMtd', type=CardholderAuthentication2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardDataNtryMd', type=CardDataReading1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardPres', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrdhldrPres', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FllbckInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OnLineCntxt', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxChanl', type=TransactionChannel1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxEnvt', type=TransactionEnvironment1Code, min=0, max=1, mutex_group=None, array=False),
	))