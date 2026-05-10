from . import base_types
from ._DecimalNumber import DecimalNumber
from ._Case6 import Case6
from ._OriginalGroupInformation29 import OriginalGroupInformation29
from ._PaymentCancellationReason6 import PaymentCancellationReason6
from ._PaymentTransaction154 import PaymentTransaction154
from ._Max35Text import Max35Text
from ._Max15NumericText import Max15NumericText
from ._GroupCancellationIndicator import GroupCancellationIndicator

class OriginalPaymentInstruction49(base_types._BaseFieldType):

	__slots__ = ["_PmtInfCxl", "_TxInf", "_OrgnlPmtInfId", "_CtrlSum", "_Case", "_NbOfTxs", "_CxlRsnInf", "_PmtCxlId", "_OrgnlGrpInf"]
	@property
	def Case(self):
		return self._Case

	@Case.setter
	def Case(self, value):
		self._Case = value if type(value) != base_types.auto else self.make_default("Case")

	@Case.deleter
	def Case(self):
		del self._Case
		self._Case = None

	@property
	def CtrlSum(self):
		return self._CtrlSum

	@CtrlSum.setter
	def CtrlSum(self, value):
		self._CtrlSum = value if type(value) != base_types.auto else self.make_default("CtrlSum")

	@CtrlSum.deleter
	def CtrlSum(self):
		del self._CtrlSum
		self._CtrlSum = None

	@property
	def CxlRsnInf(self):
		return self._CxlRsnInf

	@CxlRsnInf.setter
	def CxlRsnInf(self, value):
		self._CxlRsnInf = value if type(value) != base_types.auto else self.make_default("CxlRsnInf")

	@CxlRsnInf.deleter
	def CxlRsnInf(self):
		del self._CxlRsnInf
		self._CxlRsnInf = None

	@property
	def NbOfTxs(self):
		return self._NbOfTxs

	@NbOfTxs.setter
	def NbOfTxs(self, value):
		self._NbOfTxs = value if type(value) != base_types.auto else self.make_default("NbOfTxs")

	@NbOfTxs.deleter
	def NbOfTxs(self):
		del self._NbOfTxs
		self._NbOfTxs = None

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
	def PmtCxlId(self):
		return self._PmtCxlId

	@PmtCxlId.setter
	def PmtCxlId(self, value):
		self._PmtCxlId = value if type(value) != base_types.auto else self.make_default("PmtCxlId")

	@PmtCxlId.deleter
	def PmtCxlId(self):
		del self._PmtCxlId
		self._PmtCxlId = None

	@property
	def PmtInfCxl(self):
		return self._PmtInfCxl

	@PmtInfCxl.setter
	def PmtInfCxl(self, value):
		self._PmtInfCxl = value if type(value) != base_types.auto else self.make_default("PmtInfCxl")

	@PmtInfCxl.deleter
	def PmtInfCxl(self):
		del self._PmtInfCxl
		self._PmtInfCxl = None

	@property
	def TxInf(self):
		return self._TxInf

	@TxInf.setter
	def TxInf(self, value):
		self._TxInf = value if type(value) != base_types.auto else self.make_default("TxInf")

	@TxInf.deleter
	def TxInf(self):
		del self._TxInf
		self._TxInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Case', type=Case6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrlSum', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlRsnInf', type=PaymentCancellationReason6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NbOfTxs', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlGrpInf', type=OriginalGroupInformation29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlPmtInfId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtCxlId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtInfCxl', type=GroupCancellationIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxInf', type=PaymentTransaction154, min=0, max=None, mutex_group=None, array=True),
	))

