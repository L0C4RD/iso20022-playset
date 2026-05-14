# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Case6 import Case6
from ._DecimalNumber import DecimalNumber
from ._GroupCancellationIndicator import GroupCancellationIndicator
from ._ISODateTime import ISODateTime
from ._Max15NumericText import Max15NumericText
from ._Max35Text import Max35Text
from ._PaymentCancellationReason6 import PaymentCancellationReason6

class OriginalGroupHeader21(base_types._BaseFieldType):

	__slots__ = ["_Case", "_CtrlSum", "_CxlRsnInf", "_GrpCxl", "_GrpCxlId", "_NbOfTxs", "_OrgnlCreDtTm", "_OrgnlMsgId", "_OrgnlMsgNmId"]
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
	def GrpCxl(self):
		return self._GrpCxl

	@GrpCxl.setter
	def GrpCxl(self, value):
		self._GrpCxl = value if type(value) != base_types.auto else self.make_default("GrpCxl")

	@GrpCxl.deleter
	def GrpCxl(self):
		del self._GrpCxl
		self._GrpCxl = None

	@property
	def GrpCxlId(self):
		return self._GrpCxlId

	@GrpCxlId.setter
	def GrpCxlId(self, value):
		self._GrpCxlId = value if type(value) != base_types.auto else self.make_default("GrpCxlId")

	@GrpCxlId.deleter
	def GrpCxlId(self):
		del self._GrpCxlId
		self._GrpCxlId = None

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