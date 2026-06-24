# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ShareholdersIdentificationDisclosureRequestV04 import ShareholdersIdentificationDisclosureRequestV04

class SEEV_045_001_04():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:seev.045.001.04"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_ShrhldrsIdDsclsrReq"]
		@property
		def ShrhldrsIdDsclsrReq(self):
			return self._ShrhldrsIdDsclsrReq

		@ShrhldrsIdDsclsrReq.setter
		def ShrhldrsIdDsclsrReq(self, value):
			self._ShrhldrsIdDsclsrReq = value if type(value) != base_types.auto else self.make_default("ShrhldrsIdDsclsrReq")

		@ShrhldrsIdDsclsrReq.deleter
		def ShrhldrsIdDsclsrReq(self):
			del self._ShrhldrsIdDsclsrReq
			self._ShrhldrsIdDsclsrReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ShrhldrsIdDsclsrReq', type=ShareholdersIdentificationDisclosureRequestV04, min=1, max=1, mutex_group=None, array=False),
		))