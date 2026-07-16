# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Account7
from . import Extended350Code
from . import InvestmentFundRole2Code
from . import PartyIdentification2Choice

class Intermediary11(base_types._BaseFieldType):

	__slots__ = ["_Acct", "_Id", "_Role", "_XtndedRole"]
	@property
	def Acct(self):
		return self._Acct

	@Acct.setter
	def Acct(self, value):
		self._Acct = value if value is not None else base_types.UninitialisedField(self, 'Acct', Account7, False)

	@Acct.deleter
	def Acct(self):
		del self._Acct
		self._Acct = base_types.UninitialisedField(self, 'Acct', Account7, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', PartyIdentification2Choice, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', PartyIdentification2Choice, False)

	@property
	def Role(self):
		return self._Role

	@Role.setter
	def Role(self, value):
		self._Role = value if value is not None else base_types.UninitialisedField(self, 'Role', InvestmentFundRole2Code, False)

	@Role.deleter
	def Role(self):
		del self._Role
		self._Role = base_types.UninitialisedField(self, 'Role', InvestmentFundRole2Code, False)

	@property
	def XtndedRole(self):
		return self._XtndedRole

	@XtndedRole.setter
	def XtndedRole(self, value):
		self._XtndedRole = value if value is not None else base_types.UninitialisedField(self, 'XtndedRole', Extended350Code, False)

	@XtndedRole.deleter
	def XtndedRole(self):
		del self._XtndedRole
		self._XtndedRole = base_types.UninitialisedField(self, 'XtndedRole', Extended350Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Acct', type=Account7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=PartyIdentification2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Role', type=InvestmentFundRole2Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='XtndedRole', type=Extended350Code, min=0, max=1, mutex_group=1, array=False),
	))