# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CapturedSignature1
from . import CardPaymentServiceType12Code
from . import CardPaymentServiceType15Code
from . import CardPaymentServiceType9Code
from . import CardPaymentTransaction144
from . import ContentInformationType40
from . import CustomerOrder1
from . import LanguageCode
from . import PaymentInstrumentType2Code
from . import PaymentTransaction165
from . import PaymentTypeInformation26
from . import TrueFalseIndicator

class RetailerPaymentResult7(base_types._BaseFieldType):

	__slots__ = ["_AddtlSvc", "_CstmrLang", "_CstmrOrdr", "_ImgCaptrdSgntr", "_MrchntOvrrdFlg", "_OnlnFlg", "_PmtInstrm", "_PmtTpInf", "_PrtctdCaptrdSgntr", "_ReqdTx", "_SvcAttr", "_TxRspn", "_TxTp"]
	@property
	def AddtlSvc(self):
		return self._AddtlSvc

	@AddtlSvc.setter
	def AddtlSvc(self, value):
		self._AddtlSvc = value if value is not None else base_types.UninitialisedField(self, 'AddtlSvc', CardPaymentServiceType9Code, True)

	@AddtlSvc.deleter
	def AddtlSvc(self):
		del self._AddtlSvc
		self._AddtlSvc = base_types.UninitialisedField(self, 'AddtlSvc', CardPaymentServiceType9Code, True)

	@property
	def CstmrLang(self):
		return self._CstmrLang

	@CstmrLang.setter
	def CstmrLang(self, value):
		self._CstmrLang = value if value is not None else base_types.UninitialisedField(self, 'CstmrLang', LanguageCode, False)

	@CstmrLang.deleter
	def CstmrLang(self):
		del self._CstmrLang
		self._CstmrLang = base_types.UninitialisedField(self, 'CstmrLang', LanguageCode, False)

	@property
	def CstmrOrdr(self):
		return self._CstmrOrdr

	@CstmrOrdr.setter
	def CstmrOrdr(self, value):
		self._CstmrOrdr = value if value is not None else base_types.UninitialisedField(self, 'CstmrOrdr', CustomerOrder1, True)

	@CstmrOrdr.deleter
	def CstmrOrdr(self):
		del self._CstmrOrdr
		self._CstmrOrdr = base_types.UninitialisedField(self, 'CstmrOrdr', CustomerOrder1, True)

	@property
	def ImgCaptrdSgntr(self):
		return self._ImgCaptrdSgntr

	@ImgCaptrdSgntr.setter
	def ImgCaptrdSgntr(self, value):
		self._ImgCaptrdSgntr = value if value is not None else base_types.UninitialisedField(self, 'ImgCaptrdSgntr', CapturedSignature1, False)

	@ImgCaptrdSgntr.deleter
	def ImgCaptrdSgntr(self):
		del self._ImgCaptrdSgntr
		self._ImgCaptrdSgntr = base_types.UninitialisedField(self, 'ImgCaptrdSgntr', CapturedSignature1, False)

	@property
	def MrchntOvrrdFlg(self):
		return self._MrchntOvrrdFlg

	@MrchntOvrrdFlg.setter
	def MrchntOvrrdFlg(self, value):
		self._MrchntOvrrdFlg = value if value is not None else base_types.UninitialisedField(self, 'MrchntOvrrdFlg', TrueFalseIndicator, False)

	@MrchntOvrrdFlg.deleter
	def MrchntOvrrdFlg(self):
		del self._MrchntOvrrdFlg
		self._MrchntOvrrdFlg = base_types.UninitialisedField(self, 'MrchntOvrrdFlg', TrueFalseIndicator, False)

	@property
	def OnlnFlg(self):
		return self._OnlnFlg

	@OnlnFlg.setter
	def OnlnFlg(self, value):
		self._OnlnFlg = value if value is not None else base_types.UninitialisedField(self, 'OnlnFlg', TrueFalseIndicator, False)

	@OnlnFlg.deleter
	def OnlnFlg(self):
		del self._OnlnFlg
		self._OnlnFlg = base_types.UninitialisedField(self, 'OnlnFlg', TrueFalseIndicator, False)

	@property
	def PmtInstrm(self):
		return self._PmtInstrm

	@PmtInstrm.setter
	def PmtInstrm(self, value):
		self._PmtInstrm = value if value is not None else base_types.UninitialisedField(self, 'PmtInstrm', PaymentInstrumentType2Code, True)

	@PmtInstrm.deleter
	def PmtInstrm(self):
		del self._PmtInstrm
		self._PmtInstrm = base_types.UninitialisedField(self, 'PmtInstrm', PaymentInstrumentType2Code, True)

	@property
	def PmtTpInf(self):
		return self._PmtTpInf

	@PmtTpInf.setter
	def PmtTpInf(self, value):
		self._PmtTpInf = value if value is not None else base_types.UninitialisedField(self, 'PmtTpInf', PaymentTypeInformation26, False)

	@PmtTpInf.deleter
	def PmtTpInf(self):
		del self._PmtTpInf
		self._PmtTpInf = base_types.UninitialisedField(self, 'PmtTpInf', PaymentTypeInformation26, False)

	@property
	def PrtctdCaptrdSgntr(self):
		return self._PrtctdCaptrdSgntr

	@PrtctdCaptrdSgntr.setter
	def PrtctdCaptrdSgntr(self, value):
		self._PrtctdCaptrdSgntr = value if value is not None else base_types.UninitialisedField(self, 'PrtctdCaptrdSgntr', ContentInformationType40, False)

	@PrtctdCaptrdSgntr.deleter
	def PrtctdCaptrdSgntr(self):
		del self._PrtctdCaptrdSgntr
		self._PrtctdCaptrdSgntr = base_types.UninitialisedField(self, 'PrtctdCaptrdSgntr', ContentInformationType40, False)

	@property
	def ReqdTx(self):
		return self._ReqdTx

	@ReqdTx.setter
	def ReqdTx(self, value):
		self._ReqdTx = value if value is not None else base_types.UninitialisedField(self, 'ReqdTx', PaymentTransaction165, False)

	@ReqdTx.deleter
	def ReqdTx(self):
		del self._ReqdTx
		self._ReqdTx = base_types.UninitialisedField(self, 'ReqdTx', PaymentTransaction165, False)

	@property
	def SvcAttr(self):
		return self._SvcAttr

	@SvcAttr.setter
	def SvcAttr(self, value):
		self._SvcAttr = value if value is not None else base_types.UninitialisedField(self, 'SvcAttr', CardPaymentServiceType15Code, False)

	@SvcAttr.deleter
	def SvcAttr(self):
		del self._SvcAttr
		self._SvcAttr = base_types.UninitialisedField(self, 'SvcAttr', CardPaymentServiceType15Code, False)

	@property
	def TxRspn(self):
		return self._TxRspn

	@TxRspn.setter
	def TxRspn(self, value):
		self._TxRspn = value if value is not None else base_types.UninitialisedField(self, 'TxRspn', CardPaymentTransaction144, False)

	@TxRspn.deleter
	def TxRspn(self):
		del self._TxRspn
		self._TxRspn = base_types.UninitialisedField(self, 'TxRspn', CardPaymentTransaction144, False)

	@property
	def TxTp(self):
		return self._TxTp

	@TxTp.setter
	def TxTp(self, value):
		self._TxTp = value if value is not None else base_types.UninitialisedField(self, 'TxTp', CardPaymentServiceType12Code, False)

	@TxTp.deleter
	def TxTp(self):
		del self._TxTp
		self._TxTp = base_types.UninitialisedField(self, 'TxTp', CardPaymentServiceType12Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlSvc', type=CardPaymentServiceType9Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CstmrLang', type=LanguageCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrOrdr', type=CustomerOrder1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ImgCaptrdSgntr', type=CapturedSignature1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrchntOvrrdFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OnlnFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtInstrm', type=PaymentInstrumentType2Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PmtTpInf', type=PaymentTypeInformation26, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdCaptrdSgntr', type=ContentInformationType40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdTx', type=PaymentTransaction165, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcAttr', type=CardPaymentServiceType15Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxRspn', type=CardPaymentTransaction144, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTp', type=CardPaymentServiceType12Code, min=1, max=1, mutex_group=None, array=False),
	))