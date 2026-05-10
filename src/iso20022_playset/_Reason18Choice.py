from . import base_types
from ._ProprietaryReason4 import ProprietaryReason4
from ._NoReasonCode import NoReasonCode

class Reason18Choice(base_types._BaseFieldType):

	__slots__ = ["_Rsn", "_NoSpcfdRsn"]
	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if type(value) != base_types.auto else self.make_default("Rsn")

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = None

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
		base_types.FieldEntry(name='Rsn', type=ProprietaryReason4, min=0, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='NoSpcfdRsn', type=NoReasonCode, min=0, max=1, mutex_group=1, array=False),
	))

