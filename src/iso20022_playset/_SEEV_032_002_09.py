# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionEventProcessingStatusAdvice002V09

class SEEV_032_002_09():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:seev.032.002.09"
		_docname = "seev.032.002.09"

		__slots__ = ["_CorpActnEvtPrcgStsAdvc"]
		@property
		def CorpActnEvtPrcgStsAdvc(self):
			return self._CorpActnEvtPrcgStsAdvc

		@CorpActnEvtPrcgStsAdvc.setter
		def CorpActnEvtPrcgStsAdvc(self, value):
			self._CorpActnEvtPrcgStsAdvc = value if value is not None else base_types.UninitialisedField(self, 'CorpActnEvtPrcgStsAdvc', CorporateActionEventProcessingStatusAdvice002V09, False)

		@CorpActnEvtPrcgStsAdvc.deleter
		def CorpActnEvtPrcgStsAdvc(self):
			del self._CorpActnEvtPrcgStsAdvc
			self._CorpActnEvtPrcgStsAdvc = base_types.UninitialisedField(self, 'CorpActnEvtPrcgStsAdvc', CorporateActionEventProcessingStatusAdvice002V09, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CorpActnEvtPrcgStsAdvc', type=CorporateActionEventProcessingStatusAdvice002V09, min=1, max=1, mutex_group=None, array=False),
		))