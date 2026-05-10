from . import base_types
from .ATMReconciliationResponseV01 import ATMReconciliationResponseV01

class CAAM_016_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ATMRcncltnRspn"]
		@property
		def ATMRcncltnRspn(self):
			return self._ATMRcncltnRspn

		@ATMRcncltnRspn.setter
		def ATMRcncltnRspn(self, value):
			self._ATMRcncltnRspn = value if type(value) != auto else self.make_default("ATMRcncltnRspn")

		@ATMRcncltnRspn.deleter
		def ATMRcncltnRspn(self):
			del self._ATMRcncltnRspn
			self._ATMRcncltnRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMRcncltnRspn', type=ATMReconciliationResponseV01, min=1, max=1, mutex_group=None, array=False),
		))

