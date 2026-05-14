from . import base_types
from ._AuthorisationResponseV05 import AuthorisationResponseV05

class CAIN_002_001_05():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AuthstnRspn"]
		@property
		def AuthstnRspn(self):
			return self._AuthstnRspn

		@AuthstnRspn.setter
		def AuthstnRspn(self, value):
			self._AuthstnRspn = value if type(value) != base_types.auto else self.make_default("AuthstnRspn")

		@AuthstnRspn.deleter
		def AuthstnRspn(self):
			del self._AuthstnRspn
			self._AuthstnRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AuthstnRspn', type=AuthorisationResponseV05, min=1, max=1, mutex_group=None, array=False),
		))

