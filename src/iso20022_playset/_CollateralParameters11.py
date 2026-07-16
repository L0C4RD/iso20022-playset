# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CollateralRole1Code
from . import CollateralTransactionType1Choice
from . import ExposureType23Choice
from . import GenericIdentification1
from . import GenericIdentification30
from . import RateOrType1Choice
from . import YesNoIndicator

class CollateralParameters11(base_types._BaseFieldType):

	__slots__ = ["_CollInstrTp", "_CollSd", "_ElgbltySetPrfl", "_SttlmPrc", "_TrfTitl", "_ValSghtMrgnRate", "_XpsrTp"]
	@property
	def CollInstrTp(self):
		return self._CollInstrTp

	@CollInstrTp.setter
	def CollInstrTp(self, value):
		self._CollInstrTp = value if value is not None else base_types.UninitialisedField(self, 'CollInstrTp', CollateralTransactionType1Choice, False)

	@CollInstrTp.deleter
	def CollInstrTp(self):
		del self._CollInstrTp
		self._CollInstrTp = base_types.UninitialisedField(self, 'CollInstrTp', CollateralTransactionType1Choice, False)

	@property
	def CollSd(self):
		return self._CollSd

	@CollSd.setter
	def CollSd(self, value):
		self._CollSd = value if value is not None else base_types.UninitialisedField(self, 'CollSd', CollateralRole1Code, False)

	@CollSd.deleter
	def CollSd(self):
		del self._CollSd
		self._CollSd = base_types.UninitialisedField(self, 'CollSd', CollateralRole1Code, False)

	@property
	def ElgbltySetPrfl(self):
		return self._ElgbltySetPrfl

	@ElgbltySetPrfl.setter
	def ElgbltySetPrfl(self, value):
		self._ElgbltySetPrfl = value if value is not None else base_types.UninitialisedField(self, 'ElgbltySetPrfl', GenericIdentification1, False)

	@ElgbltySetPrfl.deleter
	def ElgbltySetPrfl(self):
		del self._ElgbltySetPrfl
		self._ElgbltySetPrfl = base_types.UninitialisedField(self, 'ElgbltySetPrfl', GenericIdentification1, False)

	@property
	def SttlmPrc(self):
		return self._SttlmPrc

	@SttlmPrc.setter
	def SttlmPrc(self, value):
		self._SttlmPrc = value if value is not None else base_types.UninitialisedField(self, 'SttlmPrc', GenericIdentification30, False)

	@SttlmPrc.deleter
	def SttlmPrc(self):
		del self._SttlmPrc
		self._SttlmPrc = base_types.UninitialisedField(self, 'SttlmPrc', GenericIdentification30, False)

	@property
	def TrfTitl(self):
		return self._TrfTitl

	@TrfTitl.setter
	def TrfTitl(self, value):
		self._TrfTitl = value if value is not None else base_types.UninitialisedField(self, 'TrfTitl', YesNoIndicator, False)

	@TrfTitl.deleter
	def TrfTitl(self):
		del self._TrfTitl
		self._TrfTitl = base_types.UninitialisedField(self, 'TrfTitl', YesNoIndicator, False)

	@property
	def ValSghtMrgnRate(self):
		return self._ValSghtMrgnRate

	@ValSghtMrgnRate.setter
	def ValSghtMrgnRate(self, value):
		self._ValSghtMrgnRate = value if value is not None else base_types.UninitialisedField(self, 'ValSghtMrgnRate', RateOrType1Choice, False)

	@ValSghtMrgnRate.deleter
	def ValSghtMrgnRate(self):
		del self._ValSghtMrgnRate
		self._ValSghtMrgnRate = base_types.UninitialisedField(self, 'ValSghtMrgnRate', RateOrType1Choice, False)

	@property
	def XpsrTp(self):
		return self._XpsrTp

	@XpsrTp.setter
	def XpsrTp(self, value):
		self._XpsrTp = value if value is not None else base_types.UninitialisedField(self, 'XpsrTp', ExposureType23Choice, False)

	@XpsrTp.deleter
	def XpsrTp(self):
		del self._XpsrTp
		self._XpsrTp = base_types.UninitialisedField(self, 'XpsrTp', ExposureType23Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollInstrTp', type=CollateralTransactionType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollSd', type=CollateralRole1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElgbltySetPrfl', type=GenericIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmPrc', type=GenericIdentification30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfTitl', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValSghtMrgnRate', type=RateOrType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpsrTp', type=ExposureType23Choice, min=1, max=1, mutex_group=None, array=False),
	))