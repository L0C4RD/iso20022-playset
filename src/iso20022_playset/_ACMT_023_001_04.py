from . import base_types
from .IdentificationVerificationRequestV04 import IdentificationVerificationRequestV04

class ACMT_023_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_IdVrfctnReq"]
		@property
		def IdVrfctnReq(self):
			return self._IdVrfctnReq

		@IdVrfctnReq.setter
		def IdVrfctnReq(self, value):
			self._IdVrfctnReq = value if type(value) != base_types.auto else self.make_default("IdVrfctnReq")

		@IdVrfctnReq.deleter
		def IdVrfctnReq(self):
			del self._IdVrfctnReq
			self._IdVrfctnReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='IdVrfctnReq', type=IdentificationVerificationRequestV04, min=1, max=1, mutex_group=None, array=False),
		))

