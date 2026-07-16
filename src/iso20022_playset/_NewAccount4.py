# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CashAccount43
from . import IndividualPerson44
from . import Organisation43

class NewAccount4(base_types._BaseFieldType):

	__slots__ = ["_Acct", "_AcctPty", "_Org"]
	@property
	def Acct(self):
		return self._Acct

	@Acct.setter
	def Acct(self, value):
		self._Acct = value if value is not None else base_types.UninitialisedField(self, 'Acct', CashAccount43, False)

	@Acct.deleter
	def Acct(self):
		del self._Acct
		self._Acct = base_types.UninitialisedField(self, 'Acct', CashAccount43, False)

	@property
	def AcctPty(self):
		return self._AcctPty

	@AcctPty.setter
	def AcctPty(self, value):
		self._AcctPty = value if value is not None else base_types.UninitialisedField(self, 'AcctPty', IndividualPerson44, True)

	@AcctPty.deleter
	def AcctPty(self):
		del self._AcctPty
		self._AcctPty = base_types.UninitialisedField(self, 'AcctPty', IndividualPerson44, True)

	@property
	def Org(self):
		return self._Org

	@Org.setter
	def Org(self, value):
		self._Org = value if value is not None else base_types.UninitialisedField(self, 'Org', Organisation43, False)

	@Org.deleter
	def Org(self):
		del self._Org
		self._Org = base_types.UninitialisedField(self, 'Org', Organisation43, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Acct', type=CashAccount43, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctPty', type=IndividualPerson44, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Org', type=Organisation43, min=0, max=1, mutex_group=None, array=False),
	))