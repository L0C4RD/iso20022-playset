# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._MisMatchAcceptanceNotificationV03 import MisMatchAcceptanceNotificationV03

class TSMT_021_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsmt.021.001.03"
		_docname = "tsmt.021.001.03"

		__slots__ = ["_MisMtchAccptncNtfctn"]
		@property
		def MisMtchAccptncNtfctn(self):
			return self._MisMtchAccptncNtfctn

		@MisMtchAccptncNtfctn.setter
		def MisMtchAccptncNtfctn(self, value):
			self._MisMtchAccptncNtfctn = value if type(value) != base_types.auto else self.make_default("MisMtchAccptncNtfctn")

		@MisMtchAccptncNtfctn.deleter
		def MisMtchAccptncNtfctn(self):
			del self._MisMtchAccptncNtfctn
			self._MisMtchAccptncNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='MisMtchAccptncNtfctn', type=MisMatchAcceptanceNotificationV03, min=1, max=1, mutex_group=None, array=False),
		))