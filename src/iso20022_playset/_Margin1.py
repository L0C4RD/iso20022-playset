# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SegregatedIndependentAmountMargin1
from . import VariationMargin1

class Margin1(base_types._BaseFieldType):

	__slots__ = ["_SgrtdIndpdntAmtMrgn", "_VartnMrgn"]
	@property
	def SgrtdIndpdntAmtMrgn(self):
		return self._SgrtdIndpdntAmtMrgn

	@SgrtdIndpdntAmtMrgn.setter
	def SgrtdIndpdntAmtMrgn(self, value):
		self._SgrtdIndpdntAmtMrgn = value if value is not None else base_types.UninitialisedField(self, 'SgrtdIndpdntAmtMrgn', SegregatedIndependentAmountMargin1, False)

	@SgrtdIndpdntAmtMrgn.deleter
	def SgrtdIndpdntAmtMrgn(self):
		del self._SgrtdIndpdntAmtMrgn
		self._SgrtdIndpdntAmtMrgn = base_types.UninitialisedField(self, 'SgrtdIndpdntAmtMrgn', SegregatedIndependentAmountMargin1, False)

	@property
	def VartnMrgn(self):
		return self._VartnMrgn

	@VartnMrgn.setter
	def VartnMrgn(self, value):
		self._VartnMrgn = value if value is not None else base_types.UninitialisedField(self, 'VartnMrgn', VariationMargin1, False)

	@VartnMrgn.deleter
	def VartnMrgn(self):
		del self._VartnMrgn
		self._VartnMrgn = base_types.UninitialisedField(self, 'VartnMrgn', VariationMargin1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='SgrtdIndpdntAmtMrgn', type=SegregatedIndependentAmountMargin1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VartnMrgn', type=VariationMargin1, min=1, max=1, mutex_group=None, array=False),
	))