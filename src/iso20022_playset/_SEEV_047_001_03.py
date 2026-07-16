# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ShareholdersIdentificationDisclosureResponseV03

class SEEV_047_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03"
		_docname = "seev.047.001.03"

		__slots__ = ["_ShrhldrsIdDsclsrRspn"]
		@property
		def ShrhldrsIdDsclsrRspn(self):
			return self._ShrhldrsIdDsclsrRspn

		@ShrhldrsIdDsclsrRspn.setter
		def ShrhldrsIdDsclsrRspn(self, value):
			self._ShrhldrsIdDsclsrRspn = value if value is not None else base_types.UninitialisedField(self, 'ShrhldrsIdDsclsrRspn', ShareholdersIdentificationDisclosureResponseV03, False)

		@ShrhldrsIdDsclsrRspn.deleter
		def ShrhldrsIdDsclsrRspn(self):
			del self._ShrhldrsIdDsclsrRspn
			self._ShrhldrsIdDsclsrRspn = base_types.UninitialisedField(self, 'ShrhldrsIdDsclsrRspn', ShareholdersIdentificationDisclosureResponseV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ShrhldrsIdDsclsrRspn', type=ShareholdersIdentificationDisclosureResponseV03, min=1, max=1, mutex_group=None, array=False),
		))