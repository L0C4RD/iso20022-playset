from . import base_types
import ATMReconciliationRequestV01

class CAAM_015_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ATMRcncltnReq"]
		@property
		def ATMRcncltnReq(self):
			return self._ATMRcncltnReq

		@ATMRcncltnReq.setter
		def ATMRcncltnReq(self, value):
			self._ATMRcncltnReq = value if type(value) != auto else self.make_default("ATMRcncltnReq")

		@ATMRcncltnReq.deleter
		def ATMRcncltnReq(self):
			del self._ATMRcncltnReq
			self._ATMRcncltnReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMRcncltnReq', type=ATMReconciliationRequestV01, min=1, max=1, mutex_group=None, array=False),
		))

