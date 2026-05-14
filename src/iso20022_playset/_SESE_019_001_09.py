from . import base_types
from ._AccountHoldingInformationRequestV09 import AccountHoldingInformationRequestV09

class SESE_019_001_09():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AcctHldgInfReq"]
		@property
		def AcctHldgInfReq(self):
			return self._AcctHldgInfReq

		@AcctHldgInfReq.setter
		def AcctHldgInfReq(self, value):
			self._AcctHldgInfReq = value if type(value) != base_types.auto else self.make_default("AcctHldgInfReq")

		@AcctHldgInfReq.deleter
		def AcctHldgInfReq(self):
			del self._AcctHldgInfReq
			self._AcctHldgInfReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctHldgInfReq', type=AccountHoldingInformationRequestV09, min=1, max=1, mutex_group=None, array=False),
		))

