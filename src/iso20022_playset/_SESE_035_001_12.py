# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesFinancingConfirmationV12

class SESE_035_001_12():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:sese.035.001.12"
		_docname = "sese.035.001.12"

		__slots__ = ["_SctiesFincgConf"]
		@property
		def SctiesFincgConf(self):
			return self._SctiesFincgConf

		@SctiesFincgConf.setter
		def SctiesFincgConf(self, value):
			self._SctiesFincgConf = value if value is not None else base_types.UninitialisedField(self, 'SctiesFincgConf', SecuritiesFinancingConfirmationV12, False)

		@SctiesFincgConf.deleter
		def SctiesFincgConf(self):
			del self._SctiesFincgConf
			self._SctiesFincgConf = base_types.UninitialisedField(self, 'SctiesFincgConf', SecuritiesFinancingConfirmationV12, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesFincgConf', type=SecuritiesFinancingConfirmationV12, min=1, max=1, mutex_group=None, array=False),
		))