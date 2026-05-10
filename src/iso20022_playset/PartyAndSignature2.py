from . import base_types
import PartyIdentification43
import ProprietaryData3

class PartyAndSignature2(base_types._BaseFieldType):

	__slots__ = ["_Sgntr", "_Pty"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Sgntr', type=ProprietaryData3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pty', type=PartyIdentification43, min=1, max=1, mutex_group=None, array=False),
	))

