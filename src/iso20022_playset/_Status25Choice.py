from . import base_types
from ._AccountManagementStatus1Code import AccountManagementStatus1Code
from ._RejectionReason31 import RejectionReason31

class Status25Choice(base_types._BaseFieldType):

	__slots__ = ["_Rjctd", "_Sts"]
	@property
	def Rjctd(self):
		return self._Rjctd

	@Rjctd.setter
	def Rjctd(self, value):
		self._Rjctd = value if type(value) != base_types.auto else self.make_default("Rjctd")

	@Rjctd.deleter
	def Rjctd(self):
		del self._Rjctd
		self._Rjctd = None

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != base_types.auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rjctd', type=RejectionReason31, min=1, max=10, mutex_group=1, array=True),
		base_types.FieldEntry(name='Sts', type=AccountManagementStatus1Code, min=0, max=1, mutex_group=1, array=False),
	))

