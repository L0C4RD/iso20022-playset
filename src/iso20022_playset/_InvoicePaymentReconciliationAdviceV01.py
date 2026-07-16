# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BusinessLetter1
from . import DecimalNumber
from . import EncapsulatedBusinessMessage1
from . import Max15NumericText
from . import ReconciliationList1

class InvoicePaymentReconciliationAdviceV01(base_types._BaseFieldType):

	__slots__ = ["_AttchdMsg", "_CtrlSum", "_Hdr", "_ItmCnt", "_RcncltnCnt", "_RcncltnList"]
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
	def RcncltnCnt(self):
		return self._RcncltnCnt

	@RcncltnCnt.setter
	def RcncltnCnt(self, value):
		self._RcncltnCnt = value if value is not None else base_types.UninitialisedField(self, 'RcncltnCnt', Max15NumericText, False)

	@RcncltnCnt.deleter
	def RcncltnCnt(self):
		del self._RcncltnCnt
		self._RcncltnCnt = base_types.UninitialisedField(self, 'RcncltnCnt', Max15NumericText, False)

	@property
	def RcncltnList(self):
		return self._RcncltnList

	@RcncltnList.setter
	def RcncltnList(self, value):
		self._RcncltnList = value if value is not None else base_types.UninitialisedField(self, 'RcncltnList', ReconciliationList1, True)

	@RcncltnList.deleter
	def RcncltnList(self):
		del self._RcncltnList
		self._RcncltnList = base_types.UninitialisedField(self, 'RcncltnList', ReconciliationList1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AttchdMsg', type=EncapsulatedBusinessMessage1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CtrlSum', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=BusinessLetter1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ItmCnt', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnCnt', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnList', type=ReconciliationList1, min=1, max=None, mutex_group=None, array=True),
	))