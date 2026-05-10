from . import base_types
from .AcknowledgementV03 import AcknowledgementV03

class TSMT_001_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_Ack"]
		@property
		def Ack(self):
			return self._Ack

		@Ack.setter
		def Ack(self, value):
			self._Ack = value if type(value) != auto else self.make_default("Ack")

		@Ack.deleter
		def Ack(self):
			del self._Ack
			self._Ack = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='Ack', type=AcknowledgementV03, min=1, max=1, mutex_group=None, array=False),
		))

