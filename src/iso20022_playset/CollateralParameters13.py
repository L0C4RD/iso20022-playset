import base_types
import CollateralTransactionType1Choice
import ExposureType23Choice
import YesNoIndicator
import CollateralAmount5
import CollateralRole1Code
import GenericIdentification30

class CollateralParameters13(base_types._BaseFieldType):

	__slots__ = ["_CollSd", "_SttlmApprvd", "_Prty", "_CollAmt", "_CollInstrTp", "_AutomtcAllcn", "_CollApprvd", "_XpsrTp"]
	@property
	def CollSd(self):
		return self._CollSd

	@CollSd.setter
	def CollSd(self, value):
		self._CollSd = value if type(value) != auto else self.make_default("CollSd")

	@CollSd.deleter
	def CollSd(self):
		del self._CollSd
		self._CollSd = None

	@property
	def SttlmApprvd(self):
		return self._SttlmApprvd

	@SttlmApprvd.setter
	def SttlmApprvd(self, value):
		self._SttlmApprvd = value if type(value) != auto else self.make_default("SttlmApprvd")

	@SttlmApprvd.deleter
	def SttlmApprvd(self):
		del self._SttlmApprvd
		self._SttlmApprvd = None

	@property
	def Prty(self):
		return self._Prty

	@Prty.setter
	def Prty(self, value):
		self._Prty = value if type(value) != auto else self.make_default("Prty")

	@Prty.deleter
	def Prty(self):
		del self._Prty
		self._Prty = None

	@property
	def CollAmt(self):
		return self._CollAmt

	@CollAmt.setter
	def CollAmt(self, value):
		self._CollAmt = value if type(value) != auto else self.make_default("CollAmt")

	@CollAmt.deleter
	def CollAmt(self):
		del self._CollAmt
		self._CollAmt = None

	@property
	def CollInstrTp(self):
		return self._CollInstrTp

	@CollInstrTp.setter
	def CollInstrTp(self, value):
		self._CollInstrTp = value if type(value) != auto else self.make_default("CollInstrTp")

	@CollInstrTp.deleter
	def CollInstrTp(self):
		del self._CollInstrTp
		self._CollInstrTp = None

	@property
	def AutomtcAllcn(self):
		return self._AutomtcAllcn

	@AutomtcAllcn.setter
	def AutomtcAllcn(self, value):
		self._AutomtcAllcn = value if type(value) != auto else self.make_default("AutomtcAllcn")

	@AutomtcAllcn.deleter
	def AutomtcAllcn(self):
		del self._AutomtcAllcn
		self._AutomtcAllcn = None

	@property
	def CollApprvd(self):
		return self._CollApprvd

	@CollApprvd.setter
	def CollApprvd(self, value):
		self._CollApprvd = value if type(value) != auto else self.make_default("CollApprvd")

	@CollApprvd.deleter
	def CollApprvd(self):
		del self._CollApprvd
		self._CollApprvd = None

	@property
	def XpsrTp(self):
		return self._XpsrTp

	@XpsrTp.setter
	def XpsrTp(self, value):
		self._XpsrTp = value if type(value) != auto else self.make_default("XpsrTp")

	@XpsrTp.deleter
	def XpsrTp(self):
		del self._XpsrTp
		self._XpsrTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollSd', type=CollateralRole1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmApprvd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prty', type=GenericIdentification30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollAmt', type=CollateralAmount5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollInstrTp', type=CollateralTransactionType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AutomtcAllcn', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollApprvd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpsrTp', type=ExposureType23Choice, min=1, max=1, mutex_group=None, array=False),
	))

