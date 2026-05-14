# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ATICAPartyType1Code import ATICAPartyType1Code
from ._AdditionalEnteredFleetData1 import AdditionalEnteredFleetData1
from ._DriverOrVehicleCardData1 import DriverOrVehicleCardData1
from ._Exact1Text import Exact1Text
from ._FleetDriverData2 import FleetDriverData2
from ._FleetLineItem7 import FleetLineItem7
from ._FleetTransactionDetail2 import FleetTransactionDetail2
from ._FleetVehicleData1 import FleetVehicleData1
from ._LocalAmenity2 import LocalAmenity2
from ._Max10Text import Max10Text
from ._Max1Number import Max1Number
from ._Max35Text import Max35Text
from ._Max4AlphaNumericText import Max4AlphaNumericText
from ._Max70Text import Max70Text

class FleetData7(base_types._BaseFieldType):

	__slots__ = ["_AddtlNtrdData", "_AgtFuelPrmptCd", "_CardFuelPrmptCd", "_Drvr", "_DrvrOrVhclCard", "_DscntMtd", "_DscntNtty", "_DscntPlanId", "_LclAmnty", "_LineItm", "_PurchsRstrctnInd", "_TripBllgId", "_TripCtrlNb", "_TripDlvryTcktNb", "_TripInvcNb", "_TripJobNb", "_TripNb", "_TripWorkOrdr", "_TxRltdData", "_Vhcl"]
	@property
	def AddtlNtrdData(self):
		return self._AddtlNtrdData

	@AddtlNtrdData.setter
	def AddtlNtrdData(self, value):
		self._AddtlNtrdData = value if type(value) != base_types.auto else self.make_default("AddtlNtrdData")

	@AddtlNtrdData.deleter
	def AddtlNtrdData(self):
		del self._AddtlNtrdData
		self._AddtlNtrdData = None

	@property
	def AgtFuelPrmptCd(self):
		return self._AgtFuelPrmptCd

	@AgtFuelPrmptCd.setter
	def AgtFuelPrmptCd(self, value):
		self._AgtFuelPrmptCd = value if type(value) != base_types.auto else self.make_default("AgtFuelPrmptCd")

	@AgtFuelPrmptCd.deleter
	def AgtFuelPrmptCd(self):
		del self._AgtFuelPrmptCd
		self._AgtFuelPrmptCd = None

	@property
	def CardFuelPrmptCd(self):
		return self._CardFuelPrmptCd

	@CardFuelPrmptCd.setter
	def CardFuelPrmptCd(self, value):
		self._CardFuelPrmptCd = value if type(value) != base_types.auto else self.make_default("CardFuelPrmptCd")

	@CardFuelPrmptCd.deleter
	def CardFuelPrmptCd(self):
		del self._CardFuelPrmptCd
		self._CardFuelPrmptCd = None

	@property
	def Drvr(self):
		return self._Drvr

	@Drvr.setter
	def Drvr(self, value):
		self._Drvr = value if type(value) != base_types.auto else self.make_default("Drvr")

	@Drvr.deleter
	def Drvr(self):
		del self._Drvr
		self._Drvr = None

	@property
	def DrvrOrVhclCard(self):
		return self._DrvrOrVhclCard

	@DrvrOrVhclCard.setter
	def DrvrOrVhclCard(self, value):
		self._DrvrOrVhclCard = value if type(value) != base_types.auto else self.make_default("DrvrOrVhclCard")

	@DrvrOrVhclCard.deleter
	def DrvrOrVhclCard(self):
		del self._DrvrOrVhclCard
		self._DrvrOrVhclCard = None

	@property
	def DscntMtd(self):
		return self._DscntMtd

	@DscntMtd.setter
	def DscntMtd(self, value):
		self._DscntMtd = value if type(value) != base_types.auto else self.make_default("DscntMtd")

	@DscntMtd.deleter
	def DscntMtd(self):
		del self._DscntMtd
		self._DscntMtd = None

	@property
	def DscntNtty(self):
		return self._DscntNtty

	@DscntNtty.setter
	def DscntNtty(self, value):
		self._DscntNtty = value if type(value) != base_types.auto else self.make_default("DscntNtty")

	@DscntNtty.deleter
	def DscntNtty(self):
		del self._DscntNtty
		self._DscntNtty = None

	@property
	def DscntPlanId(self):
		return self._DscntPlanId

	@DscntPlanId.setter
	def DscntPlanId(self, value):
		self._DscntPlanId = value if type(value) != base_types.auto else self.make_default("DscntPlanId")

	@DscntPlanId.deleter
	def DscntPlanId(self):
		del self._DscntPlanId
		self._DscntPlanId = None

	@property
	def LclAmnty(self):
		return self._LclAmnty

	@LclAmnty.setter
	def LclAmnty(self, value):
		self._LclAmnty = value if type(value) != base_types.auto else self.make_default("LclAmnty")

	@LclAmnty.deleter
	def LclAmnty(self):
		del self._LclAmnty
		self._LclAmnty = None

	@property
	def LineItm(self):
		return self._LineItm

	@LineItm.setter
	def LineItm(self, value):
		self._LineItm = value if type(value) != base_types.auto else self.make_default("LineItm")

	@LineItm.deleter
	def LineItm(self):
		del self._LineItm
		self._LineItm = None

	@property
	def PurchsRstrctnInd(self):
		return self._PurchsRstrctnInd

	@PurchsRstrctnInd.setter
	def PurchsRstrctnInd(self, value):
		self._PurchsRstrctnInd = value if type(value) != base_types.auto else self.make_default("PurchsRstrctnInd")

	@PurchsRstrctnInd.deleter
	def PurchsRstrctnInd(self):
		del self._PurchsRstrctnInd
		self._PurchsRstrctnInd = None

	@property
	def TripBllgId(self):
		return self._TripBllgId

	@TripBllgId.setter
	def TripBllgId(self, value):
		self._TripBllgId = value if type(value) != base_types.auto else self.make_default("TripBllgId")

	@TripBllgId.deleter
	def TripBllgId(self):
		del self._TripBllgId
		self._TripBllgId = None

	@property
	def TripCtrlNb(self):
		return self._TripCtrlNb

	@TripCtrlNb.setter
	def TripCtrlNb(self, value):
		self._TripCtrlNb = value if type(value) != base_types.auto else self.make_default("TripCtrlNb")

	@TripCtrlNb.deleter
	def TripCtrlNb(self):
		del self._TripCtrlNb
		self._TripCtrlNb = None

	@property
	def TripDlvryTcktNb(self):
		return self._TripDlvryTcktNb

	@TripDlvryTcktNb.setter
	def TripDlvryTcktNb(self, value):
		self._TripDlvryTcktNb = value if type(value) != base_types.auto else self.make_default("TripDlvryTcktNb")

	@TripDlvryTcktNb.deleter
	def TripDlvryTcktNb(self):
		del self._TripDlvryTcktNb
		self._TripDlvryTcktNb = None

	@property
	def TripInvcNb(self):
		return self._TripInvcNb

	@TripInvcNb.setter
	def TripInvcNb(self, value):
		self._TripInvcNb = value if type(value) != base_types.auto else self.make_default("TripInvcNb")

	@TripInvcNb.deleter
	def TripInvcNb(self):
		del self._TripInvcNb
		self._TripInvcNb = None

	@property
	def TripJobNb(self):
		return self._TripJobNb

	@TripJobNb.setter
	def TripJobNb(self, value):
		self._TripJobNb = value if type(value) != base_types.auto else self.make_default("TripJobNb")

	@TripJobNb.deleter
	def TripJobNb(self):
		del self._TripJobNb
		self._TripJobNb = None

	@property
	def TripNb(self):
		return self._TripNb

	@TripNb.setter
	def TripNb(self, value):
		self._TripNb = value if type(value) != base_types.auto else self.make_default("TripNb")

	@TripNb.deleter
	def TripNb(self):
		del self._TripNb
		self._TripNb = None

	@property
	def TripWorkOrdr(self):
		return self._TripWorkOrdr

	@TripWorkOrdr.setter
	def TripWorkOrdr(self, value):
		self._TripWorkOrdr = value if type(value) != base_types.auto else self.make_default("TripWorkOrdr")

	@TripWorkOrdr.deleter
	def TripWorkOrdr(self):
		del self._TripWorkOrdr
		self._TripWorkOrdr = None

	@property
	def TxRltdData(self):
		return self._TxRltdData

	@TxRltdData.setter
	def TxRltdData(self, value):
		self._TxRltdData = value if type(value) != base_types.auto else self.make_default("TxRltdData")

	@TxRltdData.deleter
	def TxRltdData(self):
		del self._TxRltdData
		self._TxRltdData = None

	@property
	def Vhcl(self):
		return self._Vhcl

	@Vhcl.setter
	def Vhcl(self, value):
		self._Vhcl = value if type(value) != base_types.auto else self.make_default("Vhcl")

	@Vhcl.deleter
	def Vhcl(self):
		del self._Vhcl
		self._Vhcl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlNtrdData', type=AdditionalEnteredFleetData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgtFuelPrmptCd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardFuelPrmptCd', type=Max1Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Drvr', type=FleetDriverData2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrvrOrVhclCard', type=DriverOrVehicleCardData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DscntMtd', type=Max4AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DscntNtty', type=ATICAPartyType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DscntPlanId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclAmnty', type=LocalAmenity2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LineItm', type=FleetLineItem7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PurchsRstrctnInd', type=Exact1Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TripBllgId', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TripCtrlNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TripDlvryTcktNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TripInvcNb', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TripJobNb', type=Max10Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TripNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TripWorkOrdr', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxRltdData', type=FleetTransactionDetail2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Vhcl', type=FleetVehicleData1, min=0, max=1, mutex_group=None, array=False),
	))