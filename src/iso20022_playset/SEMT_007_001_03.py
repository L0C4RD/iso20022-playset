from . import base_types
import StatementOfInvestmentFundTransactionsCancellationV03

class SEMT_007_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_StmtOfInvstmtFndTxsCxl"]
		@property
		def StmtOfInvstmtFndTxsCxl(self):
			return self._StmtOfInvstmtFndTxsCxl

		@StmtOfInvstmtFndTxsCxl.setter
		def StmtOfInvstmtFndTxsCxl(self, value):
			self._StmtOfInvstmtFndTxsCxl = value if type(value) != auto else self.make_default("StmtOfInvstmtFndTxsCxl")

		@StmtOfInvstmtFndTxsCxl.deleter
		def StmtOfInvstmtFndTxsCxl(self):
			del self._StmtOfInvstmtFndTxsCxl
			self._StmtOfInvstmtFndTxsCxl = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='StmtOfInvstmtFndTxsCxl', type=StatementOfInvestmentFundTransactionsCancellationV03, min=1, max=1, mutex_group=None, array=False),
		))

