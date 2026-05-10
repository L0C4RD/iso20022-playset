from . import base_types
from .RejectedElement1 import RejectedElement1
from .Reason2 import Reason2

class RejectionReason1Choice(base_types._BaseFieldType):

	__slots__ = ["_RjctdElmt", "_GblRjctnRsn"]
	@property
	def RjctdElmt(self):
		return self._RjctdElmt

	@RjctdElmt.setter
	def RjctdElmt(self, value):
		self._RjctdElmt = value if type(value) != auto else self.make_default("RjctdElmt")

	@RjctdElmt.deleter
	def RjctdElmt(self):
		del self._RjctdElmt
		self._RjctdElmt = None

	@property
	def GblRjctnRsn(self):
		return self._GblRjctnRsn

	@GblRjctnRsn.setter
	def GblRjctnRsn(self, value):
		self._GblRjctnRsn = value if type(value) != auto else self.make_default("GblRjctnRsn")

	@GblRjctnRsn.deleter
	def GblRjctnRsn(self):
		del self._GblRjctnRsn
		self._GblRjctnRsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RjctdElmt', type=RejectedElement1, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='GblRjctnRsn', type=Reason2, min=0, max=1, mutex_group=1, array=False),
	))

