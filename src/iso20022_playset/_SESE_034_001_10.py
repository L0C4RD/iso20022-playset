# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesFinancingStatusAdviceV10

class SESE_034_001_10():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:sese.034.001.10"
		_docname = "sese.034.001.10"

		__slots__ = ["_SctiesFincgStsAdvc"]
		@property
		def SctiesFincgStsAdvc(self):
			return self._SctiesFincgStsAdvc

		@SctiesFincgStsAdvc.setter
		def SctiesFincgStsAdvc(self, value):
			self._SctiesFincgStsAdvc = value if value is not None else base_types.UninitialisedField(self, 'SctiesFincgStsAdvc', SecuritiesFinancingStatusAdviceV10, False)

		@SctiesFincgStsAdvc.deleter
		def SctiesFincgStsAdvc(self):
			del self._SctiesFincgStsAdvc
			self._SctiesFincgStsAdvc = base_types.UninitialisedField(self, 'SctiesFincgStsAdvc', SecuritiesFinancingStatusAdviceV10, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesFincgStsAdvc', type=SecuritiesFinancingStatusAdviceV10, min=1, max=1, mutex_group=None, array=False),
		))