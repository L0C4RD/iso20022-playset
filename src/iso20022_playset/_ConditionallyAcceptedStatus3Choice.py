# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ConditionallyAcceptedStatusReason3
from . import NoReasonCode

class ConditionallyAcceptedStatus3Choice(base_types._BaseFieldType):

	__slots__ = ["_NoSpcfdRsn", "_RsnDtls"]
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

	@property
	def RsnDtls(self):
		return self._RsnDtls

	@RsnDtls.setter
	def RsnDtls(self, value):
		self._RsnDtls = value if value is not None else base_types.UninitialisedField(self, 'RsnDtls', ConditionallyAcceptedStatusReason3, True)

	@RsnDtls.deleter
	def RsnDtls(self):
		del self._RsnDtls
		self._RsnDtls = base_types.UninitialisedField(self, 'RsnDtls', ConditionallyAcceptedStatusReason3, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NoSpcfdRsn', type=NoReasonCode, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RsnDtls', type=ConditionallyAcceptedStatusReason3, min=1, max=5, mutex_group=1, array=True),
	))