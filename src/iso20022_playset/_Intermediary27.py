# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Account7
from . import PartyIdentification2Choice
from . import Role4Choice

class Intermediary27(base_types._BaseFieldType):

	__slots__ = ["_Acct", "_Id", "_Role"]
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
		self._Role = value if value is not None else base_types.UninitialisedField(self, 'Role', Role4Choice, False)

	@Role.deleter
	def Role(self):
		del self._Role
		self._Role = base_types.UninitialisedField(self, 'Role', Role4Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Acct', type=Account7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=PartyIdentification2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Role', type=Role4Choice, min=0, max=1, mutex_group=None, array=False),
	))