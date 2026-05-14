# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BusinessLetter1 import BusinessLetter1
from ._DecimalNumber import DecimalNumber
from ._EncapsulatedBusinessMessage1 import EncapsulatedBusinessMessage1
from ._FinancingItemList1 import FinancingItemList1
from ._Max15NumericText import Max15NumericText

class InvoiceAssignmentAcknowledgementV01(base_types._BaseFieldType):

	__slots__ = ["_AttchdMsg", "_CtrlSum", "_Hdr", "_ItmCnt", "_PmtStsCnt", "_PmtStsList"]
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

	@property
	def PmtStsCnt(self):
		return self._PmtStsCnt

	@PmtStsCnt.setter
	def PmtStsCnt(self, value):
		self._PmtStsCnt = value if type(value) != base_types.auto else self.make_default("PmtStsCnt")

	@PmtStsCnt.deleter
	def PmtStsCnt(self):
		del self._PmtStsCnt
		self._PmtStsCnt = None

	@property
	def PmtStsList(self):
		return self._PmtStsList

	@PmtStsList.setter
	def PmtStsList(self, value):
		self._PmtStsList = value if type(value) != base_types.auto else self.make_default("PmtStsList")

	@PmtStsList.deleter
	def PmtStsList(self):
		del self._PmtStsList
		self._PmtStsList = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AttchdMsg', type=EncapsulatedBusinessMessage1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CtrlSum', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=BusinessLetter1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ItmCnt', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtStsCnt', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtStsList', type=FinancingItemList1, min=1, max=None, mutex_group=None, array=True),
	))