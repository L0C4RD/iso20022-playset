# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CreditorPaymentActivationRequestStatusReportV12

class PAIN_014_001_12():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:pain.014.001.12"
		_docname = "pain.014.001.12"

		__slots__ = ["_CdtrPmtActvtnReqStsRpt"]
		@property
		def CdtrPmtActvtnReqStsRpt(self):
			return self._CdtrPmtActvtnReqStsRpt

		@CdtrPmtActvtnReqStsRpt.setter
		def CdtrPmtActvtnReqStsRpt(self, value):
			self._CdtrPmtActvtnReqStsRpt = value if value is not None else base_types.UninitialisedField(self, 'CdtrPmtActvtnReqStsRpt', CreditorPaymentActivationRequestStatusReportV12, False)

		@CdtrPmtActvtnReqStsRpt.deleter
		def CdtrPmtActvtnReqStsRpt(self):
			del self._CdtrPmtActvtnReqStsRpt
			self._CdtrPmtActvtnReqStsRpt = base_types.UninitialisedField(self, 'CdtrPmtActvtnReqStsRpt', CreditorPaymentActivationRequestStatusReportV12, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CdtrPmtActvtnReqStsRpt', type=CreditorPaymentActivationRequestStatusReportV12, min=1, max=1, mutex_group=None, array=False),
		))