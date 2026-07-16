# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import TransferOutConfirmationV10

class SESE_003_001_10():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:sese.003.001.10"
		_docname = "sese.003.001.10"

		__slots__ = ["_TrfOutConf"]
		@property
		def TrfOutConf(self):
			return self._TrfOutConf

		@TrfOutConf.setter
		def TrfOutConf(self, value):
			self._TrfOutConf = value if value is not None else base_types.UninitialisedField(self, 'TrfOutConf', TransferOutConfirmationV10, False)

		@TrfOutConf.deleter
		def TrfOutConf(self):
			del self._TrfOutConf
			self._TrfOutConf = base_types.UninitialisedField(self, 'TrfOutConf', TransferOutConfirmationV10, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='TrfOutConf', type=TransferOutConfirmationV10, min=1, max=1, mutex_group=None, array=False),
		))