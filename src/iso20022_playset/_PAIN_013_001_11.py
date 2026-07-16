# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CreditorPaymentActivationRequestV11

class PAIN_013_001_11():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:pain.013.001.11"
		_docname = "pain.013.001.11"

		__slots__ = ["_CdtrPmtActvtnReq"]
		@property
		def CdtrPmtActvtnReq(self):
			return self._CdtrPmtActvtnReq

		@CdtrPmtActvtnReq.setter
		def CdtrPmtActvtnReq(self, value):
			self._CdtrPmtActvtnReq = value if value is not None else base_types.UninitialisedField(self, 'CdtrPmtActvtnReq', CreditorPaymentActivationRequestV11, False)

		@CdtrPmtActvtnReq.deleter
		def CdtrPmtActvtnReq(self):
			del self._CdtrPmtActvtnReq
			self._CdtrPmtActvtnReq = base_types.UninitialisedField(self, 'CdtrPmtActvtnReq', CreditorPaymentActivationRequestV11, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CdtrPmtActvtnReq', type=CreditorPaymentActivationRequestV11, min=1, max=1, mutex_group=None, array=False),
		))