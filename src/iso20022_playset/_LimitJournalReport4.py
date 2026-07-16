# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import LimitIdentification7
from . import LimitJournalReportOrError8Choice

class LimitJournalReport4(base_types._BaseFieldType):

	__slots__ = ["_LmtId", "_LmtRpt"]
	@property
	def LmtId(self):
		return self._LmtId

	@LmtId.setter
	def LmtId(self, value):
		self._LmtId = value if value is not None else base_types.UninitialisedField(self, 'LmtId', LimitIdentification7, False)

	@LmtId.deleter
	def LmtId(self):
		del self._LmtId
		self._LmtId = base_types.UninitialisedField(self, 'LmtId', LimitIdentification7, False)

	@property
	def LmtRpt(self):
		return self._LmtRpt

	@LmtRpt.setter
	def LmtRpt(self, value):
		self._LmtRpt = value if value is not None else base_types.UninitialisedField(self, 'LmtRpt', LimitJournalReportOrError8Choice, False)

	@LmtRpt.deleter
	def LmtRpt(self):
		del self._LmtRpt
		self._LmtRpt = base_types.UninitialisedField(self, 'LmtRpt', LimitJournalReportOrError8Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='LmtId', type=LimitIdentification7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LmtRpt', type=LimitJournalReportOrError8Choice, min=1, max=1, mutex_group=None, array=False),
	))