# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesTradeConfirmationV05

class SETR_027_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:setr.027.001.05"
		_docname = "setr.027.001.05"

		__slots__ = ["_SctiesTradConf"]
		@property
		def SctiesTradConf(self):
			return self._SctiesTradConf

		@SctiesTradConf.setter
		def SctiesTradConf(self, value):
			self._SctiesTradConf = value if value is not None else base_types.UninitialisedField(self, 'SctiesTradConf', SecuritiesTradeConfirmationV05, False)

		@SctiesTradConf.deleter
		def SctiesTradConf(self):
			del self._SctiesTradConf
			self._SctiesTradConf = base_types.UninitialisedField(self, 'SctiesTradConf', SecuritiesTradeConfirmationV05, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesTradConf', type=SecuritiesTradeConfirmationV05, min=1, max=1, mutex_group=None, array=False),
		))