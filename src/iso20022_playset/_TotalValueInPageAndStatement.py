# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount

class TotalValueInPageAndStatement(base_types._BaseFieldType):

	__slots__ = ["_TtlHldgsValOfPg", "_TtlHldgsValOfStmt"]
	@property
	def TtlHldgsValOfPg(self):
		return self._TtlHldgsValOfPg

	@TtlHldgsValOfPg.setter
	def TtlHldgsValOfPg(self, value):
		self._TtlHldgsValOfPg = value if value is not None else base_types.UninitialisedField(self, 'TtlHldgsValOfPg', ActiveCurrencyAndAmount, False)

	@TtlHldgsValOfPg.deleter
	def TtlHldgsValOfPg(self):
		del self._TtlHldgsValOfPg
		self._TtlHldgsValOfPg = base_types.UninitialisedField(self, 'TtlHldgsValOfPg', ActiveCurrencyAndAmount, False)

	@property
	def TtlHldgsValOfStmt(self):
		return self._TtlHldgsValOfStmt

	@TtlHldgsValOfStmt.setter
	def TtlHldgsValOfStmt(self, value):
		self._TtlHldgsValOfStmt = value if value is not None else base_types.UninitialisedField(self, 'TtlHldgsValOfStmt', ActiveCurrencyAndAmount, False)

	@TtlHldgsValOfStmt.deleter
	def TtlHldgsValOfStmt(self):
		del self._TtlHldgsValOfStmt
		self._TtlHldgsValOfStmt = base_types.UninitialisedField(self, 'TtlHldgsValOfStmt', ActiveCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='TtlHldgsValOfPg', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlHldgsValOfStmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))