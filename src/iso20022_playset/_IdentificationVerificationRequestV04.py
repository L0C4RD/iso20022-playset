# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import IdentificationAssignment4
from . import IdentificationVerification5
from . import SupplementaryData1

class IdentificationVerificationRequestV04(base_types._BaseFieldType):

	__slots__ = ["_Assgnmt", "_SplmtryData", "_Vrfctn"]
	@property
	def Assgnmt(self):
		return self._Assgnmt

	@Assgnmt.setter
	def Assgnmt(self, value):
		self._Assgnmt = value if value is not None else base_types.UninitialisedField(self, 'Assgnmt', IdentificationAssignment4, False)

	@Assgnmt.deleter
	def Assgnmt(self):
		del self._Assgnmt
		self._Assgnmt = base_types.UninitialisedField(self, 'Assgnmt', IdentificationAssignment4, False)

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
	def Vrfctn(self):
		return self._Vrfctn

	@Vrfctn.setter
	def Vrfctn(self, value):
		self._Vrfctn = value if value is not None else base_types.UninitialisedField(self, 'Vrfctn', IdentificationVerification5, True)

	@Vrfctn.deleter
	def Vrfctn(self):
		del self._Vrfctn
		self._Vrfctn = base_types.UninitialisedField(self, 'Vrfctn', IdentificationVerification5, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Assgnmt', type=IdentificationAssignment4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Vrfctn', type=IdentificationVerification5, min=1, max=None, mutex_group=None, array=True),
	))