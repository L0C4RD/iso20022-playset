from . import base_types
from .PartyIdentification238 import PartyIdentification238
from .PartyIdentification221 import PartyIdentification221

class PartyIdentification232Choice(base_types._BaseFieldType):

	__slots__ = ["_NtrlPrsn", "_LglPrsn"]
	@property
	def NtrlPrsn(self):
		return self._NtrlPrsn

	@NtrlPrsn.setter
	def NtrlPrsn(self, value):
		self._NtrlPrsn = value if type(value) != auto else self.make_default("NtrlPrsn")

	@NtrlPrsn.deleter
	def NtrlPrsn(self):
		del self._NtrlPrsn
		self._NtrlPrsn = None

	@property
	def LglPrsn(self):
		return self._LglPrsn

	@LglPrsn.setter
	def LglPrsn(self, value):
		self._LglPrsn = value if type(value) != auto else self.make_default("LglPrsn")

	@LglPrsn.deleter
	def LglPrsn(self):
		del self._LglPrsn
		self._LglPrsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NtrlPrsn', type=PartyIdentification238, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='LglPrsn', type=PartyIdentification221, min=0, max=1, mutex_group=1, array=False),
	))

