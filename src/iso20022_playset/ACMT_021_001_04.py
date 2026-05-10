from . import base_types
from .AccountClosingAdditionalInformationRequestV04 import AccountClosingAdditionalInformationRequestV04

class ACMT_021_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AcctClsgAddtlInfReq"]
		@property
		def AcctClsgAddtlInfReq(self):
			return self._AcctClsgAddtlInfReq

		@AcctClsgAddtlInfReq.setter
		def AcctClsgAddtlInfReq(self, value):
			self._AcctClsgAddtlInfReq = value if type(value) != base_types.auto else self.make_default("AcctClsgAddtlInfReq")

		@AcctClsgAddtlInfReq.deleter
		def AcctClsgAddtlInfReq(self):
			del self._AcctClsgAddtlInfReq
			self._AcctClsgAddtlInfReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctClsgAddtlInfReq', type=AccountClosingAdditionalInformationRequestV04, min=1, max=1, mutex_group=None, array=False),
		))

