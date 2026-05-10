import base_types
import ContractRegistrationRequestV04

class AUTH_018_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CtrctRegnReq"]
		@property
		def CtrctRegnReq(self):
			return self._CtrctRegnReq

		@CtrctRegnReq.setter
		def CtrctRegnReq(self, value):
			self._CtrctRegnReq = value if type(value) != auto else self.make_default("CtrctRegnReq")

		@CtrctRegnReq.deleter
		def CtrctRegnReq(self):
			del self._CtrctRegnReq
			self._CtrctRegnReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CtrctRegnReq', type=ContractRegistrationRequestV04, min=1, max=1, mutex_group=None, array=False),
		))

