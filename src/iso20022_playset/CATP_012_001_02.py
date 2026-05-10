from . import base_types
from .ATMDepositRequestV02 import ATMDepositRequestV02

class CATP_012_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ATMDpstReq"]
		@property
		def ATMDpstReq(self):
			return self._ATMDpstReq

		@ATMDpstReq.setter
		def ATMDpstReq(self, value):
			self._ATMDpstReq = value if type(value) != auto else self.make_default("ATMDpstReq")

		@ATMDpstReq.deleter
		def ATMDpstReq(self):
			del self._ATMDpstReq
			self._ATMDpstReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMDpstReq', type=ATMDepositRequestV02, min=1, max=1, mutex_group=None, array=False),
		))

