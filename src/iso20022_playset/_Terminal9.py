from . import base_types
from ._Number import Number
from ._DisplayCapabilities6 import DisplayCapabilities6
from ._CardReadingCapabilities1 import CardReadingCapabilities1
from ._GeographicPointInDecimalDegrees import GeographicPointInDecimalDegrees
from ._OnLineCapability2Code import OnLineCapability2Code
from ._AdditionalData1 import AdditionalData1
from ._Max16Text import Max16Text
from ._Max256Text import Max256Text
from ._CardholderVerificationCapabilities1 import CardholderVerificationCapabilities1
from ._Software1 import Software1
from ._PINEntrySecurityCharacteristic1Code import PINEntrySecurityCharacteristic1Code
from ._TrueFalseIndicator import TrueFalseIndicator
from ._Max35Text import Max35Text
from ._TerminalIntegrationCategory1Code import TerminalIntegrationCategory1Code
from ._TerminalType1Code import TerminalType1Code
from ._CardWritingCapabilities1 import CardWritingCapabilities1

class Terminal9(base_types._BaseFieldType):

	__slots__ = ["_WrtgCpblty", "_Sftwr", "_TempScrStorg", "_RdngCpblty", "_OnBrd", "_CrdhldrVrfctnCpblty", "_PINNtrySctyChrtc", "_CertfctnId", "_CardCaptrCpbl", "_SrlNb", "_Id", "_PINLngthCpblty", "_Tp", "_MxScrptLngth", "_GeogcLctn", "_ApprvlCdLngth", "_AddtlId", "_OnLineCpblty", "_Outdr", "_OffPrmiss", "_OthrPINNtrySctyChrtc", "_OthrTp", "_MsgCpblty", "_IntgtnTp"]
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
	def PINNtrySctyChrtc(self):
		return self._PINNtrySctyChrtc

	@PINNtrySctyChrtc.setter
	def PINNtrySctyChrtc(self, value):
		self._PINNtrySctyChrtc = value if type(value) != base_types.auto else self.make_default("PINNtrySctyChrtc")

	@PINNtrySctyChrtc.deleter
	def PINNtrySctyChrtc(self):
		del self._PINNtrySctyChrtc
		self._PINNtrySctyChrtc = None

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
	def AddtlId(self):
		return self._AddtlId

	@AddtlId.setter
	def AddtlId(self, value):
		self._AddtlId = value if type(value) != base_types.auto else self.make_default("AddtlId")

	@AddtlId.deleter
	def AddtlId(self):
		del self._AddtlId
		self._AddtlId = None

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
	def OthrPINNtrySctyChrtc(self):
		return self._OthrPINNtrySctyChrtc

	@OthrPINNtrySctyChrtc.setter
	def OthrPINNtrySctyChrtc(self, value):
		self._OthrPINNtrySctyChrtc = value if type(value) != base_types.auto else self.make_default("OthrPINNtrySctyChrtc")

	@OthrPINNtrySctyChrtc.deleter
	def OthrPINNtrySctyChrtc(self):
		del self._OthrPINNtrySctyChrtc
		self._OthrPINNtrySctyChrtc = None

	@property
	def OthrTp(self):
		return self._OthrTp

	@OthrTp.setter
	def OthrTp(self, value):
		self._OthrTp = value if type(value) != base_types.auto else self.make_default("OthrTp")

	@OthrTp.deleter
	def OthrTp(self):
		del self._OthrTp
		self._OthrTp = None

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
	def IntgtnTp(self):
		return self._IntgtnTp

	@IntgtnTp.setter
	def IntgtnTp(self, value):
		self._IntgtnTp = value if type(value) != base_types.auto else self.make_default("IntgtnTp")

	@IntgtnTp.deleter
	def IntgtnTp(self):
		del self._IntgtnTp
		self._IntgtnTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='WrtgCpblty', type=CardWritingCapabilities1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sftwr', type=Software1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TempScrStorg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RdngCpblty', type=CardReadingCapabilities1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OnBrd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrdhldrVrfctnCpblty', type=CardholderVerificationCapabilities1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PINNtrySctyChrtc', type=PINEntrySecurityCharacteristic1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertfctnId', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardCaptrCpbl', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SrlNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PINLngthCpblty', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=TerminalType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MxScrptLngth', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GeogcLctn', type=GeographicPointInDecimalDegrees, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ApprvlCdLngth', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlId', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OnLineCpblty', type=OnLineCapability2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Outdr', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OffPrmiss', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrPINNtrySctyChrtc', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgCpblty', type=DisplayCapabilities6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IntgtnTp', type=TerminalIntegrationCategory1Code, min=0, max=1, mutex_group=None, array=False),
	))

