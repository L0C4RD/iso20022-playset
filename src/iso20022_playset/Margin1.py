from . import base_types
from .SegregatedIndependentAmountMargin1 import SegregatedIndependentAmountMargin1
from .VariationMargin1 import VariationMargin1

class Margin1(base_types._BaseFieldType):

	__slots__ = ["_SgrtdIndpdntAmtMrgn", "_VartnMrgn"]
	@property
	def SgrtdIndpdntAmtMrgn(self):
		return self._SgrtdIndpdntAmtMrgn

	@SgrtdIndpdntAmtMrgn.setter
	def SgrtdIndpdntAmtMrgn(self, value):
		self._SgrtdIndpdntAmtMrgn = value if type(value) != auto else self.make_default("SgrtdIndpdntAmtMrgn")

	@SgrtdIndpdntAmtMrgn.deleter
	def SgrtdIndpdntAmtMrgn(self):
		del self._SgrtdIndpdntAmtMrgn
		self._SgrtdIndpdntAmtMrgn = None

	@property
	def VartnMrgn(self):
		return self._VartnMrgn

	@VartnMrgn.setter
	def VartnMrgn(self, value):
		self._VartnMrgn = value if type(value) != auto else self.make_default("VartnMrgn")

	@VartnMrgn.deleter
	def VartnMrgn(self):
		del self._VartnMrgn
		self._VartnMrgn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SgrtdIndpdntAmtMrgn', type=SegregatedIndependentAmountMargin1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VartnMrgn', type=VariationMargin1, min=1, max=1, mutex_group=None, array=False),
	))

