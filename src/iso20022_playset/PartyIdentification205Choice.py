from . import base_types
from .PartyIdentification202 import PartyIdentification202
from .PartyIdentification201 import PartyIdentification201

class PartyIdentification205Choice(base_types._BaseFieldType):

	__slots__ = ["_LglPrsn", "_NtrlPrsn"]
	@property
	def LglPrsn(self):
		return self._LglPrsn

	@LglPrsn.setter
	def LglPrsn(self, value):
		self._LglPrsn = value if type(value) != base_types.auto else self.make_default("LglPrsn")

	@LglPrsn.deleter
	def LglPrsn(self):
		del self._LglPrsn
		self._LglPrsn = None

	@property
	def NtrlPrsn(self):
		return self._NtrlPrsn

	@NtrlPrsn.setter
	def NtrlPrsn(self, value):
		self._NtrlPrsn = value if type(value) != base_types.auto else self.make_default("NtrlPrsn")

	@NtrlPrsn.deleter
	def NtrlPrsn(self):
		del self._NtrlPrsn
		self._NtrlPrsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LglPrsn', type=PartyIdentification201, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NtrlPrsn', type=PartyIdentification202, min=0, max=1, mutex_group=1, array=False),
	))

