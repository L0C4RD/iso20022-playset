# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesFinancingReportingMissingCollateralRequestV02

class AUTH_083_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.083.001.02"
		_docname = "auth.083.001.02"

		__slots__ = ["_SctiesFincgRptgMssngCollReq"]
		@property
		def SctiesFincgRptgMssngCollReq(self):
			return self._SctiesFincgRptgMssngCollReq

		@SctiesFincgRptgMssngCollReq.setter
		def SctiesFincgRptgMssngCollReq(self, value):
			self._SctiesFincgRptgMssngCollReq = value if value is not None else base_types.UninitialisedField(self, 'SctiesFincgRptgMssngCollReq', SecuritiesFinancingReportingMissingCollateralRequestV02, False)

		@SctiesFincgRptgMssngCollReq.deleter
		def SctiesFincgRptgMssngCollReq(self):
			del self._SctiesFincgRptgMssngCollReq
			self._SctiesFincgRptgMssngCollReq = base_types.UninitialisedField(self, 'SctiesFincgRptgMssngCollReq', SecuritiesFinancingReportingMissingCollateralRequestV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesFincgRptgMssngCollReq', type=SecuritiesFinancingReportingMissingCollateralRequestV02, min=1, max=1, mutex_group=None, array=False),
		))