from . import base_types
from ._CreditTransferTransaction59 import CreditTransferTransaction59

class SettlementMethod5Choice(base_types._BaseFieldType):

	__slots__ = ["_Dbt", "_Cdt"]
	@property
	def Dbt(self):
		return self._Dbt

	@Dbt.setter
	def Dbt(self, value):
		self._Dbt = value if type(value) != base_types.auto else self.make_default("Dbt")

	@Dbt.deleter
	def Dbt(self):
		del self._Dbt
		self._Dbt = None

	@property
	def Cdt(self):
		return self._Cdt

	@Cdt.setter
	def Cdt(self, value):
		self._Cdt = value if type(value) != base_types.auto else self.make_default("Cdt")

	@Cdt.deleter
	def Cdt(self):
		del self._Cdt
		self._Cdt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dbt', type=CreditTransferTransaction59, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Cdt', type=CreditTransferTransaction59, min=0, max=1, mutex_group=1, array=False),
	))

