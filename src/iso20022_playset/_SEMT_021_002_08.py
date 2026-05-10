from . import base_types
from ._SecuritiesStatementQuery002V08 import SecuritiesStatementQuery002V08

class SEMT_021_002_08():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesStmtQry"]
		@property
		def SctiesStmtQry(self):
			return self._SctiesStmtQry

		@SctiesStmtQry.setter
		def SctiesStmtQry(self, value):
			self._SctiesStmtQry = value if type(value) != base_types.auto else self.make_default("SctiesStmtQry")

		@SctiesStmtQry.deleter
		def SctiesStmtQry(self):
			del self._SctiesStmtQry
			self._SctiesStmtQry = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesStmtQry', type=SecuritiesStatementQuery002V08, min=1, max=1, mutex_group=None, array=False),
		))

