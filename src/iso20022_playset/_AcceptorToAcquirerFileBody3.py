# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AcceptorCancellationAdvice15
from . import AcceptorCompletionAdvice15
from . import CardPaymentBatchTransfer14

class AcceptorToAcquirerFileBody3(base_types._BaseFieldType):

	__slots__ = ["_BtchTrf", "_CmpltnAdvc", "_CxlAdvc"]
	@property
	def BtchTrf(self):
		return self._BtchTrf

	@BtchTrf.setter
	def BtchTrf(self, value):
		self._BtchTrf = value if value is not None else base_types.UninitialisedField(self, 'BtchTrf', CardPaymentBatchTransfer14, False)

	@BtchTrf.deleter
	def BtchTrf(self):
		del self._BtchTrf
		self._BtchTrf = base_types.UninitialisedField(self, 'BtchTrf', CardPaymentBatchTransfer14, False)

	@property
	def CmpltnAdvc(self):
		return self._CmpltnAdvc

	@CmpltnAdvc.setter
	def CmpltnAdvc(self, value):
		self._CmpltnAdvc = value if value is not None else base_types.UninitialisedField(self, 'CmpltnAdvc', AcceptorCompletionAdvice15, False)

	@CmpltnAdvc.deleter
	def CmpltnAdvc(self):
		del self._CmpltnAdvc
		self._CmpltnAdvc = base_types.UninitialisedField(self, 'CmpltnAdvc', AcceptorCompletionAdvice15, False)

	@property
	def CxlAdvc(self):
		return self._CxlAdvc

	@CxlAdvc.setter
	def CxlAdvc(self, value):
		self._CxlAdvc = value if value is not None else base_types.UninitialisedField(self, 'CxlAdvc', AcceptorCancellationAdvice15, False)

	@CxlAdvc.deleter
	def CxlAdvc(self):
		del self._CxlAdvc
		self._CxlAdvc = base_types.UninitialisedField(self, 'CxlAdvc', AcceptorCancellationAdvice15, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BtchTrf', type=CardPaymentBatchTransfer14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmpltnAdvc', type=AcceptorCompletionAdvice15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlAdvc', type=AcceptorCancellationAdvice15, min=0, max=1, mutex_group=None, array=False),
	))