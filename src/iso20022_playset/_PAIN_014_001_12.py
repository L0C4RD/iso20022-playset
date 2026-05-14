# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CreditorPaymentActivationRequestStatusReportV12 import CreditorPaymentActivationRequestStatusReportV12

class PAIN_014_001_12():

	class Document(base_types._BaseFieldType):

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
			base_types.FieldEntry(name='CdtrPmtActvtnReqStsRpt', type=CreditorPaymentActivationRequestStatusReportV12, min=1, max=1, mutex_group=None, array=False),
		))