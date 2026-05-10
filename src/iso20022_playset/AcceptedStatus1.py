from . import base_types
from .NoReasonCode import NoReasonCode

class AcceptedStatus1(base_types._BaseFieldType):

	__slots__ = ["_NoSpcfdRsn"]
	@property
	def NoSpcfdRsn(self):
		return self._NoSpcfdRsn

	@NoSpcfdRsn.setter
	def NoSpcfdRsn(self, value):
		self._NoSpcfdRsn = value if type(value) != base_types.auto else self.make_default("NoSpcfdRsn")

	@NoSpcfdRsn.deleter
	def NoSpcfdRsn(self):
		del self._NoSpcfdRsn
		self._NoSpcfdRsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NoSpcfdRsn', type=NoReasonCode, min=1, max=1, mutex_group=None, array=False),
	))

