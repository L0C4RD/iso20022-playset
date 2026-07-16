# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CardDataReading1Code
from . import CardholderVerificationCapability1Code
from . import DisplayCapabilities1
from . import Max3NumericText
from . import OnLineCapability1Code

class PointOfInteractionCapabilities1(base_types._BaseFieldType):

	__slots__ = ["_CardRdngCpblties", "_CrdhldrVrfctnCpblties", "_DispCpblties", "_OnLineCpblties", "_PrtLineWidth"]
	@property
	def CardRdngCpblties(self):
		return self._CardRdngCpblties

	@CardRdngCpblties.setter
	def CardRdngCpblties(self, value):
		self._CardRdngCpblties = value if value is not None else base_types.UninitialisedField(self, 'CardRdngCpblties', CardDataReading1Code, True)

	@CardRdngCpblties.deleter
	def CardRdngCpblties(self):
		del self._CardRdngCpblties
		self._CardRdngCpblties = base_types.UninitialisedField(self, 'CardRdngCpblties', CardDataReading1Code, True)

	@property
	def CrdhldrVrfctnCpblties(self):
		return self._CrdhldrVrfctnCpblties

	@CrdhldrVrfctnCpblties.setter
	def CrdhldrVrfctnCpblties(self, value):
		self._CrdhldrVrfctnCpblties = value if value is not None else base_types.UninitialisedField(self, 'CrdhldrVrfctnCpblties', CardholderVerificationCapability1Code, True)

	@CrdhldrVrfctnCpblties.deleter
	def CrdhldrVrfctnCpblties(self):
		del self._CrdhldrVrfctnCpblties
		self._CrdhldrVrfctnCpblties = base_types.UninitialisedField(self, 'CrdhldrVrfctnCpblties', CardholderVerificationCapability1Code, True)

	@property
	def DispCpblties(self):
		return self._DispCpblties

	@DispCpblties.setter
	def DispCpblties(self, value):
		self._DispCpblties = value if value is not None else base_types.UninitialisedField(self, 'DispCpblties', DisplayCapabilities1, True)

	@DispCpblties.deleter
	def DispCpblties(self):
		del self._DispCpblties
		self._DispCpblties = base_types.UninitialisedField(self, 'DispCpblties', DisplayCapabilities1, True)

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
	def PrtLineWidth(self):
		return self._PrtLineWidth

	@PrtLineWidth.setter
	def PrtLineWidth(self, value):
		self._PrtLineWidth = value if value is not None else base_types.UninitialisedField(self, 'PrtLineWidth', Max3NumericText, False)

	@PrtLineWidth.deleter
	def PrtLineWidth(self):
		del self._PrtLineWidth
		self._PrtLineWidth = base_types.UninitialisedField(self, 'PrtLineWidth', Max3NumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CardRdngCpblties', type=CardDataReading1Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CrdhldrVrfctnCpblties', type=CardholderVerificationCapability1Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DispCpblties', type=DisplayCapabilities1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OnLineCpblties', type=OnLineCapability1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtLineWidth', type=Max3NumericText, min=0, max=1, mutex_group=None, array=False),
	))