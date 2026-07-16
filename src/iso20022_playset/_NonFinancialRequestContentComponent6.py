# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CardPaymentTransaction146
from . import ExternallyDefinedData5
from . import NonFinancialRequestType2Code

class NonFinancialRequestContentComponent6(base_types._BaseFieldType):

	__slots__ = ["_AddtlReq", "_NonFinReqTp", "_Tx"]
	@property
	def AddtlReq(self):
		return self._AddtlReq

	@AddtlReq.setter
	def AddtlReq(self, value):
		self._AddtlReq = value if value is not None else base_types.UninitialisedField(self, 'AddtlReq', ExternallyDefinedData5, True)

	@AddtlReq.deleter
	def AddtlReq(self):
		del self._AddtlReq
		self._AddtlReq = base_types.UninitialisedField(self, 'AddtlReq', ExternallyDefinedData5, True)

	@property
	def NonFinReqTp(self):
		return self._NonFinReqTp

	@NonFinReqTp.setter
	def NonFinReqTp(self, value):
		self._NonFinReqTp = value if value is not None else base_types.UninitialisedField(self, 'NonFinReqTp', NonFinancialRequestType2Code, True)

	@NonFinReqTp.deleter
	def NonFinReqTp(self):
		del self._NonFinReqTp
		self._NonFinReqTp = base_types.UninitialisedField(self, 'NonFinReqTp', NonFinancialRequestType2Code, True)

	@property
	def Tx(self):
		return self._Tx

	@Tx.setter
	def Tx(self, value):
		self._Tx = value if value is not None else base_types.UninitialisedField(self, 'Tx', CardPaymentTransaction146, False)

	@Tx.deleter
	def Tx(self):
		del self._Tx
		self._Tx = base_types.UninitialisedField(self, 'Tx', CardPaymentTransaction146, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlReq', type=ExternallyDefinedData5, min=0, max=8, mutex_group=None, array=True),
		base_types.FieldEntry(name='NonFinReqTp', type=NonFinancialRequestType2Code, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tx', type=CardPaymentTransaction146, min=0, max=1, mutex_group=None, array=False),
	))