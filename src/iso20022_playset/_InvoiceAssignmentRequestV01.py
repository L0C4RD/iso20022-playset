# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BusinessLetter1
from . import DecimalNumber
from . import EncapsulatedBusinessMessage1
from . import FinancingItemList1
from . import Max15NumericText

class InvoiceAssignmentRequestV01(base_types._BaseFieldType):

	__slots__ = ["_AssgnmtCnt", "_AssgnmtList", "_AttchdMsg", "_CtrlSum", "_Hdr", "_ItmCnt"]
	@property
	def AssgnmtCnt(self):
		return self._AssgnmtCnt

	@AssgnmtCnt.setter
	def AssgnmtCnt(self, value):
		self._AssgnmtCnt = value if value is not None else base_types.UninitialisedField(self, 'AssgnmtCnt', Max15NumericText, False)

	@AssgnmtCnt.deleter
	def AssgnmtCnt(self):
		del self._AssgnmtCnt
		self._AssgnmtCnt = base_types.UninitialisedField(self, 'AssgnmtCnt', Max15NumericText, False)

	@property
	def AssgnmtList(self):
		return self._AssgnmtList

	@AssgnmtList.setter
	def AssgnmtList(self, value):
		self._AssgnmtList = value if value is not None else base_types.UninitialisedField(self, 'AssgnmtList', FinancingItemList1, True)

	@AssgnmtList.deleter
	def AssgnmtList(self):
		del self._AssgnmtList
		self._AssgnmtList = base_types.UninitialisedField(self, 'AssgnmtList', FinancingItemList1, True)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AssgnmtCnt', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AssgnmtList', type=FinancingItemList1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AttchdMsg', type=EncapsulatedBusinessMessage1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CtrlSum', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=BusinessLetter1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ItmCnt', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
	))