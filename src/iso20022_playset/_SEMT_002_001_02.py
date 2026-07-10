# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CustodyStatementOfHoldingsV02 import CustodyStatementOfHoldingsV02

class SEMT_002_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:semt.002.001.02"
		_docname = "semt.002.001.02"

		__slots__ = ["_CtdyStmtOfHldgsV02"]
		@property
		def CtdyStmtOfHldgsV02(self):
			return self._CtdyStmtOfHldgsV02

		@CtdyStmtOfHldgsV02.setter
		def CtdyStmtOfHldgsV02(self, value):
			self._CtdyStmtOfHldgsV02 = value if type(value) != base_types.auto else self.make_default("CtdyStmtOfHldgsV02")

		@CtdyStmtOfHldgsV02.deleter
		def CtdyStmtOfHldgsV02(self):
			del self._CtdyStmtOfHldgsV02
			self._CtdyStmtOfHldgsV02 = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CtdyStmtOfHldgsV02', type=CustodyStatementOfHoldingsV02, min=1, max=1, mutex_group=None, array=False),
		))