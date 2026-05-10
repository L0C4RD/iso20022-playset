from . import base_types
from .SecuritiesAccountModificationRequestV01 import SecuritiesAccountModificationRequestV01

class REDA_023_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesAcctModReq"]
		@property
		def SctiesAcctModReq(self):
			return self._SctiesAcctModReq

		@SctiesAcctModReq.setter
		def SctiesAcctModReq(self, value):
			self._SctiesAcctModReq = value if type(value) != base_types.auto else self.make_default("SctiesAcctModReq")

		@SctiesAcctModReq.deleter
		def SctiesAcctModReq(self):
			del self._SctiesAcctModReq
			self._SctiesAcctModReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesAcctModReq', type=SecuritiesAccountModificationRequestV01, min=1, max=1, mutex_group=None, array=False),
		))

