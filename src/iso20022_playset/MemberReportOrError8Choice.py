from . import base_types
from .Member7 import Member7
from .ErrorHandling3 import ErrorHandling3

class MemberReportOrError8Choice(base_types._BaseFieldType):

	__slots__ = ["_BizErr", "_Mmb"]
	@property
	def BizErr(self):
		return self._BizErr

	@BizErr.setter
	def BizErr(self, value):
		self._BizErr = value if type(value) != auto else self.make_default("BizErr")

	@BizErr.deleter
	def BizErr(self):
		del self._BizErr
		self._BizErr = None

	@property
	def Mmb(self):
		return self._Mmb

	@Mmb.setter
	def Mmb(self, value):
		self._Mmb = value if type(value) != auto else self.make_default("Mmb")

	@Mmb.deleter
	def Mmb(self):
		del self._Mmb
		self._Mmb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BizErr', type=ErrorHandling3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Mmb', type=Member7, min=0, max=1, mutex_group=1, array=False),
	))

