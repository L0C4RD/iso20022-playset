# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._TransactionAdviceV07 import TransactionAdviceV07

class CAAA_020_001_07():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:caaa.020.001.07",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_TxAdvc"]
		@property
		def TxAdvc(self):
			return self._TxAdvc

		@TxAdvc.setter
		def TxAdvc(self, value):
			self._TxAdvc = value if type(value) != base_types.auto else self.make_default("TxAdvc")

		@TxAdvc.deleter
		def TxAdvc(self):
			del self._TxAdvc
			self._TxAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='TxAdvc', type=TransactionAdviceV07, min=1, max=1, mutex_group=None, array=False),
		))