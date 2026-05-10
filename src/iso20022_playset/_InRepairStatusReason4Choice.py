from . import base_types
from .InRepairStatusReason4 import InRepairStatusReason4
from .NoReasonCode import NoReasonCode

class InRepairStatusReason4Choice(base_types._BaseFieldType):

	__slots__ = ["_RsnDtls", "_NoSpcfdRsn"]
	@property
	def RsnDtls(self):
		return self._RsnDtls

	@RsnDtls.setter
	def RsnDtls(self, value):
		self._RsnDtls = value if type(value) != base_types.auto else self.make_default("RsnDtls")

	@RsnDtls.deleter
	def RsnDtls(self):
		del self._RsnDtls
		self._RsnDtls = None

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
		base_types.FieldEntry(name='RsnDtls', type=InRepairStatusReason4, min=1, max=5, mutex_group=1, array=True),
		base_types.FieldEntry(name='NoSpcfdRsn', type=NoReasonCode, min=0, max=1, mutex_group=1, array=False),
	))

