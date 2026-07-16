# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CollateralRole1Code
from . import CollateralTransactionType1Choice
from . import ExposureType23Choice
from . import GenericIdentification30
from . import YesNoIndicator

class CollateralParameters12(base_types._BaseFieldType):

	__slots__ = ["_AutomtcAllcn", "_CollApprvd", "_CollInstrTp", "_CollSd", "_Prty", "_SttlmApprvd", "_SttlmPrc", "_XpsrTp"]
	@property
	def AutomtcAllcn(self):
		return self._AutomtcAllcn

	@AutomtcAllcn.setter
	def AutomtcAllcn(self, value):
		self._AutomtcAllcn = value if value is not None else base_types.UninitialisedField(self, 'AutomtcAllcn', YesNoIndicator, False)

	@AutomtcAllcn.deleter
	def AutomtcAllcn(self):
		del self._AutomtcAllcn
		self._AutomtcAllcn = base_types.UninitialisedField(self, 'AutomtcAllcn', YesNoIndicator, False)

	@property
	def CollApprvd(self):
		return self._CollApprvd

	@CollApprvd.setter
	def CollApprvd(self, value):
		self._CollApprvd = value if value is not None else base_types.UninitialisedField(self, 'CollApprvd', YesNoIndicator, False)

	@CollApprvd.deleter
	def CollApprvd(self):
		del self._CollApprvd
		self._CollApprvd = base_types.UninitialisedField(self, 'CollApprvd', YesNoIndicator, False)

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
	def Prty(self):
		return self._Prty

	@Prty.setter
	def Prty(self, value):
		self._Prty = value if value is not None else base_types.UninitialisedField(self, 'Prty', GenericIdentification30, False)

	@Prty.deleter
	def Prty(self):
		del self._Prty
		self._Prty = base_types.UninitialisedField(self, 'Prty', GenericIdentification30, False)

	@property
	def SttlmApprvd(self):
		return self._SttlmApprvd

	@SttlmApprvd.setter
	def SttlmApprvd(self, value):
		self._SttlmApprvd = value if value is not None else base_types.UninitialisedField(self, 'SttlmApprvd', YesNoIndicator, False)

	@SttlmApprvd.deleter
	def SttlmApprvd(self):
		del self._SttlmApprvd
		self._SttlmApprvd = base_types.UninitialisedField(self, 'SttlmApprvd', YesNoIndicator, False)

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
		base_types.FieldEntry(name='AutomtcAllcn', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollApprvd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollInstrTp', type=CollateralTransactionType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollSd', type=CollateralRole1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prty', type=GenericIdentification30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmApprvd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmPrc', type=GenericIdentification30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpsrTp', type=ExposureType23Choice, min=1, max=1, mutex_group=None, array=False),
	))