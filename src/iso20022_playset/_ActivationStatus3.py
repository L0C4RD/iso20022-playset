# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateAndDateTime2Choice
from . import DebtorActivationStatusReason3
from . import OriginalActivation3Choice
from . import OriginalBusinessInstruction1
from . import ServiceStatus1Choice
from . import SupplementaryData1

class ActivationStatus3(base_types._BaseFieldType):

	__slots__ = ["_FctvActvtnDt", "_OrgnlActvtnRef", "_OrgnlBizInstr", "_SplmtryData", "_Sts", "_StsRsn"]
	@property
	def FctvActvtnDt(self):
		return self._FctvActvtnDt

	@FctvActvtnDt.setter
	def FctvActvtnDt(self, value):
		self._FctvActvtnDt = value if value is not None else base_types.UninitialisedField(self, 'FctvActvtnDt', DateAndDateTime2Choice, False)

	@FctvActvtnDt.deleter
	def FctvActvtnDt(self):
		del self._FctvActvtnDt
		self._FctvActvtnDt = base_types.UninitialisedField(self, 'FctvActvtnDt', DateAndDateTime2Choice, False)

	@property
	def OrgnlActvtnRef(self):
		return self._OrgnlActvtnRef

	@OrgnlActvtnRef.setter
	def OrgnlActvtnRef(self, value):
		self._OrgnlActvtnRef = value if value is not None else base_types.UninitialisedField(self, 'OrgnlActvtnRef', OriginalActivation3Choice, False)

	@OrgnlActvtnRef.deleter
	def OrgnlActvtnRef(self):
		del self._OrgnlActvtnRef
		self._OrgnlActvtnRef = base_types.UninitialisedField(self, 'OrgnlActvtnRef', OriginalActivation3Choice, False)

	@property
	def OrgnlBizInstr(self):
		return self._OrgnlBizInstr

	@OrgnlBizInstr.setter
	def OrgnlBizInstr(self, value):
		self._OrgnlBizInstr = value if value is not None else base_types.UninitialisedField(self, 'OrgnlBizInstr', OriginalBusinessInstruction1, False)

	@OrgnlBizInstr.deleter
	def OrgnlBizInstr(self):
		del self._OrgnlBizInstr
		self._OrgnlBizInstr = base_types.UninitialisedField(self, 'OrgnlBizInstr', OriginalBusinessInstruction1, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', ServiceStatus1Choice, False)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', ServiceStatus1Choice, False)

	@property
	def StsRsn(self):
		return self._StsRsn

	@StsRsn.setter
	def StsRsn(self, value):
		self._StsRsn = value if value is not None else base_types.UninitialisedField(self, 'StsRsn', DebtorActivationStatusReason3, False)

	@StsRsn.deleter
	def StsRsn(self):
		del self._StsRsn
		self._StsRsn = base_types.UninitialisedField(self, 'StsRsn', DebtorActivationStatusReason3, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FctvActvtnDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlActvtnRef', type=OriginalActivation3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlBizInstr', type=OriginalBusinessInstruction1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sts', type=ServiceStatus1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsRsn', type=DebtorActivationStatusReason3, min=0, max=1, mutex_group=None, array=False),
	))