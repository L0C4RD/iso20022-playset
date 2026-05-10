from . import base_types
import InvestmentFundRole2Code
import Extended350Code
import PartyIdentification2Choice
import Account7

class Intermediary11(base_types._BaseFieldType):

	__slots__ = ["_Acct", "_Id", "_XtndedRole", "_Role"]
	@property
	def Acct(self):
		return self._Acct

	@Acct.setter
	def Acct(self, value):
		self._Acct = value if type(value) != auto else self.make_default("Acct")

	@Acct.deleter
	def Acct(self):
		del self._Acct
		self._Acct = None

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

	@property
	def XtndedRole(self):
		return self._XtndedRole

	@XtndedRole.setter
	def XtndedRole(self, value):
		self._XtndedRole = value if type(value) != auto else self.make_default("XtndedRole")

	@XtndedRole.deleter
	def XtndedRole(self):
		del self._XtndedRole
		self._XtndedRole = None

	@property
	def Role(self):
		return self._Role

	@Role.setter
	def Role(self, value):
		self._Role = value if type(value) != auto else self.make_default("Role")

	@Role.deleter
	def Role(self):
		del self._Role
		self._Role = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Acct', type=Account7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=PartyIdentification2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XtndedRole', type=Extended350Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Role', type=InvestmentFundRole2Code, min=0, max=1, mutex_group=1, array=False),
	))

