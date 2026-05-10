import base_types
import SupplementaryData1
import GroupHeader119
import CreditTransferTransaction66

class FinancialInstitutionDirectDebitV06(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_CdtInstr", "_GrpHdr"]
	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def CdtInstr(self):
		return self._CdtInstr

	@CdtInstr.setter
	def CdtInstr(self, value):
		self._CdtInstr = value if type(value) != auto else self.make_default("CdtInstr")

	@CdtInstr.deleter
	def CdtInstr(self):
		del self._CdtInstr
		self._CdtInstr = None

	@property
	def GrpHdr(self):
		return self._GrpHdr

	@GrpHdr.setter
	def GrpHdr(self, value):
		self._GrpHdr = value if type(value) != auto else self.make_default("GrpHdr")

	@GrpHdr.deleter
	def GrpHdr(self):
		del self._GrpHdr
		self._GrpHdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CdtInstr', type=CreditTransferTransaction66, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='GrpHdr', type=GroupHeader119, min=1, max=1, mutex_group=None, array=False),
	))

