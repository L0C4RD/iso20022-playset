from . import base_types
import CollateralProposalResponseV06

class COLR_008_001_06():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CollPrpslRspn"]
		@property
		def CollPrpslRspn(self):
			return self._CollPrpslRspn

		@CollPrpslRspn.setter
		def CollPrpslRspn(self, value):
			self._CollPrpslRspn = value if type(value) != auto else self.make_default("CollPrpslRspn")

		@CollPrpslRspn.deleter
		def CollPrpslRspn(self):
			del self._CollPrpslRspn
			self._CollPrpslRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CollPrpslRspn', type=CollateralProposalResponseV06, min=1, max=1, mutex_group=None, array=False),
		))

