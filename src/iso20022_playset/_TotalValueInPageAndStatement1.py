from . import base_types
from .AmountAndDirection6 import AmountAndDirection6

class TotalValueInPageAndStatement1(base_types._BaseFieldType):

	__slots__ = ["_TtlBookValOfStmt", "_TtlHldgsValOfStmt", "_TtlElgblCollVal", "_TtlHldgsValOfPg"]
	@property
	def TtlBookValOfStmt(self):
		return self._TtlBookValOfStmt

	@TtlBookValOfStmt.setter
	def TtlBookValOfStmt(self, value):
		self._TtlBookValOfStmt = value if type(value) != base_types.auto else self.make_default("TtlBookValOfStmt")

	@TtlBookValOfStmt.deleter
	def TtlBookValOfStmt(self):
		del self._TtlBookValOfStmt
		self._TtlBookValOfStmt = None

	@property
	def TtlHldgsValOfStmt(self):
		return self._TtlHldgsValOfStmt

	@TtlHldgsValOfStmt.setter
	def TtlHldgsValOfStmt(self, value):
		self._TtlHldgsValOfStmt = value if type(value) != base_types.auto else self.make_default("TtlHldgsValOfStmt")

	@TtlHldgsValOfStmt.deleter
	def TtlHldgsValOfStmt(self):
		del self._TtlHldgsValOfStmt
		self._TtlHldgsValOfStmt = None

	@property
	def TtlElgblCollVal(self):
		return self._TtlElgblCollVal

	@TtlElgblCollVal.setter
	def TtlElgblCollVal(self, value):
		self._TtlElgblCollVal = value if type(value) != base_types.auto else self.make_default("TtlElgblCollVal")

	@TtlElgblCollVal.deleter
	def TtlElgblCollVal(self):
		del self._TtlElgblCollVal
		self._TtlElgblCollVal = None

	@property
	def TtlHldgsValOfPg(self):
		return self._TtlHldgsValOfPg

	@TtlHldgsValOfPg.setter
	def TtlHldgsValOfPg(self, value):
		self._TtlHldgsValOfPg = value if type(value) != base_types.auto else self.make_default("TtlHldgsValOfPg")

	@TtlHldgsValOfPg.deleter
	def TtlHldgsValOfPg(self):
		del self._TtlHldgsValOfPg
		self._TtlHldgsValOfPg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TtlBookValOfStmt', type=AmountAndDirection6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlHldgsValOfStmt', type=AmountAndDirection6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlElgblCollVal', type=AmountAndDirection6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlHldgsValOfPg', type=AmountAndDirection6, min=0, max=1, mutex_group=None, array=False),
	))

