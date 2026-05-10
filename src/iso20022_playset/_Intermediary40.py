from . import base_types
from ._Account22 import Account22
from ._InvestmentFundRole2Choice import InvestmentFundRole2Choice
from ._OrderOriginatorEligibility1Code import OrderOriginatorEligibility1Code
from ._PartyIdentification113 import PartyIdentification113

class Intermediary40(base_types._BaseFieldType):

	__slots__ = ["_Acct", "_Id", "_OrdrOrgtrElgblty", "_Role"]
	@property
	def Acct(self):
		return self._Acct

	@Acct.setter
	def Acct(self, value):
		self._Acct = value if type(value) != base_types.auto else self.make_default("Acct")

	@Acct.deleter
	def Acct(self):
		del self._Acct
		self._Acct = None

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
	def OrdrOrgtrElgblty(self):
		return self._OrdrOrgtrElgblty

	@OrdrOrgtrElgblty.setter
	def OrdrOrgtrElgblty(self, value):
		self._OrdrOrgtrElgblty = value if type(value) != base_types.auto else self.make_default("OrdrOrgtrElgblty")

	@OrdrOrgtrElgblty.deleter
	def OrdrOrgtrElgblty(self):
		del self._OrdrOrgtrElgblty
		self._OrdrOrgtrElgblty = None

	@property
	def Role(self):
		return self._Role

	@Role.setter
	def Role(self, value):
		self._Role = value if type(value) != base_types.auto else self.make_default("Role")

	@Role.deleter
	def Role(self):
		del self._Role
		self._Role = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Acct', type=Account22, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=PartyIdentification113, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrOrgtrElgblty', type=OrderOriginatorEligibility1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Role', type=InvestmentFundRole2Choice, min=0, max=1, mutex_group=None, array=False),
	))

