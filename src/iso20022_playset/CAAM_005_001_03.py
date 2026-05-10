from . import base_types
from .ATMDiagnosticRequestV03 import ATMDiagnosticRequestV03

class CAAM_005_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ATMDgnstcReq"]
		@property
		def ATMDgnstcReq(self):
			return self._ATMDgnstcReq

		@ATMDgnstcReq.setter
		def ATMDgnstcReq(self, value):
			self._ATMDgnstcReq = value if type(value) != auto else self.make_default("ATMDgnstcReq")

		@ATMDgnstcReq.deleter
		def ATMDgnstcReq(self):
			del self._ATMDgnstcReq
			self._ATMDgnstcReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMDgnstcReq', type=ATMDiagnosticRequestV03, min=1, max=1, mutex_group=None, array=False),
		))

