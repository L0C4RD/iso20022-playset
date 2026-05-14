# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesTransactionCancellationRequestStatusAdviceV08 import SecuritiesTransactionCancellationRequestStatusAdviceV08

class SESE_027_001_08():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesTxCxlReqStsAdvc"]
		@property
		def SctiesTxCxlReqStsAdvc(self):
			return self._SctiesTxCxlReqStsAdvc

		@SctiesTxCxlReqStsAdvc.setter
		def SctiesTxCxlReqStsAdvc(self, value):
			self._SctiesTxCxlReqStsAdvc = value if type(value) != base_types.auto else self.make_default("SctiesTxCxlReqStsAdvc")

		@SctiesTxCxlReqStsAdvc.deleter
		def SctiesTxCxlReqStsAdvc(self):
			del self._SctiesTxCxlReqStsAdvc
			self._SctiesTxCxlReqStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesTxCxlReqStsAdvc', type=SecuritiesTransactionCancellationRequestStatusAdviceV08, min=1, max=1, mutex_group=None, array=False),
		))