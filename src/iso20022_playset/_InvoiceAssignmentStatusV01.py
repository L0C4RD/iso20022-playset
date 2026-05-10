from . import base_types
from ._BusinessLetter1 import BusinessLetter1
from ._DecimalNumber import DecimalNumber
from ._EncapsulatedBusinessMessage1 import EncapsulatedBusinessMessage1
from ._FinancingItemList1 import FinancingItemList1
from ._Max15NumericText import Max15NumericText

class InvoiceAssignmentStatusV01(base_types._BaseFieldType):

	__slots__ = ["_AssgnmtCnt", "_AssgnmtList", "_AttchdMsg", "_CtrlSum", "_Hdr", "_ItmCnt"]
	@property
	def AssgnmtCnt(self):
		return self._AssgnmtCnt

	@AssgnmtCnt.setter
	def AssgnmtCnt(self, value):
		self._AssgnmtCnt = value if type(value) != base_types.auto else self.make_default("AssgnmtCnt")

	@AssgnmtCnt.deleter
	def AssgnmtCnt(self):
		del self._AssgnmtCnt
		self._AssgnmtCnt = None

	@property
	def AssgnmtList(self):
		return self._AssgnmtList

	@AssgnmtList.setter
	def AssgnmtList(self, value):
		self._AssgnmtList = value if type(value) != base_types.auto else self.make_default("AssgnmtList")

	@AssgnmtList.deleter
	def AssgnmtList(self):
		del self._AssgnmtList
		self._AssgnmtList = None

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
		base_types.FieldEntry(name='AssgnmtCnt', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AssgnmtList', type=FinancingItemList1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AttchdMsg', type=EncapsulatedBusinessMessage1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CtrlSum', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=BusinessLetter1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ItmCnt', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
	))

