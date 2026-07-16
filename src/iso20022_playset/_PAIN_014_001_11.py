# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CreditorPaymentActivationRequestStatusReportV11

class PAIN_014_001_11():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:pain.014.001.11"
		_docname = "pain.014.001.11"

		__slots__ = ["_CdtrPmtActvtnReqStsRpt"]
		@property
		def CdtrPmtActvtnReqStsRpt(self):
			return self._CdtrPmtActvtnReqStsRpt

		@CdtrPmtActvtnReqStsRpt.setter
		def CdtrPmtActvtnReqStsRpt(self, value):
			self._CdtrPmtActvtnReqStsRpt = value if value is not None else base_types.UninitialisedField(self, 'CdtrPmtActvtnReqStsRpt', CreditorPaymentActivationRequestStatusReportV11, False)

		@CdtrPmtActvtnReqStsRpt.deleter
		def CdtrPmtActvtnReqStsRpt(self):
			del self._CdtrPmtActvtnReqStsRpt
			self._CdtrPmtActvtnReqStsRpt = base_types.UninitialisedField(self, 'CdtrPmtActvtnReqStsRpt', CreditorPaymentActivationRequestStatusReportV11, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CdtrPmtActvtnReqStsRpt', type=CreditorPaymentActivationRequestStatusReportV11, min=1, max=1, mutex_group=None, array=False),
		))