from . import base_types
from ._IntraPositionPending12 import IntraPositionPending12
from ._PendingStatusAndReason4 import PendingStatusAndReason4

class IntraPositionPending11(base_types._BaseFieldType):

	__slots__ = ["_Mvmnt", "_StsAndRsn"]
	@property
	def Mvmnt(self):
		return self._Mvmnt

	@Mvmnt.setter
	def Mvmnt(self, value):
		self._Mvmnt = value if type(value) != base_types.auto else self.make_default("Mvmnt")

	@Mvmnt.deleter
	def Mvmnt(self):
		del self._Mvmnt
		self._Mvmnt = None

	@property
	def StsAndRsn(self):
		return self._StsAndRsn

	@StsAndRsn.setter
	def StsAndRsn(self, value):
		self._StsAndRsn = value if type(value) != base_types.auto else self.make_default("StsAndRsn")

	@StsAndRsn.deleter
	def StsAndRsn(self):
		del self._StsAndRsn
		self._StsAndRsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Mvmnt', type=IntraPositionPending12, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StsAndRsn', type=PendingStatusAndReason4, min=0, max=1, mutex_group=None, array=False),
	))

