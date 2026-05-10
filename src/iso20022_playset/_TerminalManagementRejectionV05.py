from . import base_types
from ._TMSHeader1 import TMSHeader1
from ._AcceptorRejection3 import AcceptorRejection3

class TerminalManagementRejectionV05(base_types._BaseFieldType):

	__slots__ = ["_Hdr", "_Rjct"]
	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if type(value) != base_types.auto else self.make_default("Hdr")

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = None

	@property
	def Rjct(self):
		return self._Rjct

	@Rjct.setter
	def Rjct(self, value):
		self._Rjct = value if type(value) != base_types.auto else self.make_default("Rjct")

	@Rjct.deleter
	def Rjct(self):
		del self._Rjct
		self._Rjct = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Hdr', type=TMSHeader1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rjct', type=AcceptorRejection3, min=1, max=1, mutex_group=None, array=False),
	))

