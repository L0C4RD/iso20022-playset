from . import base_types
from .SecuritiesAccountCreationRequestV01 import SecuritiesAccountCreationRequestV01

class REDA_018_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesAcctCreReq"]
		@property
		def SctiesAcctCreReq(self):
			return self._SctiesAcctCreReq

		@SctiesAcctCreReq.setter
		def SctiesAcctCreReq(self, value):
			self._SctiesAcctCreReq = value if type(value) != auto else self.make_default("SctiesAcctCreReq")

		@SctiesAcctCreReq.deleter
		def SctiesAcctCreReq(self):
			del self._SctiesAcctCreReq
			self._SctiesAcctCreReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesAcctCreReq', type=SecuritiesAccountCreationRequestV01, min=1, max=1, mutex_group=None, array=False),
		))

