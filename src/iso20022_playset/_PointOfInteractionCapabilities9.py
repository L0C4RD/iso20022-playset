# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CardDataReading8Code
from . import CardholderVerificationCapability4Code
from . import DisplayCapabilities4
from . import OnLineCapability1Code
from . import PositiveNumber
from . import TrueFalseIndicator

class PointOfInteractionCapabilities9(base_types._BaseFieldType):

	__slots__ = ["_ApprvlCdLngth", "_CardCaptrCpbl", "_CardRdngCpblties", "_CrdhldrVrfctnCpblties", "_MsgCpblties", "_MxScrptLngth", "_OnLineCpblties", "_PINLngthCpblties"]
	@property
	def ApprvlCdLngth(self):
		return self._ApprvlCdLngth

	@ApprvlCdLngth.setter
	def ApprvlCdLngth(self, value):
		self._ApprvlCdLngth = value if value is not None else base_types.UninitialisedField(self, 'ApprvlCdLngth', PositiveNumber, False)

	@ApprvlCdLngth.deleter
	def ApprvlCdLngth(self):
		del self._ApprvlCdLngth
		self._ApprvlCdLngth = base_types.UninitialisedField(self, 'ApprvlCdLngth', PositiveNumber, False)

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
	def CardRdngCpblties(self):
		return self._CardRdngCpblties

	@CardRdngCpblties.setter
	def CardRdngCpblties(self, value):
		self._CardRdngCpblties = value if value is not None else base_types.UninitialisedField(self, 'CardRdngCpblties', CardDataReading8Code, True)

	@CardRdngCpblties.deleter
	def CardRdngCpblties(self):
		del self._CardRdngCpblties
		self._CardRdngCpblties = base_types.UninitialisedField(self, 'CardRdngCpblties', CardDataReading8Code, True)

	@property
	def CrdhldrVrfctnCpblties(self):
		return self._CrdhldrVrfctnCpblties

	@CrdhldrVrfctnCpblties.setter
	def CrdhldrVrfctnCpblties(self, value):
		self._CrdhldrVrfctnCpblties = value if value is not None else base_types.UninitialisedField(self, 'CrdhldrVrfctnCpblties', CardholderVerificationCapability4Code, True)

	@CrdhldrVrfctnCpblties.deleter
	def CrdhldrVrfctnCpblties(self):
		del self._CrdhldrVrfctnCpblties
		self._CrdhldrVrfctnCpblties = base_types.UninitialisedField(self, 'CrdhldrVrfctnCpblties', CardholderVerificationCapability4Code, True)

	@property
	def MsgCpblties(self):
		return self._MsgCpblties

	@MsgCpblties.setter
	def MsgCpblties(self, value):
		self._MsgCpblties = value if value is not None else base_types.UninitialisedField(self, 'MsgCpblties', DisplayCapabilities4, True)

	@MsgCpblties.deleter
	def MsgCpblties(self):
		del self._MsgCpblties
		self._MsgCpblties = base_types.UninitialisedField(self, 'MsgCpblties', DisplayCapabilities4, True)

	@property
	def MxScrptLngth(self):
		return self._MxScrptLngth

	@MxScrptLngth.setter
	def MxScrptLngth(self, value):
		self._MxScrptLngth = value if value is not None else base_types.UninitialisedField(self, 'MxScrptLngth', PositiveNumber, False)

	@MxScrptLngth.deleter
	def MxScrptLngth(self):
		del self._MxScrptLngth
		self._MxScrptLngth = base_types.UninitialisedField(self, 'MxScrptLngth', PositiveNumber, False)

	@property
	def OnLineCpblties(self):
		return self._OnLineCpblties

	@OnLineCpblties.setter
	def OnLineCpblties(self, value):
		self._OnLineCpblties = value if value is not None else base_types.UninitialisedField(self, 'OnLineCpblties', OnLineCapability1Code, False)

	@OnLineCpblties.deleter
	def OnLineCpblties(self):
		del self._OnLineCpblties
		self._OnLineCpblties = base_types.UninitialisedField(self, 'OnLineCpblties', OnLineCapability1Code, False)

	@property
	def PINLngthCpblties(self):
		return self._PINLngthCpblties

	@PINLngthCpblties.setter
	def PINLngthCpblties(self, value):
		self._PINLngthCpblties = value if value is not None else base_types.UninitialisedField(self, 'PINLngthCpblties', PositiveNumber, False)

	@PINLngthCpblties.deleter
	def PINLngthCpblties(self):
		del self._PINLngthCpblties
		self._PINLngthCpblties = base_types.UninitialisedField(self, 'PINLngthCpblties', PositiveNumber, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ApprvlCdLngth', type=PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardCaptrCpbl', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardRdngCpblties', type=CardDataReading8Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CrdhldrVrfctnCpblties', type=CardholderVerificationCapability4Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgCpblties', type=DisplayCapabilities4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MxScrptLngth', type=PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OnLineCpblties', type=OnLineCapability1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PINLngthCpblties', type=PositiveNumber, min=0, max=1, mutex_group=None, array=False),
	))