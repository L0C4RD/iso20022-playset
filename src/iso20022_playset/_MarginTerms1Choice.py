# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Margin1
from . import SegregatedIndependentAmountMargin1

class MarginTerms1Choice(base_types._BaseFieldType):

	__slots__ = ["_MrgnDtls", "_SgrtdIndpdntAmtMrgn"]
	@property
	def MrgnDtls(self):
		return self._MrgnDtls

	@MrgnDtls.setter
	def MrgnDtls(self, value):
		self._MrgnDtls = value if value is not None else base_types.UninitialisedField(self, 'MrgnDtls', Margin1, False)

	@MrgnDtls.deleter
	def MrgnDtls(self):
		del self._MrgnDtls
		self._MrgnDtls = base_types.UninitialisedField(self, 'MrgnDtls', Margin1, False)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='MrgnDtls', type=Margin1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SgrtdIndpdntAmtMrgn', type=SegregatedIndependentAmountMargin1, min=0, max=1, mutex_group=1, array=False),
	))