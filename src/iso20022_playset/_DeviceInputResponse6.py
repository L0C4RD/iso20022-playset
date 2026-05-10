from . import base_types
from ._InputResult6 import InputResult6
from ._OutputResult2 import OutputResult2

class DeviceInputResponse6(base_types._BaseFieldType):

	__slots__ = ["_OutptRslt", "_InptRslt"]
	@property
	def InptRslt(self):
		return self._InptRslt

	@InptRslt.setter
	def InptRslt(self, value):
		self._InptRslt = value if type(value) != base_types.auto else self.make_default("InptRslt")

	@InptRslt.deleter
	def InptRslt(self):
		del self._InptRslt
		self._InptRslt = None

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
		base_types.FieldEntry(name='InptRslt', type=InputResult6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OutptRslt', type=OutputResult2, min=0, max=1, mutex_group=None, array=False),
	))

