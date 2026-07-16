# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CollateralProposal6Choice
from . import ProposalType1Code

class Proposal6(base_types._BaseFieldType):

	__slots__ = ["_CollPrpsl", "_CollPrpslTp"]
	@property
	def CollPrpsl(self):
		return self._CollPrpsl

	@CollPrpsl.setter
	def CollPrpsl(self, value):
		self._CollPrpsl = value if value is not None else base_types.UninitialisedField(self, 'CollPrpsl', CollateralProposal6Choice, False)

	@CollPrpsl.deleter
	def CollPrpsl(self):
		del self._CollPrpsl
		self._CollPrpsl = base_types.UninitialisedField(self, 'CollPrpsl', CollateralProposal6Choice, False)

	@property
	def CollPrpslTp(self):
		return self._CollPrpslTp

	@CollPrpslTp.setter
	def CollPrpslTp(self, value):
		self._CollPrpslTp = value if value is not None else base_types.UninitialisedField(self, 'CollPrpslTp', ProposalType1Code, False)

	@CollPrpslTp.deleter
	def CollPrpslTp(self):
		del self._CollPrpslTp
		self._CollPrpslTp = base_types.UninitialisedField(self, 'CollPrpslTp', ProposalType1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollPrpsl', type=CollateralProposal6Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollPrpslTp', type=ProposalType1Code, min=1, max=1, mutex_group=None, array=False),
	))