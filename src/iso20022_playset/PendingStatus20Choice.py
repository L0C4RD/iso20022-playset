from . import base_types
from .NoSpecifiedReason1 import NoSpecifiedReason1

class PendingStatus20Choice(base_types._BaseFieldType):

	__slots__ = ["_UdrInvstgtn", "_Fwdd"]
	@property
	def UdrInvstgtn(self):
		return self._UdrInvstgtn

	@UdrInvstgtn.setter
	def UdrInvstgtn(self, value):
		self._UdrInvstgtn = value if type(value) != base_types.auto else self.make_default("UdrInvstgtn")

	@UdrInvstgtn.deleter
	def UdrInvstgtn(self):
		del self._UdrInvstgtn
		self._UdrInvstgtn = None

	@property
	def Fwdd(self):
		return self._Fwdd

	@Fwdd.setter
	def Fwdd(self, value):
		self._Fwdd = value if type(value) != base_types.auto else self.make_default("Fwdd")

	@Fwdd.deleter
	def Fwdd(self):
		del self._Fwdd
		self._Fwdd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='UdrInvstgtn', type=NoSpecifiedReason1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Fwdd', type=NoSpecifiedReason1, min=0, max=1, mutex_group=1, array=False),
	))

