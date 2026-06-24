# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SaleToPOIReportResponseV07 import SaleToPOIReportResponseV07

class CASP_010_001_07():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:casp.010.001.07"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_SaleToPOIRptRspn"]
		@property
		def SaleToPOIRptRspn(self):
			return self._SaleToPOIRptRspn

		@SaleToPOIRptRspn.setter
		def SaleToPOIRptRspn(self, value):
			self._SaleToPOIRptRspn = value if type(value) != base_types.auto else self.make_default("SaleToPOIRptRspn")

		@SaleToPOIRptRspn.deleter
		def SaleToPOIRptRspn(self):
			del self._SaleToPOIRptRspn
			self._SaleToPOIRptRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SaleToPOIRptRspn', type=SaleToPOIReportResponseV07, min=1, max=1, mutex_group=None, array=False),
		))