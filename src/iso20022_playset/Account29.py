import base_types
import PartyIdentification120Choice
import AccountIdentification26

class Account29(base_types._BaseFieldType):

	__slots__ = ["_AcctSvcr", "_Id"]
	@property
	def AcctSvcr(self):
		return self._AcctSvcr

	@AcctSvcr.setter
	def AcctSvcr(self, value):
		self._AcctSvcr = value if type(value) != auto else self.make_default("AcctSvcr")

	@AcctSvcr.deleter
	def AcctSvcr(self):
		del self._AcctSvcr
		self._AcctSvcr = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctSvcr', type=PartyIdentification120Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=AccountIdentification26, min=1, max=1, mutex_group=None, array=False),
	))

