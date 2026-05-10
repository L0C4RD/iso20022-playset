from . import base_types
from ._InvestigatedParties1Choice import InvestigatedParties1Choice
from ._CashAccount43 import CashAccount43
from ._AuthorityRequestType1 import AuthorityRequestType1

class AccountAndParties3(base_types._BaseFieldType):

	__slots__ = ["_InvstgtdPties", "_AuthrtyReqTp", "_Id"]
	@property
	def AuthrtyReqTp(self):
		return self._AuthrtyReqTp

	@AuthrtyReqTp.setter
	def AuthrtyReqTp(self, value):
		self._AuthrtyReqTp = value if type(value) != base_types.auto else self.make_default("AuthrtyReqTp")

	@AuthrtyReqTp.deleter
	def AuthrtyReqTp(self):
		del self._AuthrtyReqTp
		self._AuthrtyReqTp = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def InvstgtdPties(self):
		return self._InvstgtdPties

	@InvstgtdPties.setter
	def InvstgtdPties(self, value):
		self._InvstgtdPties = value if type(value) != base_types.auto else self.make_default("InvstgtdPties")

	@InvstgtdPties.deleter
	def InvstgtdPties(self):
		del self._InvstgtdPties
		self._InvstgtdPties = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AuthrtyReqTp', type=AuthorityRequestType1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Id', type=CashAccount43, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstgtdPties', type=InvestigatedParties1Choice, min=1, max=1, mutex_group=None, array=False),
	))

