# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CancellationStatusReason5
from . import Case6
from . import DecimalNumber
from . import GroupCancellationStatus1Code
from . import ISODateTime
from . import Max15NumericText
from . import Max35Text
from . import NumberOfTransactionsPerStatus1

class OriginalGroupHeader23(base_types._BaseFieldType):

	__slots__ = ["_CxlStsRsnInf", "_GrpCxlSts", "_NbOfTxsPerCxlSts", "_OrgnlCreDtTm", "_OrgnlCtrlSum", "_OrgnlGrpCxlId", "_OrgnlMsgId", "_OrgnlMsgNmId", "_OrgnlNbOfTxs", "_RslvdCase"]
	@property
	def CxlStsRsnInf(self):
		return self._CxlStsRsnInf

	@CxlStsRsnInf.setter
	def CxlStsRsnInf(self, value):
		self._CxlStsRsnInf = value if value is not None else base_types.UninitialisedField(self, 'CxlStsRsnInf', CancellationStatusReason5, True)

	@CxlStsRsnInf.deleter
	def CxlStsRsnInf(self):
		del self._CxlStsRsnInf
		self._CxlStsRsnInf = base_types.UninitialisedField(self, 'CxlStsRsnInf', CancellationStatusReason5, True)

	@property
	def GrpCxlSts(self):
		return self._GrpCxlSts

	@GrpCxlSts.setter
	def GrpCxlSts(self, value):
		self._GrpCxlSts = value if value is not None else base_types.UninitialisedField(self, 'GrpCxlSts', GroupCancellationStatus1Code, False)

	@GrpCxlSts.deleter
	def GrpCxlSts(self):
		del self._GrpCxlSts
		self._GrpCxlSts = base_types.UninitialisedField(self, 'GrpCxlSts', GroupCancellationStatus1Code, False)

	@property
	def NbOfTxsPerCxlSts(self):
		return self._NbOfTxsPerCxlSts

	@NbOfTxsPerCxlSts.setter
	def NbOfTxsPerCxlSts(self, value):
		self._NbOfTxsPerCxlSts = value if value is not None else base_types.UninitialisedField(self, 'NbOfTxsPerCxlSts', NumberOfTransactionsPerStatus1, True)

	@NbOfTxsPerCxlSts.deleter
	def NbOfTxsPerCxlSts(self):
		del self._NbOfTxsPerCxlSts
		self._NbOfTxsPerCxlSts = base_types.UninitialisedField(self, 'NbOfTxsPerCxlSts', NumberOfTransactionsPerStatus1, True)

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
	def OrgnlGrpCxlId(self):
		return self._OrgnlGrpCxlId

	@OrgnlGrpCxlId.setter
	def OrgnlGrpCxlId(self, value):
		self._OrgnlGrpCxlId = value if value is not None else base_types.UninitialisedField(self, 'OrgnlGrpCxlId', Max35Text, False)

	@OrgnlGrpCxlId.deleter
	def OrgnlGrpCxlId(self):
		del self._OrgnlGrpCxlId
		self._OrgnlGrpCxlId = base_types.UninitialisedField(self, 'OrgnlGrpCxlId', Max35Text, False)

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
	def RslvdCase(self):
		return self._RslvdCase

	@RslvdCase.setter
	def RslvdCase(self, value):
		self._RslvdCase = value if value is not None else base_types.UninitialisedField(self, 'RslvdCase', Case6, False)

	@RslvdCase.deleter
	def RslvdCase(self):
		del self._RslvdCase
		self._RslvdCase = base_types.UninitialisedField(self, 'RslvdCase', Case6, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CxlStsRsnInf', type=CancellationStatusReason5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='GrpCxlSts', type=GroupCancellationStatus1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfTxsPerCxlSts', type=NumberOfTransactionsPerStatus1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlCreDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlCtrlSum', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlGrpCxlId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlMsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlMsgNmId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlNbOfTxs', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RslvdCase', type=Case6, min=0, max=1, mutex_group=None, array=False),
	))