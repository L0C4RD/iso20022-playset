# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CreditTransferTransaction66
from . import GroupHeader119
from . import SupplementaryData1

class FinancialInstitutionDirectDebitV06(base_types._BaseFieldType):

	__slots__ = ["_CdtInstr", "_GrpHdr", "_SplmtryData"]
	@property
	def CdtInstr(self):
		return self._CdtInstr

	@CdtInstr.setter
	def CdtInstr(self, value):
		self._CdtInstr = value if value is not None else base_types.UninitialisedField(self, 'CdtInstr', CreditTransferTransaction66, True)

	@CdtInstr.deleter
	def CdtInstr(self):
		del self._CdtInstr
		self._CdtInstr = base_types.UninitialisedField(self, 'CdtInstr', CreditTransferTransaction66, True)

	@property
	def GrpHdr(self):
		return self._GrpHdr

	@GrpHdr.setter
	def GrpHdr(self, value):
		self._GrpHdr = value if value is not None else base_types.UninitialisedField(self, 'GrpHdr', GroupHeader119, False)

	@GrpHdr.deleter
	def GrpHdr(self):
		del self._GrpHdr
		self._GrpHdr = base_types.UninitialisedField(self, 'GrpHdr', GroupHeader119, False)

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
		base_types.FieldEntry(name='CdtInstr', type=CreditTransferTransaction66, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='GrpHdr', type=GroupHeader119, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))