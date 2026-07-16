# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import TransferInConfirmationV10

class SESE_007_001_10():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:sese.007.001.10"
		_docname = "sese.007.001.10"

		__slots__ = ["_TrfInConf"]
		@property
		def TrfInConf(self):
			return self._TrfInConf

		@TrfInConf.setter
		def TrfInConf(self, value):
			self._TrfInConf = value if value is not None else base_types.UninitialisedField(self, 'TrfInConf', TransferInConfirmationV10, False)

		@TrfInConf.deleter
		def TrfInConf(self):
			del self._TrfInConf
			self._TrfInConf = base_types.UninitialisedField(self, 'TrfInConf', TransferInConfirmationV10, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='TrfInConf', type=TransferInConfirmationV10, min=1, max=1, mutex_group=None, array=False),
		))