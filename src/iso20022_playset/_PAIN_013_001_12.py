from . import base_types
from ._CreditorPaymentActivationRequestV12 import CreditorPaymentActivationRequestV12

class PAIN_013_001_12():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CdtrPmtActvtnReq"]
		@property
		def CdtrPmtActvtnReq(self):
			return self._CdtrPmtActvtnReq

		@CdtrPmtActvtnReq.setter
		def CdtrPmtActvtnReq(self, value):
			self._CdtrPmtActvtnReq = value if type(value) != base_types.auto else self.make_default("CdtrPmtActvtnReq")

		@CdtrPmtActvtnReq.deleter
		def CdtrPmtActvtnReq(self):
			del self._CdtrPmtActvtnReq
			self._CdtrPmtActvtnReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CdtrPmtActvtnReq', type=CreditorPaymentActivationRequestV12, min=1, max=1, mutex_group=None, array=False),
		))

