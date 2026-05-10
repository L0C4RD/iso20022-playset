from . import base_types
from .AccountOpeningRequestV05 import AccountOpeningRequestV05

class ACMT_007_001_05():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AcctOpngReq"]
		@property
		def AcctOpngReq(self):
			return self._AcctOpngReq

		@AcctOpngReq.setter
		def AcctOpngReq(self, value):
			self._AcctOpngReq = value if type(value) != base_types.auto else self.make_default("AcctOpngReq")

		@AcctOpngReq.deleter
		def AcctOpngReq(self):
			del self._AcctOpngReq
			self._AcctOpngReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctOpngReq', type=AccountOpeningRequestV05, min=1, max=1, mutex_group=None, array=False),
		))

