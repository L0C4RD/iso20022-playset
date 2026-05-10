from . import base_types
from .EncapsulatedBusinessMessage1 import EncapsulatedBusinessMessage1
from .FinancingAgreementList1 import FinancingAgreementList1
from .DecimalNumber import DecimalNumber
from .BusinessLetter1 import BusinessLetter1
from .Max15NumericText import Max15NumericText

class PartyRegistrationAndGuaranteeNotificationV01(base_types._BaseFieldType):

	__slots__ = ["_CtrlSum", "_NtfctnCnt", "_Hdr", "_AttchdMsg", "_NtfctnList", "_ItmCnt"]
	@property
	def CtrlSum(self):
		return self._CtrlSum

	@CtrlSum.setter
	def CtrlSum(self, value):
		self._CtrlSum = value if type(value) != base_types.auto else self.make_default("CtrlSum")

	@CtrlSum.deleter
	def CtrlSum(self):
		del self._CtrlSum
		self._CtrlSum = None

	@property
	def NtfctnCnt(self):
		return self._NtfctnCnt

	@NtfctnCnt.setter
	def NtfctnCnt(self, value):
		self._NtfctnCnt = value if type(value) != base_types.auto else self.make_default("NtfctnCnt")

	@NtfctnCnt.deleter
	def NtfctnCnt(self):
		del self._NtfctnCnt
		self._NtfctnCnt = None

	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if type(value) != base_types.auto else self.make_default("Hdr")

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = None

	@property
	def AttchdMsg(self):
		return self._AttchdMsg

	@AttchdMsg.setter
	def AttchdMsg(self, value):
		self._AttchdMsg = value if type(value) != base_types.auto else self.make_default("AttchdMsg")

	@AttchdMsg.deleter
	def AttchdMsg(self):
		del self._AttchdMsg
		self._AttchdMsg = None

	@property
	def NtfctnList(self):
		return self._NtfctnList

	@NtfctnList.setter
	def NtfctnList(self, value):
		self._NtfctnList = value if type(value) != base_types.auto else self.make_default("NtfctnList")

	@NtfctnList.deleter
	def NtfctnList(self):
		del self._NtfctnList
		self._NtfctnList = None

	@property
	def ItmCnt(self):
		return self._ItmCnt

	@ItmCnt.setter
	def ItmCnt(self, value):
		self._ItmCnt = value if type(value) != base_types.auto else self.make_default("ItmCnt")

	@ItmCnt.deleter
	def ItmCnt(self):
		del self._ItmCnt
		self._ItmCnt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtrlSum', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtfctnCnt', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=BusinessLetter1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AttchdMsg', type=EncapsulatedBusinessMessage1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NtfctnList', type=FinancingAgreementList1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ItmCnt', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
	))

