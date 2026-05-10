from . import base_types
import ATMReconciliationAcknowledgementV03

class CAAM_010_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ATMRcncltnAck"]
		@property
		def ATMRcncltnAck(self):
			return self._ATMRcncltnAck

		@ATMRcncltnAck.setter
		def ATMRcncltnAck(self, value):
			self._ATMRcncltnAck = value if type(value) != auto else self.make_default("ATMRcncltnAck")

		@ATMRcncltnAck.deleter
		def ATMRcncltnAck(self):
			del self._ATMRcncltnAck
			self._ATMRcncltnAck = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMRcncltnAck', type=ATMReconciliationAcknowledgementV03, min=1, max=1, mutex_group=None, array=False),
		))

