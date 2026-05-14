from . import base_types
from ._AuthorisationInitiationV05 import AuthorisationInitiationV05

class CAIN_001_001_05():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AuthstnInitn"]
		@property
		def AuthstnInitn(self):
			return self._AuthstnInitn

		@AuthstnInitn.setter
		def AuthstnInitn(self, value):
			self._AuthstnInitn = value if type(value) != base_types.auto else self.make_default("AuthstnInitn")

		@AuthstnInitn.deleter
		def AuthstnInitn(self):
			del self._AuthstnInitn
			self._AuthstnInitn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AuthstnInitn', type=AuthorisationInitiationV05, min=1, max=1, mutex_group=None, array=False),
		))

