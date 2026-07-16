# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import TransactionAdviceV06

class CAAA_020_001_06():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caaa.020.001.06"
		_docname = "caaa.020.001.06"

		__slots__ = ["_TxAdvc"]
		@property
		def TxAdvc(self):
			return self._TxAdvc

		@TxAdvc.setter
		def TxAdvc(self, value):
			self._TxAdvc = value if value is not None else base_types.UninitialisedField(self, 'TxAdvc', TransactionAdviceV06, False)

		@TxAdvc.deleter
		def TxAdvc(self):
			del self._TxAdvc
			self._TxAdvc = base_types.UninitialisedField(self, 'TxAdvc', TransactionAdviceV06, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='TxAdvc', type=TransactionAdviceV06, min=1, max=1, mutex_group=None, array=False),
		))