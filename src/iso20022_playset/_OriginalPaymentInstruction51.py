# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DecimalNumber
from . import ExternalPaymentGroupStatus1Code
from . import Max15NumericText
from . import Max35Text
from . import NumberOfTransactionsPerStatus5
from . import PaymentTransaction160
from . import StatusReasonInformation14

class OriginalPaymentInstruction51(base_types._BaseFieldType):

	__slots__ = ["_NbOfTxsPerSts", "_OrgnlCtrlSum", "_OrgnlNbOfTxs", "_OrgnlPmtInfId", "_PmtInfSts", "_StsRsnInf", "_TxInfAndSts"]
	@property
	def NbOfTxsPerSts(self):
		return self._NbOfTxsPerSts

	@NbOfTxsPerSts.setter
	def NbOfTxsPerSts(self, value):
		self._NbOfTxsPerSts = value if value is not None else base_types.UninitialisedField(self, 'NbOfTxsPerSts', NumberOfTransactionsPerStatus5, True)

	@NbOfTxsPerSts.deleter
	def NbOfTxsPerSts(self):
		del self._NbOfTxsPerSts
		self._NbOfTxsPerSts = base_types.UninitialisedField(self, 'NbOfTxsPerSts', NumberOfTransactionsPerStatus5, True)

	@property
	def OrgnlCtrlSum(self):
		return self._OrgnlCtrlSum

	@OrgnlCtrlSum.setter
	def OrgnlCtrlSum(self, value):
		self._OrgnlCtrlSum = value if value is not None else base_types.UninitialisedField(self, 'OrgnlCtrlSum', DecimalNumber, False)

	@OrgnlCtrlSum.deleter
	def OrgnlCtrlSum(self):
		del self._OrgnlCtrlSum
		self._OrgnlCtrlSum = base_types.UninitialisedField(self, 'OrgnlCtrlSum', DecimalNumber, False)

	@property
	def OrgnlNbOfTxs(self):
		return self._OrgnlNbOfTxs

	@OrgnlNbOfTxs.setter
	def OrgnlNbOfTxs(self, value):
		self._OrgnlNbOfTxs = value if value is not None else base_types.UninitialisedField(self, 'OrgnlNbOfTxs', Max15NumericText, False)

	@OrgnlNbOfTxs.deleter
	def OrgnlNbOfTxs(self):
		del self._OrgnlNbOfTxs
		self._OrgnlNbOfTxs = base_types.UninitialisedField(self, 'OrgnlNbOfTxs', Max15NumericText, False)

	@property
	def OrgnlPmtInfId(self):
		return self._OrgnlPmtInfId

	@OrgnlPmtInfId.setter
	def OrgnlPmtInfId(self, value):
		self._OrgnlPmtInfId = value if value is not None else base_types.UninitialisedField(self, 'OrgnlPmtInfId', Max35Text, False)

	@OrgnlPmtInfId.deleter
	def OrgnlPmtInfId(self):
		del self._OrgnlPmtInfId
		self._OrgnlPmtInfId = base_types.UninitialisedField(self, 'OrgnlPmtInfId', Max35Text, False)

	@property
	def PmtInfSts(self):
		return self._PmtInfSts

	@PmtInfSts.setter
	def PmtInfSts(self, value):
		self._PmtInfSts = value if value is not None else base_types.UninitialisedField(self, 'PmtInfSts', ExternalPaymentGroupStatus1Code, False)

	@PmtInfSts.deleter
	def PmtInfSts(self):
		del self._PmtInfSts
		self._PmtInfSts = base_types.UninitialisedField(self, 'PmtInfSts', ExternalPaymentGroupStatus1Code, False)

	@property
	def StsRsnInf(self):
		return self._StsRsnInf

	@StsRsnInf.setter
	def StsRsnInf(self, value):
		self._StsRsnInf = value if value is not None else base_types.UninitialisedField(self, 'StsRsnInf', StatusReasonInformation14, True)

	@StsRsnInf.deleter
	def StsRsnInf(self):
		del self._StsRsnInf
		self._StsRsnInf = base_types.UninitialisedField(self, 'StsRsnInf', StatusReasonInformation14, True)

	@property
	def TxInfAndSts(self):
		return self._TxInfAndSts

	@TxInfAndSts.setter
	def TxInfAndSts(self, value):
		self._TxInfAndSts = value if value is not None else base_types.UninitialisedField(self, 'TxInfAndSts', PaymentTransaction160, True)

	@TxInfAndSts.deleter
	def TxInfAndSts(self):
		del self._TxInfAndSts
		self._TxInfAndSts = base_types.UninitialisedField(self, 'TxInfAndSts', PaymentTransaction160, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NbOfTxsPerSts', type=NumberOfTransactionsPerStatus5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlCtrlSum', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlNbOfTxs', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlPmtInfId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtInfSts', type=ExternalPaymentGroupStatus1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsRsnInf', type=StatusReasonInformation14, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxInfAndSts', type=PaymentTransaction160, min=0, max=None, mutex_group=None, array=True),
	))