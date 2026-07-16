# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CardPaymentEnvironment81
from . import DeviceDisplayResponse2
from . import DeviceInitialisationCardReaderResponse2
from . import DeviceInputResponse6
from . import DevicePrintResponse1
from . import DeviceSecureInputResponse6
from . import DeviceSendApplicationProtocolDataUnitCardReaderResponse1
from . import DeviceTransmitMessageResponse1
from . import PaymentContext30
from . import ResponseType11
from . import RetailerService9Code
from . import SupplementaryData1

class DeviceResponse8(base_types._BaseFieldType):

	__slots__ = ["_CardRdrApplPrtcolDataUnitRspn", "_Cntxt", "_DispRspn", "_Envt", "_InitlstnCardRdrRspn", "_InptRspn", "_PrtRspn", "_Rspn", "_ScrInptRspn", "_SplmtryData", "_SvcCntt", "_TrnsmssnRspn"]
	@property
	def CardRdrApplPrtcolDataUnitRspn(self):
		return self._CardRdrApplPrtcolDataUnitRspn

	@CardRdrApplPrtcolDataUnitRspn.setter
	def CardRdrApplPrtcolDataUnitRspn(self, value):
		self._CardRdrApplPrtcolDataUnitRspn = value if value is not None else base_types.UninitialisedField(self, 'CardRdrApplPrtcolDataUnitRspn', DeviceSendApplicationProtocolDataUnitCardReaderResponse1, False)

	@CardRdrApplPrtcolDataUnitRspn.deleter
	def CardRdrApplPrtcolDataUnitRspn(self):
		del self._CardRdrApplPrtcolDataUnitRspn
		self._CardRdrApplPrtcolDataUnitRspn = base_types.UninitialisedField(self, 'CardRdrApplPrtcolDataUnitRspn', DeviceSendApplicationProtocolDataUnitCardReaderResponse1, False)

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
	def DispRspn(self):
		return self._DispRspn

	@DispRspn.setter
	def DispRspn(self, value):
		self._DispRspn = value if value is not None else base_types.UninitialisedField(self, 'DispRspn', DeviceDisplayResponse2, False)

	@DispRspn.deleter
	def DispRspn(self):
		del self._DispRspn
		self._DispRspn = base_types.UninitialisedField(self, 'DispRspn', DeviceDisplayResponse2, False)

	@property
	def Envt(self):
		return self._Envt

	@Envt.setter
	def Envt(self, value):
		self._Envt = value if value is not None else base_types.UninitialisedField(self, 'Envt', CardPaymentEnvironment81, False)

	@Envt.deleter
	def Envt(self):
		del self._Envt
		self._Envt = base_types.UninitialisedField(self, 'Envt', CardPaymentEnvironment81, False)

	@property
	def InitlstnCardRdrRspn(self):
		return self._InitlstnCardRdrRspn

	@InitlstnCardRdrRspn.setter
	def InitlstnCardRdrRspn(self, value):
		self._InitlstnCardRdrRspn = value if value is not None else base_types.UninitialisedField(self, 'InitlstnCardRdrRspn', DeviceInitialisationCardReaderResponse2, False)

	@InitlstnCardRdrRspn.deleter
	def InitlstnCardRdrRspn(self):
		del self._InitlstnCardRdrRspn
		self._InitlstnCardRdrRspn = base_types.UninitialisedField(self, 'InitlstnCardRdrRspn', DeviceInitialisationCardReaderResponse2, False)

	@property
	def InptRspn(self):
		return self._InptRspn

	@InptRspn.setter
	def InptRspn(self, value):
		self._InptRspn = value if value is not None else base_types.UninitialisedField(self, 'InptRspn', DeviceInputResponse6, False)

	@InptRspn.deleter
	def InptRspn(self):
		del self._InptRspn
		self._InptRspn = base_types.UninitialisedField(self, 'InptRspn', DeviceInputResponse6, False)

	@property
	def PrtRspn(self):
		return self._PrtRspn

	@PrtRspn.setter
	def PrtRspn(self, value):
		self._PrtRspn = value if value is not None else base_types.UninitialisedField(self, 'PrtRspn', DevicePrintResponse1, False)

	@PrtRspn.deleter
	def PrtRspn(self):
		del self._PrtRspn
		self._PrtRspn = base_types.UninitialisedField(self, 'PrtRspn', DevicePrintResponse1, False)

	@property
	def Rspn(self):
		return self._Rspn

	@Rspn.setter
	def Rspn(self, value):
		self._Rspn = value if value is not None else base_types.UninitialisedField(self, 'Rspn', ResponseType11, False)

	@Rspn.deleter
	def Rspn(self):
		del self._Rspn
		self._Rspn = base_types.UninitialisedField(self, 'Rspn', ResponseType11, False)

	@property
	def ScrInptRspn(self):
		return self._ScrInptRspn

	@ScrInptRspn.setter
	def ScrInptRspn(self, value):
		self._ScrInptRspn = value if value is not None else base_types.UninitialisedField(self, 'ScrInptRspn', DeviceSecureInputResponse6, False)

	@ScrInptRspn.deleter
	def ScrInptRspn(self):
		del self._ScrInptRspn
		self._ScrInptRspn = base_types.UninitialisedField(self, 'ScrInptRspn', DeviceSecureInputResponse6, False)

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
		self._SvcCntt = value if value is not None else base_types.UninitialisedField(self, 'SvcCntt', RetailerService9Code, False)

	@SvcCntt.deleter
	def SvcCntt(self):
		del self._SvcCntt
		self._SvcCntt = base_types.UninitialisedField(self, 'SvcCntt', RetailerService9Code, False)

	@property
	def TrnsmssnRspn(self):
		return self._TrnsmssnRspn

	@TrnsmssnRspn.setter
	def TrnsmssnRspn(self, value):
		self._TrnsmssnRspn = value if value is not None else base_types.UninitialisedField(self, 'TrnsmssnRspn', DeviceTransmitMessageResponse1, False)

	@TrnsmssnRspn.deleter
	def TrnsmssnRspn(self):
		del self._TrnsmssnRspn
		self._TrnsmssnRspn = base_types.UninitialisedField(self, 'TrnsmssnRspn', DeviceTransmitMessageResponse1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CardRdrApplPrtcolDataUnitRspn', type=DeviceSendApplicationProtocolDataUnitCardReaderResponse1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cntxt', type=PaymentContext30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DispRspn', type=DeviceDisplayResponse2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Envt', type=CardPaymentEnvironment81, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitlstnCardRdrRspn', type=DeviceInitialisationCardReaderResponse2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InptRspn', type=DeviceInputResponse6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtRspn', type=DevicePrintResponse1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rspn', type=ResponseType11, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScrInptRspn', type=DeviceSecureInputResponse6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SvcCntt', type=RetailerService9Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrnsmssnRspn', type=DeviceTransmitMessageResponse1, min=0, max=1, mutex_group=None, array=False),
	))