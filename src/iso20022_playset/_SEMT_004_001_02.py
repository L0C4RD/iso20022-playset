# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CustodyStatementOfHoldingsCancellationV02

class SEMT_004_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02"
		_docname = "semt.004.001.02"

		__slots__ = ["_CtdyStmtOfHldgsCxlV02"]
		@property
		def CtdyStmtOfHldgsCxlV02(self):
			return self._CtdyStmtOfHldgsCxlV02

		@CtdyStmtOfHldgsCxlV02.setter
		def CtdyStmtOfHldgsCxlV02(self, value):
			self._CtdyStmtOfHldgsCxlV02 = value if value is not None else base_types.UninitialisedField(self, 'CtdyStmtOfHldgsCxlV02', CustodyStatementOfHoldingsCancellationV02, False)

		@CtdyStmtOfHldgsCxlV02.deleter
		def CtdyStmtOfHldgsCxlV02(self):
			del self._CtdyStmtOfHldgsCxlV02
			self._CtdyStmtOfHldgsCxlV02 = base_types.UninitialisedField(self, 'CtdyStmtOfHldgsCxlV02', CustodyStatementOfHoldingsCancellationV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CtdyStmtOfHldgsCxlV02', type=CustodyStatementOfHoldingsCancellationV02, min=1, max=1, mutex_group=None, array=False),
		))