# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PercentageRate
from . import VolumeMetrics4

class PositionSetMetrics11(base_types._BaseFieldType):

	__slots__ = ["_CshRinvstmtRate", "_VolMtrcs"]
	@property
	def CshRinvstmtRate(self):
		return self._CshRinvstmtRate

	@CshRinvstmtRate.setter
	def CshRinvstmtRate(self, value):
		self._CshRinvstmtRate = value if value is not None else base_types.UninitialisedField(self, 'CshRinvstmtRate', PercentageRate, False)

	@CshRinvstmtRate.deleter
	def CshRinvstmtRate(self):
		del self._CshRinvstmtRate
		self._CshRinvstmtRate = base_types.UninitialisedField(self, 'CshRinvstmtRate', PercentageRate, False)

	@property
	def VolMtrcs(self):
		return self._VolMtrcs

	@VolMtrcs.setter
	def VolMtrcs(self, value):
		self._VolMtrcs = value if value is not None else base_types.UninitialisedField(self, 'VolMtrcs', VolumeMetrics4, False)

	@VolMtrcs.deleter
	def VolMtrcs(self):
		del self._VolMtrcs
		self._VolMtrcs = base_types.UninitialisedField(self, 'VolMtrcs', VolumeMetrics4, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshRinvstmtRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VolMtrcs', type=VolumeMetrics4, min=0, max=1, mutex_group=None, array=False),
	))