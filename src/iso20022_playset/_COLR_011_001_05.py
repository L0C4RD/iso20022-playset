# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CollateralSubstitutionResponseV05

class COLR_011_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:colr.011.001.05"
		_docname = "colr.011.001.05"

		__slots__ = ["_CollSbstitnRspn"]
		@property
		def CollSbstitnRspn(self):
			return self._CollSbstitnRspn

		@CollSbstitnRspn.setter
		def CollSbstitnRspn(self, value):
			self._CollSbstitnRspn = value if value is not None else base_types.UninitialisedField(self, 'CollSbstitnRspn', CollateralSubstitutionResponseV05, False)

		@CollSbstitnRspn.deleter
		def CollSbstitnRspn(self):
			del self._CollSbstitnRspn
			self._CollSbstitnRspn = base_types.UninitialisedField(self, 'CollSbstitnRspn', CollateralSubstitutionResponseV05, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CollSbstitnRspn', type=CollateralSubstitutionResponseV05, min=1, max=1, mutex_group=None, array=False),
		))