# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionMovementPreliminaryAdviceCancellationAdvice002V13

class SEEV_044_002_13():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:seev.044.002.13"
		_docname = "seev.044.002.13"

		__slots__ = ["_CorpActnMvmntPrlimryAdvcCxlAdvc"]
		@property
		def CorpActnMvmntPrlimryAdvcCxlAdvc(self):
			return self._CorpActnMvmntPrlimryAdvcCxlAdvc

		@CorpActnMvmntPrlimryAdvcCxlAdvc.setter
		def CorpActnMvmntPrlimryAdvcCxlAdvc(self, value):
			self._CorpActnMvmntPrlimryAdvcCxlAdvc = value if value is not None else base_types.UninitialisedField(self, 'CorpActnMvmntPrlimryAdvcCxlAdvc', CorporateActionMovementPreliminaryAdviceCancellationAdvice002V13, False)

		@CorpActnMvmntPrlimryAdvcCxlAdvc.deleter
		def CorpActnMvmntPrlimryAdvcCxlAdvc(self):
			del self._CorpActnMvmntPrlimryAdvcCxlAdvc
			self._CorpActnMvmntPrlimryAdvcCxlAdvc = base_types.UninitialisedField(self, 'CorpActnMvmntPrlimryAdvcCxlAdvc', CorporateActionMovementPreliminaryAdviceCancellationAdvice002V13, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CorpActnMvmntPrlimryAdvcCxlAdvc', type=CorporateActionMovementPreliminaryAdviceCancellationAdvice002V13, min=1, max=1, mutex_group=None, array=False),
		))