# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CancellationStatusReason5
from . import Case6
from . import DecimalNumber
from . import GroupCancellationStatus1Code
from . import Max15NumericText
from . import Max35Text
from . import NumberOfCancellationsPerStatus1
from . import OriginalGroupInformation33
from . import PaymentTransaction175

class OriginalPaymentInstruction54(base_types._BaseFieldType):

	__slots__ = ["_CxlStsRsnInf", "_NbOfTxsPerCxlSts", "_OrgnlCtrlSum", "_OrgnlGrpInf", "_OrgnlNbOfTxs", "_OrgnlPmtInfCxlId", "_OrgnlPmtInfId", "_PmtInfCxlSts", "_RslvdCase", "_TxInfAndSts"]
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
	def NbOfTxsPerCxlSts(self):
		return self._NbOfTxsPerCxlSts

	@NbOfTxsPerCxlSts.setter
	def NbOfTxsPerCxlSts(self, value):
		self._NbOfTxsPerCxlSts = value if value is not None else base_types.UninitialisedField(self, 'NbOfTxsPerCxlSts', NumberOfCancellationsPerStatus1, True)

	@NbOfTxsPerCxlSts.deleter
	def NbOfTxsPerCxlSts(self):
		del self._NbOfTxsPerCxlSts
		self._NbOfTxsPerCxlSts = base_types.UninitialisedField(self, 'NbOfTxsPerCxlSts', NumberOfCancellationsPerStatus1, True)

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
	def OrgnlGrpInf(self):
		return self._OrgnlGrpInf

	@OrgnlGrpInf.setter
	def OrgnlGrpInf(self, value):
		self._OrgnlGrpInf = value if value is not None else base_types.UninitialisedField(self, 'OrgnlGrpInf', OriginalGroupInformation33, False)

	@OrgnlGrpInf.deleter
	def OrgnlGrpInf(self):
		del self._OrgnlGrpInf
		self._OrgnlGrpInf = base_types.UninitialisedField(self, 'OrgnlGrpInf', OriginalGroupInformation33, False)

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
	def OrgnlPmtInfCxlId(self):
		return self._OrgnlPmtInfCxlId

	@OrgnlPmtInfCxlId.setter
	def OrgnlPmtInfCxlId(self, value):
		self._OrgnlPmtInfCxlId = value if value is not None else base_types.UninitialisedField(self, 'OrgnlPmtInfCxlId', Max35Text, False)

	@OrgnlPmtInfCxlId.deleter
	def OrgnlPmtInfCxlId(self):
		del self._OrgnlPmtInfCxlId
		self._OrgnlPmtInfCxlId = base_types.UninitialisedField(self, 'OrgnlPmtInfCxlId', Max35Text, False)

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
	def PmtInfCxlSts(self):
		return self._PmtInfCxlSts

	@PmtInfCxlSts.setter
	def PmtInfCxlSts(self, value):
		self._PmtInfCxlSts = value if value is not None else base_types.UninitialisedField(self, 'PmtInfCxlSts', GroupCancellationStatus1Code, False)

	@PmtInfCxlSts.deleter
	def PmtInfCxlSts(self):
		del self._PmtInfCxlSts
		self._PmtInfCxlSts = base_types.UninitialisedField(self, 'PmtInfCxlSts', GroupCancellationStatus1Code, False)

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

	@property
	def TxInfAndSts(self):
		return self._TxInfAndSts

	@TxInfAndSts.setter
	def TxInfAndSts(self, value):
		self._TxInfAndSts = value if value is not None else base_types.UninitialisedField(self, 'TxInfAndSts', PaymentTransaction175, True)

	@TxInfAndSts.deleter
	def TxInfAndSts(self):
		del self._TxInfAndSts
		self._TxInfAndSts = base_types.UninitialisedField(self, 'TxInfAndSts', PaymentTransaction175, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CxlStsRsnInf', type=CancellationStatusReason5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NbOfTxsPerCxlSts', type=NumberOfCancellationsPerStatus1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlCtrlSum', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlGrpInf', type=OriginalGroupInformation33, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlNbOfTxs', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlPmtInfCxlId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlPmtInfId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtInfCxlSts', type=GroupCancellationStatus1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RslvdCase', type=Case6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxInfAndSts', type=PaymentTransaction175, min=0, max=None, mutex_group=None, array=True),
	))