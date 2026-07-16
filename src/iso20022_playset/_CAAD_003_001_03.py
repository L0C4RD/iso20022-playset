# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BatchTransferInitiationV03

class CAAD_003_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03"
		_docname = "caad.003.001.03"

		__slots__ = ["_BtchTrfInitn"]
		@property
		def BtchTrfInitn(self):
			return self._BtchTrfInitn

		@BtchTrfInitn.setter
		def BtchTrfInitn(self, value):
			self._BtchTrfInitn = value if value is not None else base_types.UninitialisedField(self, 'BtchTrfInitn', BatchTransferInitiationV03, False)

		@BtchTrfInitn.deleter
		def BtchTrfInitn(self):
			del self._BtchTrfInitn
			self._BtchTrfInitn = base_types.UninitialisedField(self, 'BtchTrfInitn', BatchTransferInitiationV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='BtchTrfInitn', type=BatchTransferInitiationV03, min=1, max=1, mutex_group=None, array=False),
		))