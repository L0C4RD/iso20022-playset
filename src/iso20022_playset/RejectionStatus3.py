from . import base_types
from .RejectionReason68Code import RejectionReason68Code
from .Max35Text import Max35Text

class RejectionStatus3(base_types._BaseFieldType):

	__slots__ = ["_RjctdRsn", "_AddtlInf"]
	@property
	def RjctdRsn(self):
		return self._RjctdRsn

	@RjctdRsn.setter
	def RjctdRsn(self, value):
		self._RjctdRsn = value if type(value) != base_types.auto else self.make_default("RjctdRsn")

	@RjctdRsn.deleter
	def RjctdRsn(self):
		del self._RjctdRsn
		self._RjctdRsn = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RjctdRsn', type=RejectionReason68Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

