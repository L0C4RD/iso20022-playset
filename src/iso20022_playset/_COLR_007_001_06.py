# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CollateralProposalV06 import CollateralProposalV06

class COLR_007_001_06():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:colr.007.001.06"
		_docname = "colr.007.001.06"

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