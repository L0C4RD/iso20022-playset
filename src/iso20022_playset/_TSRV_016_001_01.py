# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DemandRefusalNotificationV01

class TSRV_016_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01"
		_docname = "tsrv.016.001.01"

		__slots__ = ["_DmndRfslNtfctn"]
		@property
		def DmndRfslNtfctn(self):
			return self._DmndRfslNtfctn

		@DmndRfslNtfctn.setter
		def DmndRfslNtfctn(self, value):
			self._DmndRfslNtfctn = value if value is not None else base_types.UninitialisedField(self, 'DmndRfslNtfctn', DemandRefusalNotificationV01, False)

		@DmndRfslNtfctn.deleter
		def DmndRfslNtfctn(self):
			del self._DmndRfslNtfctn
			self._DmndRfslNtfctn = base_types.UninitialisedField(self, 'DmndRfslNtfctn', DemandRefusalNotificationV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='DmndRfslNtfctn', type=DemandRefusalNotificationV01, min=1, max=1, mutex_group=None, array=False),
		))