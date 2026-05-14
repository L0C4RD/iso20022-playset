# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AcceptorCancellationAdviceResponse14 import AcceptorCancellationAdviceResponse14
from ._AcceptorCompletionAdviceResponse14 import AcceptorCompletionAdviceResponse14
from ._CardPaymentBatchTransferResponse13 import CardPaymentBatchTransferResponse13

class AcquirerToAcceptorFileBody3(base_types._BaseFieldType):

	__slots__ = ["_BtchTrfRspn", "_CmpltnAdvcRspn", "_CxlRspn"]
	@property
	def BtchTrfRspn(self):
		return self._BtchTrfRspn

	@BtchTrfRspn.setter
	def BtchTrfRspn(self, value):
		self._BtchTrfRspn = value if type(value) != base_types.auto else self.make_default("BtchTrfRspn")

	@BtchTrfRspn.deleter
	def BtchTrfRspn(self):
		del self._BtchTrfRspn
		self._BtchTrfRspn = None

	@property
	def CmpltnAdvcRspn(self):
		return self._CmpltnAdvcRspn

	@CmpltnAdvcRspn.setter
	def CmpltnAdvcRspn(self, value):
		self._CmpltnAdvcRspn = value if type(value) != base_types.auto else self.make_default("CmpltnAdvcRspn")

	@CmpltnAdvcRspn.deleter
	def CmpltnAdvcRspn(self):
		del self._CmpltnAdvcRspn
		self._CmpltnAdvcRspn = None

	@property
	def CxlRspn(self):
		return self._CxlRspn

	@CxlRspn.setter
	def CxlRspn(self, value):
		self._CxlRspn = value if type(value) != base_types.auto else self.make_default("CxlRspn")

	@CxlRspn.deleter
	def CxlRspn(self):
		del self._CxlRspn
		self._CxlRspn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BtchTrfRspn', type=CardPaymentBatchTransferResponse13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmpltnAdvcRspn', type=AcceptorCompletionAdviceResponse14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlRspn', type=AcceptorCancellationAdviceResponse14, min=0, max=1, mutex_group=None, array=False),
	))