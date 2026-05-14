from . import base_types
from ._CardPaymentEnvironment82 import CardPaymentEnvironment82
from ._DeviceDisplayRequest7 import DeviceDisplayRequest7
from ._DeviceInitialisationCardReaderRequest7 import DeviceInitialisationCardReaderRequest7
from ._DeviceInputNotification7 import DeviceInputNotification7
from ._DeviceInputRequest7 import DeviceInputRequest7
from ._DevicePlayResourceRequest1 import DevicePlayResourceRequest1
from ._DevicePoweroffCardReaderRequest7 import DevicePoweroffCardReaderRequest7
from ._DevicePrintRequest7 import DevicePrintRequest7
from ._DeviceSecureInputRequest6 import DeviceSecureInputRequest6
from ._DeviceSendApplicationProtocolDataUnitCardReaderRequest1 import DeviceSendApplicationProtocolDataUnitCardReaderRequest1
from ._DeviceTransmitMessageRequest2 import DeviceTransmitMessageRequest2
from ._PaymentContext30 import PaymentContext30
from ._RetailerService8Code import RetailerService8Code
from ._SupplementaryData1 import SupplementaryData1

class DeviceRequest9(base_types._BaseFieldType):

	__slots__ = ["_CardRdrAPDUReq", "_Cntxt", "_DispReq", "_Envt", "_InitlstnCardRdrReq", "_InptNtfctn", "_InptReq", "_PlayRsrcReq", "_PrtReq", "_PwrOffCardRdrReq", "_ScrInptReq", "_SplmtryData", "_SvcCntt", "_TrnsmssnReq"]
	@property
	def CardRdrAPDUReq(self):
		return self._CardRdrAPDUReq

	@CardRdrAPDUReq.setter
	def CardRdrAPDUReq(self, value):
		self._CardRdrAPDUReq = value if type(value) != base_types.auto else self.make_default("CardRdrAPDUReq")

	@CardRdrAPDUReq.deleter
	def CardRdrAPDUReq(self):
		del self._CardRdrAPDUReq
		self._CardRdrAPDUReq = None

	@property
	def Cntxt(self):
		return self._Cntxt

	@Cntxt.setter
	def Cntxt(self, value):
		self._Cntxt = value if type(value) != base_types.auto else self.make_default("Cntxt")

	@Cntxt.deleter
	def Cntxt(self):
		del self._Cntxt
		self._Cntxt = None

	@property
	def DispReq(self):
		return self._DispReq

	@DispReq.setter
	def DispReq(self, value):
		self._DispReq = value if type(value) != base_types.auto else self.make_default("DispReq")

	@DispReq.deleter
	def DispReq(self):
		del self._DispReq
		self._DispReq = None

	@property
	def Envt(self):
		return self._Envt

	@Envt.setter
	def Envt(self, value):
		self._Envt = value if type(value) != base_types.auto else self.make_default("Envt")

	@Envt.deleter
	def Envt(self):
		del self._Envt
		self._Envt = None

	@property
	def InitlstnCardRdrReq(self):
		return self._InitlstnCardRdrReq

	@InitlstnCardRdrReq.setter
	def InitlstnCardRdrReq(self, value):
		self._InitlstnCardRdrReq = value if type(value) != base_types.auto else self.make_default("InitlstnCardRdrReq")

	@InitlstnCardRdrReq.deleter
	def InitlstnCardRdrReq(self):
		del self._InitlstnCardRdrReq
		self._InitlstnCardRdrReq = None

	@property
	def InptNtfctn(self):
		return self._InptNtfctn

	@InptNtfctn.setter
	def InptNtfctn(self, value):
		self._InptNtfctn = value if type(value) != base_types.auto else self.make_default("InptNtfctn")

	@InptNtfctn.deleter
	def InptNtfctn(self):
		del self._InptNtfctn
		self._InptNtfctn = None

	@property
	def InptReq(self):
		return self._InptReq

	@InptReq.setter
	def InptReq(self, value):
		self._InptReq = value if type(value) != base_types.auto else self.make_default("InptReq")

	@InptReq.deleter
	def InptReq(self):
		del self._InptReq
		self._InptReq = None

	@property
	def PlayRsrcReq(self):
		return self._PlayRsrcReq

	@PlayRsrcReq.setter
	def PlayRsrcReq(self, value):
		self._PlayRsrcReq = value if type(value) != base_types.auto else self.make_default("PlayRsrcReq")

	@PlayRsrcReq.deleter
	def PlayRsrcReq(self):
		del self._PlayRsrcReq
		self._PlayRsrcReq = None

	@property
	def PrtReq(self):
		return self._PrtReq

	@PrtReq.setter
	def PrtReq(self, value):
		self._PrtReq = value if type(value) != base_types.auto else self.make_default("PrtReq")

	@PrtReq.deleter
	def PrtReq(self):
		del self._PrtReq
		self._PrtReq = None

	@property
	def PwrOffCardRdrReq(self):
		return self._PwrOffCardRdrReq

	@PwrOffCardRdrReq.setter
	def PwrOffCardRdrReq(self, value):
		self._PwrOffCardRdrReq = value if type(value) != base_types.auto else self.make_default("PwrOffCardRdrReq")

	@PwrOffCardRdrReq.deleter
	def PwrOffCardRdrReq(self):
		del self._PwrOffCardRdrReq
		self._PwrOffCardRdrReq = None

	@property
	def ScrInptReq(self):
		return self._ScrInptReq

	@ScrInptReq.setter
	def ScrInptReq(self, value):
		self._ScrInptReq = value if type(value) != base_types.auto else self.make_default("ScrInptReq")

	@ScrInptReq.deleter
	def ScrInptReq(self):
		del self._ScrInptReq
		self._ScrInptReq = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def SvcCntt(self):
		return self._SvcCntt

	@SvcCntt.setter
	def SvcCntt(self, value):
		self._SvcCntt = value if type(value) != base_types.auto else self.make_default("SvcCntt")

	@SvcCntt.deleter
	def SvcCntt(self):
		del self._SvcCntt
		self._SvcCntt = None

	@property
	def TrnsmssnReq(self):
		return self._TrnsmssnReq

	@TrnsmssnReq.setter
	def TrnsmssnReq(self, value):
		self._TrnsmssnReq = value if type(value) != base_types.auto else self.make_default("TrnsmssnReq")

	@TrnsmssnReq.deleter
	def TrnsmssnReq(self):
		del self._TrnsmssnReq
		self._TrnsmssnReq = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CardRdrAPDUReq', type=DeviceSendApplicationProtocolDataUnitCardReaderRequest1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cntxt', type=PaymentContext30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DispReq', type=DeviceDisplayRequest7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Envt', type=CardPaymentEnvironment82, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitlstnCardRdrReq', type=DeviceInitialisationCardReaderRequest7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InptNtfctn', type=DeviceInputNotification7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InptReq', type=DeviceInputRequest7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlayRsrcReq', type=DevicePlayResourceRequest1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtReq', type=DevicePrintRequest7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PwrOffCardRdrReq', type=DevicePoweroffCardReaderRequest7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScrInptReq', type=DeviceSecureInputRequest6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SvcCntt', type=RetailerService8Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrnsmssnReq', type=DeviceTransmitMessageRequest2, min=0, max=1, mutex_group=None, array=False),
	))

