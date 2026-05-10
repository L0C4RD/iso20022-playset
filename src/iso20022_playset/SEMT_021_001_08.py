from . import base_types
import SecuritiesStatementQueryV08

class SEMT_021_001_08():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesStmtQry"]
		@property
		def SctiesStmtQry(self):
			return self._SctiesStmtQry

		@SctiesStmtQry.setter
		def SctiesStmtQry(self, value):
			self._SctiesStmtQry = value if type(value) != auto else self.make_default("SctiesStmtQry")

		@SctiesStmtQry.deleter
		def SctiesStmtQry(self):
			del self._SctiesStmtQry
			self._SctiesStmtQry = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesStmtQry', type=SecuritiesStatementQueryV08, min=1, max=1, mutex_group=None, array=False),
		))

