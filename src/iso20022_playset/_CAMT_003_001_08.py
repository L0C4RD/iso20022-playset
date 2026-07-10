# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._GetAccountV08 import GetAccountV08

class CAMT_003_001_08():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.003.001.08"
		_docname = "camt.003.001.08"

		__slots__ = ["_GetAcct"]
		@property
		def GetAcct(self):
			return self._GetAcct

		@GetAcct.setter
		def GetAcct(self, value):
			self._GetAcct = value if type(value) != base_types.auto else self.make_default("GetAcct")

		@GetAcct.deleter
		def GetAcct(self):
			del self._GetAcct
			self._GetAcct = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='GetAcct', type=GetAccountV08, min=1, max=1, mutex_group=None, array=False),
		))