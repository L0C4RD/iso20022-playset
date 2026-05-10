from . import base_types
from .SegregatedIndependentAmountMargin1 import SegregatedIndependentAmountMargin1
from .Margin1 import Margin1

class MarginTerms1Choice(base_types._BaseFieldType):

	__slots__ = ["_MrgnDtls", "_SgrtdIndpdntAmtMrgn"]
	@property
	def MrgnDtls(self):
		return self._MrgnDtls

	@MrgnDtls.setter
	def MrgnDtls(self, value):
		self._MrgnDtls = value if type(value) != base_types.auto else self.make_default("MrgnDtls")

	@MrgnDtls.deleter
	def MrgnDtls(self):
		del self._MrgnDtls
		self._MrgnDtls = None

	@property
	def SgrtdIndpdntAmtMrgn(self):
		return self._SgrtdIndpdntAmtMrgn

	@SgrtdIndpdntAmtMrgn.setter
	def SgrtdIndpdntAmtMrgn(self, value):
		self._SgrtdIndpdntAmtMrgn = value if type(value) != base_types.auto else self.make_default("SgrtdIndpdntAmtMrgn")

	@SgrtdIndpdntAmtMrgn.deleter
	def SgrtdIndpdntAmtMrgn(self):
		del self._SgrtdIndpdntAmtMrgn
		self._SgrtdIndpdntAmtMrgn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MrgnDtls', type=Margin1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SgrtdIndpdntAmtMrgn', type=SegregatedIndependentAmountMargin1, min=0, max=1, mutex_group=1, array=False),
	))

