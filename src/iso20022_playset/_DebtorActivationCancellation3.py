# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DebtorActivationCancellationReason3
from . import OriginalActivation3Choice
from . import OriginalBusinessInstruction1
from . import SupplementaryData1

class DebtorActivationCancellation3(base_types._BaseFieldType):

	__slots__ = ["_CxlRsn", "_OrgnlActvtn", "_OrgnlBizInstr", "_SplmtryData"]
	@property
	def CxlRsn(self):
		return self._CxlRsn

	@CxlRsn.setter
	def CxlRsn(self, value):
		self._CxlRsn = value if value is not None else base_types.UninitialisedField(self, 'CxlRsn', DebtorActivationCancellationReason3, False)

	@CxlRsn.deleter
	def CxlRsn(self):
		del self._CxlRsn
		self._CxlRsn = base_types.UninitialisedField(self, 'CxlRsn', DebtorActivationCancellationReason3, False)

	@property
	def OrgnlActvtn(self):
		return self._OrgnlActvtn

	@OrgnlActvtn.setter
	def OrgnlActvtn(self, value):
		self._OrgnlActvtn = value if value is not None else base_types.UninitialisedField(self, 'OrgnlActvtn', OriginalActivation3Choice, False)

	@OrgnlActvtn.deleter
	def OrgnlActvtn(self):
		del self._OrgnlActvtn
		self._OrgnlActvtn = base_types.UninitialisedField(self, 'OrgnlActvtn', OriginalActivation3Choice, False)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='CxlRsn', type=DebtorActivationCancellationReason3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlActvtn', type=OriginalActivation3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlBizInstr', type=OriginalBusinessInstruction1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))