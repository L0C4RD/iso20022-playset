# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import TimeOutNotificationV03

class TSMT_040_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsmt.040.001.03"
		_docname = "tsmt.040.001.03"

		__slots__ = ["_TmOutNtfctn"]
		@property
		def TmOutNtfctn(self):
			return self._TmOutNtfctn

		@TmOutNtfctn.setter
		def TmOutNtfctn(self, value):
			self._TmOutNtfctn = value if value is not None else base_types.UninitialisedField(self, 'TmOutNtfctn', TimeOutNotificationV03, False)

		@TmOutNtfctn.deleter
		def TmOutNtfctn(self):
			del self._TmOutNtfctn
			self._TmOutNtfctn = base_types.UninitialisedField(self, 'TmOutNtfctn', TimeOutNotificationV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='TmOutNtfctn', type=TimeOutNotificationV03, min=1, max=1, mutex_group=None, array=False),
		))