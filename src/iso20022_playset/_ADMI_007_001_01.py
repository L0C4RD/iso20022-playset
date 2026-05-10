from . import base_types
from ._ReceiptAcknowledgementV01 import ReceiptAcknowledgementV01

class ADMI_007_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_RctAck"]
		@property
		def RctAck(self):
			return self._RctAck

		@RctAck.setter
		def RctAck(self, value):
			self._RctAck = value if type(value) != base_types.auto else self.make_default("RctAck")

		@RctAck.deleter
		def RctAck(self):
			del self._RctAck
			self._RctAck = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RctAck', type=ReceiptAcknowledgementV01, min=1, max=1, mutex_group=None, array=False),
		))

