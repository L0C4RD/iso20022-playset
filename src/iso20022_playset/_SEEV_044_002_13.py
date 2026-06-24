# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CorporateActionMovementPreliminaryAdviceCancellationAdvice002V13 import CorporateActionMovementPreliminaryAdviceCancellationAdvice002V13

class SEEV_044_002_13():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:seev.044.002.13"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_CorpActnMvmntPrlimryAdvcCxlAdvc"]
		@property
		def CorpActnMvmntPrlimryAdvcCxlAdvc(self):
			return self._CorpActnMvmntPrlimryAdvcCxlAdvc

		@CorpActnMvmntPrlimryAdvcCxlAdvc.setter
		def CorpActnMvmntPrlimryAdvcCxlAdvc(self, value):
			self._CorpActnMvmntPrlimryAdvcCxlAdvc = value if type(value) != base_types.auto else self.make_default("CorpActnMvmntPrlimryAdvcCxlAdvc")

		@CorpActnMvmntPrlimryAdvcCxlAdvc.deleter
		def CorpActnMvmntPrlimryAdvcCxlAdvc(self):
			del self._CorpActnMvmntPrlimryAdvcCxlAdvc
			self._CorpActnMvmntPrlimryAdvcCxlAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CorpActnMvmntPrlimryAdvcCxlAdvc', type=CorporateActionMovementPreliminaryAdviceCancellationAdvice002V13, min=1, max=1, mutex_group=None, array=False),
		))