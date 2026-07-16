# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Case6
from . import DecimalNumber
from . import GroupCancellationIndicator
from . import Max15NumericText
from . import Max35Text
from . import OriginalGroupInformation29
from . import PaymentCancellationReason6
from . import PaymentTransaction154

class OriginalPaymentInstruction49(base_types._BaseFieldType):

	__slots__ = ["_Case", "_CtrlSum", "_CxlRsnInf", "_NbOfTxs", "_OrgnlGrpInf", "_OrgnlPmtInfId", "_PmtCxlId", "_PmtInfCxl", "_TxInf"]
	@property
	def Case(self):
		return self._Case

	@Case.setter
	def Case(self, value):
		self._Case = value if value is not None else base_types.UninitialisedField(self, 'Case', Case6, False)

	@Case.deleter
	def Case(self):
		del self._Case
		self._Case = base_types.UninitialisedField(self, 'Case', Case6, False)

	@property
	def CtrlSum(self):
		return self._CtrlSum

	@CtrlSum.setter
	def CtrlSum(self, value):
		self._CtrlSum = value if value is not None else base_types.UninitialisedField(self, 'CtrlSum', DecimalNumber, False)

	@CtrlSum.deleter
	def CtrlSum(self):
		del self._CtrlSum
		self._CtrlSum = base_types.UninitialisedField(self, 'CtrlSum', DecimalNumber, False)

	@property
	def CxlRsnInf(self):
		return self._CxlRsnInf

	@CxlRsnInf.setter
	def CxlRsnInf(self, value):
		self._CxlRsnInf = value if value is not None else base_types.UninitialisedField(self, 'CxlRsnInf', PaymentCancellationReason6, True)

	@CxlRsnInf.deleter
	def CxlRsnInf(self):
		del self._CxlRsnInf
		self._CxlRsnInf = base_types.UninitialisedField(self, 'CxlRsnInf', PaymentCancellationReason6, True)

	@property
	def NbOfTxs(self):
		return self._NbOfTxs

	@NbOfTxs.setter
	def NbOfTxs(self, value):
		self._NbOfTxs = value if value is not None else base_types.UninitialisedField(self, 'NbOfTxs', Max15NumericText, False)

	@NbOfTxs.deleter
	def NbOfTxs(self):
		del self._NbOfTxs
		self._NbOfTxs = base_types.UninitialisedField(self, 'NbOfTxs', Max15NumericText, False)

	@property
	def OrgnlGrpInf(self):
		return self._OrgnlGrpInf

	@OrgnlGrpInf.setter
	def OrgnlGrpInf(self, value):
		self._OrgnlGrpInf = value if value is not None else base_types.UninitialisedField(self, 'OrgnlGrpInf', OriginalGroupInformation29, False)

	@OrgnlGrpInf.deleter
	def OrgnlGrpInf(self):
		del self._OrgnlGrpInf
		self._OrgnlGrpInf = base_types.UninitialisedField(self, 'OrgnlGrpInf', OriginalGroupInformation29, False)

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
	def PmtCxlId(self):
		return self._PmtCxlId

	@PmtCxlId.setter
	def PmtCxlId(self, value):
		self._PmtCxlId = value if value is not None else base_types.UninitialisedField(self, 'PmtCxlId', Max35Text, False)

	@PmtCxlId.deleter
	def PmtCxlId(self):
		del self._PmtCxlId
		self._PmtCxlId = base_types.UninitialisedField(self, 'PmtCxlId', Max35Text, False)

	@property
	def PmtInfCxl(self):
		return self._PmtInfCxl

	@PmtInfCxl.setter
	def PmtInfCxl(self, value):
		self._PmtInfCxl = value if value is not None else base_types.UninitialisedField(self, 'PmtInfCxl', GroupCancellationIndicator, False)

	@PmtInfCxl.deleter
	def PmtInfCxl(self):
		del self._PmtInfCxl
		self._PmtInfCxl = base_types.UninitialisedField(self, 'PmtInfCxl', GroupCancellationIndicator, False)

	@property
	def TxInf(self):
		return self._TxInf

	@TxInf.setter
	def TxInf(self, value):
		self._TxInf = value if value is not None else base_types.UninitialisedField(self, 'TxInf', PaymentTransaction154, True)

	@TxInf.deleter
	def TxInf(self):
		del self._TxInf
		self._TxInf = base_types.UninitialisedField(self, 'TxInf', PaymentTransaction154, True)

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