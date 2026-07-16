# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DecimalNumber
from . import ExternalPaymentGroupStatus1Code
from . import ISODateTime
from . import Max15NumericText
from . import Max35Text
from . import NumberOfTransactionsPerStatus5
from . import StatusReasonInformation14

class OriginalGroupHeader22(base_types._BaseFieldType):

	__slots__ = ["_GrpSts", "_NbOfTxsPerSts", "_OrgnlCreDtTm", "_OrgnlCtrlSum", "_OrgnlMsgId", "_OrgnlMsgNmId", "_OrgnlNbOfTxs", "_StsRsnInf"]
	@property
	def GrpSts(self):
		return self._GrpSts

	@GrpSts.setter
	def GrpSts(self, value):
		self._GrpSts = value if value is not None else base_types.UninitialisedField(self, 'GrpSts', ExternalPaymentGroupStatus1Code, False)

	@GrpSts.deleter
	def GrpSts(self):
		del self._GrpSts
		self._GrpSts = base_types.UninitialisedField(self, 'GrpSts', ExternalPaymentGroupStatus1Code, False)

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
	def OrgnlCreDtTm(self):
		return self._OrgnlCreDtTm

	@OrgnlCreDtTm.setter
	def OrgnlCreDtTm(self, value):
		self._OrgnlCreDtTm = value if value is not None else base_types.UninitialisedField(self, 'OrgnlCreDtTm', ISODateTime, False)

	@OrgnlCreDtTm.deleter
	def OrgnlCreDtTm(self):
		del self._OrgnlCreDtTm
		self._OrgnlCreDtTm = base_types.UninitialisedField(self, 'OrgnlCreDtTm', ISODateTime, False)

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
	def OrgnlMsgId(self):
		return self._OrgnlMsgId

	@OrgnlMsgId.setter
	def OrgnlMsgId(self, value):
		self._OrgnlMsgId = value if value is not None else base_types.UninitialisedField(self, 'OrgnlMsgId', Max35Text, False)

	@OrgnlMsgId.deleter
	def OrgnlMsgId(self):
		del self._OrgnlMsgId
		self._OrgnlMsgId = base_types.UninitialisedField(self, 'OrgnlMsgId', Max35Text, False)

	@property
	def OrgnlMsgNmId(self):
		return self._OrgnlMsgNmId

	@OrgnlMsgNmId.setter
	def OrgnlMsgNmId(self, value):
		self._OrgnlMsgNmId = value if value is not None else base_types.UninitialisedField(self, 'OrgnlMsgNmId', Max35Text, False)

	@OrgnlMsgNmId.deleter
	def OrgnlMsgNmId(self):
		del self._OrgnlMsgNmId
		self._OrgnlMsgNmId = base_types.UninitialisedField(self, 'OrgnlMsgNmId', Max35Text, False)

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
	def StsRsnInf(self):
		return self._StsRsnInf

	@StsRsnInf.setter
	def StsRsnInf(self, value):
		self._StsRsnInf = value if value is not None else base_types.UninitialisedField(self, 'StsRsnInf', StatusReasonInformation14, True)

	@StsRsnInf.deleter
	def StsRsnInf(self):
		del self._StsRsnInf
		self._StsRsnInf = base_types.UninitialisedField(self, 'StsRsnInf', StatusReasonInformation14, True)

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