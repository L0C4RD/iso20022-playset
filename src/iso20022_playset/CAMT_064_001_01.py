import base_types
import LimitUtilisationJournalQueryV01

class CAMT_064_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_LmtUtlstnJrnlQry"]
		@property
		def LmtUtlstnJrnlQry(self):
			return self._LmtUtlstnJrnlQry

		@LmtUtlstnJrnlQry.setter
		def LmtUtlstnJrnlQry(self, value):
			self._LmtUtlstnJrnlQry = value if type(value) != auto else self.make_default("LmtUtlstnJrnlQry")

		@LmtUtlstnJrnlQry.deleter
		def LmtUtlstnJrnlQry(self):
			del self._LmtUtlstnJrnlQry
			self._LmtUtlstnJrnlQry = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='LmtUtlstnJrnlQry', type=LimitUtilisationJournalQueryV01, min=1, max=1, mutex_group=None, array=False),
		))

