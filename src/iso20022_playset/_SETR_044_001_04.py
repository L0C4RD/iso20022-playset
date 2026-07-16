# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesTradeConfirmationStatusAdviceV04

class SETR_044_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04"
		_docname = "setr.044.001.04"

		__slots__ = ["_SctiesTradConfStsAdvc"]
		@property
		def SctiesTradConfStsAdvc(self):
			return self._SctiesTradConfStsAdvc

		@SctiesTradConfStsAdvc.setter
		def SctiesTradConfStsAdvc(self, value):
			self._SctiesTradConfStsAdvc = value if value is not None else base_types.UninitialisedField(self, 'SctiesTradConfStsAdvc', SecuritiesTradeConfirmationStatusAdviceV04, False)

		@SctiesTradConfStsAdvc.deleter
		def SctiesTradConfStsAdvc(self):
			del self._SctiesTradConfStsAdvc
			self._SctiesTradConfStsAdvc = base_types.UninitialisedField(self, 'SctiesTradConfStsAdvc', SecuritiesTradeConfirmationStatusAdviceV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesTradConfStsAdvc', type=SecuritiesTradeConfirmationStatusAdviceV04, min=1, max=1, mutex_group=None, array=False),
		))