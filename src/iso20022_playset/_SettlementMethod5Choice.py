# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CreditTransferTransaction59

class SettlementMethod5Choice(base_types._BaseFieldType):

	__slots__ = ["_Cdt", "_Dbt"]
	@property
	def Cdt(self):
		return self._Cdt

	@Cdt.setter
	def Cdt(self, value):
		self._Cdt = value if value is not None else base_types.UninitialisedField(self, 'Cdt', CreditTransferTransaction59, False)

	@Cdt.deleter
	def Cdt(self):
		del self._Cdt
		self._Cdt = base_types.UninitialisedField(self, 'Cdt', CreditTransferTransaction59, False)

	@property
	def Dbt(self):
		return self._Dbt

	@Dbt.setter
	def Dbt(self, value):
		self._Dbt = value if value is not None else base_types.UninitialisedField(self, 'Dbt', CreditTransferTransaction59, False)

	@Dbt.deleter
	def Dbt(self):
		del self._Dbt
		self._Dbt = base_types.UninitialisedField(self, 'Dbt', CreditTransferTransaction59, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cdt', type=CreditTransferTransaction59, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Dbt', type=CreditTransferTransaction59, min=0, max=1, mutex_group=1, array=False),
	))