from . import base_types
import CardPaymentBatchTransfer13
import AcceptorCompletionAdvice14
import AcceptorCancellationAdvice14

class AcceptorToAcquirerFileBody2(base_types._BaseFieldType):

	__slots__ = ["_CxlAdvc", "_BtchTrf", "_CmpltnAdvc"]
	@property
	def CxlAdvc(self):
		return self._CxlAdvc

	@CxlAdvc.setter
	def CxlAdvc(self, value):
		self._CxlAdvc = value if type(value) != auto else self.make_default("CxlAdvc")

	@CxlAdvc.deleter
	def CxlAdvc(self):
		del self._CxlAdvc
		self._CxlAdvc = None

	@property
	def BtchTrf(self):
		return self._BtchTrf

	@BtchTrf.setter
	def BtchTrf(self, value):
		self._BtchTrf = value if type(value) != auto else self.make_default("BtchTrf")

	@BtchTrf.deleter
	def BtchTrf(self):
		del self._BtchTrf
		self._BtchTrf = None

	@property
	def CmpltnAdvc(self):
		return self._CmpltnAdvc

	@CmpltnAdvc.setter
	def CmpltnAdvc(self, value):
		self._CmpltnAdvc = value if type(value) != auto else self.make_default("CmpltnAdvc")

	@CmpltnAdvc.deleter
	def CmpltnAdvc(self):
		del self._CmpltnAdvc
		self._CmpltnAdvc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CxlAdvc', type=AcceptorCancellationAdvice14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BtchTrf', type=CardPaymentBatchTransfer13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmpltnAdvc', type=AcceptorCompletionAdvice14, min=0, max=1, mutex_group=None, array=False),
	))

