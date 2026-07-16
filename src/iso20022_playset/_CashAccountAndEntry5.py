# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CashAccount43
from . import CashEntry2

class CashAccountAndEntry5(base_types._BaseFieldType):

	__slots__ = ["_Acct", "_Ntry"]
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
	def Ntry(self):
		return self._Ntry

	@Ntry.setter
	def Ntry(self, value):
		self._Ntry = value if value is not None else base_types.UninitialisedField(self, 'Ntry', CashEntry2, False)

	@Ntry.deleter
	def Ntry(self):
		del self._Ntry
		self._Ntry = base_types.UninitialisedField(self, 'Ntry', CashEntry2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Acct', type=CashAccount43, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ntry', type=CashEntry2, min=0, max=1, mutex_group=None, array=False),
	))