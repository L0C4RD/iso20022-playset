from . import base_types
from ._Max35Text import Max35Text
from ._BranchAndFinancialInstitutionIdentification8 import BranchAndFinancialInstitutionIdentification8

class ProprietaryAgent5(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_Agt"]
	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def Agt(self):
		return self._Agt

	@Agt.setter
	def Agt(self, value):
		self._Agt = value if type(value) != base_types.auto else self.make_default("Agt")

	@Agt.deleter
	def Agt(self):
		del self._Agt
		self._Agt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tp', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Agt', type=BranchAndFinancialInstitutionIdentification8, min=1, max=1, mutex_group=None, array=False),
	))

