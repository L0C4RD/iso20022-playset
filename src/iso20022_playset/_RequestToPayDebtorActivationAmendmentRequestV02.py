# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActivationHeader3
from . import DebtorActivationAmendment5
from . import SupplementaryData1

class RequestToPayDebtorActivationAmendmentRequestV02(base_types._BaseFieldType):

	__slots__ = ["_AmdmntData", "_Hdr", "_SplmtryData"]
	@property
	def AmdmntData(self):
		return self._AmdmntData

	@AmdmntData.setter
	def AmdmntData(self, value):
		self._AmdmntData = value if value is not None else base_types.UninitialisedField(self, 'AmdmntData', DebtorActivationAmendment5, True)

	@AmdmntData.deleter
	def AmdmntData(self):
		del self._AmdmntData
		self._AmdmntData = base_types.UninitialisedField(self, 'AmdmntData', DebtorActivationAmendment5, True)

	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if value is not None else base_types.UninitialisedField(self, 'Hdr', ActivationHeader3, False)

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = base_types.UninitialisedField(self, 'Hdr', ActivationHeader3, False)

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
		base_types.FieldEntry(name='AmdmntData', type=DebtorActivationAmendment5, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Hdr', type=ActivationHeader3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))