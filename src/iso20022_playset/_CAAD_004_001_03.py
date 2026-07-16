# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BatchTransferResponseV03

class CAAD_004_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caad.004.001.03"
		_docname = "caad.004.001.03"

		__slots__ = ["_BtchTrfRspn"]
		@property
		def BtchTrfRspn(self):
			return self._BtchTrfRspn

		@BtchTrfRspn.setter
		def BtchTrfRspn(self, value):
			self._BtchTrfRspn = value if value is not None else base_types.UninitialisedField(self, 'BtchTrfRspn', BatchTransferResponseV03, False)

		@BtchTrfRspn.deleter
		def BtchTrfRspn(self):
			del self._BtchTrfRspn
			self._BtchTrfRspn = base_types.UninitialisedField(self, 'BtchTrfRspn', BatchTransferResponseV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='BtchTrfRspn', type=BatchTransferResponseV03, min=1, max=1, mutex_group=None, array=False),
		))