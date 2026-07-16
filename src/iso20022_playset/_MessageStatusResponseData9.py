# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CardAcquisitionResponse3
from . import DeviceSendApplicationProtocolDataUnitCardReaderResponse1
from . import GenericIdentification177
from . import LoyaltyResponse3
from . import Max35Text
from . import PaymentResponse7
from . import ResponseType11
from . import ReversalResponse9
from . import StoredValueResponse8

class MessageStatusResponseData9(base_types._BaseFieldType):

	__slots__ = ["_InitgPty", "_RpeatdCardAcqstnRspn", "_RpeatdLltyRspn", "_RpeatdPmtRspn", "_RpeatdRvslRspn", "_RpeatdSndApplPrtcolDataUnitCardRdrRspn", "_RpeatdStordValRspn", "_TxRspn", "_XchgId"]
	@property
	def InitgPty(self):
		return self._InitgPty

	@InitgPty.setter
	def InitgPty(self, value):
		self._InitgPty = value if value is not None else base_types.UninitialisedField(self, 'InitgPty', GenericIdentification177, False)

	@InitgPty.deleter
	def InitgPty(self):
		del self._InitgPty
		self._InitgPty = base_types.UninitialisedField(self, 'InitgPty', GenericIdentification177, False)

	@property
	def RpeatdCardAcqstnRspn(self):
		return self._RpeatdCardAcqstnRspn

	@RpeatdCardAcqstnRspn.setter
	def RpeatdCardAcqstnRspn(self, value):
		self._RpeatdCardAcqstnRspn = value if value is not None else base_types.UninitialisedField(self, 'RpeatdCardAcqstnRspn', CardAcquisitionResponse3, False)

	@RpeatdCardAcqstnRspn.deleter
	def RpeatdCardAcqstnRspn(self):
		del self._RpeatdCardAcqstnRspn
		self._RpeatdCardAcqstnRspn = base_types.UninitialisedField(self, 'RpeatdCardAcqstnRspn', CardAcquisitionResponse3, False)

	@property
	def RpeatdLltyRspn(self):
		return self._RpeatdLltyRspn

	@RpeatdLltyRspn.setter
	def RpeatdLltyRspn(self, value):
		self._RpeatdLltyRspn = value if value is not None else base_types.UninitialisedField(self, 'RpeatdLltyRspn', LoyaltyResponse3, False)

	@RpeatdLltyRspn.deleter
	def RpeatdLltyRspn(self):
		del self._RpeatdLltyRspn
		self._RpeatdLltyRspn = base_types.UninitialisedField(self, 'RpeatdLltyRspn', LoyaltyResponse3, False)

	@property
	def RpeatdPmtRspn(self):
		return self._RpeatdPmtRspn

	@RpeatdPmtRspn.setter
	def RpeatdPmtRspn(self, value):
		self._RpeatdPmtRspn = value if value is not None else base_types.UninitialisedField(self, 'RpeatdPmtRspn', PaymentResponse7, False)

	@RpeatdPmtRspn.deleter
	def RpeatdPmtRspn(self):
		del self._RpeatdPmtRspn
		self._RpeatdPmtRspn = base_types.UninitialisedField(self, 'RpeatdPmtRspn', PaymentResponse7, False)

	@property
	def RpeatdRvslRspn(self):
		return self._RpeatdRvslRspn

	@RpeatdRvslRspn.setter
	def RpeatdRvslRspn(self, value):
		self._RpeatdRvslRspn = value if value is not None else base_types.UninitialisedField(self, 'RpeatdRvslRspn', ReversalResponse9, False)

	@RpeatdRvslRspn.deleter
	def RpeatdRvslRspn(self):
		del self._RpeatdRvslRspn
		self._RpeatdRvslRspn = base_types.UninitialisedField(self, 'RpeatdRvslRspn', ReversalResponse9, False)

	@property
	def RpeatdSndApplPrtcolDataUnitCardRdrRspn(self):
		return self._RpeatdSndApplPrtcolDataUnitCardRdrRspn

	@RpeatdSndApplPrtcolDataUnitCardRdrRspn.setter
	def RpeatdSndApplPrtcolDataUnitCardRdrRspn(self, value):
		self._RpeatdSndApplPrtcolDataUnitCardRdrRspn = value if value is not None else base_types.UninitialisedField(self, 'RpeatdSndApplPrtcolDataUnitCardRdrRspn', DeviceSendApplicationProtocolDataUnitCardReaderResponse1, False)

	@RpeatdSndApplPrtcolDataUnitCardRdrRspn.deleter
	def RpeatdSndApplPrtcolDataUnitCardRdrRspn(self):
		del self._RpeatdSndApplPrtcolDataUnitCardRdrRspn
		self._RpeatdSndApplPrtcolDataUnitCardRdrRspn = base_types.UninitialisedField(self, 'RpeatdSndApplPrtcolDataUnitCardRdrRspn', DeviceSendApplicationProtocolDataUnitCardReaderResponse1, False)

	@property
	def RpeatdStordValRspn(self):
		return self._RpeatdStordValRspn

	@RpeatdStordValRspn.setter
	def RpeatdStordValRspn(self, value):
		self._RpeatdStordValRspn = value if value is not None else base_types.UninitialisedField(self, 'RpeatdStordValRspn', StoredValueResponse8, False)

	@RpeatdStordValRspn.deleter
	def RpeatdStordValRspn(self):
		del self._RpeatdStordValRspn
		self._RpeatdStordValRspn = base_types.UninitialisedField(self, 'RpeatdStordValRspn', StoredValueResponse8, False)

	@property
	def TxRspn(self):
		return self._TxRspn

	@TxRspn.setter
	def TxRspn(self, value):
		self._TxRspn = value if value is not None else base_types.UninitialisedField(self, 'TxRspn', ResponseType11, False)

	@TxRspn.deleter
	def TxRspn(self):
		del self._TxRspn
		self._TxRspn = base_types.UninitialisedField(self, 'TxRspn', ResponseType11, False)

	@property
	def XchgId(self):
		return self._XchgId

	@XchgId.setter
	def XchgId(self, value):
		self._XchgId = value if value is not None else base_types.UninitialisedField(self, 'XchgId', Max35Text, False)

	@XchgId.deleter
	def XchgId(self):
		del self._XchgId
		self._XchgId = base_types.UninitialisedField(self, 'XchgId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='InitgPty', type=GenericIdentification177, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RpeatdCardAcqstnRspn', type=CardAcquisitionResponse3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RpeatdLltyRspn', type=LoyaltyResponse3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RpeatdPmtRspn', type=PaymentResponse7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RpeatdRvslRspn', type=ReversalResponse9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RpeatdSndApplPrtcolDataUnitCardRdrRspn', type=DeviceSendApplicationProtocolDataUnitCardReaderResponse1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RpeatdStordValRspn', type=StoredValueResponse8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxRspn', type=ResponseType11, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))