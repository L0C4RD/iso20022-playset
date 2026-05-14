# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CollateralAmount16 import CollateralAmount16
from ._CollateralStatus1Code import CollateralStatus1Code
from ._ExposureType23Choice import ExposureType23Choice
from ._GenericIdentification30 import GenericIdentification30
from ._PercentageRate import PercentageRate

class ExposureTypeAggregation3(base_types._BaseFieldType):

	__slots__ = ["_GblXpsrTpSts", "_MrgnRate", "_SttlmPrc", "_ValtnAmts", "_XpsrTp"]
	@property
	def GblXpsrTpSts(self):
		return self._GblXpsrTpSts

	@GblXpsrTpSts.setter
	def GblXpsrTpSts(self, value):
		self._GblXpsrTpSts = value if type(value) != base_types.auto else self.make_default("GblXpsrTpSts")

	@GblXpsrTpSts.deleter
	def GblXpsrTpSts(self):
		del self._GblXpsrTpSts
		self._GblXpsrTpSts = None

	@property
	def MrgnRate(self):
		return self._MrgnRate

	@MrgnRate.setter
	def MrgnRate(self, value):
		self._MrgnRate = value if type(value) != base_types.auto else self.make_default("MrgnRate")

	@MrgnRate.deleter
	def MrgnRate(self):
		del self._MrgnRate
		self._MrgnRate = None

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
	def ValtnAmts(self):
		return self._ValtnAmts

	@ValtnAmts.setter
	def ValtnAmts(self, value):
		self._ValtnAmts = value if type(value) != base_types.auto else self.make_default("ValtnAmts")

	@ValtnAmts.deleter
	def ValtnAmts(self):
		del self._ValtnAmts
		self._ValtnAmts = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='GblXpsrTpSts', type=CollateralStatus1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmPrc', type=GenericIdentification30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnAmts', type=CollateralAmount16, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='XpsrTp', type=ExposureType23Choice, min=1, max=1, mutex_group=None, array=False),
	))