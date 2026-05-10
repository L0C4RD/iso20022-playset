import base_types
import DevicePrintRequest6
import DeviceSecureInputRequest6
import DeviceSendApplicationProtocolDataUnitCardReaderRequest1
import SupplementaryData1
import DevicePoweroffCardReaderRequest6
import DeviceInputRequest6
import DeviceTransmitMessageRequest2
import RetailerService8Code
import PaymentContext30
import CardPaymentEnvironment81
import DeviceInputNotification6
import DevicePlayResourceRequest1
import DeviceDisplayRequest6
import DeviceInitialisationCardReaderRequest6

class DeviceRequest8(base_types._BaseFieldType):

	__slots__ = ["_CardRdrAPDUReq", "_Envt", "_PrtReq", "_InitlstnCardRdrReq", "_InptNtfctn", "_PlayRsrcReq", "_ScrInptReq", "_InptReq", "_PwrOffCardRdrReq", "_DispReq", "_TrnsmssnReq", "_Cntxt", "_SvcCntt", "_SplmtryData"]
	@property
	def CardRdrAPDUReq(self):
		return self._CardRdrAPDUReq

	@CardRdrAPDUReq.setter
	def CardRdrAPDUReq(self, value):
		self._CardRdrAPDUReq = value if type(value) != auto else self.make_default("CardRdrAPDUReq")

	@CardRdrAPDUReq.deleter
	def CardRdrAPDUReq(self):
		del self._CardRdrAPDUReq
		self._CardRdrAPDUReq = None

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
	def PrtReq(self):
		return self._PrtReq

	@PrtReq.setter
	def PrtReq(self, value):
		self._PrtReq = value if type(value) != auto else self.make_default("PrtReq")

	@PrtReq.deleter
	def PrtReq(self):
		del self._PrtReq
		self._PrtReq = None

	@property
	def InitlstnCardRdrReq(self):
		return self._InitlstnCardRdrReq

	@InitlstnCardRdrReq.setter
	def InitlstnCardRdrReq(self, value):
		self._InitlstnCardRdrReq = value if type(value) != auto else self.make_default("InitlstnCardRdrReq")

	@InitlstnCardRdrReq.deleter
	def InitlstnCardRdrReq(self):
		del self._InitlstnCardRdrReq
		self._InitlstnCardRdrReq = None

	@property
	def InptNtfctn(self):
		return self._InptNtfctn

	@InptNtfctn.setter
	def InptNtfctn(self, value):
		self._InptNtfctn = value if type(value) != auto else self.make_default("InptNtfctn")

	@InptNtfctn.deleter
	def InptNtfctn(self):
		del self._InptNtfctn
		self._InptNtfctn = None

	@property
	def PlayRsrcReq(self):
		return self._PlayRsrcReq

	@PlayRsrcReq.setter
	def PlayRsrcReq(self, value):
		self._PlayRsrcReq = value if type(value) != auto else self.make_default("PlayRsrcReq")

	@PlayRsrcReq.deleter
	def PlayRsrcReq(self):
		del self._PlayRsrcReq
		self._PlayRsrcReq = None

	@property
	def ScrInptReq(self):
		return self._ScrInptReq

	@ScrInptReq.setter
	def ScrInptReq(self, value):
		self._ScrInptReq = value if type(value) != auto else self.make_default("ScrInptReq")

	@ScrInptReq.deleter
	def ScrInptReq(self):
		del self._ScrInptReq
		self._ScrInptReq = None

	@property
	def InptReq(self):
		return self._InptReq

	@InptReq.setter
	def InptReq(self, value):
		self._InptReq = value if type(value) != auto else self.make_default("InptReq")

	@InptReq.deleter
	def InptReq(self):
		del self._InptReq
		self._InptReq = None

	@property
	def PwrOffCardRdrReq(self):
		return self._PwrOffCardRdrReq

	@PwrOffCardRdrReq.setter
	def PwrOffCardRdrReq(self, value):
		self._PwrOffCardRdrReq = value if type(value) != auto else self.make_default("PwrOffCardRdrReq")

	@PwrOffCardRdrReq.deleter
	def PwrOffCardRdrReq(self):
		del self._PwrOffCardRdrReq
		self._PwrOffCardRdrReq = None

	@property
	def DispReq(self):
		return self._DispReq

	@DispReq.setter
	def DispReq(self, value):
		self._DispReq = value if type(value) != auto else self.make_default("DispReq")

	@DispReq.deleter
	def DispReq(self):
		del self._DispReq
		self._DispReq = None

	@property
	def TrnsmssnReq(self):
		return self._TrnsmssnReq

	@TrnsmssnReq.setter
	def TrnsmssnReq(self, value):
		self._TrnsmssnReq = value if type(value) != auto else self.make_default("TrnsmssnReq")

	@TrnsmssnReq.deleter
	def TrnsmssnReq(self):
		del self._TrnsmssnReq
		self._TrnsmssnReq = None

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
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CardRdrAPDUReq', type=DeviceSendApplicationProtocolDataUnitCardReaderRequest1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Envt', type=CardPaymentEnvironment81, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtReq', type=DevicePrintRequest6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitlstnCardRdrReq', type=DeviceInitialisationCardReaderRequest6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InptNtfctn', type=DeviceInputNotification6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlayRsrcReq', type=DevicePlayResourceRequest1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScrInptReq', type=DeviceSecureInputRequest6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InptReq', type=DeviceInputRequest6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PwrOffCardRdrReq', type=DevicePoweroffCardReaderRequest6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DispReq', type=DeviceDisplayRequest6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrnsmssnReq', type=DeviceTransmitMessageRequest2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cntxt', type=PaymentContext30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcCntt', type=RetailerService8Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

