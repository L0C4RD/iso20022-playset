from . import base_types
from .GenericIdentification30 import GenericIdentification30
from .CollateralTransactionType1Choice import CollateralTransactionType1Choice
from .YesNoIndicator import YesNoIndicator
from .CollateralRole1Code import CollateralRole1Code
from .RateOrType1Choice import RateOrType1Choice
from .ExposureType23Choice import ExposureType23Choice
from .GenericIdentification1 import GenericIdentification1

class CollateralParameters11(base_types._BaseFieldType):

	__slots__ = ["_SttlmPrc", "_ElgbltySetPrfl", "_CollInstrTp", "_XpsrTp", "_CollSd", "_ValSghtMrgnRate", "_TrfTitl"]
	@property
	def SttlmPrc(self):
		return self._SttlmPrc

	@SttlmPrc.setter
	def SttlmPrc(self, value):
		self._SttlmPrc = value if type(value) != base_types.auto else self.make_default("SttlmPrc")

	@SttlmPrc.deleter
	def SttlmPrc(self):
		del self._SttlmPrc
		self._SttlmPrc = None

	@property
	def ElgbltySetPrfl(self):
		return self._ElgbltySetPrfl

	@ElgbltySetPrfl.setter
	def ElgbltySetPrfl(self, value):
		self._ElgbltySetPrfl = value if type(value) != base_types.auto else self.make_default("ElgbltySetPrfl")

	@ElgbltySetPrfl.deleter
	def ElgbltySetPrfl(self):
		del self._ElgbltySetPrfl
		self._ElgbltySetPrfl = None

	@property
	def CollInstrTp(self):
		return self._CollInstrTp

	@CollInstrTp.setter
	def CollInstrTp(self, value):
		self._CollInstrTp = value if type(value) != base_types.auto else self.make_default("CollInstrTp")

	@CollInstrTp.deleter
	def CollInstrTp(self):
		del self._CollInstrTp
		self._CollInstrTp = None

	@property
	def XpsrTp(self):
		return self._XpsrTp

	@XpsrTp.setter
	def XpsrTp(self, value):
		self._XpsrTp = value if type(value) != base_types.auto else self.make_default("XpsrTp")

	@XpsrTp.deleter
	def XpsrTp(self):
		del self._XpsrTp
		self._XpsrTp = None

	@property
	def CollSd(self):
		return self._CollSd

	@CollSd.setter
	def CollSd(self, value):
		self._CollSd = value if type(value) != base_types.auto else self.make_default("CollSd")

	@CollSd.deleter
	def CollSd(self):
		del self._CollSd
		self._CollSd = None

	@property
	def ValSghtMrgnRate(self):
		return self._ValSghtMrgnRate

	@ValSghtMrgnRate.setter
	def ValSghtMrgnRate(self, value):
		self._ValSghtMrgnRate = value if type(value) != base_types.auto else self.make_default("ValSghtMrgnRate")

	@ValSghtMrgnRate.deleter
	def ValSghtMrgnRate(self):
		del self._ValSghtMrgnRate
		self._ValSghtMrgnRate = None

	@property
	def TrfTitl(self):
		return self._TrfTitl

	@TrfTitl.setter
	def TrfTitl(self, value):
		self._TrfTitl = value if type(value) != base_types.auto else self.make_default("TrfTitl")

	@TrfTitl.deleter
	def TrfTitl(self):
		del self._TrfTitl
		self._TrfTitl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SttlmPrc', type=GenericIdentification30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElgbltySetPrfl', type=GenericIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollInstrTp', type=CollateralTransactionType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpsrTp', type=ExposureType23Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollSd', type=CollateralRole1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValSghtMrgnRate', type=RateOrType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfTitl', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
	))

