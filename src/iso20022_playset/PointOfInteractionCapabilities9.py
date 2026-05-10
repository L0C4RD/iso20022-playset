from . import base_types
import DisplayCapabilities4
import CardholderVerificationCapability4Code
import TrueFalseIndicator
import CardDataReading8Code
import OnLineCapability1Code
import PositiveNumber

class PointOfInteractionCapabilities9(base_types._BaseFieldType):

	__slots__ = ["_MxScrptLngth", "_PINLngthCpblties", "_MsgCpblties", "_CrdhldrVrfctnCpblties", "_ApprvlCdLngth", "_CardRdngCpblties", "_OnLineCpblties", "_CardCaptrCpbl"]
	@property
	def MxScrptLngth(self):
		return self._MxScrptLngth

	@MxScrptLngth.setter
	def MxScrptLngth(self, value):
		self._MxScrptLngth = value if type(value) != auto else self.make_default("MxScrptLngth")

	@MxScrptLngth.deleter
	def MxScrptLngth(self):
		del self._MxScrptLngth
		self._MxScrptLngth = None

	@property
	def PINLngthCpblties(self):
		return self._PINLngthCpblties

	@PINLngthCpblties.setter
	def PINLngthCpblties(self, value):
		self._PINLngthCpblties = value if type(value) != auto else self.make_default("PINLngthCpblties")

	@PINLngthCpblties.deleter
	def PINLngthCpblties(self):
		del self._PINLngthCpblties
		self._PINLngthCpblties = None

	@property
	def MsgCpblties(self):
		return self._MsgCpblties

	@MsgCpblties.setter
	def MsgCpblties(self, value):
		self._MsgCpblties = value if type(value) != auto else self.make_default("MsgCpblties")

	@MsgCpblties.deleter
	def MsgCpblties(self):
		del self._MsgCpblties
		self._MsgCpblties = None

	@property
	def CrdhldrVrfctnCpblties(self):
		return self._CrdhldrVrfctnCpblties

	@CrdhldrVrfctnCpblties.setter
	def CrdhldrVrfctnCpblties(self, value):
		self._CrdhldrVrfctnCpblties = value if type(value) != auto else self.make_default("CrdhldrVrfctnCpblties")

	@CrdhldrVrfctnCpblties.deleter
	def CrdhldrVrfctnCpblties(self):
		del self._CrdhldrVrfctnCpblties
		self._CrdhldrVrfctnCpblties = None

	@property
	def ApprvlCdLngth(self):
		return self._ApprvlCdLngth

	@ApprvlCdLngth.setter
	def ApprvlCdLngth(self, value):
		self._ApprvlCdLngth = value if type(value) != auto else self.make_default("ApprvlCdLngth")

	@ApprvlCdLngth.deleter
	def ApprvlCdLngth(self):
		del self._ApprvlCdLngth
		self._ApprvlCdLngth = None

	@property
	def CardRdngCpblties(self):
		return self._CardRdngCpblties

	@CardRdngCpblties.setter
	def CardRdngCpblties(self, value):
		self._CardRdngCpblties = value if type(value) != auto else self.make_default("CardRdngCpblties")

	@CardRdngCpblties.deleter
	def CardRdngCpblties(self):
		del self._CardRdngCpblties
		self._CardRdngCpblties = None

	@property
	def OnLineCpblties(self):
		return self._OnLineCpblties

	@OnLineCpblties.setter
	def OnLineCpblties(self, value):
		self._OnLineCpblties = value if type(value) != auto else self.make_default("OnLineCpblties")

	@OnLineCpblties.deleter
	def OnLineCpblties(self):
		del self._OnLineCpblties
		self._OnLineCpblties = None

	@property
	def CardCaptrCpbl(self):
		return self._CardCaptrCpbl

	@CardCaptrCpbl.setter
	def CardCaptrCpbl(self, value):
		self._CardCaptrCpbl = value if type(value) != auto else self.make_default("CardCaptrCpbl")

	@CardCaptrCpbl.deleter
	def CardCaptrCpbl(self):
		del self._CardCaptrCpbl
		self._CardCaptrCpbl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MxScrptLngth', type=PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PINLngthCpblties', type=PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgCpblties', type=DisplayCapabilities4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CrdhldrVrfctnCpblties', type=CardholderVerificationCapability4Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ApprvlCdLngth', type=PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardRdngCpblties', type=CardDataReading8Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OnLineCpblties', type=OnLineCapability1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardCaptrCpbl', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))

