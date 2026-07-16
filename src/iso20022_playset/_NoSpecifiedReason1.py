# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import NoReasonCode

class NoSpecifiedReason1(base_types._BaseFieldType):

	__slots__ = ["_NoSpcfdRsn"]
	@property
	def NoSpcfdRsn(self):
		return self._NoSpcfdRsn

	@NoSpcfdRsn.setter
	def NoSpcfdRsn(self, value):
		self._NoSpcfdRsn = value if value is not None else base_types.UninitialisedField(self, 'NoSpcfdRsn', NoReasonCode, False)

	@NoSpcfdRsn.deleter
	def NoSpcfdRsn(self):
		del self._NoSpcfdRsn
		self._NoSpcfdRsn = base_types.UninitialisedField(self, 'NoSpcfdRsn', NoReasonCode, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NoSpcfdRsn', type=NoReasonCode, min=1, max=1, mutex_group=None, array=False),
	))