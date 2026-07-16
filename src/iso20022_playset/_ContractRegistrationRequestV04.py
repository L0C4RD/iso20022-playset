# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ContractRegistration7
from . import CurrencyControlHeader8
from . import SupplementaryData1

class ContractRegistrationRequestV04(base_types._BaseFieldType):

	__slots__ = ["_CtrctRegn", "_GrpHdr", "_SplmtryData"]
	@property
	def CtrctRegn(self):
		return self._CtrctRegn

	@CtrctRegn.setter
	def CtrctRegn(self, value):
		self._CtrctRegn = value if value is not None else base_types.UninitialisedField(self, 'CtrctRegn', ContractRegistration7, True)

	@CtrctRegn.deleter
	def CtrctRegn(self):
		del self._CtrctRegn
		self._CtrctRegn = base_types.UninitialisedField(self, 'CtrctRegn', ContractRegistration7, True)

	@property
	def GrpHdr(self):
		return self._GrpHdr

	@GrpHdr.setter
	def GrpHdr(self, value):
		self._GrpHdr = value if value is not None else base_types.UninitialisedField(self, 'GrpHdr', CurrencyControlHeader8, False)

	@GrpHdr.deleter
	def GrpHdr(self):
		del self._GrpHdr
		self._GrpHdr = base_types.UninitialisedField(self, 'GrpHdr', CurrencyControlHeader8, False)

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
		base_types.FieldEntry(name='CtrctRegn', type=ContractRegistration7, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='GrpHdr', type=CurrencyControlHeader8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))