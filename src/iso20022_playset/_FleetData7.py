# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATICAPartyType1Code
from . import AdditionalEnteredFleetData1
from . import DriverOrVehicleCardData1
from . import Exact1Text
from . import FleetDriverData2
from . import FleetLineItem7
from . import FleetTransactionDetail2
from . import FleetVehicleData1
from . import LocalAmenity2
from . import Max10Text
from . import Max1Number
from . import Max35Text
from . import Max4AlphaNumericText
from . import Max70Text

class FleetData7(base_types._BaseFieldType):

	__slots__ = ["_AddtlNtrdData", "_AgtFuelPrmptCd", "_CardFuelPrmptCd", "_Drvr", "_DrvrOrVhclCard", "_DscntMtd", "_DscntNtty", "_DscntPlanId", "_LclAmnty", "_LineItm", "_PurchsRstrctnInd", "_TripBllgId", "_TripCtrlNb", "_TripDlvryTcktNb", "_TripInvcNb", "_TripJobNb", "_TripNb", "_TripWorkOrdr", "_TxRltdData", "_Vhcl"]
	@property
	def AddtlNtrdData(self):
		return self._AddtlNtrdData

	@AddtlNtrdData.setter
	def AddtlNtrdData(self, value):
		self._AddtlNtrdData = value if value is not None else base_types.UninitialisedField(self, 'AddtlNtrdData', AdditionalEnteredFleetData1, False)

	@AddtlNtrdData.deleter
	def AddtlNtrdData(self):
		del self._AddtlNtrdData
		self._AddtlNtrdData = base_types.UninitialisedField(self, 'AddtlNtrdData', AdditionalEnteredFleetData1, False)

	@property
	def AgtFuelPrmptCd(self):
		return self._AgtFuelPrmptCd

	@AgtFuelPrmptCd.setter
	def AgtFuelPrmptCd(self, value):
		self._AgtFuelPrmptCd = value if value is not None else base_types.UninitialisedField(self, 'AgtFuelPrmptCd', Max35Text, False)

	@AgtFuelPrmptCd.deleter
	def AgtFuelPrmptCd(self):
		del self._AgtFuelPrmptCd
		self._AgtFuelPrmptCd = base_types.UninitialisedField(self, 'AgtFuelPrmptCd', Max35Text, False)

	@property
	def CardFuelPrmptCd(self):
		return self._CardFuelPrmptCd

	@CardFuelPrmptCd.setter
	def CardFuelPrmptCd(self, value):
		self._CardFuelPrmptCd = value if value is not None else base_types.UninitialisedField(self, 'CardFuelPrmptCd', Max1Number, False)

	@CardFuelPrmptCd.deleter
	def CardFuelPrmptCd(self):
		del self._CardFuelPrmptCd
		self._CardFuelPrmptCd = base_types.UninitialisedField(self, 'CardFuelPrmptCd', Max1Number, False)

	@property
	def Drvr(self):
		return self._Drvr

	@Drvr.setter
	def Drvr(self, value):
		self._Drvr = value if value is not None else base_types.UninitialisedField(self, 'Drvr', FleetDriverData2, False)

	@Drvr.deleter
	def Drvr(self):
		del self._Drvr
		self._Drvr = base_types.UninitialisedField(self, 'Drvr', FleetDriverData2, False)

	@property
	def DrvrOrVhclCard(self):
		return self._DrvrOrVhclCard

	@DrvrOrVhclCard.setter
	def DrvrOrVhclCard(self, value):
		self._DrvrOrVhclCard = value if value is not None else base_types.UninitialisedField(self, 'DrvrOrVhclCard', DriverOrVehicleCardData1, False)

	@DrvrOrVhclCard.deleter
	def DrvrOrVhclCard(self):
		del self._DrvrOrVhclCard
		self._DrvrOrVhclCard = base_types.UninitialisedField(self, 'DrvrOrVhclCard', DriverOrVehicleCardData1, False)

	@property
	def DscntMtd(self):
		return self._DscntMtd

	@DscntMtd.setter
	def DscntMtd(self, value):
		self._DscntMtd = value if value is not None else base_types.UninitialisedField(self, 'DscntMtd', Max4AlphaNumericText, False)

	@DscntMtd.deleter
	def DscntMtd(self):
		del self._DscntMtd
		self._DscntMtd = base_types.UninitialisedField(self, 'DscntMtd', Max4AlphaNumericText, False)

	@property
	def DscntNtty(self):
		return self._DscntNtty

	@DscntNtty.setter
	def DscntNtty(self, value):
		self._DscntNtty = value if value is not None else base_types.UninitialisedField(self, 'DscntNtty', ATICAPartyType1Code, False)

	@DscntNtty.deleter
	def DscntNtty(self):
		del self._DscntNtty
		self._DscntNtty = base_types.UninitialisedField(self, 'DscntNtty', ATICAPartyType1Code, False)

	@property
	def DscntPlanId(self):
		return self._DscntPlanId

	@DscntPlanId.setter
	def DscntPlanId(self, value):
		self._DscntPlanId = value if value is not None else base_types.UninitialisedField(self, 'DscntPlanId', Max35Text, False)

	@DscntPlanId.deleter
	def DscntPlanId(self):
		del self._DscntPlanId
		self._DscntPlanId = base_types.UninitialisedField(self, 'DscntPlanId', Max35Text, False)

	@property
	def LclAmnty(self):
		return self._LclAmnty

	@LclAmnty.setter
	def LclAmnty(self, value):
		self._LclAmnty = value if value is not None else base_types.UninitialisedField(self, 'LclAmnty', LocalAmenity2, True)

	@LclAmnty.deleter
	def LclAmnty(self):
		del self._LclAmnty
		self._LclAmnty = base_types.UninitialisedField(self, 'LclAmnty', LocalAmenity2, True)

	@property
	def LineItm(self):
		return self._LineItm

	@LineItm.setter
	def LineItm(self, value):
		self._LineItm = value if value is not None else base_types.UninitialisedField(self, 'LineItm', FleetLineItem7, True)

	@LineItm.deleter
	def LineItm(self):
		del self._LineItm
		self._LineItm = base_types.UninitialisedField(self, 'LineItm', FleetLineItem7, True)

	@property
	def PurchsRstrctnInd(self):
		return self._PurchsRstrctnInd

	@PurchsRstrctnInd.setter
	def PurchsRstrctnInd(self, value):
		self._PurchsRstrctnInd = value if value is not None else base_types.UninitialisedField(self, 'PurchsRstrctnInd', Exact1Text, False)

	@PurchsRstrctnInd.deleter
	def PurchsRstrctnInd(self):
		del self._PurchsRstrctnInd
		self._PurchsRstrctnInd = base_types.UninitialisedField(self, 'PurchsRstrctnInd', Exact1Text, False)

	@property
	def TripBllgId(self):
		return self._TripBllgId

	@TripBllgId.setter
	def TripBllgId(self, value):
		self._TripBllgId = value if value is not None else base_types.UninitialisedField(self, 'TripBllgId', Max70Text, False)

	@TripBllgId.deleter
	def TripBllgId(self):
		del self._TripBllgId
		self._TripBllgId = base_types.UninitialisedField(self, 'TripBllgId', Max70Text, False)

	@property
	def TripCtrlNb(self):
		return self._TripCtrlNb

	@TripCtrlNb.setter
	def TripCtrlNb(self, value):
		self._TripCtrlNb = value if value is not None else base_types.UninitialisedField(self, 'TripCtrlNb', Max35Text, False)

	@TripCtrlNb.deleter
	def TripCtrlNb(self):
		del self._TripCtrlNb
		self._TripCtrlNb = base_types.UninitialisedField(self, 'TripCtrlNb', Max35Text, False)

	@property
	def TripDlvryTcktNb(self):
		return self._TripDlvryTcktNb

	@TripDlvryTcktNb.setter
	def TripDlvryTcktNb(self, value):
		self._TripDlvryTcktNb = value if value is not None else base_types.UninitialisedField(self, 'TripDlvryTcktNb', Max35Text, False)

	@TripDlvryTcktNb.deleter
	def TripDlvryTcktNb(self):
		del self._TripDlvryTcktNb
		self._TripDlvryTcktNb = base_types.UninitialisedField(self, 'TripDlvryTcktNb', Max35Text, False)

	@property
	def TripInvcNb(self):
		return self._TripInvcNb

	@TripInvcNb.setter
	def TripInvcNb(self, value):
		self._TripInvcNb = value if value is not None else base_types.UninitialisedField(self, 'TripInvcNb', Max70Text, False)

	@TripInvcNb.deleter
	def TripInvcNb(self):
		del self._TripInvcNb
		self._TripInvcNb = base_types.UninitialisedField(self, 'TripInvcNb', Max70Text, False)

	@property
	def TripJobNb(self):
		return self._TripJobNb

	@TripJobNb.setter
	def TripJobNb(self, value):
		self._TripJobNb = value if value is not None else base_types.UninitialisedField(self, 'TripJobNb', Max10Text, False)

	@TripJobNb.deleter
	def TripJobNb(self):
		del self._TripJobNb
		self._TripJobNb = base_types.UninitialisedField(self, 'TripJobNb', Max10Text, False)

	@property
	def TripNb(self):
		return self._TripNb

	@TripNb.setter
	def TripNb(self, value):
		self._TripNb = value if value is not None else base_types.UninitialisedField(self, 'TripNb', Max35Text, False)

	@TripNb.deleter
	def TripNb(self):
		del self._TripNb
		self._TripNb = base_types.UninitialisedField(self, 'TripNb', Max35Text, False)

	@property
	def TripWorkOrdr(self):
		return self._TripWorkOrdr

	@TripWorkOrdr.setter
	def TripWorkOrdr(self, value):
		self._TripWorkOrdr = value if value is not None else base_types.UninitialisedField(self, 'TripWorkOrdr', Max70Text, False)

	@TripWorkOrdr.deleter
	def TripWorkOrdr(self):
		del self._TripWorkOrdr
		self._TripWorkOrdr = base_types.UninitialisedField(self, 'TripWorkOrdr', Max70Text, False)

	@property
	def TxRltdData(self):
		return self._TxRltdData

	@TxRltdData.setter
	def TxRltdData(self, value):
		self._TxRltdData = value if value is not None else base_types.UninitialisedField(self, 'TxRltdData', FleetTransactionDetail2, True)

	@TxRltdData.deleter
	def TxRltdData(self):
		del self._TxRltdData
		self._TxRltdData = base_types.UninitialisedField(self, 'TxRltdData', FleetTransactionDetail2, True)

	@property
	def Vhcl(self):
		return self._Vhcl

	@Vhcl.setter
	def Vhcl(self, value):
		self._Vhcl = value if value is not None else base_types.UninitialisedField(self, 'Vhcl', FleetVehicleData1, False)

	@Vhcl.deleter
	def Vhcl(self):
		del self._Vhcl
		self._Vhcl = base_types.UninitialisedField(self, 'Vhcl', FleetVehicleData1, False)

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