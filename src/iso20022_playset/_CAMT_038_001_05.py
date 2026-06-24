# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CaseStatusReportRequestV05 import CaseStatusReportRequestV05

class CAMT_038_001_05():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:camt.038.001.05"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_CaseStsRptReq"]
		@property
		def CaseStsRptReq(self):
			return self._CaseStsRptReq

		@CaseStsRptReq.setter
		def CaseStsRptReq(self, value):
			self._CaseStsRptReq = value if type(value) != base_types.auto else self.make_default("CaseStsRptReq")

		@CaseStsRptReq.deleter
		def CaseStsRptReq(self):
			del self._CaseStsRptReq
			self._CaseStsRptReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CaseStsRptReq', type=CaseStatusReportRequestV05, min=1, max=1, mutex_group=None, array=False),
		))