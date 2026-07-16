# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BusinessLetter1
from . import DecimalNumber
from . import EncapsulatedBusinessMessage1
from . import FinancingItemList1
from . import Max15NumericText

class InvoiceAssignmentAcknowledgementV01(base_types._BaseFieldType):

	__slots__ = ["_AttchdMsg", "_CtrlSum", "_Hdr", "_ItmCnt", "_PmtStsCnt", "_PmtStsList"]
	@property
	def AttchdMsg(self):
		return self._AttchdMsg

	@AttchdMsg.setter
	def AttchdMsg(self, value):
		self._AttchdMsg = value if value is not None else base_types.UninitialisedField(self, 'AttchdMsg', EncapsulatedBusinessMessage1, True)

	@AttchdMsg.deleter
	def AttchdMsg(self):
		del self._AttchdMsg
		self._AttchdMsg = base_types.UninitialisedField(self, 'AttchdMsg', EncapsulatedBusinessMessage1, True)

	@property
	def CtrlSum(self):
		return self._CtrlSum

	@CtrlSum.setter
	def CtrlSum(self, value):
		self._CtrlSum = value if value is not None else base_types.UninitialisedField(self, 'CtrlSum', DecimalNumber, False)

	@CtrlSum.deleter
	def CtrlSum(self):
		del self._CtrlSum
		self._CtrlSum = base_types.UninitialisedField(self, 'CtrlSum', DecimalNumber, False)

	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if value is not None else base_types.UninitialisedField(self, 'Hdr', BusinessLetter1, False)

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = base_types.UninitialisedField(self, 'Hdr', BusinessLetter1, False)

	@property
	def ItmCnt(self):
		return self._ItmCnt

	@ItmCnt.setter
	def ItmCnt(self, value):
		self._ItmCnt = value if value is not None else base_types.UninitialisedField(self, 'ItmCnt', Max15NumericText, False)

	@ItmCnt.deleter
	def ItmCnt(self):
		del self._ItmCnt
		self._ItmCnt = base_types.UninitialisedField(self, 'ItmCnt', Max15NumericText, False)

	@property
	def PmtStsCnt(self):
		return self._PmtStsCnt

	@PmtStsCnt.setter
	def PmtStsCnt(self, value):
		self._PmtStsCnt = value if value is not None else base_types.UninitialisedField(self, 'PmtStsCnt', Max15NumericText, False)

	@PmtStsCnt.deleter
	def PmtStsCnt(self):
		del self._PmtStsCnt
		self._PmtStsCnt = base_types.UninitialisedField(self, 'PmtStsCnt', Max15NumericText, False)

	@property
	def PmtStsList(self):
		return self._PmtStsList

	@PmtStsList.setter
	def PmtStsList(self, value):
		self._PmtStsList = value if value is not None else base_types.UninitialisedField(self, 'PmtStsList', FinancingItemList1, True)

	@PmtStsList.deleter
	def PmtStsList(self):
		del self._PmtStsList
		self._PmtStsList = base_types.UninitialisedField(self, 'PmtStsList', FinancingItemList1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AttchdMsg', type=EncapsulatedBusinessMessage1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CtrlSum', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=BusinessLetter1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ItmCnt', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtStsCnt', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtStsList', type=FinancingItemList1, min=1, max=None, mutex_group=None, array=True),
	))