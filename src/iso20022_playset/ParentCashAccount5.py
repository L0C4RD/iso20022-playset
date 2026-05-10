from . import base_types
import CashAccount40
import AccountLevel1Code
import BranchAndFinancialInstitutionIdentification8

class ParentCashAccount5(base_types._BaseFieldType):

	__slots__ = ["_Lvl", "_Id", "_Svcr"]
	@property
	def Lvl(self):
		return self._Lvl

	@Lvl.setter
	def Lvl(self, value):
		self._Lvl = value if type(value) != auto else self.make_default("Lvl")

	@Lvl.deleter
	def Lvl(self):
		del self._Lvl
		self._Lvl = None

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
	def Svcr(self):
		return self._Svcr

	@Svcr.setter
	def Svcr(self, value):
		self._Svcr = value if type(value) != auto else self.make_default("Svcr")

	@Svcr.deleter
	def Svcr(self):
		del self._Svcr
		self._Svcr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Lvl', type=AccountLevel1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=CashAccount40, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Svcr', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
	))

