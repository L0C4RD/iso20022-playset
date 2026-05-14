# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AccountIdentification5 import AccountIdentification5
from ._FinancialAssetBalanceType1Code import FinancialAssetBalanceType1Code
from ._GenericIdentification30 import GenericIdentification30

class BalanceType7Choice(base_types._BaseFieldType):

	__slots__ = ["_Acct", "_Cd", "_Prtry"]
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
	def Cd(self):
		return self._Cd

	@Cd.setter
	def Cd(self, value):
		self._Cd = value if type(value) != base_types.auto else self.make_default("Cd")

	@Cd.deleter
	def Cd(self):
		del self._Cd
		self._Cd = None

	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if type(value) != base_types.auto else self.make_default("Prtry")

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Acct', type=AccountIdentification5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Cd', type=FinancialAssetBalanceType1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=GenericIdentification30, min=0, max=1, mutex_group=1, array=False),
	))