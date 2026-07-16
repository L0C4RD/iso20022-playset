# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountLevel1Code
from . import BranchAndFinancialInstitutionIdentification8
from . import CashAccount40

class ParentCashAccount5(base_types._BaseFieldType):

	__slots__ = ["_Id", "_Lvl", "_Svcr"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', CashAccount40, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', CashAccount40, False)

	@property
	def Lvl(self):
		return self._Lvl

	@Lvl.setter
	def Lvl(self, value):
		self._Lvl = value if value is not None else base_types.UninitialisedField(self, 'Lvl', AccountLevel1Code, False)

	@Lvl.deleter
	def Lvl(self):
		del self._Lvl
		self._Lvl = base_types.UninitialisedField(self, 'Lvl', AccountLevel1Code, False)

	@property
	def Svcr(self):
		return self._Svcr

	@Svcr.setter
	def Svcr(self, value):
		self._Svcr = value if value is not None else base_types.UninitialisedField(self, 'Svcr', BranchAndFinancialInstitutionIdentification8, False)

	@Svcr.deleter
	def Svcr(self):
		del self._Svcr
		self._Svcr = base_types.UninitialisedField(self, 'Svcr', BranchAndFinancialInstitutionIdentification8, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=CashAccount40, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lvl', type=AccountLevel1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Svcr', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
	))