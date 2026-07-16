# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CollateralMovement12
from . import CollateralProposal7

class CollateralProposal6Choice(base_types._BaseFieldType):

	__slots__ = ["_CollPrpslDtls", "_SgrtdIndpdntAmt"]
	@property
	def CollPrpslDtls(self):
		return self._CollPrpslDtls

	@CollPrpslDtls.setter
	def CollPrpslDtls(self, value):
		self._CollPrpslDtls = value if value is not None else base_types.UninitialisedField(self, 'CollPrpslDtls', CollateralProposal7, False)

	@CollPrpslDtls.deleter
	def CollPrpslDtls(self):
		del self._CollPrpslDtls
		self._CollPrpslDtls = base_types.UninitialisedField(self, 'CollPrpslDtls', CollateralProposal7, False)

	@property
	def SgrtdIndpdntAmt(self):
		return self._SgrtdIndpdntAmt

	@SgrtdIndpdntAmt.setter
	def SgrtdIndpdntAmt(self, value):
		self._SgrtdIndpdntAmt = value if value is not None else base_types.UninitialisedField(self, 'SgrtdIndpdntAmt', CollateralMovement12, False)

	@SgrtdIndpdntAmt.deleter
	def SgrtdIndpdntAmt(self):
		del self._SgrtdIndpdntAmt
		self._SgrtdIndpdntAmt = base_types.UninitialisedField(self, 'SgrtdIndpdntAmt', CollateralMovement12, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollPrpslDtls', type=CollateralProposal7, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SgrtdIndpdntAmt', type=CollateralMovement12, min=0, max=1, mutex_group=1, array=False),
	))