# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BranchAndFinancialInstitutionIdentification8
from . import Max35Text
from . import RegisteredContract17
from . import SupplementaryData1
from . import TradeParty6

class RegisteredContract16(base_types._BaseFieldType):

	__slots__ = ["_CtrctRegnAmdmntId", "_RegdCtrctAmdmnt", "_RegnAgt", "_RptgPty", "_SplmtryData"]
	@property
	def CtrctRegnAmdmntId(self):
		return self._CtrctRegnAmdmntId

	@CtrctRegnAmdmntId.setter
	def CtrctRegnAmdmntId(self, value):
		self._CtrctRegnAmdmntId = value if value is not None else base_types.UninitialisedField(self, 'CtrctRegnAmdmntId', Max35Text, False)

	@CtrctRegnAmdmntId.deleter
	def CtrctRegnAmdmntId(self):
		del self._CtrctRegnAmdmntId
		self._CtrctRegnAmdmntId = base_types.UninitialisedField(self, 'CtrctRegnAmdmntId', Max35Text, False)

	@property
	def RegdCtrctAmdmnt(self):
		return self._RegdCtrctAmdmnt

	@RegdCtrctAmdmnt.setter
	def RegdCtrctAmdmnt(self, value):
		self._RegdCtrctAmdmnt = value if value is not None else base_types.UninitialisedField(self, 'RegdCtrctAmdmnt', RegisteredContract17, True)

	@RegdCtrctAmdmnt.deleter
	def RegdCtrctAmdmnt(self):
		del self._RegdCtrctAmdmnt
		self._RegdCtrctAmdmnt = base_types.UninitialisedField(self, 'RegdCtrctAmdmnt', RegisteredContract17, True)

	@property
	def RegnAgt(self):
		return self._RegnAgt

	@RegnAgt.setter
	def RegnAgt(self, value):
		self._RegnAgt = value if value is not None else base_types.UninitialisedField(self, 'RegnAgt', BranchAndFinancialInstitutionIdentification8, False)

	@RegnAgt.deleter
	def RegnAgt(self):
		del self._RegnAgt
		self._RegnAgt = base_types.UninitialisedField(self, 'RegnAgt', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def RptgPty(self):
		return self._RptgPty

	@RptgPty.setter
	def RptgPty(self, value):
		self._RptgPty = value if value is not None else base_types.UninitialisedField(self, 'RptgPty', TradeParty6, False)

	@RptgPty.deleter
	def RptgPty(self):
		del self._RptgPty
		self._RptgPty = base_types.UninitialisedField(self, 'RptgPty', TradeParty6, False)

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
		base_types.FieldEntry(name='CtrctRegnAmdmntId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegdCtrctAmdmnt', type=RegisteredContract17, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RegnAgt', type=BranchAndFinancialInstitutionIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgPty', type=TradeParty6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))