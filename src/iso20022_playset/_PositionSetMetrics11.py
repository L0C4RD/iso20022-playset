from . import base_types
from .VolumeMetrics4 import VolumeMetrics4
from .PercentageRate import PercentageRate

class PositionSetMetrics11(base_types._BaseFieldType):

	__slots__ = ["_VolMtrcs", "_CshRinvstmtRate"]
	@property
	def VolMtrcs(self):
		return self._VolMtrcs

	@VolMtrcs.setter
	def VolMtrcs(self, value):
		self._VolMtrcs = value if type(value) != base_types.auto else self.make_default("VolMtrcs")

	@VolMtrcs.deleter
	def VolMtrcs(self):
		del self._VolMtrcs
		self._VolMtrcs = None

	@property
	def CshRinvstmtRate(self):
		return self._CshRinvstmtRate

	@CshRinvstmtRate.setter
	def CshRinvstmtRate(self, value):
		self._CshRinvstmtRate = value if type(value) != base_types.auto else self.make_default("CshRinvstmtRate")

	@CshRinvstmtRate.deleter
	def CshRinvstmtRate(self):
		del self._CshRinvstmtRate
		self._CshRinvstmtRate = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='VolMtrcs', type=VolumeMetrics4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshRinvstmtRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
	))

