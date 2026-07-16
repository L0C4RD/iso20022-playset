# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import OutputResult3

class DeviceDisplayResponse3(base_types._BaseFieldType):

	__slots__ = ["_OutptRslt"]
	@property
	def OutptRslt(self):
		return self._OutptRslt

	@OutptRslt.setter
	def OutptRslt(self, value):
		self._OutptRslt = value if value is not None else base_types.UninitialisedField(self, 'OutptRslt', OutputResult3, True)

	@OutptRslt.deleter
	def OutptRslt(self):
		del self._OutptRslt
		self._OutptRslt = base_types.UninitialisedField(self, 'OutptRslt', OutputResult3, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OutptRslt', type=OutputResult3, min=1, max=None, mutex_group=None, array=True),
	))