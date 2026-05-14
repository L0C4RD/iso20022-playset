# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ATICALaxProcessing import ATICALaxProcessing
from ._CardDataReading11Code import CardDataReading11Code
from ._CardDataWriting2Code import CardDataWriting2Code
from ._CardholderVerificationCapability6Code import CardholderVerificationCapability6Code
from ._DisplayCapabilities6 import DisplayCapabilities6
from ._GeographicPointInDecimalDegreesText import GeographicPointInDecimalDegreesText
from ._ISO8583AccountEntryDeviceTypeCode import ISO8583AccountEntryDeviceTypeCode
from ._ISO8583PINEntryCapabilityCode import ISO8583PINEntryCapabilityCode
from ._ISOMax3ACountryCode import ISOMax3ACountryCode
from ._Max16Text import Max16Text
from ._Max256Text import Max256Text
from ._Max35Text import Max35Text
from ._Number import Number
from ._OnLineCapability2Code import OnLineCapability2Code
from ._Software2 import Software2
from ._TerminalIntegrationCategory1Code import TerminalIntegrationCategory1Code
from ._TerminalType2Code import TerminalType2Code
from ._TrueFalseIndicator import TrueFalseIndicator

class Terminal10(base_types._BaseFieldType):

	__slots__ = ["_ApprvlCdLngth", "_CardCaptrCpbl", "_CertfctnId", "_CrdhldrVrfctnCpblty", "_Ctry", "_GeogcLctn", "_Id", "_IntgtnTp", "_MsgCpblty", "_MxScrptLngth", "_NcrptnMtd", "_NtlData", "_OffPrmiss", "_OnBrd", "_OnLineCpblty", "_Outdr", "_PINLngthCpblty", "_PINNtryCpblty", "_PrvtData", "_RdngCpblty", "_Sftwr", "_SnglTap", "_SrlNb", "_SubTp", "_TempScrStorg", "_TermnlLineNcrptnCertfd", "_Tp", "_UnqKeyPerTermnlCertfd", "_WrtgCpblty"]
	@property
	def ApprvlCdLngth(self):
		return self._ApprvlCdLngth

	@ApprvlCdLngth.setter
	def ApprvlCdLngth(self, value):
		self._ApprvlCdLngth = value if type(value) != base_types.auto else self.make_default("ApprvlCdLngth")

	@ApprvlCdLngth.deleter
	def ApprvlCdLngth(self):
		del self._ApprvlCdLngth
		self._ApprvlCdLngth = None

	@property
	def CardCaptrCpbl(self):
		return self._CardCaptrCpbl

	@CardCaptrCpbl.setter
	def CardCaptrCpbl(self, value):
		self._CardCaptrCpbl = value if type(value) != base_types.auto else self.make_default("CardCaptrCpbl")

	@CardCaptrCpbl.deleter
	def CardCaptrCpbl(self):
		del self._CardCaptrCpbl
		self._CardCaptrCpbl = None

	@property
	def CertfctnId(self):
		return self._CertfctnId

	@CertfctnId.setter
	def CertfctnId(self, value):
		self._CertfctnId = value if type(value) != base_types.auto else self.make_default("CertfctnId")

	@CertfctnId.deleter
	def CertfctnId(self):
		del self._CertfctnId
		self._CertfctnId = None

	@property
	def CrdhldrVrfctnCpblty(self):
		return self._CrdhldrVrfctnCpblty

	@CrdhldrVrfctnCpblty.setter
	def CrdhldrVrfctnCpblty(self, value):
		self._CrdhldrVrfctnCpblty = value if type(value) != base_types.auto else self.make_default("CrdhldrVrfctnCpblty")

	@CrdhldrVrfctnCpblty.deleter
	def CrdhldrVrfctnCpblty(self):
		del self._CrdhldrVrfctnCpblty
		self._CrdhldrVrfctnCpblty = None

	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if type(value) != base_types.auto else self.make_default("Ctry")

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = None

	@property
	def GeogcLctn(self):
		return self._GeogcLctn

	@GeogcLctn.setter
	def GeogcLctn(self, value):
		self._GeogcLctn = value if type(value) != base_types.auto else self.make_default("GeogcLctn")

	@GeogcLctn.deleter
	def GeogcLctn(self):
		del self._GeogcLctn
		self._GeogcLctn = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def IntgtnTp(self):
		return self._IntgtnTp

	@IntgtnTp.setter
	def IntgtnTp(self, value):
		self._IntgtnTp = value if type(value) != base_types.auto else self.make_default("IntgtnTp")

	@IntgtnTp.deleter
	def IntgtnTp(self):
		del self._IntgtnTp
		self._IntgtnTp = None

	@property
	def MsgCpblty(self):
		return self._MsgCpblty

	@MsgCpblty.setter
	def MsgCpblty(self, value):
		self._MsgCpblty = value if type(value) != base_types.auto else self.make_default("MsgCpblty")

	@MsgCpblty.deleter
	def MsgCpblty(self):
		del self._MsgCpblty
		self._MsgCpblty = None

	@property
	def MxScrptLngth(self):
		return self._MxScrptLngth

	@MxScrptLngth.setter
	def MxScrptLngth(self, value):
		self._MxScrptLngth = value if type(value) != base_types.auto else self.make_default("MxScrptLngth")

	@MxScrptLngth.deleter
	def MxScrptLngth(self):
		del self._MxScrptLngth
		self._MxScrptLngth = None

	@property
	def NcrptnMtd(self):
		return self._NcrptnMtd

	@NcrptnMtd.setter
	def NcrptnMtd(self, value):
		self._NcrptnMtd = value if type(value) != base_types.auto else self.make_default("NcrptnMtd")

	@NcrptnMtd.deleter
	def NcrptnMtd(self):
		del self._NcrptnMtd
		self._NcrptnMtd = None

	@property
	def NtlData(self):
		return self._NtlData

	@NtlData.setter
	def NtlData(self, value):
		self._NtlData = value if type(value) != base_types.auto else self.make_default("NtlData")

	@NtlData.deleter
	def NtlData(self):
		del self._NtlData
		self._NtlData = None

	@property
	def OffPrmiss(self):
		return self._OffPrmiss

	@OffPrmiss.setter
	def OffPrmiss(self, value):
		self._OffPrmiss = value if type(value) != base_types.auto else self.make_default("OffPrmiss")

	@OffPrmiss.deleter
	def OffPrmiss(self):
		del self._OffPrmiss
		self._OffPrmiss = None

	@property
	def OnBrd(self):
		return self._OnBrd

	@OnBrd.setter
	def OnBrd(self, value):
		self._OnBrd = value if type(value) != base_types.auto else self.make_default("OnBrd")

	@OnBrd.deleter
	def OnBrd(self):
		del self._OnBrd
		self._OnBrd = None

	@property
	def OnLineCpblty(self):
		return self._OnLineCpblty

	@OnLineCpblty.setter
	def OnLineCpblty(self, value):
		self._OnLineCpblty = value if type(value) != base_types.auto else self.make_default("OnLineCpblty")

	@OnLineCpblty.deleter
	def OnLineCpblty(self):
		del self._OnLineCpblty
		self._OnLineCpblty = None

	@property
	def Outdr(self):
		return self._Outdr

	@Outdr.setter
	def Outdr(self, value):
		self._Outdr = value if type(value) != base_types.auto else self.make_default("Outdr")

	@Outdr.deleter
	def Outdr(self):
		del self._Outdr
		self._Outdr = None

	@property
	def PINLngthCpblty(self):
		return self._PINLngthCpblty

	@PINLngthCpblty.setter
	def PINLngthCpblty(self, value):
		self._PINLngthCpblty = value if type(value) != base_types.auto else self.make_default("PINLngthCpblty")

	@PINLngthCpblty.deleter
	def PINLngthCpblty(self):
		del self._PINLngthCpblty
		self._PINLngthCpblty = None

	@property
	def PINNtryCpblty(self):
		return self._PINNtryCpblty

	@PINNtryCpblty.setter
	def PINNtryCpblty(self, value):
		self._PINNtryCpblty = value if type(value) != base_types.auto else self.make_default("PINNtryCpblty")

	@PINNtryCpblty.deleter
	def PINNtryCpblty(self):
		del self._PINNtryCpblty
		self._PINNtryCpblty = None

	@property
	def PrvtData(self):
		return self._PrvtData

	@PrvtData.setter
	def PrvtData(self, value):
		self._PrvtData = value if type(value) != base_types.auto else self.make_default("PrvtData")

	@PrvtData.deleter
	def PrvtData(self):
		del self._PrvtData
		self._PrvtData = None

	@property
	def RdngCpblty(self):
		return self._RdngCpblty

	@RdngCpblty.setter
	def RdngCpblty(self, value):
		self._RdngCpblty = value if type(value) != base_types.auto else self.make_default("RdngCpblty")

	@RdngCpblty.deleter
	def RdngCpblty(self):
		del self._RdngCpblty
		self._RdngCpblty = None

	@property
	def Sftwr(self):
		return self._Sftwr

	@Sftwr.setter
	def Sftwr(self, value):
		self._Sftwr = value if type(value) != base_types.auto else self.make_default("Sftwr")

	@Sftwr.deleter
	def Sftwr(self):
		del self._Sftwr
		self._Sftwr = None

	@property
	def SnglTap(self):
		return self._SnglTap

	@SnglTap.setter
	def SnglTap(self, value):
		self._SnglTap = value if type(value) != base_types.auto else self.make_default("SnglTap")

	@SnglTap.deleter
	def SnglTap(self):
		del self._SnglTap
		self._SnglTap = None

	@property
	def SrlNb(self):
		return self._SrlNb

	@SrlNb.setter
	def SrlNb(self, value):
		self._SrlNb = value if type(value) != base_types.auto else self.make_default("SrlNb")

	@SrlNb.deleter
	def SrlNb(self):
		del self._SrlNb
		self._SrlNb = None

	@property
	def SubTp(self):
		return self._SubTp

	@SubTp.setter
	def SubTp(self, value):
		self._SubTp = value if type(value) != base_types.auto else self.make_default("SubTp")

	@SubTp.deleter
	def SubTp(self):
		del self._SubTp
		self._SubTp = None

	@property
	def TempScrStorg(self):
		return self._TempScrStorg

	@TempScrStorg.setter
	def TempScrStorg(self, value):
		self._TempScrStorg = value if type(value) != base_types.auto else self.make_default("TempScrStorg")

	@TempScrStorg.deleter
	def TempScrStorg(self):
		del self._TempScrStorg
		self._TempScrStorg = None

	@property
	def TermnlLineNcrptnCertfd(self):
		return self._TermnlLineNcrptnCertfd

	@TermnlLineNcrptnCertfd.setter
	def TermnlLineNcrptnCertfd(self, value):
		self._TermnlLineNcrptnCertfd = value if type(value) != base_types.auto else self.make_default("TermnlLineNcrptnCertfd")

	@TermnlLineNcrptnCertfd.deleter
	def TermnlLineNcrptnCertfd(self):
		del self._TermnlLineNcrptnCertfd
		self._TermnlLineNcrptnCertfd = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def UnqKeyPerTermnlCertfd(self):
		return self._UnqKeyPerTermnlCertfd

	@UnqKeyPerTermnlCertfd.setter
	def UnqKeyPerTermnlCertfd(self, value):
		self._UnqKeyPerTermnlCertfd = value if type(value) != base_types.auto else self.make_default("UnqKeyPerTermnlCertfd")

	@UnqKeyPerTermnlCertfd.deleter
	def UnqKeyPerTermnlCertfd(self):
		del self._UnqKeyPerTermnlCertfd
		self._UnqKeyPerTermnlCertfd = None

	@property
	def WrtgCpblty(self):
		return self._WrtgCpblty

	@WrtgCpblty.setter
	def WrtgCpblty(self, value):
		self._WrtgCpblty = value if type(value) != base_types.auto else self.make_default("WrtgCpblty")

	@WrtgCpblty.deleter
	def WrtgCpblty(self):
		del self._WrtgCpblty
		self._WrtgCpblty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ApprvlCdLngth', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardCaptrCpbl', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertfctnId', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrdhldrVrfctnCpblty', type=CardholderVerificationCapability6Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ctry', type=ISOMax3ACountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GeogcLctn', type=GeographicPointInDecimalDegreesText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max16Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntgtnTp', type=TerminalIntegrationCategory1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgCpblty', type=DisplayCapabilities6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MxScrptLngth', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NcrptnMtd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtlData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OffPrmiss', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OnBrd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OnLineCpblty', type=OnLineCapability2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Outdr', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PINLngthCpblty', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PINNtryCpblty', type=ISO8583PINEntryCapabilityCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvtData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RdngCpblty', type=CardDataReading11Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sftwr', type=Software2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SnglTap', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SrlNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubTp', type=ISO8583AccountEntryDeviceTypeCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TempScrStorg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TermnlLineNcrptnCertfd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=TerminalType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnqKeyPerTermnlCertfd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WrtgCpblty', type=CardDataWriting2Code, min=0, max=None, mutex_group=None, array=True),
	))