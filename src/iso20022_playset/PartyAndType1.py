import base_types
import PartyType1Choice
import PartyIdentification43

class PartyAndType1(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_Pty"]
	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

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
		base_types.FieldEntry(name='Tp', type=PartyType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pty', type=PartyIdentification43, min=0, max=1, mutex_group=None, array=False),
	))

