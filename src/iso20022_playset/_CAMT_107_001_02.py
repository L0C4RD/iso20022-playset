# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ChequePresentmentNotificationV02

class CAMT_107_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.107.001.02"
		_docname = "camt.107.001.02"

		__slots__ = ["_ChqPresntmntNtfctn"]
		@property
		def ChqPresntmntNtfctn(self):
			return self._ChqPresntmntNtfctn

		@ChqPresntmntNtfctn.setter
		def ChqPresntmntNtfctn(self, value):
			self._ChqPresntmntNtfctn = value if value is not None else base_types.UninitialisedField(self, 'ChqPresntmntNtfctn', ChequePresentmentNotificationV02, False)

		@ChqPresntmntNtfctn.deleter
		def ChqPresntmntNtfctn(self):
			del self._ChqPresntmntNtfctn
			self._ChqPresntmntNtfctn = base_types.UninitialisedField(self, 'ChqPresntmntNtfctn', ChequePresentmentNotificationV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ChqPresntmntNtfctn', type=ChequePresentmentNotificationV02, min=1, max=1, mutex_group=None, array=False),
		))