from . import base_types
from .ErrorHandling5 import ErrorHandling5
from .LimitJournal3 import LimitJournal3

class LimitJournalReportOrError8Choice(base_types._BaseFieldType):

	__slots__ = ["_LmtJrnl", "_BizErr"]
	@property
	def LmtJrnl(self):
		return self._LmtJrnl

	@LmtJrnl.setter
	def LmtJrnl(self, value):
		self._LmtJrnl = value if type(value) != base_types.auto else self.make_default("LmtJrnl")

	@LmtJrnl.deleter
	def LmtJrnl(self):
		del self._LmtJrnl
		self._LmtJrnl = None

	@property
	def BizErr(self):
		return self._BizErr

	@BizErr.setter
	def BizErr(self, value):
		self._BizErr = value if type(value) != base_types.auto else self.make_default("BizErr")

	@BizErr.deleter
	def BizErr(self):
		del self._BizErr
		self._BizErr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LmtJrnl', type=LimitJournal3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='BizErr', type=ErrorHandling5, min=1, max=None, mutex_group=1, array=True),
	))

