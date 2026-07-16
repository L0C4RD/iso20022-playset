# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection6

class TotalValueInPageAndStatement2(base_types._BaseFieldType):

	__slots__ = ["_TtlBookValOfStmt", "_TtlHldgsValOfPg", "_TtlHldgsValOfStmt"]
	@property
	def TtlBookValOfStmt(self):
		return self._TtlBookValOfStmt

	@TtlBookValOfStmt.setter
	def TtlBookValOfStmt(self, value):
		self._TtlBookValOfStmt = value if value is not None else base_types.UninitialisedField(self, 'TtlBookValOfStmt', AmountAndDirection6, False)

	@TtlBookValOfStmt.deleter
	def TtlBookValOfStmt(self):
		del self._TtlBookValOfStmt
		self._TtlBookValOfStmt = base_types.UninitialisedField(self, 'TtlBookValOfStmt', AmountAndDirection6, False)

	@property
	def TtlHldgsValOfPg(self):
		return self._TtlHldgsValOfPg

	@TtlHldgsValOfPg.setter
	def TtlHldgsValOfPg(self, value):
		self._TtlHldgsValOfPg = value if value is not None else base_types.UninitialisedField(self, 'TtlHldgsValOfPg', AmountAndDirection6, False)

	@TtlHldgsValOfPg.deleter
	def TtlHldgsValOfPg(self):
		del self._TtlHldgsValOfPg
		self._TtlHldgsValOfPg = base_types.UninitialisedField(self, 'TtlHldgsValOfPg', AmountAndDirection6, False)

	@property
	def TtlHldgsValOfStmt(self):
		return self._TtlHldgsValOfStmt

	@TtlHldgsValOfStmt.setter
	def TtlHldgsValOfStmt(self, value):
		self._TtlHldgsValOfStmt = value if value is not None else base_types.UninitialisedField(self, 'TtlHldgsValOfStmt', AmountAndDirection6, False)

	@TtlHldgsValOfStmt.deleter
	def TtlHldgsValOfStmt(self):
		del self._TtlHldgsValOfStmt
		self._TtlHldgsValOfStmt = base_types.UninitialisedField(self, 'TtlHldgsValOfStmt', AmountAndDirection6, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='TtlBookValOfStmt', type=AmountAndDirection6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlHldgsValOfPg', type=AmountAndDirection6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlHldgsValOfStmt', type=AmountAndDirection6, min=1, max=1, mutex_group=None, array=False),
	))