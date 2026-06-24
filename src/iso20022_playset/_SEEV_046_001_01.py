# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ShareholdersIdentificationDisclosureRequestCancellationAdviceV01 import ShareholdersIdentificationDisclosureRequestCancellationAdviceV01

class SEEV_046_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:seev.046.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_ShrhldrsIdDsclsrReqCxlAdvc"]
		@property
		def ShrhldrsIdDsclsrReqCxlAdvc(self):
			return self._ShrhldrsIdDsclsrReqCxlAdvc

		@ShrhldrsIdDsclsrReqCxlAdvc.setter
		def ShrhldrsIdDsclsrReqCxlAdvc(self, value):
			self._ShrhldrsIdDsclsrReqCxlAdvc = value if type(value) != base_types.auto else self.make_default("ShrhldrsIdDsclsrReqCxlAdvc")

		@ShrhldrsIdDsclsrReqCxlAdvc.deleter
		def ShrhldrsIdDsclsrReqCxlAdvc(self):
			del self._ShrhldrsIdDsclsrReqCxlAdvc
			self._ShrhldrsIdDsclsrReqCxlAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ShrhldrsIdDsclsrReqCxlAdvc', type=ShareholdersIdentificationDisclosureRequestCancellationAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))