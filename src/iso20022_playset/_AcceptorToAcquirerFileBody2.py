# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AcceptorCancellationAdvice14 import AcceptorCancellationAdvice14
from ._AcceptorCompletionAdvice14 import AcceptorCompletionAdvice14
from ._CardPaymentBatchTransfer13 import CardPaymentBatchTransfer13

class AcceptorToAcquirerFileBody2(base_types._BaseFieldType):

	__slots__ = ["_BtchTrf", "_CmpltnAdvc", "_CxlAdvc"]
	@property
	def BtchTrf(self):
		return self._BtchTrf

	@BtchTrf.setter
	def BtchTrf(self, value):
		self._BtchTrf = value if type(value) != base_types.auto else self.make_default("BtchTrf")

	@BtchTrf.deleter
	def BtchTrf(self):
		del self._BtchTrf
		self._BtchTrf = None

	@property
	def CmpltnAdvc(self):
		return self._CmpltnAdvc

	@CmpltnAdvc.setter
	def CmpltnAdvc(self, value):
		self._CmpltnAdvc = value if type(value) != base_types.auto else self.make_default("CmpltnAdvc")

	@CmpltnAdvc.deleter
	def CmpltnAdvc(self):
		del self._CmpltnAdvc
		self._CmpltnAdvc = None

	@property
	def CxlAdvc(self):
		return self._CxlAdvc

	@CxlAdvc.setter
	def CxlAdvc(self, value):
		self._CxlAdvc = value if type(value) != base_types.auto else self.make_default("CxlAdvc")

	@CxlAdvc.deleter
	def CxlAdvc(self):
		del self._CxlAdvc
		self._CxlAdvc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BtchTrf', type=CardPaymentBatchTransfer13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmpltnAdvc', type=AcceptorCompletionAdvice14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlAdvc', type=AcceptorCancellationAdvice14, min=0, max=1, mutex_group=None, array=False),
	))