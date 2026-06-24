# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CorporateActionMovementReversalAdviceV16 import CorporateActionMovementReversalAdviceV16

class SEEV_037_001_16():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:seev.037.001.16"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_CorpActnMvmntRvslAdvc"]
		@property
		def CorpActnMvmntRvslAdvc(self):
			return self._CorpActnMvmntRvslAdvc

		@CorpActnMvmntRvslAdvc.setter
		def CorpActnMvmntRvslAdvc(self, value):
			self._CorpActnMvmntRvslAdvc = value if type(value) != base_types.auto else self.make_default("CorpActnMvmntRvslAdvc")

		@CorpActnMvmntRvslAdvc.deleter
		def CorpActnMvmntRvslAdvc(self):
			del self._CorpActnMvmntRvslAdvc
			self._CorpActnMvmntRvslAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CorpActnMvmntRvslAdvc', type=CorporateActionMovementReversalAdviceV16, min=1, max=1, mutex_group=None, array=False),
		))