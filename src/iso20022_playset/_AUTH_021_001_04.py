from . import base_types
from .ContractRegistrationAmendmentRequestV04 import ContractRegistrationAmendmentRequestV04

class AUTH_021_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CtrctRegnAmdmntReq"]
		@property
		def CtrctRegnAmdmntReq(self):
			return self._CtrctRegnAmdmntReq

		@CtrctRegnAmdmntReq.setter
		def CtrctRegnAmdmntReq(self, value):
			self._CtrctRegnAmdmntReq = value if type(value) != base_types.auto else self.make_default("CtrctRegnAmdmntReq")

		@CtrctRegnAmdmntReq.deleter
		def CtrctRegnAmdmntReq(self):
			del self._CtrctRegnAmdmntReq
			self._CtrctRegnAmdmntReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CtrctRegnAmdmntReq', type=ContractRegistrationAmendmentRequestV04, min=1, max=1, mutex_group=None, array=False),
		))

