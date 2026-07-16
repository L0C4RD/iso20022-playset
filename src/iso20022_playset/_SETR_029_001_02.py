# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesTradeConfirmationCancellationV02

class SETR_029_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:setr.029.001.02"
		_docname = "setr.029.001.02"

		__slots__ = ["_SctiesTradConfCxl"]
		@property
		def SctiesTradConfCxl(self):
			return self._SctiesTradConfCxl

		@SctiesTradConfCxl.setter
		def SctiesTradConfCxl(self, value):
			self._SctiesTradConfCxl = value if value is not None else base_types.UninitialisedField(self, 'SctiesTradConfCxl', SecuritiesTradeConfirmationCancellationV02, False)

		@SctiesTradConfCxl.deleter
		def SctiesTradConfCxl(self):
			del self._SctiesTradConfCxl
			self._SctiesTradConfCxl = base_types.UninitialisedField(self, 'SctiesTradConfCxl', SecuritiesTradeConfirmationCancellationV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesTradConfCxl', type=SecuritiesTradeConfirmationCancellationV02, min=1, max=1, mutex_group=None, array=False),
		))