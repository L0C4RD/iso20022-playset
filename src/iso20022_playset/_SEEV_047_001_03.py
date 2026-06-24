# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ShareholdersIdentificationDisclosureResponseV03 import ShareholdersIdentificationDisclosureResponseV03

class SEEV_047_001_03():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:seev.047.001.03"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_ShrhldrsIdDsclsrRspn"]
		@property
		def ShrhldrsIdDsclsrRspn(self):
			return self._ShrhldrsIdDsclsrRspn

		@ShrhldrsIdDsclsrRspn.setter
		def ShrhldrsIdDsclsrRspn(self, value):
			self._ShrhldrsIdDsclsrRspn = value if type(value) != base_types.auto else self.make_default("ShrhldrsIdDsclsrRspn")

		@ShrhldrsIdDsclsrRspn.deleter
		def ShrhldrsIdDsclsrRspn(self):
			del self._ShrhldrsIdDsclsrRspn
			self._ShrhldrsIdDsclsrRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ShrhldrsIdDsclsrRspn', type=ShareholdersIdentificationDisclosureResponseV03, min=1, max=1, mutex_group=None, array=False),
		))