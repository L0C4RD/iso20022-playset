# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CorporateActionCancellationAdvice002V13 import CorporateActionCancellationAdvice002V13

class SEEV_039_002_13():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:seev.039.002.13"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_CorpActnCxlAdvc"]
		@property
		def CorpActnCxlAdvc(self):
			return self._CorpActnCxlAdvc

		@CorpActnCxlAdvc.setter
		def CorpActnCxlAdvc(self, value):
			self._CorpActnCxlAdvc = value if type(value) != base_types.auto else self.make_default("CorpActnCxlAdvc")

		@CorpActnCxlAdvc.deleter
		def CorpActnCxlAdvc(self):
			del self._CorpActnCxlAdvc
			self._CorpActnCxlAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CorpActnCxlAdvc', type=CorporateActionCancellationAdvice002V13, min=1, max=1, mutex_group=None, array=False),
		))