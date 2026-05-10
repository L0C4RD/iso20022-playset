from . import base_types
from ._ReversalResponse9 import ReversalResponse9
from ._CardAcquisitionResponse3 import CardAcquisitionResponse3
from ._GenericIdentification177 import GenericIdentification177
from ._ResponseType11 import ResponseType11
from ._StoredValueResponse8 import StoredValueResponse8
from ._Max35Text import Max35Text
from ._LoyaltyResponse3 import LoyaltyResponse3
from ._DeviceSendApplicationProtocolDataUnitCardReaderResponse1 import DeviceSendApplicationProtocolDataUnitCardReaderResponse1
from ._PaymentResponse7 import PaymentResponse7

class MessageStatusResponseData9(base_types._BaseFieldType):

	__slots__ = ["_RpeatdRvslRspn", "_RpeatdLltyRspn", "_RpeatdSndApplPrtcolDataUnitCardRdrRspn", "_TxRspn", "_RpeatdCardAcqstnRspn", "_RpeatdPmtRspn", "_RpeatdStordValRspn", "_InitgPty", "_XchgId"]
	@property
	def InitgPty(self):
		return self._InitgPty

	@InitgPty.setter
	def InitgPty(self, value):
		self._InitgPty = value if type(value) != base_types.auto else self.make_default("InitgPty")

	@InitgPty.deleter
	def InitgPty(self):
		del self._InitgPty
		self._InitgPty = None

	@property
	def RpeatdCardAcqstnRspn(self):
		return self._RpeatdCardAcqstnRspn

	@RpeatdCardAcqstnRspn.setter
	def RpeatdCardAcqstnRspn(self, value):
		self._RpeatdCardAcqstnRspn = value if type(value) != base_types.auto else self.make_default("RpeatdCardAcqstnRspn")

	@RpeatdCardAcqstnRspn.deleter
	def RpeatdCardAcqstnRspn(self):
		del self._RpeatdCardAcqstnRspn
		self._RpeatdCardAcqstnRspn = None

	@property
	def RpeatdLltyRspn(self):
		return self._RpeatdLltyRspn

	@RpeatdLltyRspn.setter
	def RpeatdLltyRspn(self, value):
		self._RpeatdLltyRspn = value if type(value) != base_types.auto else self.make_default("RpeatdLltyRspn")

	@RpeatdLltyRspn.deleter
	def RpeatdLltyRspn(self):
		del self._RpeatdLltyRspn
		self._RpeatdLltyRspn = None

	@property
	def RpeatdPmtRspn(self):
		return self._RpeatdPmtRspn

	@RpeatdPmtRspn.setter
	def RpeatdPmtRspn(self, value):
		self._RpeatdPmtRspn = value if type(value) != base_types.auto else self.make_default("RpeatdPmtRspn")

	@RpeatdPmtRspn.deleter
	def RpeatdPmtRspn(self):
		del self._RpeatdPmtRspn
		self._RpeatdPmtRspn = None

	@property
	def RpeatdRvslRspn(self):
		return self._RpeatdRvslRspn

	@RpeatdRvslRspn.setter
	def RpeatdRvslRspn(self, value):
		self._RpeatdRvslRspn = value if type(value) != base_types.auto else self.make_default("RpeatdRvslRspn")

	@RpeatdRvslRspn.deleter
	def RpeatdRvslRspn(self):
		del self._RpeatdRvslRspn
		self._RpeatdRvslRspn = None

	@property
	def RpeatdSndApplPrtcolDataUnitCardRdrRspn(self):
		return self._RpeatdSndApplPrtcolDataUnitCardRdrRspn

	@RpeatdSndApplPrtcolDataUnitCardRdrRspn.setter
	def RpeatdSndApplPrtcolDataUnitCardRdrRspn(self, value):
		self._RpeatdSndApplPrtcolDataUnitCardRdrRspn = value if type(value) != base_types.auto else self.make_default("RpeatdSndApplPrtcolDataUnitCardRdrRspn")

	@RpeatdSndApplPrtcolDataUnitCardRdrRspn.deleter
	def RpeatdSndApplPrtcolDataUnitCardRdrRspn(self):
		del self._RpeatdSndApplPrtcolDataUnitCardRdrRspn
		self._RpeatdSndApplPrtcolDataUnitCardRdrRspn = None

	@property
	def RpeatdStordValRspn(self):
		return self._RpeatdStordValRspn

	@RpeatdStordValRspn.setter
	def RpeatdStordValRspn(self, value):
		self._RpeatdStordValRspn = value if type(value) != base_types.auto else self.make_default("RpeatdStordValRspn")

	@RpeatdStordValRspn.deleter
	def RpeatdStordValRspn(self):
		del self._RpeatdStordValRspn
		self._RpeatdStordValRspn = None

	@property
	def TxRspn(self):
		return self._TxRspn

	@TxRspn.setter
	def TxRspn(self, value):
		self._TxRspn = value if type(value) != base_types.auto else self.make_default("TxRspn")

	@TxRspn.deleter
	def TxRspn(self):
		del self._TxRspn
		self._TxRspn = None

	@property
	def XchgId(self):
		return self._XchgId

	@XchgId.setter
	def XchgId(self, value):
		self._XchgId = value if type(value) != base_types.auto else self.make_default("XchgId")

	@XchgId.deleter
	def XchgId(self):
		del self._XchgId
		self._XchgId = None

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

