# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._StatementOfInvestmentFundTransactionsCancellationV03 import StatementOfInvestmentFundTransactionsCancellationV03

class SEMT_007_001_03():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:semt.007.001.03",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_StmtOfInvstmtFndTxsCxl"]
		@property
		def StmtOfInvstmtFndTxsCxl(self):
			return self._StmtOfInvstmtFndTxsCxl

		@StmtOfInvstmtFndTxsCxl.setter
		def StmtOfInvstmtFndTxsCxl(self, value):
			self._StmtOfInvstmtFndTxsCxl = value if type(value) != base_types.auto else self.make_default("StmtOfInvstmtFndTxsCxl")

		@StmtOfInvstmtFndTxsCxl.deleter
		def StmtOfInvstmtFndTxsCxl(self):
			del self._StmtOfInvstmtFndTxsCxl
			self._StmtOfInvstmtFndTxsCxl = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='StmtOfInvstmtFndTxsCxl', type=StatementOfInvestmentFundTransactionsCancellationV03, min=1, max=1, mutex_group=None, array=False),
		))