# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CancelCaseAssignmentV05 import CancelCaseAssignmentV05

class CAMT_032_001_05():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:camt.032.001.05"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_CclCaseAssgnmt"]
		@property
		def CclCaseAssgnmt(self):
			return self._CclCaseAssgnmt

		@CclCaseAssgnmt.setter
		def CclCaseAssgnmt(self, value):
			self._CclCaseAssgnmt = value if type(value) != base_types.auto else self.make_default("CclCaseAssgnmt")

		@CclCaseAssgnmt.deleter
		def CclCaseAssgnmt(self):
			del self._CclCaseAssgnmt
			self._CclCaseAssgnmt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CclCaseAssgnmt', type=CancelCaseAssignmentV05, min=1, max=1, mutex_group=None, array=False),
		))