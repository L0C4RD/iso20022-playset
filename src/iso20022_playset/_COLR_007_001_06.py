from . import base_types
from .CollateralProposalV06 import CollateralProposalV06

class COLR_007_001_06():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CollPrpsl"]
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
			base_types.FieldEntry(name='CollPrpsl', type=CollateralProposalV06, min=1, max=1, mutex_group=None, array=False),
		))

