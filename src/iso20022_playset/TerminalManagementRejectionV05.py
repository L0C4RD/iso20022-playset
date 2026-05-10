import base_types
import AcceptorRejection3
import TMSHeader1

class TerminalManagementRejectionV05(base_types._BaseFieldType):

	__slots__ = ["_Rjct", "_Hdr"]
	@property
	def Rjct(self):
		return self._Rjct

	@Rjct.setter
	def Rjct(self, value):
		self._Rjct = value if type(value) != auto else self.make_default("Rjct")

	@Rjct.deleter
	def Rjct(self):
		del self._Rjct
		self._Rjct = None

	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if type(value) != auto else self.make_default("Hdr")

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rjct', type=AcceptorRejection3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=TMSHeader1, min=1, max=1, mutex_group=None, array=False),
	))

