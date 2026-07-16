# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BranchAndFinancialInstitutionIdentification8
from . import ContractCessionData2
from . import ContractClosureReason1Choice
from . import DocumentGeneralInformation5
from . import DocumentIdentification29
from . import Max35Text
from . import Priority2Code
from . import SupplementaryData1
from . import TradeParty6

class RegisteredContract19(base_types._BaseFieldType):

	__slots__ = ["_Attchmnt", "_ClsrRsn", "_Cssn", "_OrgnlRegdCtrct", "_Prty", "_RegdCtrctClsrId", "_RegnAgt", "_RptgPty", "_SplmtryData"]
	@property
	def Attchmnt(self):
		return self._Attchmnt

	@Attchmnt.setter
	def Attchmnt(self, value):
		self._Attchmnt = value if value is not None else base_types.UninitialisedField(self, 'Attchmnt', DocumentGeneralInformation5, True)

	@Attchmnt.deleter
	def Attchmnt(self):
		del self._Attchmnt
		self._Attchmnt = base_types.UninitialisedField(self, 'Attchmnt', DocumentGeneralInformation5, True)

	@property
	def ClsrRsn(self):
		return self._ClsrRsn

	@ClsrRsn.setter
	def ClsrRsn(self, value):
		self._ClsrRsn = value if value is not None else base_types.UninitialisedField(self, 'ClsrRsn', ContractClosureReason1Choice, False)

	@ClsrRsn.deleter
	def ClsrRsn(self):
		del self._ClsrRsn
		self._ClsrRsn = base_types.UninitialisedField(self, 'ClsrRsn', ContractClosureReason1Choice, False)

	@property
	def Cssn(self):
		return self._Cssn

	@Cssn.setter
	def Cssn(self, value):
		self._Cssn = value if value is not None else base_types.UninitialisedField(self, 'Cssn', ContractCessionData2, False)

	@Cssn.deleter
	def Cssn(self):
		del self._Cssn
		self._Cssn = base_types.UninitialisedField(self, 'Cssn', ContractCessionData2, False)

	@property
	def OrgnlRegdCtrct(self):
		return self._OrgnlRegdCtrct

	@OrgnlRegdCtrct.setter
	def OrgnlRegdCtrct(self, value):
		self._OrgnlRegdCtrct = value if value is not None else base_types.UninitialisedField(self, 'OrgnlRegdCtrct', DocumentIdentification29, False)

	@OrgnlRegdCtrct.deleter
	def OrgnlRegdCtrct(self):
		del self._OrgnlRegdCtrct
		self._OrgnlRegdCtrct = base_types.UninitialisedField(self, 'OrgnlRegdCtrct', DocumentIdentification29, False)

	@property
	def Prty(self):
		return self._Prty

	@Prty.setter
	def Prty(self, value):
		self._Prty = value if value is not None else base_types.UninitialisedField(self, 'Prty', Priority2Code, False)

	@Prty.deleter
	def Prty(self):
		del self._Prty
		self._Prty = base_types.UninitialisedField(self, 'Prty', Priority2Code, False)

	@property
	def RegdCtrctClsrId(self):
		return self._RegdCtrctClsrId

	@RegdCtrctClsrId.setter
	def RegdCtrctClsrId(self, value):
		self._RegdCtrctClsrId = value if value is not None else base_types.UninitialisedField(self, 'RegdCtrctClsrId', Max35Text, False)

	@RegdCtrctClsrId.deleter
	def RegdCtrctClsrId(self):
		del self._RegdCtrctClsrId
		self._RegdCtrctClsrId = base_types.UninitialisedField(self, 'RegdCtrctClsrId', Max35Text, False)

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
		base_types.FieldEntry(name='Attchmnt', type=DocumentGeneralInformation5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ClsrRsn', type=ContractClosureReason1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cssn', type=ContractCessionData2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlRegdCtrct', type=DocumentIdentification29, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prty', type=Priority2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegdCtrctClsrId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnAgt', type=BranchAndFinancialInstitutionIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgPty', type=TradeParty6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))