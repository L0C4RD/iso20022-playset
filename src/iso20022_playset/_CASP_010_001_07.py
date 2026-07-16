# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SaleToPOIReportResponseV07

class CASP_010_001_07():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:casp.010.001.07"
		_docname = "casp.010.001.07"

		__slots__ = ["_SaleToPOIRptRspn"]
		@property
		def SaleToPOIRptRspn(self):
			return self._SaleToPOIRptRspn

		@SaleToPOIRptRspn.setter
		def SaleToPOIRptRspn(self, value):
			self._SaleToPOIRptRspn = value if value is not None else base_types.UninitialisedField(self, 'SaleToPOIRptRspn', SaleToPOIReportResponseV07, False)

		@SaleToPOIRptRspn.deleter
		def SaleToPOIRptRspn(self):
			del self._SaleToPOIRptRspn
			self._SaleToPOIRptRspn = base_types.UninitialisedField(self, 'SaleToPOIRptRspn', SaleToPOIReportResponseV07, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SaleToPOIRptRspn', type=SaleToPOIReportResponseV07, min=1, max=1, mutex_group=None, array=False),
		))