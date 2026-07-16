# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalData1
from . import Address2
from . import CarRentalActivity1Code
from . import ContactBusiness1
from . import CustomerAssigner1Code
from . import DriverInParty3
from . import LoyaltyProgramme4
from . import Max35Text
from . import Max70Text
from . import PartyIdentification285
from . import VehicleRentalAgreement3
from . import VehicleRentalInvoice3

class VehicleRentalService3(base_types._BaseFieldType):

	__slots__ = ["_AddtlData", "_AddtlDrvr", "_CpnyAdr", "_CpnyCtct", "_CpnyId", "_CpnyNm", "_CpnyOthrTp", "_CpnyTp", "_LltyPrgrmm", "_PmryDrvr", "_RntlAgrmt", "_RntlInvc", "_RntrCorpIdr", "_RntrCorpIdrAssgnr", "_RntrCorpNm", "_RntrNm", "_SummryCmmdtyId"]
	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if value is not None else base_types.UninitialisedField(self, 'AddtlData', AdditionalData1, True)

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = base_types.UninitialisedField(self, 'AddtlData', AdditionalData1, True)

	@property
	def AddtlDrvr(self):
		return self._AddtlDrvr

	@AddtlDrvr.setter
	def AddtlDrvr(self, value):
		self._AddtlDrvr = value if value is not None else base_types.UninitialisedField(self, 'AddtlDrvr', DriverInParty3, True)

	@AddtlDrvr.deleter
	def AddtlDrvr(self):
		del self._AddtlDrvr
		self._AddtlDrvr = base_types.UninitialisedField(self, 'AddtlDrvr', DriverInParty3, True)

	@property
	def CpnyAdr(self):
		return self._CpnyAdr

	@CpnyAdr.setter
	def CpnyAdr(self, value):
		self._CpnyAdr = value if value is not None else base_types.UninitialisedField(self, 'CpnyAdr', Address2, False)

	@CpnyAdr.deleter
	def CpnyAdr(self):
		del self._CpnyAdr
		self._CpnyAdr = base_types.UninitialisedField(self, 'CpnyAdr', Address2, False)

	@property
	def CpnyCtct(self):
		return self._CpnyCtct

	@CpnyCtct.setter
	def CpnyCtct(self, value):
		self._CpnyCtct = value if value is not None else base_types.UninitialisedField(self, 'CpnyCtct', ContactBusiness1, False)

	@CpnyCtct.deleter
	def CpnyCtct(self):
		del self._CpnyCtct
		self._CpnyCtct = base_types.UninitialisedField(self, 'CpnyCtct', ContactBusiness1, False)

	@property
	def CpnyId(self):
		return self._CpnyId

	@CpnyId.setter
	def CpnyId(self, value):
		self._CpnyId = value if value is not None else base_types.UninitialisedField(self, 'CpnyId', PartyIdentification285, False)

	@CpnyId.deleter
	def CpnyId(self):
		del self._CpnyId
		self._CpnyId = base_types.UninitialisedField(self, 'CpnyId', PartyIdentification285, False)

	@property
	def CpnyNm(self):
		return self._CpnyNm

	@CpnyNm.setter
	def CpnyNm(self, value):
		self._CpnyNm = value if value is not None else base_types.UninitialisedField(self, 'CpnyNm', Max70Text, False)

	@CpnyNm.deleter
	def CpnyNm(self):
		del self._CpnyNm
		self._CpnyNm = base_types.UninitialisedField(self, 'CpnyNm', Max70Text, False)

	@property
	def CpnyOthrTp(self):
		return self._CpnyOthrTp

	@CpnyOthrTp.setter
	def CpnyOthrTp(self, value):
		self._CpnyOthrTp = value if value is not None else base_types.UninitialisedField(self, 'CpnyOthrTp', Max35Text, False)

	@CpnyOthrTp.deleter
	def CpnyOthrTp(self):
		del self._CpnyOthrTp
		self._CpnyOthrTp = base_types.UninitialisedField(self, 'CpnyOthrTp', Max35Text, False)

	@property
	def CpnyTp(self):
		return self._CpnyTp

	@CpnyTp.setter
	def CpnyTp(self, value):
		self._CpnyTp = value if value is not None else base_types.UninitialisedField(self, 'CpnyTp', CarRentalActivity1Code, False)

	@CpnyTp.deleter
	def CpnyTp(self):
		del self._CpnyTp
		self._CpnyTp = base_types.UninitialisedField(self, 'CpnyTp', CarRentalActivity1Code, False)

	@property
	def LltyPrgrmm(self):
		return self._LltyPrgrmm

	@LltyPrgrmm.setter
	def LltyPrgrmm(self, value):
		self._LltyPrgrmm = value if value is not None else base_types.UninitialisedField(self, 'LltyPrgrmm', LoyaltyProgramme4, False)

	@LltyPrgrmm.deleter
	def LltyPrgrmm(self):
		del self._LltyPrgrmm
		self._LltyPrgrmm = base_types.UninitialisedField(self, 'LltyPrgrmm', LoyaltyProgramme4, False)

	@property
	def PmryDrvr(self):
		return self._PmryDrvr

	@PmryDrvr.setter
	def PmryDrvr(self, value):
		self._PmryDrvr = value if value is not None else base_types.UninitialisedField(self, 'PmryDrvr', DriverInParty3, False)

	@PmryDrvr.deleter
	def PmryDrvr(self):
		del self._PmryDrvr
		self._PmryDrvr = base_types.UninitialisedField(self, 'PmryDrvr', DriverInParty3, False)

	@property
	def RntlAgrmt(self):
		return self._RntlAgrmt

	@RntlAgrmt.setter
	def RntlAgrmt(self, value):
		self._RntlAgrmt = value if value is not None else base_types.UninitialisedField(self, 'RntlAgrmt', VehicleRentalAgreement3, False)

	@RntlAgrmt.deleter
	def RntlAgrmt(self):
		del self._RntlAgrmt
		self._RntlAgrmt = base_types.UninitialisedField(self, 'RntlAgrmt', VehicleRentalAgreement3, False)

	@property
	def RntlInvc(self):
		return self._RntlInvc

	@RntlInvc.setter
	def RntlInvc(self, value):
		self._RntlInvc = value if value is not None else base_types.UninitialisedField(self, 'RntlInvc', VehicleRentalInvoice3, False)

	@RntlInvc.deleter
	def RntlInvc(self):
		del self._RntlInvc
		self._RntlInvc = base_types.UninitialisedField(self, 'RntlInvc', VehicleRentalInvoice3, False)

	@property
	def RntrCorpIdr(self):
		return self._RntrCorpIdr

	@RntrCorpIdr.setter
	def RntrCorpIdr(self, value):
		self._RntrCorpIdr = value if value is not None else base_types.UninitialisedField(self, 'RntrCorpIdr', Max35Text, False)

	@RntrCorpIdr.deleter
	def RntrCorpIdr(self):
		del self._RntrCorpIdr
		self._RntrCorpIdr = base_types.UninitialisedField(self, 'RntrCorpIdr', Max35Text, False)

	@property
	def RntrCorpIdrAssgnr(self):
		return self._RntrCorpIdrAssgnr

	@RntrCorpIdrAssgnr.setter
	def RntrCorpIdrAssgnr(self, value):
		self._RntrCorpIdrAssgnr = value if value is not None else base_types.UninitialisedField(self, 'RntrCorpIdrAssgnr', CustomerAssigner1Code, False)

	@RntrCorpIdrAssgnr.deleter
	def RntrCorpIdrAssgnr(self):
		del self._RntrCorpIdrAssgnr
		self._RntrCorpIdrAssgnr = base_types.UninitialisedField(self, 'RntrCorpIdrAssgnr', CustomerAssigner1Code, False)

	@property
	def RntrCorpNm(self):
		return self._RntrCorpNm

	@RntrCorpNm.setter
	def RntrCorpNm(self, value):
		self._RntrCorpNm = value if value is not None else base_types.UninitialisedField(self, 'RntrCorpNm', Max70Text, False)

	@RntrCorpNm.deleter
	def RntrCorpNm(self):
		del self._RntrCorpNm
		self._RntrCorpNm = base_types.UninitialisedField(self, 'RntrCorpNm', Max70Text, False)

	@property
	def RntrNm(self):
		return self._RntrNm

	@RntrNm.setter
	def RntrNm(self, value):
		self._RntrNm = value if value is not None else base_types.UninitialisedField(self, 'RntrNm', Max70Text, False)

	@RntrNm.deleter
	def RntrNm(self):
		del self._RntrNm
		self._RntrNm = base_types.UninitialisedField(self, 'RntrNm', Max70Text, False)

	@property
	def SummryCmmdtyId(self):
		return self._SummryCmmdtyId

	@SummryCmmdtyId.setter
	def SummryCmmdtyId(self, value):
		self._SummryCmmdtyId = value if value is not None else base_types.UninitialisedField(self, 'SummryCmmdtyId', Max35Text, False)

	@SummryCmmdtyId.deleter
	def SummryCmmdtyId(self):
		del self._SummryCmmdtyId
		self._SummryCmmdtyId = base_types.UninitialisedField(self, 'SummryCmmdtyId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlData', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlDrvr', type=DriverInParty3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CpnyAdr', type=Address2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpnyCtct', type=ContactBusiness1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpnyId', type=PartyIdentification285, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpnyNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpnyOthrTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpnyTp', type=CarRentalActivity1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LltyPrgrmm', type=LoyaltyProgramme4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmryDrvr', type=DriverInParty3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RntlAgrmt', type=VehicleRentalAgreement3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RntlInvc', type=VehicleRentalInvoice3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RntrCorpIdr', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RntrCorpIdrAssgnr', type=CustomerAssigner1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RntrCorpNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RntrNm', type=Max70Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SummryCmmdtyId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))