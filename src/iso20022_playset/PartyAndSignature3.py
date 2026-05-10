from . import base_types
import PartyIdentification135
import SkipPayload

class PartyAndSignature3(base_types._BaseFieldType):

	__slots__ = ["_Pty", "_Sgntr"]
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
	def Sgntr(self):
		return self._Sgntr

	@Sgntr.setter
	def Sgntr(self, value):
		self._Sgntr = value if type(value) != auto else self.make_default("Sgntr")

	@Sgntr.deleter
	def Sgntr(self):
		del self._Sgntr
		self._Sgntr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Pty', type=PartyIdentification135, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sgntr', type=SkipPayload, min=1, max=1, mutex_group=None, array=False),
	))

