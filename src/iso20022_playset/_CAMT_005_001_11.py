# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GetTransactionV11

class CAMT_005_001_11():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11"
		_docname = "camt.005.001.11"

		__slots__ = ["_GetTx"]
		@property
		def GetTx(self):
			return self._GetTx

		@GetTx.setter
		def GetTx(self, value):
			self._GetTx = value if value is not None else base_types.UninitialisedField(self, 'GetTx', GetTransactionV11, False)

		@GetTx.deleter
		def GetTx(self):
			del self._GetTx
			self._GetTx = base_types.UninitialisedField(self, 'GetTx', GetTransactionV11, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='GetTx', type=GetTransactionV11, min=1, max=1, mutex_group=None, array=False),
		))