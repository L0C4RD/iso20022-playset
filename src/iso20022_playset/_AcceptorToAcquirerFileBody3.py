from . import base_types
from ._AcceptorCancellationAdvice15 import AcceptorCancellationAdvice15
from ._AcceptorCompletionAdvice15 import AcceptorCompletionAdvice15
from ._CardPaymentBatchTransfer14 import CardPaymentBatchTransfer14

class AcceptorToAcquirerFileBody3(base_types._BaseFieldType):

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
		base_types.FieldEntry(name='BtchTrf', type=CardPaymentBatchTransfer14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmpltnAdvc', type=AcceptorCompletionAdvice15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlAdvc', type=AcceptorCancellationAdvice15, min=0, max=1, mutex_group=None, array=False),
	))

