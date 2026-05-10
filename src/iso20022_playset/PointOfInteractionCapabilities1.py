import base_types
import Max3NumericText
import CardDataReading1Code
import OnLineCapability1Code
import CardholderVerificationCapability1Code
import DisplayCapabilities1

class PointOfInteractionCapabilities1(base_types._BaseFieldType):

	__slots__ = ["_PrtLineWidth", "_OnLineCpblties", "_CardRdngCpblties", "_DispCpblties", "_CrdhldrVrfctnCpblties"]
	@property
	def PrtLineWidth(self):
		return self._PrtLineWidth

	@PrtLineWidth.setter
	def PrtLineWidth(self, value):
		self._PrtLineWidth = value if type(value) != auto else self.make_default("PrtLineWidth")

	@PrtLineWidth.deleter
	def PrtLineWidth(self):
		del self._PrtLineWidth
		self._PrtLineWidth = None

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
	def DispCpblties(self):
		return self._DispCpblties

	@DispCpblties.setter
	def DispCpblties(self, value):
		self._DispCpblties = value if type(value) != auto else self.make_default("DispCpblties")

	@DispCpblties.deleter
	def DispCpblties(self):
		del self._DispCpblties
		self._DispCpblties = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrtLineWidth', type=Max3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OnLineCpblties', type=OnLineCapability1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardRdngCpblties', type=CardDataReading1Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DispCpblties', type=DisplayCapabilities1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CrdhldrVrfctnCpblties', type=CardholderVerificationCapability1Code, min=0, max=None, mutex_group=None, array=True),
	))

