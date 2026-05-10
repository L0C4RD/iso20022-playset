from . import base_types
from .AccountRequestRejectionV04 import AccountRequestRejectionV04

class ACMT_011_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AcctReqRjctn"]
		@property
		def AcctReqRjctn(self):
			return self._AcctReqRjctn

		@AcctReqRjctn.setter
		def AcctReqRjctn(self, value):
			self._AcctReqRjctn = value if type(value) != base_types.auto else self.make_default("AcctReqRjctn")

		@AcctReqRjctn.deleter
		def AcctReqRjctn(self):
			del self._AcctReqRjctn
			self._AcctReqRjctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctReqRjctn', type=AccountRequestRejectionV04, min=1, max=1, mutex_group=None, array=False),
		))

