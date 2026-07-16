# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GroupHeader114
from . import PaymentInstruction51
from . import SupplementaryData1

class CustomerCreditTransferInitiationV13(base_types._BaseFieldType):

	__slots__ = ["_GrpHdr", "_PmtInf", "_SplmtryData"]
	@property
	def GrpHdr(self):
		return self._GrpHdr

	@GrpHdr.setter
	def GrpHdr(self, value):
		self._GrpHdr = value if value is not None else base_types.UninitialisedField(self, 'GrpHdr', GroupHeader114, False)

	@GrpHdr.deleter
	def GrpHdr(self):
		del self._GrpHdr
		self._GrpHdr = base_types.UninitialisedField(self, 'GrpHdr', GroupHeader114, False)

	@property
	def PmtInf(self):
		return self._PmtInf

	@PmtInf.setter
	def PmtInf(self, value):
		self._PmtInf = value if value is not None else base_types.UninitialisedField(self, 'PmtInf', PaymentInstruction51, True)

	@PmtInf.deleter
	def PmtInf(self):
		del self._PmtInf
		self._PmtInf = base_types.UninitialisedField(self, 'PmtInf', PaymentInstruction51, True)

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
		base_types.FieldEntry(name='GrpHdr', type=GroupHeader114, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtInf', type=PaymentInstruction51, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))