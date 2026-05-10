import base_types
import FinancingAgreementList1
import Max15NumericText
import DecimalNumber
import BusinessLetter1
import EncapsulatedBusinessMessage1

class PartyRegistrationAndGuaranteeAcknowledgementV01(base_types._BaseFieldType):

	__slots__ = ["_ItmCnt", "_Hdr", "_AckList", "_AttchdMsg", "_CtrlSum", "_AckCnt"]
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
	def AckList(self):
		return self._AckList

	@AckList.setter
	def AckList(self, value):
		self._AckList = value if type(value) != auto else self.make_default("AckList")

	@AckList.deleter
	def AckList(self):
		del self._AckList
		self._AckList = None

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
	def AckCnt(self):
		return self._AckCnt

	@AckCnt.setter
	def AckCnt(self, value):
		self._AckCnt = value if type(value) != auto else self.make_default("AckCnt")

	@AckCnt.deleter
	def AckCnt(self):
		del self._AckCnt
		self._AckCnt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ItmCnt', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=BusinessLetter1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AckList', type=FinancingAgreementList1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AttchdMsg', type=EncapsulatedBusinessMessage1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CtrlSum', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AckCnt', type=Max15NumericText, min=1, max=1, mutex_group=None, array=False),
	))

