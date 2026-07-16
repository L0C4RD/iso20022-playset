# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SpecialNotificationV01

class TSMT_048_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsmt.048.001.01"
		_docname = "tsmt.048.001.01"

		__slots__ = ["_SpclNtfctn"]
		@property
		def SpclNtfctn(self):
			return self._SpclNtfctn

		@SpclNtfctn.setter
		def SpclNtfctn(self, value):
			self._SpclNtfctn = value if value is not None else base_types.UninitialisedField(self, 'SpclNtfctn', SpecialNotificationV01, False)

		@SpclNtfctn.deleter
		def SpclNtfctn(self):
			del self._SpclNtfctn
			self._SpclNtfctn = base_types.UninitialisedField(self, 'SpclNtfctn', SpecialNotificationV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SpclNtfctn', type=SpecialNotificationV01, min=1, max=1, mutex_group=None, array=False),
		))