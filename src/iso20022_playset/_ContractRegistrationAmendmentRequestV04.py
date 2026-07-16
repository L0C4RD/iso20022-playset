# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CurrencyControlHeader8
from . import RegisteredContract16
from . import SupplementaryData1

class ContractRegistrationAmendmentRequestV04(base_types._BaseFieldType):

	__slots__ = ["_CtrctRegnAmdmnt", "_GrpHdr", "_SplmtryData"]
	@property
	def CtrctRegnAmdmnt(self):
		return self._CtrctRegnAmdmnt

	@CtrctRegnAmdmnt.setter
	def CtrctRegnAmdmnt(self, value):
		self._CtrctRegnAmdmnt = value if value is not None else base_types.UninitialisedField(self, 'CtrctRegnAmdmnt', RegisteredContract16, True)

	@CtrctRegnAmdmnt.deleter
	def CtrctRegnAmdmnt(self):
		del self._CtrctRegnAmdmnt
		self._CtrctRegnAmdmnt = base_types.UninitialisedField(self, 'CtrctRegnAmdmnt', RegisteredContract16, True)

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
		base_types.FieldEntry(name='CtrctRegnAmdmnt', type=RegisteredContract16, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='GrpHdr', type=CurrencyControlHeader8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))