from . import base_types
import CorporateActionInstructionStatementReport002V13

class SEEV_042_002_13():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CorpActnInstrStmtRpt"]
		@property
		def CorpActnInstrStmtRpt(self):
			return self._CorpActnInstrStmtRpt

		@CorpActnInstrStmtRpt.setter
		def CorpActnInstrStmtRpt(self, value):
			self._CorpActnInstrStmtRpt = value if type(value) != auto else self.make_default("CorpActnInstrStmtRpt")

		@CorpActnInstrStmtRpt.deleter
		def CorpActnInstrStmtRpt(self):
			del self._CorpActnInstrStmtRpt
			self._CorpActnInstrStmtRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CorpActnInstrStmtRpt', type=CorporateActionInstructionStatementReport002V13, min=1, max=1, mutex_group=None, array=False),
		))

