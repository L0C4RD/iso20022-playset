import base_types
import ExternallyDefinedData5
import CardPaymentTransaction139
import NonFinancialRequestType2Code

class NonFinancialRequestContentComponent5(base_types._BaseFieldType):

	__slots__ = ["_Tx", "_AddtlReq", "_NonFinReqTp"]
	@property
	def Tx(self):
		return self._Tx

	@Tx.setter
	def Tx(self, value):
		self._Tx = value if type(value) != auto else self.make_default("Tx")

	@Tx.deleter
	def Tx(self):
		del self._Tx
		self._Tx = None

	@property
	def AddtlReq(self):
		return self._AddtlReq

	@AddtlReq.setter
	def AddtlReq(self, value):
		self._AddtlReq = value if type(value) != auto else self.make_default("AddtlReq")

	@AddtlReq.deleter
	def AddtlReq(self):
		del self._AddtlReq
		self._AddtlReq = None

	@property
	def NonFinReqTp(self):
		return self._NonFinReqTp

	@NonFinReqTp.setter
	def NonFinReqTp(self, value):
		self._NonFinReqTp = value if type(value) != auto else self.make_default("NonFinReqTp")

	@NonFinReqTp.deleter
	def NonFinReqTp(self):
		del self._NonFinReqTp
		self._NonFinReqTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tx', type=CardPaymentTransaction139, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlReq', type=ExternallyDefinedData5, min=0, max=8, mutex_group=None, array=True),
		base_types.FieldEntry(name='NonFinReqTp', type=NonFinancialRequestType2Code, min=1, max=None, mutex_group=None, array=True),
	))

