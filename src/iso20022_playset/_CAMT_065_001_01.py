from . import base_types
from ._LimitUtilisationJournalReportV01 import LimitUtilisationJournalReportV01

class CAMT_065_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_LmtUtlstnJrnlRpt"]
		@property
		def LmtUtlstnJrnlRpt(self):
			return self._LmtUtlstnJrnlRpt

		@LmtUtlstnJrnlRpt.setter
		def LmtUtlstnJrnlRpt(self, value):
			self._LmtUtlstnJrnlRpt = value if type(value) != base_types.auto else self.make_default("LmtUtlstnJrnlRpt")

		@LmtUtlstnJrnlRpt.deleter
		def LmtUtlstnJrnlRpt(self):
			del self._LmtUtlstnJrnlRpt
			self._LmtUtlstnJrnlRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='LmtUtlstnJrnlRpt', type=LimitUtilisationJournalReportV01, min=1, max=1, mutex_group=None, array=False),
		))

