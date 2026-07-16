# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SaleToPOIReportResponseV08

class CASP_010_001_08():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:casp.010.001.08"
		_docname = "casp.010.001.08"

		__slots__ = ["_SaleToPOIRptRspn"]
		@property
		def SaleToPOIRptRspn(self):
			return self._SaleToPOIRptRspn

		@SaleToPOIRptRspn.setter
		def SaleToPOIRptRspn(self, value):
			self._SaleToPOIRptRspn = value if value is not None else base_types.UninitialisedField(self, 'SaleToPOIRptRspn', SaleToPOIReportResponseV08, False)

		@SaleToPOIRptRspn.deleter
		def SaleToPOIRptRspn(self):
			del self._SaleToPOIRptRspn
			self._SaleToPOIRptRspn = base_types.UninitialisedField(self, 'SaleToPOIRptRspn', SaleToPOIReportResponseV08, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SaleToPOIRptRspn', type=SaleToPOIReportResponseV08, min=1, max=1, mutex_group=None, array=False),
		))