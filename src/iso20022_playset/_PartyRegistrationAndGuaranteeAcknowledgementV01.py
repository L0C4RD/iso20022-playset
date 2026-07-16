# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BusinessLetter1
from . import DecimalNumber
from . import EncapsulatedBusinessMessage1
from . import FinancingAgreementList1
from . import Max15NumericText

class PartyRegistrationAndGuaranteeAcknowledgementV01(base_types._BaseFieldType):

	__slots__ = ["_AckCnt", "_AckList", "_AttchdMsg", "_CtrlSum", "_Hdr", "_ItmCnt"]
	@property
	def AckCnt(self):
		return self._AckCnt

	@AckCnt.setter
	def AckCnt(self, value):
		self._AckCnt = value if value is not None else base_types.UninitialisedField(self, 'AckCnt', Max15NumericText, False)

	@AckCnt.deleter
	def AckCnt(self):
		del self._AckCnt
		self._AckCnt = base_types.UninitialisedField(self, 'AckCnt', Max15NumericText, False)

	@property
	def AckList(self):
		return self._AckList

	@AckList.setter
	def AckList(self, value):
		self._AckList = value if value is not None else base_types.UninitialisedField(self, 'AckList', FinancingAgreementList1, True)

	@AckList.deleter
	def AckList(self):
		del self._AckList
		self._AckList = base_types.UninitialisedField(self, 'AckList', FinancingAgreementList1, True)

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
		base_types.FieldEntry(name='AckCnt', type=Max15NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AckList', type=FinancingAgreementList1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AttchdMsg', type=EncapsulatedBusinessMessage1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CtrlSum', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=BusinessLetter1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ItmCnt', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
	))