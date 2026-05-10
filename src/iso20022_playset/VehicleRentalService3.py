import base_types
import VehicleRentalAgreement3
import PartyIdentification285
import VehicleRentalInvoice3
import DriverInParty3
import Max35Text
import CarRentalActivity1Code
import CustomerAssigner1Code
import ContactBusiness1
import AdditionalData1
import Address2
import LoyaltyProgramme4
import Max70Text

class VehicleRentalService3(base_types._BaseFieldType):

	__slots__ = ["_CpnyCtct", "_RntrNm", "_AddtlData", "_CpnyId", "_RntrCorpNm", "_CpnyAdr", "_SummryCmmdtyId", "_CpnyNm", "_RntrCorpIdr", "_CpnyTp", "_CpnyOthrTp", "_PmryDrvr", "_RntlAgrmt", "_AddtlDrvr", "_RntlInvc", "_LltyPrgrmm", "_RntrCorpIdrAssgnr"]
	@property
	def CpnyCtct(self):
		return self._CpnyCtct

	@CpnyCtct.setter
	def CpnyCtct(self, value):
		self._CpnyCtct = value if type(value) != auto else self.make_default("CpnyCtct")

	@CpnyCtct.deleter
	def CpnyCtct(self):
		del self._CpnyCtct
		self._CpnyCtct = None

	@property
	def RntrNm(self):
		return self._RntrNm

	@RntrNm.setter
	def RntrNm(self, value):
		self._RntrNm = value if type(value) != auto else self.make_default("RntrNm")

	@RntrNm.deleter
	def RntrNm(self):
		del self._RntrNm
		self._RntrNm = None

	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if type(value) != auto else self.make_default("AddtlData")

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = None

	@property
	def CpnyId(self):
		return self._CpnyId

	@CpnyId.setter
	def CpnyId(self, value):
		self._CpnyId = value if type(value) != auto else self.make_default("CpnyId")

	@CpnyId.deleter
	def CpnyId(self):
		del self._CpnyId
		self._CpnyId = None

	@property
	def RntrCorpNm(self):
		return self._RntrCorpNm

	@RntrCorpNm.setter
	def RntrCorpNm(self, value):
		self._RntrCorpNm = value if type(value) != auto else self.make_default("RntrCorpNm")

	@RntrCorpNm.deleter
	def RntrCorpNm(self):
		del self._RntrCorpNm
		self._RntrCorpNm = None

	@property
	def CpnyAdr(self):
		return self._CpnyAdr

	@CpnyAdr.setter
	def CpnyAdr(self, value):
		self._CpnyAdr = value if type(value) != auto else self.make_default("CpnyAdr")

	@CpnyAdr.deleter
	def CpnyAdr(self):
		del self._CpnyAdr
		self._CpnyAdr = None

	@property
	def SummryCmmdtyId(self):
		return self._SummryCmmdtyId

	@SummryCmmdtyId.setter
	def SummryCmmdtyId(self, value):
		self._SummryCmmdtyId = value if type(value) != auto else self.make_default("SummryCmmdtyId")

	@SummryCmmdtyId.deleter
	def SummryCmmdtyId(self):
		del self._SummryCmmdtyId
		self._SummryCmmdtyId = None

	@property
	def CpnyNm(self):
		return self._CpnyNm

	@CpnyNm.setter
	def CpnyNm(self, value):
		self._CpnyNm = value if type(value) != auto else self.make_default("CpnyNm")

	@CpnyNm.deleter
	def CpnyNm(self):
		del self._CpnyNm
		self._CpnyNm = None

	@property
	def RntrCorpIdr(self):
		return self._RntrCorpIdr

	@RntrCorpIdr.setter
	def RntrCorpIdr(self, value):
		self._RntrCorpIdr = value if type(value) != auto else self.make_default("RntrCorpIdr")

	@RntrCorpIdr.deleter
	def RntrCorpIdr(self):
		del self._RntrCorpIdr
		self._RntrCorpIdr = None

	@property
	def CpnyTp(self):
		return self._CpnyTp

	@CpnyTp.setter
	def CpnyTp(self, value):
		self._CpnyTp = value if type(value) != auto else self.make_default("CpnyTp")

	@CpnyTp.deleter
	def CpnyTp(self):
		del self._CpnyTp
		self._CpnyTp = None

	@property
	def CpnyOthrTp(self):
		return self._CpnyOthrTp

	@CpnyOthrTp.setter
	def CpnyOthrTp(self, value):
		self._CpnyOthrTp = value if type(value) != auto else self.make_default("CpnyOthrTp")

	@CpnyOthrTp.deleter
	def CpnyOthrTp(self):
		del self._CpnyOthrTp
		self._CpnyOthrTp = None

	@property
	def PmryDrvr(self):
		return self._PmryDrvr

	@PmryDrvr.setter
	def PmryDrvr(self, value):
		self._PmryDrvr = value if type(value) != auto else self.make_default("PmryDrvr")

	@PmryDrvr.deleter
	def PmryDrvr(self):
		del self._PmryDrvr
		self._PmryDrvr = None

	@property
	def RntlAgrmt(self):
		return self._RntlAgrmt

	@RntlAgrmt.setter
	def RntlAgrmt(self, value):
		self._RntlAgrmt = value if type(value) != auto else self.make_default("RntlAgrmt")

	@RntlAgrmt.deleter
	def RntlAgrmt(self):
		del self._RntlAgrmt
		self._RntlAgrmt = None

	@property
	def AddtlDrvr(self):
		return self._AddtlDrvr

	@AddtlDrvr.setter
	def AddtlDrvr(self, value):
		self._AddtlDrvr = value if type(value) != auto else self.make_default("AddtlDrvr")

	@AddtlDrvr.deleter
	def AddtlDrvr(self):
		del self._AddtlDrvr
		self._AddtlDrvr = None

	@property
	def RntlInvc(self):
		return self._RntlInvc

	@RntlInvc.setter
	def RntlInvc(self, value):
		self._RntlInvc = value if type(value) != auto else self.make_default("RntlInvc")

	@RntlInvc.deleter
	def RntlInvc(self):
		del self._RntlInvc
		self._RntlInvc = None

	@property
	def LltyPrgrmm(self):
		return self._LltyPrgrmm

	@LltyPrgrmm.setter
	def LltyPrgrmm(self, value):
		self._LltyPrgrmm = value if type(value) != auto else self.make_default("LltyPrgrmm")

	@LltyPrgrmm.deleter
	def LltyPrgrmm(self):
		del self._LltyPrgrmm
		self._LltyPrgrmm = None

	@property
	def RntrCorpIdrAssgnr(self):
		return self._RntrCorpIdrAssgnr

	@RntrCorpIdrAssgnr.setter
	def RntrCorpIdrAssgnr(self, value):
		self._RntrCorpIdrAssgnr = value if type(value) != auto else self.make_default("RntrCorpIdrAssgnr")

	@RntrCorpIdrAssgnr.deleter
	def RntrCorpIdrAssgnr(self):
		del self._RntrCorpIdrAssgnr
		self._RntrCorpIdrAssgnr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CpnyCtct', type=ContactBusiness1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RntrNm', type=Max70Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlData', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CpnyId', type=PartyIdentification285, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RntrCorpNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpnyAdr', type=Address2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SummryCmmdtyId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpnyNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RntrCorpIdr', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpnyTp', type=CarRentalActivity1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpnyOthrTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmryDrvr', type=DriverInParty3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RntlAgrmt', type=VehicleRentalAgreement3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlDrvr', type=DriverInParty3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RntlInvc', type=VehicleRentalInvoice3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LltyPrgrmm', type=LoyaltyProgramme4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RntrCorpIdrAssgnr', type=CustomerAssigner1Code, min=0, max=1, mutex_group=None, array=False),
	))

