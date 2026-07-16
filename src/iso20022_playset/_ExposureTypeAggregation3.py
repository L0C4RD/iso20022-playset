# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CollateralAmount16
from . import CollateralStatus1Code
from . import ExposureType23Choice
from . import GenericIdentification30
from . import PercentageRate

class ExposureTypeAggregation3(base_types._BaseFieldType):

	__slots__ = ["_GblXpsrTpSts", "_MrgnRate", "_SttlmPrc", "_ValtnAmts", "_XpsrTp"]
	@property
	def GblXpsrTpSts(self):
		return self._GblXpsrTpSts

	@GblXpsrTpSts.setter
	def GblXpsrTpSts(self, value):
		self._GblXpsrTpSts = value if value is not None else base_types.UninitialisedField(self, 'GblXpsrTpSts', CollateralStatus1Code, False)

	@GblXpsrTpSts.deleter
	def GblXpsrTpSts(self):
		del self._GblXpsrTpSts
		self._GblXpsrTpSts = base_types.UninitialisedField(self, 'GblXpsrTpSts', CollateralStatus1Code, False)

	@property
	def MrgnRate(self):
		return self._MrgnRate

	@MrgnRate.setter
	def MrgnRate(self, value):
		self._MrgnRate = value if value is not None else base_types.UninitialisedField(self, 'MrgnRate', PercentageRate, False)

	@MrgnRate.deleter
	def MrgnRate(self):
		del self._MrgnRate
		self._MrgnRate = base_types.UninitialisedField(self, 'MrgnRate', PercentageRate, False)

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
	def ValtnAmts(self):
		return self._ValtnAmts

	@ValtnAmts.setter
	def ValtnAmts(self, value):
		self._ValtnAmts = value if value is not None else base_types.UninitialisedField(self, 'ValtnAmts', CollateralAmount16, True)

	@ValtnAmts.deleter
	def ValtnAmts(self):
		del self._ValtnAmts
		self._ValtnAmts = base_types.UninitialisedField(self, 'ValtnAmts', CollateralAmount16, True)

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
		base_types.FieldEntry(name='GblXpsrTpSts', type=CollateralStatus1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmPrc', type=GenericIdentification30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnAmts', type=CollateralAmount16, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='XpsrTp', type=ExposureType23Choice, min=1, max=1, mutex_group=None, array=False),
	))