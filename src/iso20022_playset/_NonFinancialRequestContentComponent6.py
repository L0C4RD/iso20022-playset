# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CardPaymentTransaction146 import CardPaymentTransaction146
from ._ExternallyDefinedData5 import ExternallyDefinedData5
from ._NonFinancialRequestType2Code import NonFinancialRequestType2Code

class NonFinancialRequestContentComponent6(base_types._BaseFieldType):

	__slots__ = ["_AddtlReq", "_NonFinReqTp", "_Tx"]
	@property
	def AddtlReq(self):
		return self._AddtlReq

	@AddtlReq.setter
	def AddtlReq(self, value):
		self._AddtlReq = value if type(value) != base_types.auto else self.make_default("AddtlReq")

	@AddtlReq.deleter
	def AddtlReq(self):
		del self._AddtlReq
		self._AddtlReq = None

	@property
	def NonFinReqTp(self):
		return self._NonFinReqTp

	@NonFinReqTp.setter
	def NonFinReqTp(self, value):
		self._NonFinReqTp = value if type(value) != base_types.auto else self.make_default("NonFinReqTp")

	@NonFinReqTp.deleter
	def NonFinReqTp(self):
		del self._NonFinReqTp
		self._NonFinReqTp = None

	@property
	def Tx(self):
		return self._Tx

	@Tx.setter
	def Tx(self, value):
		self._Tx = value if type(value) != base_types.auto else self.make_default("Tx")

	@Tx.deleter
	def Tx(self):
		del self._Tx
		self._Tx = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlReq', type=ExternallyDefinedData5, min=0, max=8, mutex_group=None, array=True),
		base_types.FieldEntry(name='NonFinReqTp', type=NonFinancialRequestType2Code, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tx', type=CardPaymentTransaction146, min=0, max=1, mutex_group=None, array=False),
	))