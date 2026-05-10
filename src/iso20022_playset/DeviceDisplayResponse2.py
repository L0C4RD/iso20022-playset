from . import base_types
from .OutputResult2 import OutputResult2

class DeviceDisplayResponse2(base_types._BaseFieldType):

	__slots__ = ["_OutptRslt"]
	@property
	def OutptRslt(self):
		return self._OutptRslt

	@OutptRslt.setter
	def OutptRslt(self, value):
		self._OutptRslt = value if type(value) != base_types.auto else self.make_default("OutptRslt")

	@OutptRslt.deleter
	def OutptRslt(self):
		del self._OutptRslt
		self._OutptRslt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OutptRslt', type=OutputResult2, min=1, max=None, mutex_group=None, array=True),
	))

