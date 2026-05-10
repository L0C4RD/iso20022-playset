from . import base_types
from .CreditorPaymentActivationRequestStatusReportV11 import CreditorPaymentActivationRequestStatusReportV11

class PAIN_014_001_11():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CdtrPmtActvtnReqStsRpt"]
		@property
		def CdtrPmtActvtnReqStsRpt(self):
			return self._CdtrPmtActvtnReqStsRpt

		@CdtrPmtActvtnReqStsRpt.setter
		def CdtrPmtActvtnReqStsRpt(self, value):
			self._CdtrPmtActvtnReqStsRpt = value if type(value) != auto else self.make_default("CdtrPmtActvtnReqStsRpt")

		@CdtrPmtActvtnReqStsRpt.deleter
		def CdtrPmtActvtnReqStsRpt(self):
			del self._CdtrPmtActvtnReqStsRpt
			self._CdtrPmtActvtnReqStsRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CdtrPmtActvtnReqStsRpt', type=CreditorPaymentActivationRequestStatusReportV11, min=1, max=1, mutex_group=None, array=False),
		))

