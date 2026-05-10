from . import base_types
import DocumentGeneralInformation5
import Priority2Code
import ContractClosureReason1Choice
import TradeParty6
import DocumentIdentification29
import SupplementaryData1
import BranchAndFinancialInstitutionIdentification8
import Max35Text
import ContractCessionData2

class RegisteredContract19(base_types._BaseFieldType):

	__slots__ = ["_Attchmnt", "_RegnAgt", "_ClsrRsn", "_SplmtryData", "_Cssn", "_RptgPty", "_Prty", "_RegdCtrctClsrId", "_OrgnlRegdCtrct"]
	@property
	def Attchmnt(self):
		return self._Attchmnt

	@Attchmnt.setter
	def Attchmnt(self, value):
		self._Attchmnt = value if type(value) != auto else self.make_default("Attchmnt")

	@Attchmnt.deleter
	def Attchmnt(self):
		del self._Attchmnt
		self._Attchmnt = None

	@property
	def RegnAgt(self):
		return self._RegnAgt

	@RegnAgt.setter
	def RegnAgt(self, value):
		self._RegnAgt = value if type(value) != auto else self.make_default("RegnAgt")

	@RegnAgt.deleter
	def RegnAgt(self):
		del self._RegnAgt
		self._RegnAgt = None

	@property
	def ClsrRsn(self):
		return self._ClsrRsn

	@ClsrRsn.setter
	def ClsrRsn(self, value):
		self._ClsrRsn = value if type(value) != auto else self.make_default("ClsrRsn")

	@ClsrRsn.deleter
	def ClsrRsn(self):
		del self._ClsrRsn
		self._ClsrRsn = None

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
	def Cssn(self):
		return self._Cssn

	@Cssn.setter
	def Cssn(self, value):
		self._Cssn = value if type(value) != auto else self.make_default("Cssn")

	@Cssn.deleter
	def Cssn(self):
		del self._Cssn
		self._Cssn = None

	@property
	def RptgPty(self):
		return self._RptgPty

	@RptgPty.setter
	def RptgPty(self, value):
		self._RptgPty = value if type(value) != auto else self.make_default("RptgPty")

	@RptgPty.deleter
	def RptgPty(self):
		del self._RptgPty
		self._RptgPty = None

	@property
	def Prty(self):
		return self._Prty

	@Prty.setter
	def Prty(self, value):
		self._Prty = value if type(value) != auto else self.make_default("Prty")

	@Prty.deleter
	def Prty(self):
		del self._Prty
		self._Prty = None

	@property
	def RegdCtrctClsrId(self):
		return self._RegdCtrctClsrId

	@RegdCtrctClsrId.setter
	def RegdCtrctClsrId(self, value):
		self._RegdCtrctClsrId = value if type(value) != auto else self.make_default("RegdCtrctClsrId")

	@RegdCtrctClsrId.deleter
	def RegdCtrctClsrId(self):
		del self._RegdCtrctClsrId
		self._RegdCtrctClsrId = None

	@property
	def OrgnlRegdCtrct(self):
		return self._OrgnlRegdCtrct

	@OrgnlRegdCtrct.setter
	def OrgnlRegdCtrct(self, value):
		self._OrgnlRegdCtrct = value if type(value) != auto else self.make_default("OrgnlRegdCtrct")

	@OrgnlRegdCtrct.deleter
	def OrgnlRegdCtrct(self):
		del self._OrgnlRegdCtrct
		self._OrgnlRegdCtrct = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Attchmnt', type=DocumentGeneralInformation5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RegnAgt', type=BranchAndFinancialInstitutionIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClsrRsn', type=ContractClosureReason1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Cssn', type=ContractCessionData2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgPty', type=TradeParty6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prty', type=Priority2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegdCtrctClsrId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlRegdCtrct', type=DocumentIdentification29, min=1, max=1, mutex_group=None, array=False),
	))

