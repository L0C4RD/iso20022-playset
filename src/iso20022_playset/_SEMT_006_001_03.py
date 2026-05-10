from . import base_types
from .StatementOfInvestmentFundTransactionsV03 import StatementOfInvestmentFundTransactionsV03

class SEMT_006_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_StmtOfInvstmtFndTxs"]
		@property
		def StmtOfInvstmtFndTxs(self):
			return self._StmtOfInvstmtFndTxs

		@StmtOfInvstmtFndTxs.setter
		def StmtOfInvstmtFndTxs(self, value):
			self._StmtOfInvstmtFndTxs = value if type(value) != base_types.auto else self.make_default("StmtOfInvstmtFndTxs")

		@StmtOfInvstmtFndTxs.deleter
		def StmtOfInvstmtFndTxs(self):
			del self._StmtOfInvstmtFndTxs
			self._StmtOfInvstmtFndTxs = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='StmtOfInvstmtFndTxs', type=StatementOfInvestmentFundTransactionsV03, min=1, max=1, mutex_group=None, array=False),
		))

