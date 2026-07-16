# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CollateralSubstitutionRequestV05

class COLR_010_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:colr.010.001.05"
		_docname = "colr.010.001.05"

		__slots__ = ["_CollSbstitnReq"]
		@property
		def CollSbstitnReq(self):
			return self._CollSbstitnReq

		@CollSbstitnReq.setter
		def CollSbstitnReq(self, value):
			self._CollSbstitnReq = value if value is not None else base_types.UninitialisedField(self, 'CollSbstitnReq', CollateralSubstitutionRequestV05, False)

		@CollSbstitnReq.deleter
		def CollSbstitnReq(self):
			del self._CollSbstitnReq
			self._CollSbstitnReq = base_types.UninitialisedField(self, 'CollSbstitnReq', CollateralSubstitutionRequestV05, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CollSbstitnReq', type=CollateralSubstitutionRequestV05, min=1, max=1, mutex_group=None, array=False),
		))