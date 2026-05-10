from . import base_types
from ._CollateralProposal6Choice import CollateralProposal6Choice
from ._ProposalType1Code import ProposalType1Code

class Proposal6(base_types._BaseFieldType):

	__slots__ = ["_CollPrpslTp", "_CollPrpsl"]
	@property
	def CollPrpslTp(self):
		return self._CollPrpslTp

	@CollPrpslTp.setter
	def CollPrpslTp(self, value):
		self._CollPrpslTp = value if type(value) != base_types.auto else self.make_default("CollPrpslTp")

	@CollPrpslTp.deleter
	def CollPrpslTp(self):
		del self._CollPrpslTp
		self._CollPrpslTp = None

	@property
	def CollPrpsl(self):
		return self._CollPrpsl

	@CollPrpsl.setter
	def CollPrpsl(self, value):
		self._CollPrpsl = value if type(value) != base_types.auto else self.make_default("CollPrpsl")

	@CollPrpsl.deleter
	def CollPrpsl(self):
		del self._CollPrpsl
		self._CollPrpsl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollPrpslTp', type=ProposalType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollPrpsl', type=CollateralProposal6Choice, min=1, max=1, mutex_group=None, array=False),
	))

