# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CaseStatusReportV06 import CaseStatusReportV06

class CAMT_039_001_06():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:camt.039.001.06"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_CaseStsRpt"]
		@property
		def CaseStsRpt(self):
			return self._CaseStsRpt

		@CaseStsRpt.setter
		def CaseStsRpt(self, value):
			self._CaseStsRpt = value if type(value) != base_types.auto else self.make_default("CaseStsRpt")

		@CaseStsRpt.deleter
		def CaseStsRpt(self):
			del self._CaseStsRpt
			self._CaseStsRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CaseStsRpt', type=CaseStatusReportV06, min=1, max=1, mutex_group=None, array=False),
		))