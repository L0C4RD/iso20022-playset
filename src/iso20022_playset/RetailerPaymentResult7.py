import base_types
import ContentInformationType40
import CardPaymentServiceType15Code
import CustomerOrder1
import PaymentTypeInformation26
import CapturedSignature1
import PaymentTransaction165
import CardPaymentServiceType12Code
import PaymentInstrumentType2Code
import CardPaymentTransaction144
import LanguageCode
import CardPaymentServiceType9Code
import TrueFalseIndicator

class RetailerPaymentResult7(base_types._BaseFieldType):

	__slots__ = ["_CstmrOrdr", "_TxRspn", "_PrtctdCaptrdSgntr", "_TxTp", "_OnlnFlg", "_PmtInstrm", "_AddtlSvc", "_CstmrLang", "_SvcAttr", "_ReqdTx", "_PmtTpInf", "_MrchntOvrrdFlg", "_ImgCaptrdSgntr"]
	@property
	def CstmrOrdr(self):
		return self._CstmrOrdr

	@CstmrOrdr.setter
	def CstmrOrdr(self, value):
		self._CstmrOrdr = value if type(value) != auto else self.make_default("CstmrOrdr")

	@CstmrOrdr.deleter
	def CstmrOrdr(self):
		del self._CstmrOrdr
		self._CstmrOrdr = None

	@property
	def TxRspn(self):
		return self._TxRspn

	@TxRspn.setter
	def TxRspn(self, value):
		self._TxRspn = value if type(value) != auto else self.make_default("TxRspn")

	@TxRspn.deleter
	def TxRspn(self):
		del self._TxRspn
		self._TxRspn = None

	@property
	def PrtctdCaptrdSgntr(self):
		return self._PrtctdCaptrdSgntr

	@PrtctdCaptrdSgntr.setter
	def PrtctdCaptrdSgntr(self, value):
		self._PrtctdCaptrdSgntr = value if type(value) != auto else self.make_default("PrtctdCaptrdSgntr")

	@PrtctdCaptrdSgntr.deleter
	def PrtctdCaptrdSgntr(self):
		del self._PrtctdCaptrdSgntr
		self._PrtctdCaptrdSgntr = None

	@property
	def TxTp(self):
		return self._TxTp

	@TxTp.setter
	def TxTp(self, value):
		self._TxTp = value if type(value) != auto else self.make_default("TxTp")

	@TxTp.deleter
	def TxTp(self):
		del self._TxTp
		self._TxTp = None

	@property
	def OnlnFlg(self):
		return self._OnlnFlg

	@OnlnFlg.setter
	def OnlnFlg(self, value):
		self._OnlnFlg = value if type(value) != auto else self.make_default("OnlnFlg")

	@OnlnFlg.deleter
	def OnlnFlg(self):
		del self._OnlnFlg
		self._OnlnFlg = None

	@property
	def PmtInstrm(self):
		return self._PmtInstrm

	@PmtInstrm.setter
	def PmtInstrm(self, value):
		self._PmtInstrm = value if type(value) != auto else self.make_default("PmtInstrm")

	@PmtInstrm.deleter
	def PmtInstrm(self):
		del self._PmtInstrm
		self._PmtInstrm = None

	@property
	def AddtlSvc(self):
		return self._AddtlSvc

	@AddtlSvc.setter
	def AddtlSvc(self, value):
		self._AddtlSvc = value if type(value) != auto else self.make_default("AddtlSvc")

	@AddtlSvc.deleter
	def AddtlSvc(self):
		del self._AddtlSvc
		self._AddtlSvc = None

	@property
	def CstmrLang(self):
		return self._CstmrLang

	@CstmrLang.setter
	def CstmrLang(self, value):
		self._CstmrLang = value if type(value) != auto else self.make_default("CstmrLang")

	@CstmrLang.deleter
	def CstmrLang(self):
		del self._CstmrLang
		self._CstmrLang = None

	@property
	def SvcAttr(self):
		return self._SvcAttr

	@SvcAttr.setter
	def SvcAttr(self, value):
		self._SvcAttr = value if type(value) != auto else self.make_default("SvcAttr")

	@SvcAttr.deleter
	def SvcAttr(self):
		del self._SvcAttr
		self._SvcAttr = None

	@property
	def ReqdTx(self):
		return self._ReqdTx

	@ReqdTx.setter
	def ReqdTx(self, value):
		self._ReqdTx = value if type(value) != auto else self.make_default("ReqdTx")

	@ReqdTx.deleter
	def ReqdTx(self):
		del self._ReqdTx
		self._ReqdTx = None

	@property
	def PmtTpInf(self):
		return self._PmtTpInf

	@PmtTpInf.setter
	def PmtTpInf(self, value):
		self._PmtTpInf = value if type(value) != auto else self.make_default("PmtTpInf")

	@PmtTpInf.deleter
	def PmtTpInf(self):
		del self._PmtTpInf
		self._PmtTpInf = None

	@property
	def MrchntOvrrdFlg(self):
		return self._MrchntOvrrdFlg

	@MrchntOvrrdFlg.setter
	def MrchntOvrrdFlg(self, value):
		self._MrchntOvrrdFlg = value if type(value) != auto else self.make_default("MrchntOvrrdFlg")

	@MrchntOvrrdFlg.deleter
	def MrchntOvrrdFlg(self):
		del self._MrchntOvrrdFlg
		self._MrchntOvrrdFlg = None

	@property
	def ImgCaptrdSgntr(self):
		return self._ImgCaptrdSgntr

	@ImgCaptrdSgntr.setter
	def ImgCaptrdSgntr(self, value):
		self._ImgCaptrdSgntr = value if type(value) != auto else self.make_default("ImgCaptrdSgntr")

	@ImgCaptrdSgntr.deleter
	def ImgCaptrdSgntr(self):
		del self._ImgCaptrdSgntr
		self._ImgCaptrdSgntr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CstmrOrdr', type=CustomerOrder1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxRspn', type=CardPaymentTransaction144, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdCaptrdSgntr', type=ContentInformationType40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTp', type=CardPaymentServiceType12Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OnlnFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtInstrm', type=PaymentInstrumentType2Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlSvc', type=CardPaymentServiceType9Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CstmrLang', type=LanguageCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcAttr', type=CardPaymentServiceType15Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdTx', type=PaymentTransaction165, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtTpInf', type=PaymentTypeInformation26, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrchntOvrrdFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ImgCaptrdSgntr', type=CapturedSignature1, min=0, max=1, mutex_group=None, array=False),
	))

