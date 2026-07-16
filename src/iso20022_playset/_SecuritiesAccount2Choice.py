# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesAccount19
from . import SecuritiesAccountRange2

class SecuritiesAccount2Choice(base_types._BaseFieldType):

	__slots__ = ["_Acct", "_Rg"]
	@property
	def Acct(self):
		return self._Acct

	@Acct.setter
	def Acct(self, value):
		self._Acct = value if value is not None else base_types.UninitialisedField(self, 'Acct', SecuritiesAccount19, True)

	@Acct.deleter
	def Acct(self):
		del self._Acct
		self._Acct = base_types.UninitialisedField(self, 'Acct', SecuritiesAccount19, True)

	@property
	def Rg(self):
		return self._Rg

	@Rg.setter
	def Rg(self, value):
		self._Rg = value if value is not None else base_types.UninitialisedField(self, 'Rg', SecuritiesAccountRange2, False)

	@Rg.deleter
	def Rg(self):
		del self._Rg
		self._Rg = base_types.UninitialisedField(self, 'Rg', SecuritiesAccountRange2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Acct', type=SecuritiesAccount19, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='Rg', type=SecuritiesAccountRange2, min=0, max=1, mutex_group=1, array=False),
	))