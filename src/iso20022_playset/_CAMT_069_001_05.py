# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GetStandingOrderV05

class CAMT_069_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05"
		_docname = "camt.069.001.05"

		__slots__ = ["_GetStgOrdr"]
		@property
		def GetStgOrdr(self):
			return self._GetStgOrdr

		@GetStgOrdr.setter
		def GetStgOrdr(self, value):
			self._GetStgOrdr = value if value is not None else base_types.UninitialisedField(self, 'GetStgOrdr', GetStandingOrderV05, False)

		@GetStgOrdr.deleter
		def GetStgOrdr(self):
			del self._GetStgOrdr
			self._GetStgOrdr = base_types.UninitialisedField(self, 'GetStgOrdr', GetStandingOrderV05, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='GetStgOrdr', type=GetStandingOrderV05, min=1, max=1, mutex_group=None, array=False),
		))