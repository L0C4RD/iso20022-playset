import base_types
import ExposureMetrics6

class PositionSetMetrics10(base_types._BaseFieldType):

	__slots__ = ["_VolMtrcs"]
	@property
	def VolMtrcs(self):
		return self._VolMtrcs

	@VolMtrcs.setter
	def VolMtrcs(self, value):
		self._VolMtrcs = value if type(value) != auto else self.make_default("VolMtrcs")

	@VolMtrcs.deleter
	def VolMtrcs(self):
		del self._VolMtrcs
		self._VolMtrcs = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='VolMtrcs', type=ExposureMetrics6, min=0, max=1, mutex_group=None, array=False),
	))

