from . import base_types
from .Max15NumericText import Max15NumericText
from .BusinessLetter1 import BusinessLetter1
from .ReconciliationList1 import ReconciliationList1
from .EncapsulatedBusinessMessage1 import EncapsulatedBusinessMessage1
from .DecimalNumber import DecimalNumber

class InvoicePaymentReconciliationStatusV01(base_types._BaseFieldType):

	__slots__ = ["_AttchdMsg", "_ItmCnt", "_RcncltnList", "_RcncltnCnt", "_Hdr", "_CtrlSum"]
	@property
	def AttchdMsg(self):
		return self._AttchdMsg

	@AttchdMsg.setter
	def AttchdMsg(self, value):
		self._AttchdMsg = value if type(value) != auto else self.make_default("AttchdMsg")

	@AttchdMsg.deleter
	def AttchdMsg(self):
		del self._AttchdMsg
		self._AttchdMsg = None

	@property
	def ItmCnt(self):
		return self._ItmCnt

	@ItmCnt.setter
	def ItmCnt(self, value):
		self._ItmCnt = value if type(value) != auto else self.make_default("ItmCnt")

	@ItmCnt.deleter
	def ItmCnt(self):
		del self._ItmCnt
		self._ItmCnt = None

	@property
	def RcncltnList(self):
		return self._RcncltnList

	@RcncltnList.setter
	def RcncltnList(self, value):
		self._RcncltnList = value if type(value) != auto else self.make_default("RcncltnList")

	@RcncltnList.deleter
	def RcncltnList(self):
		del self._RcncltnList
		self._RcncltnList = None

	@property
	def RcncltnCnt(self):
		return self._RcncltnCnt

	@RcncltnCnt.setter
	def RcncltnCnt(self, value):
		self._RcncltnCnt = value if type(value) != auto else self.make_default("RcncltnCnt")

	@RcncltnCnt.deleter
	def RcncltnCnt(self):
		del self._RcncltnCnt
		self._RcncltnCnt = None

	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if type(value) != auto else self.make_default("Hdr")

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = None

	@property
	def CtrlSum(self):
		return self._CtrlSum

	@CtrlSum.setter
	def CtrlSum(self, value):
		self._CtrlSum = value if type(value) != auto else self.make_default("CtrlSum")

	@CtrlSum.deleter
	def CtrlSum(self):
		del self._CtrlSum
		self._CtrlSum = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AttchdMsg', type=EncapsulatedBusinessMessage1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ItmCnt', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnList', type=ReconciliationList1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RcncltnCnt', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=BusinessLetter1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrlSum', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
	))

