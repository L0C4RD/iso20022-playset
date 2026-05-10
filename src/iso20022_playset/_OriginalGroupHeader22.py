from . import base_types
from ._DecimalNumber import DecimalNumber
from ._ExternalPaymentGroupStatus1Code import ExternalPaymentGroupStatus1Code
from ._ISODateTime import ISODateTime
from ._Max15NumericText import Max15NumericText
from ._Max35Text import Max35Text
from ._NumberOfTransactionsPerStatus5 import NumberOfTransactionsPerStatus5
from ._StatusReasonInformation14 import StatusReasonInformation14

class OriginalGroupHeader22(base_types._BaseFieldType):

	__slots__ = ["_GrpSts", "_NbOfTxsPerSts", "_OrgnlCreDtTm", "_OrgnlCtrlSum", "_OrgnlMsgId", "_OrgnlMsgNmId", "_OrgnlNbOfTxs", "_StsRsnInf"]
	@property
	def GrpSts(self):
		return self._GrpSts

	@GrpSts.setter
	def GrpSts(self, value):
		self._GrpSts = value if type(value) != base_types.auto else self.make_default("GrpSts")

	@GrpSts.deleter
	def GrpSts(self):
		del self._GrpSts
		self._GrpSts = None

	@property
	def NbOfTxsPerSts(self):
		return self._NbOfTxsPerSts

	@NbOfTxsPerSts.setter
	def NbOfTxsPerSts(self, value):
		self._NbOfTxsPerSts = value if type(value) != base_types.auto else self.make_default("NbOfTxsPerSts")

	@NbOfTxsPerSts.deleter
	def NbOfTxsPerSts(self):
		del self._NbOfTxsPerSts
		self._NbOfTxsPerSts = None

	@property
	def OrgnlCreDtTm(self):
		return self._OrgnlCreDtTm

	@OrgnlCreDtTm.setter
	def OrgnlCreDtTm(self, value):
		self._OrgnlCreDtTm = value if type(value) != base_types.auto else self.make_default("OrgnlCreDtTm")

	@OrgnlCreDtTm.deleter
	def OrgnlCreDtTm(self):
		del self._OrgnlCreDtTm
		self._OrgnlCreDtTm = None

	@property
	def OrgnlCtrlSum(self):
		return self._OrgnlCtrlSum

	@OrgnlCtrlSum.setter
	def OrgnlCtrlSum(self, value):
		self._OrgnlCtrlSum = value if type(value) != base_types.auto else self.make_default("OrgnlCtrlSum")

	@OrgnlCtrlSum.deleter
	def OrgnlCtrlSum(self):
		del self._OrgnlCtrlSum
		self._OrgnlCtrlSum = None

	@property
	def OrgnlMsgId(self):
		return self._OrgnlMsgId

	@OrgnlMsgId.setter
	def OrgnlMsgId(self, value):
		self._OrgnlMsgId = value if type(value) != base_types.auto else self.make_default("OrgnlMsgId")

	@OrgnlMsgId.deleter
	def OrgnlMsgId(self):
		del self._OrgnlMsgId
		self._OrgnlMsgId = None

	@property
	def OrgnlMsgNmId(self):
		return self._OrgnlMsgNmId

	@OrgnlMsgNmId.setter
	def OrgnlMsgNmId(self, value):
		self._OrgnlMsgNmId = value if type(value) != base_types.auto else self.make_default("OrgnlMsgNmId")

	@OrgnlMsgNmId.deleter
	def OrgnlMsgNmId(self):
		del self._OrgnlMsgNmId
		self._OrgnlMsgNmId = None

	@property
	def OrgnlNbOfTxs(self):
		return self._OrgnlNbOfTxs

	@OrgnlNbOfTxs.setter
	def OrgnlNbOfTxs(self, value):
		self._OrgnlNbOfTxs = value if type(value) != base_types.auto else self.make_default("OrgnlNbOfTxs")

	@OrgnlNbOfTxs.deleter
	def OrgnlNbOfTxs(self):
		del self._OrgnlNbOfTxs
		self._OrgnlNbOfTxs = None

	@property
	def StsRsnInf(self):
		return self._StsRsnInf

	@StsRsnInf.setter
	def StsRsnInf(self, value):
		self._StsRsnInf = value if type(value) != base_types.auto else self.make_default("StsRsnInf")

	@StsRsnInf.deleter
	def StsRsnInf(self):
		del self._StsRsnInf
		self._StsRsnInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='GrpSts', type=ExternalPaymentGroupStatus1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfTxsPerSts', type=NumberOfTransactionsPerStatus5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlCreDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlCtrlSum', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlMsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlMsgNmId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlNbOfTxs', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsRsnInf', type=StatusReasonInformation14, min=0, max=None, mutex_group=None, array=True),
	))

