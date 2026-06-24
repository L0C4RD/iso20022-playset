# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._PortfolioTransferCompletionV01 import PortfolioTransferCompletionV01

class SESE_043_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:sese.043.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_PrtflTrfCmpltn"]
		@property
		def PrtflTrfCmpltn(self):
			return self._PrtflTrfCmpltn

		@PrtflTrfCmpltn.setter
		def PrtflTrfCmpltn(self, value):
			self._PrtflTrfCmpltn = value if type(value) != base_types.auto else self.make_default("PrtflTrfCmpltn")

		@PrtflTrfCmpltn.deleter
		def PrtflTrfCmpltn(self):
			del self._PrtflTrfCmpltn
			self._PrtflTrfCmpltn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='PrtflTrfCmpltn', type=PortfolioTransferCompletionV01, min=1, max=1, mutex_group=None, array=False),
		))