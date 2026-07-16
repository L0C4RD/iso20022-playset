# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BusinessLetter1
from . import DecimalNumber
from . import EncapsulatedBusinessMessage1
from . import FinancingAgreementList1
from . import Max15NumericText

class PartyRegistrationAndGuaranteeRequestV01(base_types._BaseFieldType):

	__slots__ = ["_AgrmtCnt", "_AgrmtList", "_AttchdMsg", "_CtrlSum", "_Hdr", "_ItmCnt"]
	@property
	def AgrmtCnt(self):
		return self._AgrmtCnt

	@AgrmtCnt.setter
	def AgrmtCnt(self, value):
		self._AgrmtCnt = value if value is not None else base_types.UninitialisedField(self, 'AgrmtCnt', Max15NumericText, False)

	@AgrmtCnt.deleter
	def AgrmtCnt(self):
		del self._AgrmtCnt
		self._AgrmtCnt = base_types.UninitialisedField(self, 'AgrmtCnt', Max15NumericText, False)

	@property
	def AgrmtList(self):
		return self._AgrmtList

	@AgrmtList.setter
	def AgrmtList(self, value):
		self._AgrmtList = value if value is not None else base_types.UninitialisedField(self, 'AgrmtList', FinancingAgreementList1, True)

	@AgrmtList.deleter
	def AgrmtList(self):
		del self._AgrmtList
		self._AgrmtList = base_types.UninitialisedField(self, 'AgrmtList', FinancingAgreementList1, True)

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
		base_types.FieldEntry(name='AgrmtCnt', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgrmtList', type=FinancingAgreementList1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AttchdMsg', type=EncapsulatedBusinessMessage1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CtrlSum', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=BusinessLetter1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ItmCnt', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
	))