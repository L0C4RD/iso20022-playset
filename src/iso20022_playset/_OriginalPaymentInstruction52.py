from . import base_types
from ._DecimalNumber import DecimalNumber
from ._ExternalPaymentGroupStatus1Code import ExternalPaymentGroupStatus1Code
from ._Max15NumericText import Max15NumericText
from ._Max35Text import Max35Text
from ._NumberOfTransactionsPerStatus5 import NumberOfTransactionsPerStatus5
from ._PaymentTransaction169 import PaymentTransaction169
from ._StatusReasonInformation14 import StatusReasonInformation14

class OriginalPaymentInstruction52(base_types._BaseFieldType):

	__slots__ = ["_NbOfTxsPerSts", "_OrgnlCtrlSum", "_OrgnlNbOfTxs", "_OrgnlPmtInfId", "_PmtInfSts", "_StsRsnInf", "_TxInfAndSts"]
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
	def OrgnlPmtInfId(self):
		return self._OrgnlPmtInfId

	@OrgnlPmtInfId.setter
	def OrgnlPmtInfId(self, value):
		self._OrgnlPmtInfId = value if type(value) != base_types.auto else self.make_default("OrgnlPmtInfId")

	@OrgnlPmtInfId.deleter
	def OrgnlPmtInfId(self):
		del self._OrgnlPmtInfId
		self._OrgnlPmtInfId = None

	@property
	def PmtInfSts(self):
		return self._PmtInfSts

	@PmtInfSts.setter
	def PmtInfSts(self, value):
		self._PmtInfSts = value if type(value) != base_types.auto else self.make_default("PmtInfSts")

	@PmtInfSts.deleter
	def PmtInfSts(self):
		del self._PmtInfSts
		self._PmtInfSts = None

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

	@property
	def TxInfAndSts(self):
		return self._TxInfAndSts

	@TxInfAndSts.setter
	def TxInfAndSts(self, value):
		self._TxInfAndSts = value if type(value) != base_types.auto else self.make_default("TxInfAndSts")

	@TxInfAndSts.deleter
	def TxInfAndSts(self):
		del self._TxInfAndSts
		self._TxInfAndSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NbOfTxsPerSts', type=NumberOfTransactionsPerStatus5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlCtrlSum', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlNbOfTxs', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlPmtInfId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtInfSts', type=ExternalPaymentGroupStatus1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsRsnInf', type=StatusReasonInformation14, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxInfAndSts', type=PaymentTransaction169, min=0, max=None, mutex_group=None, array=True),
	))

