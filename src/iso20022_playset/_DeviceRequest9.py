# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CardPaymentEnvironment82
from . import DeviceDisplayRequest7
from . import DeviceInitialisationCardReaderRequest7
from . import DeviceInputNotification7
from . import DeviceInputRequest7
from . import DevicePlayResourceRequest1
from . import DevicePoweroffCardReaderRequest7
from . import DevicePrintRequest7
from . import DeviceSecureInputRequest6
from . import DeviceSendApplicationProtocolDataUnitCardReaderRequest1
from . import DeviceTransmitMessageRequest2
from . import PaymentContext30
from . import RetailerService8Code
from . import SupplementaryData1

class DeviceRequest9(base_types._BaseFieldType):

	__slots__ = ["_CardRdrAPDUReq", "_Cntxt", "_DispReq", "_Envt", "_InitlstnCardRdrReq", "_InptNtfctn", "_InptReq", "_PlayRsrcReq", "_PrtReq", "_PwrOffCardRdrReq", "_ScrInptReq", "_SplmtryData", "_SvcCntt", "_TrnsmssnReq"]
	@property
	def CardRdrAPDUReq(self):
		return self._CardRdrAPDUReq

	@CardRdrAPDUReq.setter
	def CardRdrAPDUReq(self, value):
		self._CardRdrAPDUReq = value if value is not None else base_types.UninitialisedField(self, 'CardRdrAPDUReq', DeviceSendApplicationProtocolDataUnitCardReaderRequest1, False)

	@CardRdrAPDUReq.deleter
	def CardRdrAPDUReq(self):
		del self._CardRdrAPDUReq
		self._CardRdrAPDUReq = base_types.UninitialisedField(self, 'CardRdrAPDUReq', DeviceSendApplicationProtocolDataUnitCardReaderRequest1, False)

	@property
	def Cntxt(self):
		return self._Cntxt

	@Cntxt.setter
	def Cntxt(self, value):
		self._Cntxt = value if value is not None else base_types.UninitialisedField(self, 'Cntxt', PaymentContext30, False)

	@Cntxt.deleter
	def Cntxt(self):
		del self._Cntxt
		self._Cntxt = base_types.UninitialisedField(self, 'Cntxt', PaymentContext30, False)

	@property
	def DispReq(self):
		return self._DispReq

	@DispReq.setter
	def DispReq(self, value):
		self._DispReq = value if value is not None else base_types.UninitialisedField(self, 'DispReq', DeviceDisplayRequest7, False)

	@DispReq.deleter
	def DispReq(self):
		del self._DispReq
		self._DispReq = base_types.UninitialisedField(self, 'DispReq', DeviceDisplayRequest7, False)

	@property
	def Envt(self):
		return self._Envt

	@Envt.setter
	def Envt(self, value):
		self._Envt = value if value is not None else base_types.UninitialisedField(self, 'Envt', CardPaymentEnvironment82, False)

	@Envt.deleter
	def Envt(self):
		del self._Envt
		self._Envt = base_types.UninitialisedField(self, 'Envt', CardPaymentEnvironment82, False)

	@property
	def InitlstnCardRdrReq(self):
		return self._InitlstnCardRdrReq

	@InitlstnCardRdrReq.setter
	def InitlstnCardRdrReq(self, value):
		self._InitlstnCardRdrReq = value if value is not None else base_types.UninitialisedField(self, 'InitlstnCardRdrReq', DeviceInitialisationCardReaderRequest7, False)

	@InitlstnCardRdrReq.deleter
	def InitlstnCardRdrReq(self):
		del self._InitlstnCardRdrReq
		self._InitlstnCardRdrReq = base_types.UninitialisedField(self, 'InitlstnCardRdrReq', DeviceInitialisationCardReaderRequest7, False)

	@property
	def InptNtfctn(self):
		return self._InptNtfctn

	@InptNtfctn.setter
	def InptNtfctn(self, value):
		self._InptNtfctn = value if value is not None else base_types.UninitialisedField(self, 'InptNtfctn', DeviceInputNotification7, False)

	@InptNtfctn.deleter
	def InptNtfctn(self):
		del self._InptNtfctn
		self._InptNtfctn = base_types.UninitialisedField(self, 'InptNtfctn', DeviceInputNotification7, False)

	@property
	def InptReq(self):
		return self._InptReq

	@InptReq.setter
	def InptReq(self, value):
		self._InptReq = value if value is not None else base_types.UninitialisedField(self, 'InptReq', DeviceInputRequest7, False)

	@InptReq.deleter
	def InptReq(self):
		del self._InptReq
		self._InptReq = base_types.UninitialisedField(self, 'InptReq', DeviceInputRequest7, False)

	@property
	def PlayRsrcReq(self):
		return self._PlayRsrcReq

	@PlayRsrcReq.setter
	def PlayRsrcReq(self, value):
		self._PlayRsrcReq = value if value is not None else base_types.UninitialisedField(self, 'PlayRsrcReq', DevicePlayResourceRequest1, False)

	@PlayRsrcReq.deleter
	def PlayRsrcReq(self):
		del self._PlayRsrcReq
		self._PlayRsrcReq = base_types.UninitialisedField(self, 'PlayRsrcReq', DevicePlayResourceRequest1, False)

	@property
	def PrtReq(self):
		return self._PrtReq

	@PrtReq.setter
	def PrtReq(self, value):
		self._PrtReq = value if value is not None else base_types.UninitialisedField(self, 'PrtReq', DevicePrintRequest7, False)

	@PrtReq.deleter
	def PrtReq(self):
		del self._PrtReq
		self._PrtReq = base_types.UninitialisedField(self, 'PrtReq', DevicePrintRequest7, False)

	@property
	def PwrOffCardRdrReq(self):
		return self._PwrOffCardRdrReq

	@PwrOffCardRdrReq.setter
	def PwrOffCardRdrReq(self, value):
		self._PwrOffCardRdrReq = value if value is not None else base_types.UninitialisedField(self, 'PwrOffCardRdrReq', DevicePoweroffCardReaderRequest7, False)

	@PwrOffCardRdrReq.deleter
	def PwrOffCardRdrReq(self):
		del self._PwrOffCardRdrReq
		self._PwrOffCardRdrReq = base_types.UninitialisedField(self, 'PwrOffCardRdrReq', DevicePoweroffCardReaderRequest7, False)

	@property
	def ScrInptReq(self):
		return self._ScrInptReq

	@ScrInptReq.setter
	def ScrInptReq(self, value):
		self._ScrInptReq = value if value is not None else base_types.UninitialisedField(self, 'ScrInptReq', DeviceSecureInputRequest6, False)

	@ScrInptReq.deleter
	def ScrInptReq(self):
		del self._ScrInptReq
		self._ScrInptReq = base_types.UninitialisedField(self, 'ScrInptReq', DeviceSecureInputRequest6, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@property
	def SvcCntt(self):
		return self._SvcCntt

	@SvcCntt.setter
	def SvcCntt(self, value):
		self._SvcCntt = value if value is not None else base_types.UninitialisedField(self, 'SvcCntt', RetailerService8Code, False)

	@SvcCntt.deleter
	def SvcCntt(self):
		del self._SvcCntt
		self._SvcCntt = base_types.UninitialisedField(self, 'SvcCntt', RetailerService8Code, False)

	@property
	def TrnsmssnReq(self):
		return self._TrnsmssnReq

	@TrnsmssnReq.setter
	def TrnsmssnReq(self, value):
		self._TrnsmssnReq = value if value is not None else base_types.UninitialisedField(self, 'TrnsmssnReq', DeviceTransmitMessageRequest2, False)

	@TrnsmssnReq.deleter
	def TrnsmssnReq(self):
		del self._TrnsmssnReq
		self._TrnsmssnReq = base_types.UninitialisedField(self, 'TrnsmssnReq', DeviceTransmitMessageRequest2, False)

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