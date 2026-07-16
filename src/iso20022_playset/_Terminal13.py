# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATICALaxProcessing
from . import CardDataReading11Code
from . import CardDataWriting2Code
from . import CardholderVerificationCapability6Code
from . import DisplayCapabilities6
from . import GeographicPointInDecimalDegreesText
from . import ISO8583AccountEntryDeviceTypeCode
from . import ISO8583PINEntryCapabilityCode
from . import ISOMax3ACountryCode
from . import Max16Text
from . import Max256Text
from . import Max35Text
from . import Number
from . import OnLineCapability2Code
from . import Software2
from . import TerminalIntegrationCategory1Code
from . import TerminalType2Code
from . import TrueFalseIndicator

class Terminal13(base_types._BaseFieldType):

	__slots__ = ["_ApprvlCdLngth", "_CardCaptrCpbl", "_CertfctnId", "_CrdhldrVrfctnCpblty", "_Ctry", "_GeogcLctn", "_Id", "_IntgtnTp", "_MsgCpblty", "_MxScrptLngth", "_NtlData", "_OffPrmiss", "_OnBrd", "_OnLineCpblty", "_Outdr", "_PINLngthCpblty", "_PINNtrySctyChrtc", "_PrvtData", "_RdngCpblty", "_Sftwr", "_SrlNb", "_SubTp", "_TempScrStorg", "_Tp", "_WrtgCpblty"]
	@property
	def ApprvlCdLngth(self):
		return self._ApprvlCdLngth

	@ApprvlCdLngth.setter
	def ApprvlCdLngth(self, value):
		self._ApprvlCdLngth = value if value is not None else base_types.UninitialisedField(self, 'ApprvlCdLngth', Number, False)

	@ApprvlCdLngth.deleter
	def ApprvlCdLngth(self):
		del self._ApprvlCdLngth
		self._ApprvlCdLngth = base_types.UninitialisedField(self, 'ApprvlCdLngth', Number, False)

	@property
	def CardCaptrCpbl(self):
		return self._CardCaptrCpbl

	@CardCaptrCpbl.setter
	def CardCaptrCpbl(self, value):
		self._CardCaptrCpbl = value if value is not None else base_types.UninitialisedField(self, 'CardCaptrCpbl', TrueFalseIndicator, False)

	@CardCaptrCpbl.deleter
	def CardCaptrCpbl(self):
		del self._CardCaptrCpbl
		self._CardCaptrCpbl = base_types.UninitialisedField(self, 'CardCaptrCpbl', TrueFalseIndicator, False)

	@property
	def CertfctnId(self):
		return self._CertfctnId

	@CertfctnId.setter
	def CertfctnId(self, value):
		self._CertfctnId = value if value is not None else base_types.UninitialisedField(self, 'CertfctnId', Max256Text, False)

	@CertfctnId.deleter
	def CertfctnId(self):
		del self._CertfctnId
		self._CertfctnId = base_types.UninitialisedField(self, 'CertfctnId', Max256Text, False)

	@property
	def CrdhldrVrfctnCpblty(self):
		return self._CrdhldrVrfctnCpblty

	@CrdhldrVrfctnCpblty.setter
	def CrdhldrVrfctnCpblty(self, value):
		self._CrdhldrVrfctnCpblty = value if value is not None else base_types.UninitialisedField(self, 'CrdhldrVrfctnCpblty', CardholderVerificationCapability6Code, True)

	@CrdhldrVrfctnCpblty.deleter
	def CrdhldrVrfctnCpblty(self):
		del self._CrdhldrVrfctnCpblty
		self._CrdhldrVrfctnCpblty = base_types.UninitialisedField(self, 'CrdhldrVrfctnCpblty', CardholderVerificationCapability6Code, True)

	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if value is not None else base_types.UninitialisedField(self, 'Ctry', ISOMax3ACountryCode, False)

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = base_types.UninitialisedField(self, 'Ctry', ISOMax3ACountryCode, False)

	@property
	def GeogcLctn(self):
		return self._GeogcLctn

	@GeogcLctn.setter
	def GeogcLctn(self, value):
		self._GeogcLctn = value if value is not None else base_types.UninitialisedField(self, 'GeogcLctn', GeographicPointInDecimalDegreesText, False)

	@GeogcLctn.deleter
	def GeogcLctn(self):
		del self._GeogcLctn
		self._GeogcLctn = base_types.UninitialisedField(self, 'GeogcLctn', GeographicPointInDecimalDegreesText, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max16Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max16Text, False)

	@property
	def IntgtnTp(self):
		return self._IntgtnTp

	@IntgtnTp.setter
	def IntgtnTp(self, value):
		self._IntgtnTp = value if value is not None else base_types.UninitialisedField(self, 'IntgtnTp', TerminalIntegrationCategory1Code, False)

	@IntgtnTp.deleter
	def IntgtnTp(self):
		del self._IntgtnTp
		self._IntgtnTp = base_types.UninitialisedField(self, 'IntgtnTp', TerminalIntegrationCategory1Code, False)

	@property
	def MsgCpblty(self):
		return self._MsgCpblty

	@MsgCpblty.setter
	def MsgCpblty(self, value):
		self._MsgCpblty = value if value is not None else base_types.UninitialisedField(self, 'MsgCpblty', DisplayCapabilities6, True)

	@MsgCpblty.deleter
	def MsgCpblty(self):
		del self._MsgCpblty
		self._MsgCpblty = base_types.UninitialisedField(self, 'MsgCpblty', DisplayCapabilities6, True)

	@property
	def MxScrptLngth(self):
		return self._MxScrptLngth

	@MxScrptLngth.setter
	def MxScrptLngth(self, value):
		self._MxScrptLngth = value if value is not None else base_types.UninitialisedField(self, 'MxScrptLngth', Number, False)

	@MxScrptLngth.deleter
	def MxScrptLngth(self):
		del self._MxScrptLngth
		self._MxScrptLngth = base_types.UninitialisedField(self, 'MxScrptLngth', Number, False)

	@property
	def NtlData(self):
		return self._NtlData

	@NtlData.setter
	def NtlData(self, value):
		self._NtlData = value if value is not None else base_types.UninitialisedField(self, 'NtlData', ATICALaxProcessing, True)

	@NtlData.deleter
	def NtlData(self):
		del self._NtlData
		self._NtlData = base_types.UninitialisedField(self, 'NtlData', ATICALaxProcessing, True)

	@property
	def OffPrmiss(self):
		return self._OffPrmiss

	@OffPrmiss.setter
	def OffPrmiss(self, value):
		self._OffPrmiss = value if value is not None else base_types.UninitialisedField(self, 'OffPrmiss', TrueFalseIndicator, False)

	@OffPrmiss.deleter
	def OffPrmiss(self):
		del self._OffPrmiss
		self._OffPrmiss = base_types.UninitialisedField(self, 'OffPrmiss', TrueFalseIndicator, False)

	@property
	def OnBrd(self):
		return self._OnBrd

	@OnBrd.setter
	def OnBrd(self, value):
		self._OnBrd = value if value is not None else base_types.UninitialisedField(self, 'OnBrd', TrueFalseIndicator, False)

	@OnBrd.deleter
	def OnBrd(self):
		del self._OnBrd
		self._OnBrd = base_types.UninitialisedField(self, 'OnBrd', TrueFalseIndicator, False)

	@property
	def OnLineCpblty(self):
		return self._OnLineCpblty

	@OnLineCpblty.setter
	def OnLineCpblty(self, value):
		self._OnLineCpblty = value if value is not None else base_types.UninitialisedField(self, 'OnLineCpblty', OnLineCapability2Code, False)

	@OnLineCpblty.deleter
	def OnLineCpblty(self):
		del self._OnLineCpblty
		self._OnLineCpblty = base_types.UninitialisedField(self, 'OnLineCpblty', OnLineCapability2Code, False)

	@property
	def Outdr(self):
		return self._Outdr

	@Outdr.setter
	def Outdr(self, value):
		self._Outdr = value if value is not None else base_types.UninitialisedField(self, 'Outdr', TrueFalseIndicator, False)

	@Outdr.deleter
	def Outdr(self):
		del self._Outdr
		self._Outdr = base_types.UninitialisedField(self, 'Outdr', TrueFalseIndicator, False)

	@property
	def PINLngthCpblty(self):
		return self._PINLngthCpblty

	@PINLngthCpblty.setter
	def PINLngthCpblty(self, value):
		self._PINLngthCpblty = value if value is not None else base_types.UninitialisedField(self, 'PINLngthCpblty', Number, False)

	@PINLngthCpblty.deleter
	def PINLngthCpblty(self):
		del self._PINLngthCpblty
		self._PINLngthCpblty = base_types.UninitialisedField(self, 'PINLngthCpblty', Number, False)

	@property
	def PINNtrySctyChrtc(self):
		return self._PINNtrySctyChrtc

	@PINNtrySctyChrtc.setter
	def PINNtrySctyChrtc(self, value):
		self._PINNtrySctyChrtc = value if value is not None else base_types.UninitialisedField(self, 'PINNtrySctyChrtc', ISO8583PINEntryCapabilityCode, False)

	@PINNtrySctyChrtc.deleter
	def PINNtrySctyChrtc(self):
		del self._PINNtrySctyChrtc
		self._PINNtrySctyChrtc = base_types.UninitialisedField(self, 'PINNtrySctyChrtc', ISO8583PINEntryCapabilityCode, False)

	@property
	def PrvtData(self):
		return self._PrvtData

	@PrvtData.setter
	def PrvtData(self, value):
		self._PrvtData = value if value is not None else base_types.UninitialisedField(self, 'PrvtData', ATICALaxProcessing, True)

	@PrvtData.deleter
	def PrvtData(self):
		del self._PrvtData
		self._PrvtData = base_types.UninitialisedField(self, 'PrvtData', ATICALaxProcessing, True)

	@property
	def RdngCpblty(self):
		return self._RdngCpblty

	@RdngCpblty.setter
	def RdngCpblty(self, value):
		self._RdngCpblty = value if value is not None else base_types.UninitialisedField(self, 'RdngCpblty', CardDataReading11Code, True)

	@RdngCpblty.deleter
	def RdngCpblty(self):
		del self._RdngCpblty
		self._RdngCpblty = base_types.UninitialisedField(self, 'RdngCpblty', CardDataReading11Code, True)

	@property
	def Sftwr(self):
		return self._Sftwr

	@Sftwr.setter
	def Sftwr(self, value):
		self._Sftwr = value if value is not None else base_types.UninitialisedField(self, 'Sftwr', Software2, True)

	@Sftwr.deleter
	def Sftwr(self):
		del self._Sftwr
		self._Sftwr = base_types.UninitialisedField(self, 'Sftwr', Software2, True)

	@property
	def SrlNb(self):
		return self._SrlNb

	@SrlNb.setter
	def SrlNb(self, value):
		self._SrlNb = value if value is not None else base_types.UninitialisedField(self, 'SrlNb', Max35Text, False)

	@SrlNb.deleter
	def SrlNb(self):
		del self._SrlNb
		self._SrlNb = base_types.UninitialisedField(self, 'SrlNb', Max35Text, False)

	@property
	def SubTp(self):
		return self._SubTp

	@SubTp.setter
	def SubTp(self, value):
		self._SubTp = value if value is not None else base_types.UninitialisedField(self, 'SubTp', ISO8583AccountEntryDeviceTypeCode, False)

	@SubTp.deleter
	def SubTp(self):
		del self._SubTp
		self._SubTp = base_types.UninitialisedField(self, 'SubTp', ISO8583AccountEntryDeviceTypeCode, False)

	@property
	def TempScrStorg(self):
		return self._TempScrStorg

	@TempScrStorg.setter
	def TempScrStorg(self, value):
		self._TempScrStorg = value if value is not None else base_types.UninitialisedField(self, 'TempScrStorg', TrueFalseIndicator, False)

	@TempScrStorg.deleter
	def TempScrStorg(self):
		del self._TempScrStorg
		self._TempScrStorg = base_types.UninitialisedField(self, 'TempScrStorg', TrueFalseIndicator, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', TerminalType2Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', TerminalType2Code, False)

	@property
	def WrtgCpblty(self):
		return self._WrtgCpblty

	@WrtgCpblty.setter
	def WrtgCpblty(self, value):
		self._WrtgCpblty = value if value is not None else base_types.UninitialisedField(self, 'WrtgCpblty', CardDataWriting2Code, True)

	@WrtgCpblty.deleter
	def WrtgCpblty(self):
		del self._WrtgCpblty
		self._WrtgCpblty = base_types.UninitialisedField(self, 'WrtgCpblty', CardDataWriting2Code, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ApprvlCdLngth', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardCaptrCpbl', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertfctnId', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrdhldrVrfctnCpblty', type=CardholderVerificationCapability6Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ctry', type=ISOMax3ACountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GeogcLctn', type=GeographicPointInDecimalDegreesText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntgtnTp', type=TerminalIntegrationCategory1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgCpblty', type=DisplayCapabilities6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MxScrptLngth', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtlData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OffPrmiss', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OnBrd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OnLineCpblty', type=OnLineCapability2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Outdr', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PINLngthCpblty', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PINNtrySctyChrtc', type=ISO8583PINEntryCapabilityCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvtData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RdngCpblty', type=CardDataReading11Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sftwr', type=Software2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SrlNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubTp', type=ISO8583AccountEntryDeviceTypeCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TempScrStorg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=TerminalType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WrtgCpblty', type=CardDataWriting2Code, min=0, max=None, mutex_group=None, array=True),
	))