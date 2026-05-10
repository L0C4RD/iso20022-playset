from . import base_types
from ._DecimalNumber import DecimalNumber
from ._Case6 import Case6
from ._NumberOfTransactionsPerStatus1 import NumberOfTransactionsPerStatus1
from ._GroupCancellationStatus1Code import GroupCancellationStatus1Code
from ._Max35Text import Max35Text
from ._Max15NumericText import Max15NumericText
from ._ISODateTime import ISODateTime
from ._CancellationStatusReason5 import CancellationStatusReason5

class OriginalGroupHeader23(base_types._BaseFieldType):

	__slots__ = ["_CxlStsRsnInf", "_RslvdCase", "_OrgnlGrpCxlId", "_OrgnlNbOfTxs", "_OrgnlCtrlSum", "_OrgnlCreDtTm", "_OrgnlMsgId", "_GrpCxlSts", "_OrgnlMsgNmId", "_NbOfTxsPerCxlSts"]
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
	def GrpCxlSts(self):
		return self._GrpCxlSts

	@GrpCxlSts.setter
	def GrpCxlSts(self, value):
		self._GrpCxlSts = value if type(value) != base_types.auto else self.make_default("GrpCxlSts")

	@GrpCxlSts.deleter
	def GrpCxlSts(self):
		del self._GrpCxlSts
		self._GrpCxlSts = None

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
	def OrgnlGrpCxlId(self):
		return self._OrgnlGrpCxlId

	@OrgnlGrpCxlId.setter
	def OrgnlGrpCxlId(self, value):
		self._OrgnlGrpCxlId = value if type(value) != base_types.auto else self.make_default("OrgnlGrpCxlId")

	@OrgnlGrpCxlId.deleter
	def OrgnlGrpCxlId(self):
		del self._OrgnlGrpCxlId
		self._OrgnlGrpCxlId = None

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
	def RslvdCase(self):
		return self._RslvdCase

	@RslvdCase.setter
	def RslvdCase(self, value):
		self._RslvdCase = value if type(value) != base_types.auto else self.make_default("RslvdCase")

	@RslvdCase.deleter
	def RslvdCase(self):
		del self._RslvdCase
		self._RslvdCase = None

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

