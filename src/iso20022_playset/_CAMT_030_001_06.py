# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._NotificationOfCaseAssignmentV06 import NotificationOfCaseAssignmentV06

class CAMT_030_001_06():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:camt.030.001.06"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_NtfctnOfCaseAssgnmt"]
		@property
		def NtfctnOfCaseAssgnmt(self):
			return self._NtfctnOfCaseAssgnmt

		@NtfctnOfCaseAssgnmt.setter
		def NtfctnOfCaseAssgnmt(self, value):
			self._NtfctnOfCaseAssgnmt = value if type(value) != base_types.auto else self.make_default("NtfctnOfCaseAssgnmt")

		@NtfctnOfCaseAssgnmt.deleter
		def NtfctnOfCaseAssgnmt(self):
			del self._NtfctnOfCaseAssgnmt
			self._NtfctnOfCaseAssgnmt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='NtfctnOfCaseAssgnmt', type=NotificationOfCaseAssignmentV06, min=1, max=1, mutex_group=None, array=False),
		))