from . import base_types
from ._SecuritiesAccountDeletionRequestV01 import SecuritiesAccountDeletionRequestV01

class REDA_032_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesAcctDeltnReq"]
		@property
		def SctiesAcctDeltnReq(self):
			return self._SctiesAcctDeltnReq

		@SctiesAcctDeltnReq.setter
		def SctiesAcctDeltnReq(self, value):
			self._SctiesAcctDeltnReq = value if type(value) != base_types.auto else self.make_default("SctiesAcctDeltnReq")

		@SctiesAcctDeltnReq.deleter
		def SctiesAcctDeltnReq(self):
			del self._SctiesAcctDeltnReq
			self._SctiesAcctDeltnReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesAcctDeltnReq', type=SecuritiesAccountDeletionRequestV01, min=1, max=1, mutex_group=None, array=False),
		))

