# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Case6
from . import DecimalNumber
from . import GroupCancellationIndicator
from . import ISODateTime
from . import Max15NumericText
from . import Max35Text
from . import PaymentCancellationReason6

class OriginalGroupHeader21(base_types._BaseFieldType):

	__slots__ = ["_Case", "_CtrlSum", "_CxlRsnInf", "_GrpCxl", "_GrpCxlId", "_NbOfTxs", "_OrgnlCreDtTm", "_OrgnlMsgId", "_OrgnlMsgNmId"]
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
	def GrpCxl(self):
		return self._GrpCxl

	@GrpCxl.setter
	def GrpCxl(self, value):
		self._GrpCxl = value if value is not None else base_types.UninitialisedField(self, 'GrpCxl', GroupCancellationIndicator, False)

	@GrpCxl.deleter
	def GrpCxl(self):
		del self._GrpCxl
		self._GrpCxl = base_types.UninitialisedField(self, 'GrpCxl', GroupCancellationIndicator, False)

	@property
	def GrpCxlId(self):
		return self._GrpCxlId

	@GrpCxlId.setter
	def GrpCxlId(self, value):
		self._GrpCxlId = value if value is not None else base_types.UninitialisedField(self, 'GrpCxlId', Max35Text, False)

	@GrpCxlId.deleter
	def GrpCxlId(self):
		del self._GrpCxlId
		self._GrpCxlId = base_types.UninitialisedField(self, 'GrpCxlId', Max35Text, False)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Case', type=Case6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrlSum', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlRsnInf', type=PaymentCancellationReason6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='GrpCxl', type=GroupCancellationIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrpCxlId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfTxs', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlCreDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlMsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlMsgNmId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))