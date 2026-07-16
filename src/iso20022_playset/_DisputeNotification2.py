# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SegregatedIndependentAmountDispute2
from . import VariationMarginDispute1

class DisputeNotification2(base_types._BaseFieldType):

	__slots__ = ["_SgrtdIndpdntAmtDspt", "_VartnMrgnDspt"]
	@property
	def SgrtdIndpdntAmtDspt(self):
		return self._SgrtdIndpdntAmtDspt

	@SgrtdIndpdntAmtDspt.setter
	def SgrtdIndpdntAmtDspt(self, value):
		self._SgrtdIndpdntAmtDspt = value if value is not None else base_types.UninitialisedField(self, 'SgrtdIndpdntAmtDspt', SegregatedIndependentAmountDispute2, False)

	@SgrtdIndpdntAmtDspt.deleter
	def SgrtdIndpdntAmtDspt(self):
		del self._SgrtdIndpdntAmtDspt
		self._SgrtdIndpdntAmtDspt = base_types.UninitialisedField(self, 'SgrtdIndpdntAmtDspt', SegregatedIndependentAmountDispute2, False)

	@property
	def VartnMrgnDspt(self):
		return self._VartnMrgnDspt

	@VartnMrgnDspt.setter
	def VartnMrgnDspt(self, value):
		self._VartnMrgnDspt = value if value is not None else base_types.UninitialisedField(self, 'VartnMrgnDspt', VariationMarginDispute1, False)

	@VartnMrgnDspt.deleter
	def VartnMrgnDspt(self):
		del self._VartnMrgnDspt
		self._VartnMrgnDspt = base_types.UninitialisedField(self, 'VartnMrgnDspt', VariationMarginDispute1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='SgrtdIndpdntAmtDspt', type=SegregatedIndependentAmountDispute2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VartnMrgnDspt', type=VariationMarginDispute1, min=1, max=1, mutex_group=None, array=False),
	))