# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CreditorPaymentActivationRequestStatusReportV11 import CreditorPaymentActivationRequestStatusReportV11

class PAIN_014_001_11():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:pain.014.001.11"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_CdtrPmtActvtnReqStsRpt"]
		@property
		def CdtrPmtActvtnReqStsRpt(self):
			return self._CdtrPmtActvtnReqStsRpt

		@CdtrPmtActvtnReqStsRpt.setter
		def CdtrPmtActvtnReqStsRpt(self, value):
			self._CdtrPmtActvtnReqStsRpt = value if type(value) != base_types.auto else self.make_default("CdtrPmtActvtnReqStsRpt")

		@CdtrPmtActvtnReqStsRpt.deleter
		def CdtrPmtActvtnReqStsRpt(self):
			del self._CdtrPmtActvtnReqStsRpt
			self._CdtrPmtActvtnReqStsRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CdtrPmtActvtnReqStsRpt', type=CreditorPaymentActivationRequestStatusReportV11, min=1, max=1, mutex_group=None, array=False),
		))