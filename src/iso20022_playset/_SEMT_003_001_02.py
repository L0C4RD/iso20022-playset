# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AccountingStatementOfHoldingsV02 import AccountingStatementOfHoldingsV02

class SEMT_003_001_02():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:semt.003.001.02"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_AcctgStmtOfHldgsV02"]
		@property
		def AcctgStmtOfHldgsV02(self):
			return self._AcctgStmtOfHldgsV02

		@AcctgStmtOfHldgsV02.setter
		def AcctgStmtOfHldgsV02(self, value):
			self._AcctgStmtOfHldgsV02 = value if type(value) != base_types.auto else self.make_default("AcctgStmtOfHldgsV02")

		@AcctgStmtOfHldgsV02.deleter
		def AcctgStmtOfHldgsV02(self):
			del self._AcctgStmtOfHldgsV02
			self._AcctgStmtOfHldgsV02 = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctgStmtOfHldgsV02', type=AccountingStatementOfHoldingsV02, min=1, max=1, mutex_group=None, array=False),
		))