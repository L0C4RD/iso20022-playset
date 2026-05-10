import base_types
import LimitIdentification7
import LimitJournalReportOrError8Choice

class LimitJournalReport4(base_types._BaseFieldType):

	__slots__ = ["_LmtId", "_LmtRpt"]
	@property
	def LmtId(self):
		return self._LmtId

	@LmtId.setter
	def LmtId(self, value):
		self._LmtId = value if type(value) != auto else self.make_default("LmtId")

	@LmtId.deleter
	def LmtId(self):
		del self._LmtId
		self._LmtId = None

	@property
	def LmtRpt(self):
		return self._LmtRpt

	@LmtRpt.setter
	def LmtRpt(self, value):
		self._LmtRpt = value if type(value) != auto else self.make_default("LmtRpt")

	@LmtRpt.deleter
	def LmtRpt(self):
		del self._LmtRpt
		self._LmtRpt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LmtId', type=LimitIdentification7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LmtRpt', type=LimitJournalReportOrError8Choice, min=1, max=1, mutex_group=None, array=False),
	))

