# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import LEIIdentifier
from . import PaymentAccount4

class SettlementAgent2(base_types._BaseFieldType):

	__slots__ = ["_Acct", "_Id"]
	@property
	def Acct(self):
		return self._Acct

	@Acct.setter
	def Acct(self, value):
		self._Acct = value if value is not None else base_types.UninitialisedField(self, 'Acct', PaymentAccount4, True)

	@Acct.deleter
	def Acct(self):
		del self._Acct
		self._Acct = base_types.UninitialisedField(self, 'Acct', PaymentAccount4, True)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', LEIIdentifier, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', LEIIdentifier, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Acct', type=PaymentAccount4, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Id', type=LEIIdentifier, min=1, max=1, mutex_group=None, array=False),
	))