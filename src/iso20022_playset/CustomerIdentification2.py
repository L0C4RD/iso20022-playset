from . import base_types
from .PartyIdentification272 import PartyIdentification272
from .AuthorityInvestigation2 import AuthorityInvestigation2

class CustomerIdentification2(base_types._BaseFieldType):

	__slots__ = ["_Pty", "_AuthrtyReq"]
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
	def AuthrtyReq(self):
		return self._AuthrtyReq

	@AuthrtyReq.setter
	def AuthrtyReq(self, value):
		self._AuthrtyReq = value if type(value) != auto else self.make_default("AuthrtyReq")

	@AuthrtyReq.deleter
	def AuthrtyReq(self):
		del self._AuthrtyReq
		self._AuthrtyReq = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Pty', type=PartyIdentification272, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthrtyReq', type=AuthorityInvestigation2, min=1, max=None, mutex_group=None, array=True),
	))

