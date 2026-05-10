import base_types
import DeviceTransmitMessageResponse1
import PaymentContext30
import DeviceSecureInputResponse6
import DeviceSendApplicationProtocolDataUnitCardReaderResponse1
import ResponseType11
import SupplementaryData1
import CardPaymentEnvironment81
import RetailerService9Code
import DeviceInputResponse6
import DeviceInitialisationCardReaderResponse2
import DeviceDisplayResponse2
import DevicePrintResponse1

class DeviceResponse8(base_types._BaseFieldType):

	__slots__ = ["_InitlstnCardRdrRspn", "_Rspn", "_SplmtryData", "_CardRdrApplPrtcolDataUnitRspn", "_SvcCntt", "_PrtRspn", "_ScrInptRspn", "_InptRspn", "_Envt", "_Cntxt", "_TrnsmssnRspn", "_DispRspn"]
	@property
	def InitlstnCardRdrRspn(self):
		return self._InitlstnCardRdrRspn

	@InitlstnCardRdrRspn.setter
	def InitlstnCardRdrRspn(self, value):
		self._InitlstnCardRdrRspn = value if type(value) != auto else self.make_default("InitlstnCardRdrRspn")

	@InitlstnCardRdrRspn.deleter
	def InitlstnCardRdrRspn(self):
		del self._InitlstnCardRdrRspn
		self._InitlstnCardRdrRspn = None

	@property
	def Rspn(self):
		return self._Rspn

	@Rspn.setter
	def Rspn(self, value):
		self._Rspn = value if type(value) != auto else self.make_default("Rspn")

	@Rspn.deleter
	def Rspn(self):
		del self._Rspn
		self._Rspn = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def CardRdrApplPrtcolDataUnitRspn(self):
		return self._CardRdrApplPrtcolDataUnitRspn

	@CardRdrApplPrtcolDataUnitRspn.setter
	def CardRdrApplPrtcolDataUnitRspn(self, value):
		self._CardRdrApplPrtcolDataUnitRspn = value if type(value) != auto else self.make_default("CardRdrApplPrtcolDataUnitRspn")

	@CardRdrApplPrtcolDataUnitRspn.deleter
	def CardRdrApplPrtcolDataUnitRspn(self):
		del self._CardRdrApplPrtcolDataUnitRspn
		self._CardRdrApplPrtcolDataUnitRspn = None

	@property
	def SvcCntt(self):
		return self._SvcCntt

	@SvcCntt.setter
	def SvcCntt(self, value):
		self._SvcCntt = value if type(value) != auto else self.make_default("SvcCntt")

	@SvcCntt.deleter
	def SvcCntt(self):
		del self._SvcCntt
		self._SvcCntt = None

	@property
	def PrtRspn(self):
		return self._PrtRspn

	@PrtRspn.setter
	def PrtRspn(self, value):
		self._PrtRspn = value if type(value) != auto else self.make_default("PrtRspn")

	@PrtRspn.deleter
	def PrtRspn(self):
		del self._PrtRspn
		self._PrtRspn = None

	@property
	def ScrInptRspn(self):
		return self._ScrInptRspn

	@ScrInptRspn.setter
	def ScrInptRspn(self, value):
		self._ScrInptRspn = value if type(value) != auto else self.make_default("ScrInptRspn")

	@ScrInptRspn.deleter
	def ScrInptRspn(self):
		del self._ScrInptRspn
		self._ScrInptRspn = None

	@property
	def InptRspn(self):
		return self._InptRspn

	@InptRspn.setter
	def InptRspn(self, value):
		self._InptRspn = value if type(value) != auto else self.make_default("InptRspn")

	@InptRspn.deleter
	def InptRspn(self):
		del self._InptRspn
		self._InptRspn = None

	@property
	def Envt(self):
		return self._Envt

	@Envt.setter
	def Envt(self, value):
		self._Envt = value if type(value) != auto else self.make_default("Envt")

	@Envt.deleter
	def Envt(self):
		del self._Envt
		self._Envt = None

	@property
	def Cntxt(self):
		return self._Cntxt

	@Cntxt.setter
	def Cntxt(self, value):
		self._Cntxt = value if type(value) != auto else self.make_default("Cntxt")

	@Cntxt.deleter
	def Cntxt(self):
		del self._Cntxt
		self._Cntxt = None

	@property
	def TrnsmssnRspn(self):
		return self._TrnsmssnRspn

	@TrnsmssnRspn.setter
	def TrnsmssnRspn(self, value):
		self._TrnsmssnRspn = value if type(value) != auto else self.make_default("TrnsmssnRspn")

	@TrnsmssnRspn.deleter
	def TrnsmssnRspn(self):
		del self._TrnsmssnRspn
		self._TrnsmssnRspn = None

	@property
	def DispRspn(self):
		return self._DispRspn

	@DispRspn.setter
	def DispRspn(self, value):
		self._DispRspn = value if type(value) != auto else self.make_default("DispRspn")

	@DispRspn.deleter
	def DispRspn(self):
		del self._DispRspn
		self._DispRspn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='InitlstnCardRdrRspn', type=DeviceInitialisationCardReaderResponse2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rspn', type=ResponseType11, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CardRdrApplPrtcolDataUnitRspn', type=DeviceSendApplicationProtocolDataUnitCardReaderResponse1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcCntt', type=RetailerService9Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtRspn', type=DevicePrintResponse1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScrInptRspn', type=DeviceSecureInputResponse6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InptRspn', type=DeviceInputResponse6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Envt', type=CardPaymentEnvironment81, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cntxt', type=PaymentContext30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrnsmssnRspn', type=DeviceTransmitMessageResponse1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DispRspn', type=DeviceDisplayResponse2, min=0, max=1, mutex_group=None, array=False),
	))

