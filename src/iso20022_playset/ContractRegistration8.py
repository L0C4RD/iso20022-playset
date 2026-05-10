from . import base_types
import DocumentGeneralInformation5
import Priority2Code
import ContractBalance1
import SupplementaryData1
import UnderlyingContract4Choice
import Max35Text
import Max1025Text
import PaymentScheduleType2Choice
import DocumentIdentification22

class ContractRegistration8(base_types._BaseFieldType):

	__slots__ = ["_Attchmnt", "_SplmtryData", "_Ctrct", "_PrvsRegnId", "_CtrctBal", "_CtrctRegnOpngId", "_AddtlInf", "_Prty", "_PmtSchdlTp"]
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
	def Ctrct(self):
		return self._Ctrct

	@Ctrct.setter
	def Ctrct(self, value):
		self._Ctrct = value if type(value) != auto else self.make_default("Ctrct")

	@Ctrct.deleter
	def Ctrct(self):
		del self._Ctrct
		self._Ctrct = None

	@property
	def PrvsRegnId(self):
		return self._PrvsRegnId

	@PrvsRegnId.setter
	def PrvsRegnId(self, value):
		self._PrvsRegnId = value if type(value) != auto else self.make_default("PrvsRegnId")

	@PrvsRegnId.deleter
	def PrvsRegnId(self):
		del self._PrvsRegnId
		self._PrvsRegnId = None

	@property
	def CtrctBal(self):
		return self._CtrctBal

	@CtrctBal.setter
	def CtrctBal(self, value):
		self._CtrctBal = value if type(value) != auto else self.make_default("CtrctBal")

	@CtrctBal.deleter
	def CtrctBal(self):
		del self._CtrctBal
		self._CtrctBal = None

	@property
	def CtrctRegnOpngId(self):
		return self._CtrctRegnOpngId

	@CtrctRegnOpngId.setter
	def CtrctRegnOpngId(self, value):
		self._CtrctRegnOpngId = value if type(value) != auto else self.make_default("CtrctRegnOpngId")

	@CtrctRegnOpngId.deleter
	def CtrctRegnOpngId(self):
		del self._CtrctRegnOpngId
		self._CtrctRegnOpngId = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

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
	def PmtSchdlTp(self):
		return self._PmtSchdlTp

	@PmtSchdlTp.setter
	def PmtSchdlTp(self, value):
		self._PmtSchdlTp = value if type(value) != auto else self.make_default("PmtSchdlTp")

	@PmtSchdlTp.deleter
	def PmtSchdlTp(self):
		del self._PmtSchdlTp
		self._PmtSchdlTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Attchmnt', type=DocumentGeneralInformation5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ctrct', type=UnderlyingContract4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsRegnId', type=DocumentIdentification22, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CtrctBal', type=ContractBalance1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CtrctRegnOpngId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=Max1025Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prty', type=Priority2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtSchdlTp', type=PaymentScheduleType2Choice, min=0, max=1, mutex_group=None, array=False),
	))

