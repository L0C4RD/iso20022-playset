# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesTransactionCancellationRequestQueryV01 import SecuritiesTransactionCancellationRequestQueryV01

class SEMT_032_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesTxCxlReqQry"]
		@property
		def SctiesTxCxlReqQry(self):
			return self._SctiesTxCxlReqQry

		@SctiesTxCxlReqQry.setter
		def SctiesTxCxlReqQry(self, value):
			self._SctiesTxCxlReqQry = value if type(value) != base_types.auto else self.make_default("SctiesTxCxlReqQry")

		@SctiesTxCxlReqQry.deleter
		def SctiesTxCxlReqQry(self):
			del self._SctiesTxCxlReqQry
			self._SctiesTxCxlReqQry = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesTxCxlReqQry', type=SecuritiesTransactionCancellationRequestQueryV01, min=1, max=1, mutex_group=None, array=False),
		))