# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InputResult6
from . import OutputResult2

class DeviceInputResponse6(base_types._BaseFieldType):

	__slots__ = ["_InptRslt", "_OutptRslt"]
	@property
	def InptRslt(self):
		return self._InptRslt

	@InptRslt.setter
	def InptRslt(self, value):
		self._InptRslt = value if value is not None else base_types.UninitialisedField(self, 'InptRslt', InputResult6, False)

	@InptRslt.deleter
	def InptRslt(self):
		del self._InptRslt
		self._InptRslt = base_types.UninitialisedField(self, 'InptRslt', InputResult6, False)

	@property
	def OutptRslt(self):
		return self._OutptRslt

	@OutptRslt.setter
	def OutptRslt(self, value):
		self._OutptRslt = value if value is not None else base_types.UninitialisedField(self, 'OutptRslt', OutputResult2, False)

	@OutptRslt.deleter
	def OutptRslt(self):
		del self._OutptRslt
		self._OutptRslt = base_types.UninitialisedField(self, 'OutptRslt', OutputResult2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='InptRslt', type=InputResult6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OutptRslt', type=OutputResult2, min=0, max=1, mutex_group=None, array=False),
	))