# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionCancellationAdvice002V13

class SEEV_039_002_13():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13"
		_docname = "seev.039.002.13"

		__slots__ = ["_CorpActnCxlAdvc"]
		@property
		def CorpActnCxlAdvc(self):
			return self._CorpActnCxlAdvc

		@CorpActnCxlAdvc.setter
		def CorpActnCxlAdvc(self, value):
			self._CorpActnCxlAdvc = value if value is not None else base_types.UninitialisedField(self, 'CorpActnCxlAdvc', CorporateActionCancellationAdvice002V13, False)

		@CorpActnCxlAdvc.deleter
		def CorpActnCxlAdvc(self):
			del self._CorpActnCxlAdvc
			self._CorpActnCxlAdvc = base_types.UninitialisedField(self, 'CorpActnCxlAdvc', CorporateActionCancellationAdvice002V13, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CorpActnCxlAdvc', type=CorporateActionCancellationAdvice002V13, min=1, max=1, mutex_group=None, array=False),
		))