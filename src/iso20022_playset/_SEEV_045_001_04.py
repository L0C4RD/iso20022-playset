# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ShareholdersIdentificationDisclosureRequestV04

class SEEV_045_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04"
		_docname = "seev.045.001.04"

		__slots__ = ["_ShrhldrsIdDsclsrReq"]
		@property
		def ShrhldrsIdDsclsrReq(self):
			return self._ShrhldrsIdDsclsrReq

		@ShrhldrsIdDsclsrReq.setter
		def ShrhldrsIdDsclsrReq(self, value):
			self._ShrhldrsIdDsclsrReq = value if value is not None else base_types.UninitialisedField(self, 'ShrhldrsIdDsclsrReq', ShareholdersIdentificationDisclosureRequestV04, False)

		@ShrhldrsIdDsclsrReq.deleter
		def ShrhldrsIdDsclsrReq(self):
			del self._ShrhldrsIdDsclsrReq
			self._ShrhldrsIdDsclsrReq = base_types.UninitialisedField(self, 'ShrhldrsIdDsclsrReq', ShareholdersIdentificationDisclosureRequestV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ShrhldrsIdDsclsrReq', type=ShareholdersIdentificationDisclosureRequestV04, min=1, max=1, mutex_group=None, array=False),
		))