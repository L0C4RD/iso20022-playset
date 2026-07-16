# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import StatementOfInvestmentFundTransactionsCancellationV03

class SEMT_007_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:semt.007.001.03"
		_docname = "semt.007.001.03"

		__slots__ = ["_StmtOfInvstmtFndTxsCxl"]
		@property
		def StmtOfInvstmtFndTxsCxl(self):
			return self._StmtOfInvstmtFndTxsCxl

		@StmtOfInvstmtFndTxsCxl.setter
		def StmtOfInvstmtFndTxsCxl(self, value):
			self._StmtOfInvstmtFndTxsCxl = value if value is not None else base_types.UninitialisedField(self, 'StmtOfInvstmtFndTxsCxl', StatementOfInvestmentFundTransactionsCancellationV03, False)

		@StmtOfInvstmtFndTxsCxl.deleter
		def StmtOfInvstmtFndTxsCxl(self):
			del self._StmtOfInvstmtFndTxsCxl
			self._StmtOfInvstmtFndTxsCxl = base_types.UninitialisedField(self, 'StmtOfInvstmtFndTxsCxl', StatementOfInvestmentFundTransactionsCancellationV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='StmtOfInvstmtFndTxsCxl', type=StatementOfInvestmentFundTransactionsCancellationV03, min=1, max=1, mutex_group=None, array=False),
		))