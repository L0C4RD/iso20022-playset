import base_types
import ErrorHandling5
import LimitJournal3

class LimitJournalReportOrError8Choice(base_types._BaseFieldType):

	__slots__ = ["_BizErr", "_LmtJrnl"]
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
	def LmtJrnl(self):
		return self._LmtJrnl

	@LmtJrnl.setter
	def LmtJrnl(self, value):
		self._LmtJrnl = value if type(value) != auto else self.make_default("LmtJrnl")

	@LmtJrnl.deleter
	def LmtJrnl(self):
		del self._LmtJrnl
		self._LmtJrnl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BizErr', type=ErrorHandling5, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='LmtJrnl', type=LimitJournal3, min=0, max=1, mutex_group=1, array=False),
	))

