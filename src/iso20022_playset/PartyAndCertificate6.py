import base_types
import Max10KBinary
import PartyIdentification272

class PartyAndCertificate6(base_types._BaseFieldType):

	__slots__ = ["_Pty", "_Cert"]
	@property
	def Pty(self):
		return self._Pty

	@Pty.setter
	def Pty(self, value):
		self._Pty = value if type(value) != auto else self.make_default("Pty")

	@Pty.deleter
	def Pty(self):
		del self._Pty
		self._Pty = None

	@property
	def Cert(self):
		return self._Cert

	@Cert.setter
	def Cert(self, value):
		self._Cert = value if type(value) != auto else self.make_default("Cert")

	@Cert.deleter
	def Cert(self):
		del self._Cert
		self._Cert = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Pty', type=PartyIdentification272, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cert', type=Max10KBinary, min=0, max=1, mutex_group=None, array=False),
	))

