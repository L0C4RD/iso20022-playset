import base_types
import Max70Text
import Max10Text
import LocalAmenity1
import FleetTransactionDetail1
import PlainCardData23
import FleetLineItem5
import Driver3
import Max35Text
import Max1Number
import AdditionalInformation31
import Vehicle6

class FleetData6(base_types._BaseFieldType):

	__slots__ = ["_LineItm", "_AgtFuelPrmptCd", "_CardFuelPrmptCd", "_TripJobNb", "_TripDlvryTcktNb", "_TxRltdData", "_TripCtrlNb", "_TripInvcNb", "_TripNb", "_LclAmnty", "_Drvr", "_TripWorkOrdr", "_TripBllgId", "_DrvrOrVhclCard", "_Vhcl", "_AddtlNtrdData"]
	@property
	def LineItm(self):
		return self._LineItm

	@LineItm.setter
	def LineItm(self, value):
		self._LineItm = value if type(value) != auto else self.make_default("LineItm")

	@LineItm.deleter
	def LineItm(self):
		del self._LineItm
		self._LineItm = None

	@property
	def AgtFuelPrmptCd(self):
		return self._AgtFuelPrmptCd

	@AgtFuelPrmptCd.setter
	def AgtFuelPrmptCd(self, value):
		self._AgtFuelPrmptCd = value if type(value) != auto else self.make_default("AgtFuelPrmptCd")

	@AgtFuelPrmptCd.deleter
	def AgtFuelPrmptCd(self):
		del self._AgtFuelPrmptCd
		self._AgtFuelPrmptCd = None

	@property
	def CardFuelPrmptCd(self):
		return self._CardFuelPrmptCd

	@CardFuelPrmptCd.setter
	def CardFuelPrmptCd(self, value):
		self._CardFuelPrmptCd = value if type(value) != auto else self.make_default("CardFuelPrmptCd")

	@CardFuelPrmptCd.deleter
	def CardFuelPrmptCd(self):
		del self._CardFuelPrmptCd
		self._CardFuelPrmptCd = None

	@property
	def TripJobNb(self):
		return self._TripJobNb

	@TripJobNb.setter
	def TripJobNb(self, value):
		self._TripJobNb = value if type(value) != auto else self.make_default("TripJobNb")

	@TripJobNb.deleter
	def TripJobNb(self):
		del self._TripJobNb
		self._TripJobNb = None

	@property
	def TripDlvryTcktNb(self):
		return self._TripDlvryTcktNb

	@TripDlvryTcktNb.setter
	def TripDlvryTcktNb(self, value):
		self._TripDlvryTcktNb = value if type(value) != auto else self.make_default("TripDlvryTcktNb")

	@TripDlvryTcktNb.deleter
	def TripDlvryTcktNb(self):
		del self._TripDlvryTcktNb
		self._TripDlvryTcktNb = None

	@property
	def TxRltdData(self):
		return self._TxRltdData

	@TxRltdData.setter
	def TxRltdData(self, value):
		self._TxRltdData = value if type(value) != auto else self.make_default("TxRltdData")

	@TxRltdData.deleter
	def TxRltdData(self):
		del self._TxRltdData
		self._TxRltdData = None

	@property
	def TripCtrlNb(self):
		return self._TripCtrlNb

	@TripCtrlNb.setter
	def TripCtrlNb(self, value):
		self._TripCtrlNb = value if type(value) != auto else self.make_default("TripCtrlNb")

	@TripCtrlNb.deleter
	def TripCtrlNb(self):
		del self._TripCtrlNb
		self._TripCtrlNb = None

	@property
	def TripInvcNb(self):
		return self._TripInvcNb

	@TripInvcNb.setter
	def TripInvcNb(self, value):
		self._TripInvcNb = value if type(value) != auto else self.make_default("TripInvcNb")

	@TripInvcNb.deleter
	def TripInvcNb(self):
		del self._TripInvcNb
		self._TripInvcNb = None

	@property
	def TripNb(self):
		return self._TripNb

	@TripNb.setter
	def TripNb(self, value):
		self._TripNb = value if type(value) != auto else self.make_default("TripNb")

	@TripNb.deleter
	def TripNb(self):
		del self._TripNb
		self._TripNb = None

	@property
	def LclAmnty(self):
		return self._LclAmnty

	@LclAmnty.setter
	def LclAmnty(self, value):
		self._LclAmnty = value if type(value) != auto else self.make_default("LclAmnty")

	@LclAmnty.deleter
	def LclAmnty(self):
		del self._LclAmnty
		self._LclAmnty = None

	@property
	def Drvr(self):
		return self._Drvr

	@Drvr.setter
	def Drvr(self, value):
		self._Drvr = value if type(value) != auto else self.make_default("Drvr")

	@Drvr.deleter
	def Drvr(self):
		del self._Drvr
		self._Drvr = None

	@property
	def TripWorkOrdr(self):
		return self._TripWorkOrdr

	@TripWorkOrdr.setter
	def TripWorkOrdr(self, value):
		self._TripWorkOrdr = value if type(value) != auto else self.make_default("TripWorkOrdr")

	@TripWorkOrdr.deleter
	def TripWorkOrdr(self):
		del self._TripWorkOrdr
		self._TripWorkOrdr = None

	@property
	def TripBllgId(self):
		return self._TripBllgId

	@TripBllgId.setter
	def TripBllgId(self, value):
		self._TripBllgId = value if type(value) != auto else self.make_default("TripBllgId")

	@TripBllgId.deleter
	def TripBllgId(self):
		del self._TripBllgId
		self._TripBllgId = None

	@property
	def DrvrOrVhclCard(self):
		return self._DrvrOrVhclCard

	@DrvrOrVhclCard.setter
	def DrvrOrVhclCard(self, value):
		self._DrvrOrVhclCard = value if type(value) != auto else self.make_default("DrvrOrVhclCard")

	@DrvrOrVhclCard.deleter
	def DrvrOrVhclCard(self):
		del self._DrvrOrVhclCard
		self._DrvrOrVhclCard = None

	@property
	def Vhcl(self):
		return self._Vhcl

	@Vhcl.setter
	def Vhcl(self, value):
		self._Vhcl = value if type(value) != auto else self.make_default("Vhcl")

	@Vhcl.deleter
	def Vhcl(self):
		del self._Vhcl
		self._Vhcl = None

	@property
	def AddtlNtrdData(self):
		return self._AddtlNtrdData

	@AddtlNtrdData.setter
	def AddtlNtrdData(self, value):
		self._AddtlNtrdData = value if type(value) != auto else self.make_default("AddtlNtrdData")

	@AddtlNtrdData.deleter
	def AddtlNtrdData(self):
		del self._AddtlNtrdData
		self._AddtlNtrdData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LineItm', type=FleetLineItem5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AgtFuelPrmptCd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardFuelPrmptCd', type=Max1Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TripJobNb', type=Max10Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TripDlvryTcktNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxRltdData', type=FleetTransactionDetail1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TripCtrlNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TripInvcNb', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TripNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclAmnty', type=LocalAmenity1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Drvr', type=Driver3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TripWorkOrdr', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TripBllgId', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrvrOrVhclCard', type=PlainCardData23, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vhcl', type=Vehicle6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlNtrdData', type=AdditionalInformation31, min=0, max=1, mutex_group=None, array=False),
	))

