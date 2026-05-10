import base_types
import ShippingData3
import Invoice3
import FleetData6
import TelecomServices3
import TemporaryServices3
import Sale3
import VehicleRentalService3
import Lodging4
import AdditionalData2
import PassengerTransport3
import TravelAgency4

class AddendumData6(base_types._BaseFieldType):

	__slots__ = ["_ShppgData", "_TelecomSvcs", "_AddtlData", "_TrvlAgcy", "_Invc", "_Sale", "_VhclRntl", "_Fleet", "_PssngrTrnsprt", "_Ldgg", "_TempSvcs"]
	@property
	def ShppgData(self):
		return self._ShppgData

	@ShppgData.setter
	def ShppgData(self, value):
		self._ShppgData = value if type(value) != auto else self.make_default("ShppgData")

	@ShppgData.deleter
	def ShppgData(self):
		del self._ShppgData
		self._ShppgData = None

	@property
	def TelecomSvcs(self):
		return self._TelecomSvcs

	@TelecomSvcs.setter
	def TelecomSvcs(self, value):
		self._TelecomSvcs = value if type(value) != auto else self.make_default("TelecomSvcs")

	@TelecomSvcs.deleter
	def TelecomSvcs(self):
		del self._TelecomSvcs
		self._TelecomSvcs = None

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
	def TrvlAgcy(self):
		return self._TrvlAgcy

	@TrvlAgcy.setter
	def TrvlAgcy(self, value):
		self._TrvlAgcy = value if type(value) != auto else self.make_default("TrvlAgcy")

	@TrvlAgcy.deleter
	def TrvlAgcy(self):
		del self._TrvlAgcy
		self._TrvlAgcy = None

	@property
	def Invc(self):
		return self._Invc

	@Invc.setter
	def Invc(self, value):
		self._Invc = value if type(value) != auto else self.make_default("Invc")

	@Invc.deleter
	def Invc(self):
		del self._Invc
		self._Invc = None

	@property
	def Sale(self):
		return self._Sale

	@Sale.setter
	def Sale(self, value):
		self._Sale = value if type(value) != auto else self.make_default("Sale")

	@Sale.deleter
	def Sale(self):
		del self._Sale
		self._Sale = None

	@property
	def VhclRntl(self):
		return self._VhclRntl

	@VhclRntl.setter
	def VhclRntl(self, value):
		self._VhclRntl = value if type(value) != auto else self.make_default("VhclRntl")

	@VhclRntl.deleter
	def VhclRntl(self):
		del self._VhclRntl
		self._VhclRntl = None

	@property
	def Fleet(self):
		return self._Fleet

	@Fleet.setter
	def Fleet(self, value):
		self._Fleet = value if type(value) != auto else self.make_default("Fleet")

	@Fleet.deleter
	def Fleet(self):
		del self._Fleet
		self._Fleet = None

	@property
	def PssngrTrnsprt(self):
		return self._PssngrTrnsprt

	@PssngrTrnsprt.setter
	def PssngrTrnsprt(self, value):
		self._PssngrTrnsprt = value if type(value) != auto else self.make_default("PssngrTrnsprt")

	@PssngrTrnsprt.deleter
	def PssngrTrnsprt(self):
		del self._PssngrTrnsprt
		self._PssngrTrnsprt = None

	@property
	def Ldgg(self):
		return self._Ldgg

	@Ldgg.setter
	def Ldgg(self, value):
		self._Ldgg = value if type(value) != auto else self.make_default("Ldgg")

	@Ldgg.deleter
	def Ldgg(self):
		del self._Ldgg
		self._Ldgg = None

	@property
	def TempSvcs(self):
		return self._TempSvcs

	@TempSvcs.setter
	def TempSvcs(self, value):
		self._TempSvcs = value if type(value) != auto else self.make_default("TempSvcs")

	@TempSvcs.deleter
	def TempSvcs(self):
		del self._TempSvcs
		self._TempSvcs = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ShppgData', type=ShippingData3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TelecomSvcs', type=TelecomServices3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlData', type=AdditionalData2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TrvlAgcy', type=TravelAgency4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Invc', type=Invoice3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sale', type=Sale3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VhclRntl', type=VehicleRentalService3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Fleet', type=FleetData6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PssngrTrnsprt', type=PassengerTransport3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ldgg', type=Lodging4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TempSvcs', type=TemporaryServices3, min=0, max=None, mutex_group=None, array=True),
	))

