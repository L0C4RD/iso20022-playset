# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CancelCaseAssignmentV05

class CAMT_032_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.032.001.05"
		_docname = "camt.032.001.05"

		__slots__ = ["_CclCaseAssgnmt"]
		@property
		def CclCaseAssgnmt(self):
			return self._CclCaseAssgnmt

		@CclCaseAssgnmt.setter
		def CclCaseAssgnmt(self, value):
			self._CclCaseAssgnmt = value if value is not None else base_types.UninitialisedField(self, 'CclCaseAssgnmt', CancelCaseAssignmentV05, False)

		@CclCaseAssgnmt.deleter
		def CclCaseAssgnmt(self):
			del self._CclCaseAssgnmt
			self._CclCaseAssgnmt = base_types.UninitialisedField(self, 'CclCaseAssgnmt', CancelCaseAssignmentV05, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CclCaseAssgnmt', type=CancelCaseAssignmentV05, min=1, max=1, mutex_group=None, array=False),
		))