from . import base_types
from ._SegregatedIndependentAmountDispute2 import SegregatedIndependentAmountDispute2
from ._VariationMarginDispute1 import VariationMarginDispute1

class DisputeNotification2(base_types._BaseFieldType):

	__slots__ = ["_SgrtdIndpdntAmtDspt", "_VartnMrgnDspt"]
	@property
	def SgrtdIndpdntAmtDspt(self):
		return self._SgrtdIndpdntAmtDspt

	@SgrtdIndpdntAmtDspt.setter
	def SgrtdIndpdntAmtDspt(self, value):
		self._SgrtdIndpdntAmtDspt = value if type(value) != base_types.auto else self.make_default("SgrtdIndpdntAmtDspt")

	@SgrtdIndpdntAmtDspt.deleter
	def SgrtdIndpdntAmtDspt(self):
		del self._SgrtdIndpdntAmtDspt
		self._SgrtdIndpdntAmtDspt = None

	@property
	def VartnMrgnDspt(self):
		return self._VartnMrgnDspt

	@VartnMrgnDspt.setter
	def VartnMrgnDspt(self, value):
		self._VartnMrgnDspt = value if type(value) != base_types.auto else self.make_default("VartnMrgnDspt")

	@VartnMrgnDspt.deleter
	def VartnMrgnDspt(self):
		del self._VartnMrgnDspt
		self._VartnMrgnDspt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SgrtdIndpdntAmtDspt', type=SegregatedIndependentAmountDispute2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VartnMrgnDspt', type=VariationMarginDispute1, min=1, max=1, mutex_group=None, array=False),
	))

