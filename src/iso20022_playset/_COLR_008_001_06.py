# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CollateralProposalResponseV06

class COLR_008_001_06():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:colr.008.001.06"
		_docname = "colr.008.001.06"

		__slots__ = ["_CollPrpslRspn"]
		@property
		def CollPrpslRspn(self):
			return self._CollPrpslRspn

		@CollPrpslRspn.setter
		def CollPrpslRspn(self, value):
			self._CollPrpslRspn = value if value is not None else base_types.UninitialisedField(self, 'CollPrpslRspn', CollateralProposalResponseV06, False)

		@CollPrpslRspn.deleter
		def CollPrpslRspn(self):
			del self._CollPrpslRspn
			self._CollPrpslRspn = base_types.UninitialisedField(self, 'CollPrpslRspn', CollateralProposalResponseV06, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CollPrpslRspn', type=CollateralProposalResponseV06, min=1, max=1, mutex_group=None, array=False),
		))