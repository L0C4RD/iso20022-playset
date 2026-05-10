from . import base_types
import ChargesPaymentRequestV03

class CAMT_106_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ChrgsPmtReq"]
		@property
		def ChrgsPmtReq(self):
			return self._ChrgsPmtReq

		@ChrgsPmtReq.setter
		def ChrgsPmtReq(self, value):
			self._ChrgsPmtReq = value if type(value) != auto else self.make_default("ChrgsPmtReq")

		@ChrgsPmtReq.deleter
		def ChrgsPmtReq(self):
			del self._ChrgsPmtReq
			self._ChrgsPmtReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ChrgsPmtReq', type=ChargesPaymentRequestV03, min=1, max=1, mutex_group=None, array=False),
		))

