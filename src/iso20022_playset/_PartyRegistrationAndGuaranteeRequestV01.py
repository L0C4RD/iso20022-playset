from . import base_types
from ._FinancingAgreementList1 import FinancingAgreementList1
from ._BusinessLetter1 import BusinessLetter1
from ._DecimalNumber import DecimalNumber
from ._Max15NumericText import Max15NumericText
from ._EncapsulatedBusinessMessage1 import EncapsulatedBusinessMessage1

class PartyRegistrationAndGuaranteeRequestV01(base_types._BaseFieldType):

	__slots__ = ["_Hdr", "_AttchdMsg", "_AgrmtCnt", "_AgrmtList", "_CtrlSum", "_ItmCnt"]
	@property
	def AgrmtCnt(self):
		return self._AgrmtCnt

	@AgrmtCnt.setter
	def AgrmtCnt(self, value):
		self._AgrmtCnt = value if type(value) != base_types.auto else self.make_default("AgrmtCnt")

	@AgrmtCnt.deleter
	def AgrmtCnt(self):
		del self._AgrmtCnt
		self._AgrmtCnt = None

	@property
	def AgrmtList(self):
		return self._AgrmtList

	@AgrmtList.setter
	def AgrmtList(self, value):
		self._AgrmtList = value if type(value) != base_types.auto else self.make_default("AgrmtList")

	@AgrmtList.deleter
	def AgrmtList(self):
		del self._AgrmtList
		self._AgrmtList = None

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
		base_types.FieldEntry(name='AgrmtCnt', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgrmtList', type=FinancingAgreementList1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AttchdMsg', type=EncapsulatedBusinessMessage1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CtrlSum', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=BusinessLetter1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ItmCnt', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
	))

