# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BranchAndFinancialInstitutionIdentification8
from . import ContractRegistration8
from . import Max35Text
from . import SupplementaryData1
from . import TradeParty6

class ContractRegistration7(base_types._BaseFieldType):

	__slots__ = ["_CtrctRegnId", "_CtrctRegnOpng", "_RegnAgt", "_RptgPty", "_SplmtryData"]
	@property
	def CtrctRegnId(self):
		return self._CtrctRegnId

	@CtrctRegnId.setter
	def CtrctRegnId(self, value):
		self._CtrctRegnId = value if value is not None else base_types.UninitialisedField(self, 'CtrctRegnId', Max35Text, False)

	@CtrctRegnId.deleter
	def CtrctRegnId(self):
		del self._CtrctRegnId
		self._CtrctRegnId = base_types.UninitialisedField(self, 'CtrctRegnId', Max35Text, False)

	@property
	def CtrctRegnOpng(self):
		return self._CtrctRegnOpng

	@CtrctRegnOpng.setter
	def CtrctRegnOpng(self, value):
		self._CtrctRegnOpng = value if value is not None else base_types.UninitialisedField(self, 'CtrctRegnOpng', ContractRegistration8, True)

	@CtrctRegnOpng.deleter
	def CtrctRegnOpng(self):
		del self._CtrctRegnOpng
		self._CtrctRegnOpng = base_types.UninitialisedField(self, 'CtrctRegnOpng', ContractRegistration8, True)

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
		base_types.FieldEntry(name='CtrctRegnId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctRegnOpng', type=ContractRegistration8, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RegnAgt', type=BranchAndFinancialInstitutionIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgPty', type=TradeParty6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))