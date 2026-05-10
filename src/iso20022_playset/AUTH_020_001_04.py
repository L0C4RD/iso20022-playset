from . import base_types
from .ContractRegistrationClosureRequestV04 import ContractRegistrationClosureRequestV04

class AUTH_020_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CtrctRegnClsrReq"]
		@property
		def CtrctRegnClsrReq(self):
			return self._CtrctRegnClsrReq

		@CtrctRegnClsrReq.setter
		def CtrctRegnClsrReq(self, value):
			self._CtrctRegnClsrReq = value if type(value) != auto else self.make_default("CtrctRegnClsrReq")

		@CtrctRegnClsrReq.deleter
		def CtrctRegnClsrReq(self):
			del self._CtrctRegnClsrReq
			self._CtrctRegnClsrReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CtrctRegnClsrReq', type=ContractRegistrationClosureRequestV04, min=1, max=1, mutex_group=None, array=False),
		))

