# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ErrorHandling5
from . import LimitJournal3

class LimitJournalReportOrError8Choice(base_types._BaseFieldType):

	__slots__ = ["_BizErr", "_LmtJrnl"]
	@property
	def BizErr(self):
		return self._BizErr

	@BizErr.setter
	def BizErr(self, value):
		self._BizErr = value if value is not None else base_types.UninitialisedField(self, 'BizErr', ErrorHandling5, True)

	@BizErr.deleter
	def BizErr(self):
		del self._BizErr
		self._BizErr = base_types.UninitialisedField(self, 'BizErr', ErrorHandling5, True)

	@property
	def LmtJrnl(self):
		return self._LmtJrnl

	@LmtJrnl.setter
	def LmtJrnl(self, value):
		self._LmtJrnl = value if value is not None else base_types.UninitialisedField(self, 'LmtJrnl', LimitJournal3, False)

	@LmtJrnl.deleter
	def LmtJrnl(self):
		del self._LmtJrnl
		self._LmtJrnl = base_types.UninitialisedField(self, 'LmtJrnl', LimitJournal3, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BizErr', type=ErrorHandling5, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='LmtJrnl', type=LimitJournal3, min=0, max=1, mutex_group=1, array=False),
	))