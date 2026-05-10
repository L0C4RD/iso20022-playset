from . import base_types
import CreditorPaymentActivationRequestV11

class PAIN_013_001_11():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CdtrPmtActvtnReq"]
		@property
		def CdtrPmtActvtnReq(self):
			return self._CdtrPmtActvtnReq

		@CdtrPmtActvtnReq.setter
		def CdtrPmtActvtnReq(self, value):
			self._CdtrPmtActvtnReq = value if type(value) != auto else self.make_default("CdtrPmtActvtnReq")

		@CdtrPmtActvtnReq.deleter
		def CdtrPmtActvtnReq(self):
			del self._CdtrPmtActvtnReq
			self._CdtrPmtActvtnReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CdtrPmtActvtnReq', type=CreditorPaymentActivationRequestV11, min=1, max=1, mutex_group=None, array=False),
		))

