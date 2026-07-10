# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SaleToPOIReportRequestV08 import SaleToPOIReportRequestV08

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
			self._SaleToPOIRptReq = value if type(value) != base_types.auto else self.make_default("SaleToPOIRptReq")

		@SaleToPOIRptReq.deleter
		def SaleToPOIRptReq(self):
			del self._SaleToPOIRptReq
			self._SaleToPOIRptReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SaleToPOIRptReq', type=SaleToPOIReportRequestV08, min=1, max=1, mutex_group=None, array=False),
		))