# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionNotificationV15

class SEEV_031_001_15():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:seev.031.001.15"
		_docname = "seev.031.001.15"

		__slots__ = ["_CorpActnNtfctn"]
		@property
		def CorpActnNtfctn(self):
			return self._CorpActnNtfctn

		@CorpActnNtfctn.setter
		def CorpActnNtfctn(self, value):
			self._CorpActnNtfctn = value if value is not None else base_types.UninitialisedField(self, 'CorpActnNtfctn', CorporateActionNotificationV15, False)

		@CorpActnNtfctn.deleter
		def CorpActnNtfctn(self):
			del self._CorpActnNtfctn
			self._CorpActnNtfctn = base_types.UninitialisedField(self, 'CorpActnNtfctn', CorporateActionNotificationV15, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CorpActnNtfctn', type=CorporateActionNotificationV15, min=1, max=1, mutex_group=None, array=False),
		))