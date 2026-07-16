# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionMovementReversalAdvice002V16

class SEEV_037_002_16():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:seev.037.002.16"
		_docname = "seev.037.002.16"

		__slots__ = ["_CorpActnMvmntRvslAdvc"]
		@property
		def CorpActnMvmntRvslAdvc(self):
			return self._CorpActnMvmntRvslAdvc

		@CorpActnMvmntRvslAdvc.setter
		def CorpActnMvmntRvslAdvc(self, value):
			self._CorpActnMvmntRvslAdvc = value if value is not None else base_types.UninitialisedField(self, 'CorpActnMvmntRvslAdvc', CorporateActionMovementReversalAdvice002V16, False)

		@CorpActnMvmntRvslAdvc.deleter
		def CorpActnMvmntRvslAdvc(self):
			del self._CorpActnMvmntRvslAdvc
			self._CorpActnMvmntRvslAdvc = base_types.UninitialisedField(self, 'CorpActnMvmntRvslAdvc', CorporateActionMovementReversalAdvice002V16, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CorpActnMvmntRvslAdvc', type=CorporateActionMovementReversalAdvice002V16, min=1, max=1, mutex_group=None, array=False),
		))