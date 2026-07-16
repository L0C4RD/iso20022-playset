# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Frequency6Code
from . import FrequencyAndMoment1
from . import FrequencyPeriod1

class Frequency36Choice(base_types._BaseFieldType):

	__slots__ = ["_Prd", "_PtInTm", "_Tp"]
	@property
	def Prd(self):
		return self._Prd

	@Prd.setter
	def Prd(self, value):
		self._Prd = value if value is not None else base_types.UninitialisedField(self, 'Prd', FrequencyPeriod1, False)

	@Prd.deleter
	def Prd(self):
		del self._Prd
		self._Prd = base_types.UninitialisedField(self, 'Prd', FrequencyPeriod1, False)

	@property
	def PtInTm(self):
		return self._PtInTm

	@PtInTm.setter
	def PtInTm(self, value):
		self._PtInTm = value if value is not None else base_types.UninitialisedField(self, 'PtInTm', FrequencyAndMoment1, False)

	@PtInTm.deleter
	def PtInTm(self):
		del self._PtInTm
		self._PtInTm = base_types.UninitialisedField(self, 'PtInTm', FrequencyAndMoment1, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', Frequency6Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', Frequency6Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Prd', type=FrequencyPeriod1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PtInTm', type=FrequencyAndMoment1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Tp', type=Frequency6Code, min=0, max=1, mutex_group=1, array=False),
	))