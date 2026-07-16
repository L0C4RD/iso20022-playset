# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SaleToPOIReportRequestV08

class CASP_009_001_08():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:casp.009.001.08"
		_docname = "casp.009.001.08"

		__slots__ = ["_SaleToPOIRptReq"]
		@property
		def SaleToPOIRptReq(self):
			return self._SaleToPOIRptReq

		@SaleToPOIRptReq.setter
		def SaleToPOIRptReq(self, value):
			self._SaleToPOIRptReq = value if value is not None else base_types.UninitialisedField(self, 'SaleToPOIRptReq', SaleToPOIReportRequestV08, False)

		@SaleToPOIRptReq.deleter
		def SaleToPOIRptReq(self):
			del self._SaleToPOIRptReq
			self._SaleToPOIRptReq = base_types.UninitialisedField(self, 'SaleToPOIRptReq', SaleToPOIReportRequestV08, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SaleToPOIRptReq', type=SaleToPOIReportRequestV08, min=1, max=1, mutex_group=None, array=False),
		))