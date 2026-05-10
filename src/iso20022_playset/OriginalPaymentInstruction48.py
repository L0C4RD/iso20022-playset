from . import base_types
from .DecimalNumber import DecimalNumber
from .GroupCancellationStatus1Code import GroupCancellationStatus1Code
from .OriginalGroupInformation29 import OriginalGroupInformation29
from .NumberOfCancellationsPerStatus1 import NumberOfCancellationsPerStatus1
from .Max35Text import Max35Text
from .PaymentTransaction153 import PaymentTransaction153
from .Max15NumericText import Max15NumericText
from .Case6 import Case6
from .CancellationStatusReason5 import CancellationStatusReason5

class OriginalPaymentInstruction48(base_types._BaseFieldType):

	__slots__ = ["_OrgnlPmtInfCxlId", "_OrgnlNbOfTxs", "_OrgnlCtrlSum", "_RslvdCase", "_CxlStsRsnInf", "_PmtInfCxlSts", "_TxInfAndSts", "_NbOfTxsPerCxlSts", "_OrgnlPmtInfId", "_OrgnlGrpInf"]
	@property
	def OrgnlPmtInfCxlId(self):
		return self._OrgnlPmtInfCxlId

	@OrgnlPmtInfCxlId.setter
	def OrgnlPmtInfCxlId(self, value):
		self._OrgnlPmtInfCxlId = value if type(value) != base_types.auto else self.make_default("OrgnlPmtInfCxlId")

	@OrgnlPmtInfCxlId.deleter
	def OrgnlPmtInfCxlId(self):
		del self._OrgnlPmtInfCxlId
		self._OrgnlPmtInfCxlId = None

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
	def RslvdCase(self):
		return self._RslvdCase

	@RslvdCase.setter
	def RslvdCase(self, value):
		self._RslvdCase = value if type(value) != base_types.auto else self.make_default("RslvdCase")

	@RslvdCase.deleter
	def RslvdCase(self):
		del self._RslvdCase
		self._RslvdCase = None

	@property
	def CxlStsRsnInf(self):
		return self._CxlStsRsnInf

	@CxlStsRsnInf.setter
	def CxlStsRsnInf(self, value):
		self._CxlStsRsnInf = value if type(value) != base_types.auto else self.make_default("CxlStsRsnInf")

	@CxlStsRsnInf.deleter
	def CxlStsRsnInf(self):
		del self._CxlStsRsnInf
		self._CxlStsRsnInf = None

	@property
	def PmtInfCxlSts(self):
		return self._PmtInfCxlSts

	@PmtInfCxlSts.setter
	def PmtInfCxlSts(self, value):
		self._PmtInfCxlSts = value if type(value) != base_types.auto else self.make_default("PmtInfCxlSts")

	@PmtInfCxlSts.deleter
	def PmtInfCxlSts(self):
		del self._PmtInfCxlSts
		self._PmtInfCxlSts = None

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

	@property
	def NbOfTxsPerCxlSts(self):
		return self._NbOfTxsPerCxlSts

	@NbOfTxsPerCxlSts.setter
	def NbOfTxsPerCxlSts(self, value):
		self._NbOfTxsPerCxlSts = value if type(value) != base_types.auto else self.make_default("NbOfTxsPerCxlSts")

	@NbOfTxsPerCxlSts.deleter
	def NbOfTxsPerCxlSts(self):
		del self._NbOfTxsPerCxlSts
		self._NbOfTxsPerCxlSts = None

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
	def OrgnlGrpInf(self):
		return self._OrgnlGrpInf

	@OrgnlGrpInf.setter
	def OrgnlGrpInf(self, value):
		self._OrgnlGrpInf = value if type(value) != base_types.auto else self.make_default("OrgnlGrpInf")

	@OrgnlGrpInf.deleter
	def OrgnlGrpInf(self):
		del self._OrgnlGrpInf
		self._OrgnlGrpInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlPmtInfCxlId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlNbOfTxs', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlCtrlSum', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RslvdCase', type=Case6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlStsRsnInf', type=CancellationStatusReason5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PmtInfCxlSts', type=GroupCancellationStatus1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxInfAndSts', type=PaymentTransaction153, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NbOfTxsPerCxlSts', type=NumberOfCancellationsPerStatus1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlPmtInfId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlGrpInf', type=OriginalGroupInformation29, min=0, max=1, mutex_group=None, array=False),
	))

