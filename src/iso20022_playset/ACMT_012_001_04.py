from . import base_types
from .AccountAdditionalInformationRequestV04 import AccountAdditionalInformationRequestV04

class ACMT_012_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AcctAddtlInfReq"]
		@property
		def AcctAddtlInfReq(self):
			return self._AcctAddtlInfReq

		@AcctAddtlInfReq.setter
		def AcctAddtlInfReq(self, value):
			self._AcctAddtlInfReq = value if type(value) != base_types.auto else self.make_default("AcctAddtlInfReq")

		@AcctAddtlInfReq.deleter
		def AcctAddtlInfReq(self):
			del self._AcctAddtlInfReq
			self._AcctAddtlInfReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctAddtlInfReq', type=AccountAdditionalInformationRequestV04, min=1, max=1, mutex_group=None, array=False),
		))

