# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionMovementPreliminaryAdvice002V16

class SEEV_035_002_16():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16"
		_docname = "seev.035.002.16"

		__slots__ = ["_CorpActnMvmntPrlimryAdvc"]
		@property
		def CorpActnMvmntPrlimryAdvc(self):
			return self._CorpActnMvmntPrlimryAdvc

		@CorpActnMvmntPrlimryAdvc.setter
		def CorpActnMvmntPrlimryAdvc(self, value):
			self._CorpActnMvmntPrlimryAdvc = value if value is not None else base_types.UninitialisedField(self, 'CorpActnMvmntPrlimryAdvc', CorporateActionMovementPreliminaryAdvice002V16, False)

		@CorpActnMvmntPrlimryAdvc.deleter
		def CorpActnMvmntPrlimryAdvc(self):
			del self._CorpActnMvmntPrlimryAdvc
			self._CorpActnMvmntPrlimryAdvc = base_types.UninitialisedField(self, 'CorpActnMvmntPrlimryAdvc', CorporateActionMovementPreliminaryAdvice002V16, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CorpActnMvmntPrlimryAdvc', type=CorporateActionMovementPreliminaryAdvice002V16, min=1, max=1, mutex_group=None, array=False),
		))