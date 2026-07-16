# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CollateralProposalResponse4
from . import CollateralProposalResponseType4

class CollateralProposalResponse4Choice(base_types._BaseFieldType):

	__slots__ = ["_CollPrpsl", "_SgrtdIndpdntAmt"]
	@property
	def CollPrpsl(self):
		return self._CollPrpsl

	@CollPrpsl.setter
	def CollPrpsl(self, value):
		self._CollPrpsl = value if value is not None else base_types.UninitialisedField(self, 'CollPrpsl', CollateralProposalResponse4, False)

	@CollPrpsl.deleter
	def CollPrpsl(self):
		del self._CollPrpsl
		self._CollPrpsl = base_types.UninitialisedField(self, 'CollPrpsl', CollateralProposalResponse4, False)

	@property
	def SgrtdIndpdntAmt(self):
		return self._SgrtdIndpdntAmt

	@SgrtdIndpdntAmt.setter
	def SgrtdIndpdntAmt(self, value):
		self._SgrtdIndpdntAmt = value if value is not None else base_types.UninitialisedField(self, 'SgrtdIndpdntAmt', CollateralProposalResponseType4, False)

	@SgrtdIndpdntAmt.deleter
	def SgrtdIndpdntAmt(self):
		del self._SgrtdIndpdntAmt
		self._SgrtdIndpdntAmt = base_types.UninitialisedField(self, 'SgrtdIndpdntAmt', CollateralProposalResponseType4, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollPrpsl', type=CollateralProposalResponse4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SgrtdIndpdntAmt', type=CollateralProposalResponseType4, min=0, max=1, mutex_group=1, array=False),
	))