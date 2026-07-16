# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ShareholdersIdentificationDisclosureRequestCancellationAdviceV01

class SEEV_046_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:seev.046.001.01"
		_docname = "seev.046.001.01"

		__slots__ = ["_ShrhldrsIdDsclsrReqCxlAdvc"]
		@property
		def ShrhldrsIdDsclsrReqCxlAdvc(self):
			return self._ShrhldrsIdDsclsrReqCxlAdvc

		@ShrhldrsIdDsclsrReqCxlAdvc.setter
		def ShrhldrsIdDsclsrReqCxlAdvc(self, value):
			self._ShrhldrsIdDsclsrReqCxlAdvc = value if value is not None else base_types.UninitialisedField(self, 'ShrhldrsIdDsclsrReqCxlAdvc', ShareholdersIdentificationDisclosureRequestCancellationAdviceV01, False)

		@ShrhldrsIdDsclsrReqCxlAdvc.deleter
		def ShrhldrsIdDsclsrReqCxlAdvc(self):
			del self._ShrhldrsIdDsclsrReqCxlAdvc
			self._ShrhldrsIdDsclsrReqCxlAdvc = base_types.UninitialisedField(self, 'ShrhldrsIdDsclsrReqCxlAdvc', ShareholdersIdentificationDisclosureRequestCancellationAdviceV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ShrhldrsIdDsclsrReqCxlAdvc', type=ShareholdersIdentificationDisclosureRequestCancellationAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))