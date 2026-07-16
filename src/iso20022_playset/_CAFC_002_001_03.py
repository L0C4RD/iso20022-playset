# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FeeCollectionResponseV03

class CAFC_002_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:cafc.002.001.03"
		_docname = "cafc.002.001.03"

		__slots__ = ["_FeeColltnRspn"]
		@property
		def FeeColltnRspn(self):
			return self._FeeColltnRspn

		@FeeColltnRspn.setter
		def FeeColltnRspn(self, value):
			self._FeeColltnRspn = value if value is not None else base_types.UninitialisedField(self, 'FeeColltnRspn', FeeCollectionResponseV03, False)

		@FeeColltnRspn.deleter
		def FeeColltnRspn(self):
			del self._FeeColltnRspn
			self._FeeColltnRspn = base_types.UninitialisedField(self, 'FeeColltnRspn', FeeCollectionResponseV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='FeeColltnRspn', type=FeeCollectionResponseV03, min=1, max=1, mutex_group=None, array=False),
		))