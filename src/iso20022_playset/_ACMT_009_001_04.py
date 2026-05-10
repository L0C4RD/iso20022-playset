from . import base_types
from ._AccountOpeningAdditionalInformationRequestV04 import AccountOpeningAdditionalInformationRequestV04

class ACMT_009_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AcctOpngAddtlInfReq"]
		@property
		def AcctOpngAddtlInfReq(self):
			return self._AcctOpngAddtlInfReq

		@AcctOpngAddtlInfReq.setter
		def AcctOpngAddtlInfReq(self, value):
			self._AcctOpngAddtlInfReq = value if type(value) != base_types.auto else self.make_default("AcctOpngAddtlInfReq")

		@AcctOpngAddtlInfReq.deleter
		def AcctOpngAddtlInfReq(self):
			del self._AcctOpngAddtlInfReq
			self._AcctOpngAddtlInfReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctOpngAddtlInfReq', type=AccountOpeningAdditionalInformationRequestV04, min=1, max=1, mutex_group=None, array=False),
		))

