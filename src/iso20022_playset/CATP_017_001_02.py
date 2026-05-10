import base_types
import ATMTransferResponseV02

class CATP_017_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ATMTrfRspn"]
		@property
		def ATMTrfRspn(self):
			return self._ATMTrfRspn

		@ATMTrfRspn.setter
		def ATMTrfRspn(self, value):
			self._ATMTrfRspn = value if type(value) != auto else self.make_default("ATMTrfRspn")

		@ATMTrfRspn.deleter
		def ATMTrfRspn(self):
			del self._ATMTrfRspn
			self._ATMTrfRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMTrfRspn', type=ATMTransferResponseV02, min=1, max=1, mutex_group=None, array=False),
		))

