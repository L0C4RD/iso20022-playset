from . import base_types
from .TradeLegStatementV04 import TradeLegStatementV04

class SECL_003_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_TradLegStmt"]
		@property
		def TradLegStmt(self):
			return self._TradLegStmt

		@TradLegStmt.setter
		def TradLegStmt(self, value):
			self._TradLegStmt = value if type(value) != auto else self.make_default("TradLegStmt")

		@TradLegStmt.deleter
		def TradLegStmt(self):
			del self._TradLegStmt
			self._TradLegStmt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='TradLegStmt', type=TradeLegStatementV04, min=1, max=1, mutex_group=None, array=False),
		))

