# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SaleToPOIReportRequestV07 import SaleToPOIReportRequestV07

class CASP_009_001_07():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:casp.009.001.07"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

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
			base_types.FieldEntry(name='SaleToPOIRptReq', type=SaleToPOIReportRequestV07, min=1, max=1, mutex_group=None, array=False),
		))