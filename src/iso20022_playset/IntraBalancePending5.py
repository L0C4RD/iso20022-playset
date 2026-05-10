import base_types
import PendingStatusAndReason2
import IntraBalancePending6

class IntraBalancePending5(base_types._BaseFieldType):

	__slots__ = ["_StsAndRsn", "_Mvmnt"]
	@property
	def StsAndRsn(self):
		return self._StsAndRsn

	@StsAndRsn.setter
	def StsAndRsn(self, value):
		self._StsAndRsn = value if type(value) != auto else self.make_default("StsAndRsn")

	@StsAndRsn.deleter
	def StsAndRsn(self):
		del self._StsAndRsn
		self._StsAndRsn = None

	@property
	def Mvmnt(self):
		return self._Mvmnt

	@Mvmnt.setter
	def Mvmnt(self, value):
		self._Mvmnt = value if type(value) != auto else self.make_default("Mvmnt")

	@Mvmnt.deleter
	def Mvmnt(self):
		del self._Mvmnt
		self._Mvmnt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='StsAndRsn', type=PendingStatusAndReason2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mvmnt', type=IntraBalancePending6, min=1, max=None, mutex_group=None, array=True),
	))

