# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalInformation31
from . import Driver3
from . import FleetLineItem5
from . import FleetTransactionDetail1
from . import LocalAmenity1
from . import Max10Text
from . import Max1Number
from . import Max35Text
from . import Max70Text
from . import PlainCardData23
from . import Vehicle6

class FleetData6(base_types._BaseFieldType):

	__slots__ = ["_AddtlNtrdData", "_AgtFuelPrmptCd", "_CardFuelPrmptCd", "_Drvr", "_DrvrOrVhclCard", "_LclAmnty", "_LineItm", "_TripBllgId", "_TripCtrlNb", "_TripDlvryTcktNb", "_TripInvcNb", "_TripJobNb", "_TripNb", "_TripWorkOrdr", "_TxRltdData", "_Vhcl"]
	@property
	def AddtlNtrdData(self):
		return self._AddtlNtrdData

	@AddtlNtrdData.setter
	def AddtlNtrdData(self, value):
		self._AddtlNtrdData = value if value is not None else base_types.UninitialisedField(self, 'AddtlNtrdData', AdditionalInformation31, False)

	@AddtlNtrdData.deleter
	def AddtlNtrdData(self):
		del self._AddtlNtrdData
		self._AddtlNtrdData = base_types.UninitialisedField(self, 'AddtlNtrdData', AdditionalInformation31, False)

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
		self._Drvr = value if value is not None else base_types.UninitialisedField(self, 'Drvr', Driver3, False)

	@Drvr.deleter
	def Drvr(self):
		del self._Drvr
		self._Drvr = base_types.UninitialisedField(self, 'Drvr', Driver3, False)

	@property
	def DrvrOrVhclCard(self):
		return self._DrvrOrVhclCard

	@DrvrOrVhclCard.setter
	def DrvrOrVhclCard(self, value):
		self._DrvrOrVhclCard = value if value is not None else base_types.UninitialisedField(self, 'DrvrOrVhclCard', PlainCardData23, False)

	@DrvrOrVhclCard.deleter
	def DrvrOrVhclCard(self):
		del self._DrvrOrVhclCard
		self._DrvrOrVhclCard = base_types.UninitialisedField(self, 'DrvrOrVhclCard', PlainCardData23, False)

	@property
	def LclAmnty(self):
		return self._LclAmnty

	@LclAmnty.setter
	def LclAmnty(self, value):
		self._LclAmnty = value if value is not None else base_types.UninitialisedField(self, 'LclAmnty', LocalAmenity1, True)

	@LclAmnty.deleter
	def LclAmnty(self):
		del self._LclAmnty
		self._LclAmnty = base_types.UninitialisedField(self, 'LclAmnty', LocalAmenity1, True)

	@property
	def LineItm(self):
		return self._LineItm

	@LineItm.setter
	def LineItm(self, value):
		self._LineItm = value if value is not None else base_types.UninitialisedField(self, 'LineItm', FleetLineItem5, True)

	@LineItm.deleter
	def LineItm(self):
		del self._LineItm
		self._LineItm = base_types.UninitialisedField(self, 'LineItm', FleetLineItem5, True)

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
		self._TxRltdData = value if value is not None else base_types.UninitialisedField(self, 'TxRltdData', FleetTransactionDetail1, True)

	@TxRltdData.deleter
	def TxRltdData(self):
		del self._TxRltdData
		self._TxRltdData = base_types.UninitialisedField(self, 'TxRltdData', FleetTransactionDetail1, True)

	@property
	def Vhcl(self):
		return self._Vhcl

	@Vhcl.setter
	def Vhcl(self, value):
		self._Vhcl = value if value is not None else base_types.UninitialisedField(self, 'Vhcl', Vehicle6, False)

	@Vhcl.deleter
	def Vhcl(self):
		del self._Vhcl
		self._Vhcl = base_types.UninitialisedField(self, 'Vhcl', Vehicle6, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlNtrdData', type=AdditionalInformation31, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgtFuelPrmptCd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardFuelPrmptCd', type=Max1Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Drvr', type=Driver3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrvrOrVhclCard', type=PlainCardData23, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclAmnty', type=LocalAmenity1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LineItm', type=FleetLineItem5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TripBllgId', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TripCtrlNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TripDlvryTcktNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TripInvcNb', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TripJobNb', type=Max10Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TripNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TripWorkOrdr', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxRltdData', type=FleetTransactionDetail1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Vhcl', type=Vehicle6, min=0, max=1, mutex_group=None, array=False),
	))