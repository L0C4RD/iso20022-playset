import base_types
import Max15NumericText
import EncapsulatedBusinessMessage1
import DecimalNumber
import BusinessLetter1
import FinancingItemList1

class InvoiceAssignmentAcknowledgementV01(base_types._BaseFieldType):

	__slots__ = ["_ItmCnt", "_Hdr", "_PmtStsList", "_AttchdMsg", "_CtrlSum", "_PmtStsCnt"]
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
	def PmtStsList(self):
		return self._PmtStsList

	@PmtStsList.setter
	def PmtStsList(self, value):
		self._PmtStsList = value if type(value) != auto else self.make_default("PmtStsList")

	@PmtStsList.deleter
	def PmtStsList(self):
		del self._PmtStsList
		self._PmtStsList = None

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
	def CtrlSum(self):
		return self._CtrlSum

	@CtrlSum.setter
	def CtrlSum(self, value):
		self._CtrlSum = value if type(value) != auto else self.make_default("CtrlSum")

	@CtrlSum.deleter
	def CtrlSum(self):
		del self._CtrlSum
		self._CtrlSum = None

	@property
	def PmtStsCnt(self):
		return self._PmtStsCnt

	@PmtStsCnt.setter
	def PmtStsCnt(self, value):
		self._PmtStsCnt = value if type(value) != auto else self.make_default("PmtStsCnt")

	@PmtStsCnt.deleter
	def PmtStsCnt(self):
		del self._PmtStsCnt
		self._PmtStsCnt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ItmCnt', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=BusinessLetter1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtStsList', type=FinancingItemList1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AttchdMsg', type=EncapsulatedBusinessMessage1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CtrlSum', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtStsCnt', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
	))

