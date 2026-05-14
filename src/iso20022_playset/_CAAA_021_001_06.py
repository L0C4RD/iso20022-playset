# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._TransactionAdviceResponseV06 import TransactionAdviceResponseV06

class CAAA_021_001_06():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_TxAdvcRspn"]
		@property
		def TxAdvcRspn(self):
			return self._TxAdvcRspn

		@TxAdvcRspn.setter
		def TxAdvcRspn(self, value):
			self._TxAdvcRspn = value if type(value) != base_types.auto else self.make_default("TxAdvcRspn")

		@TxAdvcRspn.deleter
		def TxAdvcRspn(self):
			del self._TxAdvcRspn
			self._TxAdvcRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='TxAdvcRspn', type=TransactionAdviceResponseV06, min=1, max=1, mutex_group=None, array=False),
		))