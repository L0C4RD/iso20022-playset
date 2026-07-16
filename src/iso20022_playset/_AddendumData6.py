# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalData2
from . import FleetData6
from . import Invoice3
from . import Lodging4
from . import PassengerTransport3
from . import Sale3
from . import ShippingData3
from . import TelecomServices3
from . import TemporaryServices3
from . import TravelAgency4
from . import VehicleRentalService3

class AddendumData6(base_types._BaseFieldType):

	__slots__ = ["_AddtlData", "_Fleet", "_Invc", "_Ldgg", "_PssngrTrnsprt", "_Sale", "_ShppgData", "_TelecomSvcs", "_TempSvcs", "_TrvlAgcy", "_VhclRntl"]
	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if value is not None else base_types.UninitialisedField(self, 'AddtlData', AdditionalData2, True)

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = base_types.UninitialisedField(self, 'AddtlData', AdditionalData2, True)

	@property
	def Fleet(self):
		return self._Fleet

	@Fleet.setter
	def Fleet(self, value):
		self._Fleet = value if value is not None else base_types.UninitialisedField(self, 'Fleet', FleetData6, False)

	@Fleet.deleter
	def Fleet(self):
		del self._Fleet
		self._Fleet = base_types.UninitialisedField(self, 'Fleet', FleetData6, False)

	@property
	def Invc(self):
		return self._Invc

	@Invc.setter
	def Invc(self, value):
		self._Invc = value if value is not None else base_types.UninitialisedField(self, 'Invc', Invoice3, False)

	@Invc.deleter
	def Invc(self):
		del self._Invc
		self._Invc = base_types.UninitialisedField(self, 'Invc', Invoice3, False)

	@property
	def Ldgg(self):
		return self._Ldgg

	@Ldgg.setter
	def Ldgg(self, value):
		self._Ldgg = value if value is not None else base_types.UninitialisedField(self, 'Ldgg', Lodging4, True)

	@Ldgg.deleter
	def Ldgg(self):
		del self._Ldgg
		self._Ldgg = base_types.UninitialisedField(self, 'Ldgg', Lodging4, True)

	@property
	def PssngrTrnsprt(self):
		return self._PssngrTrnsprt

	@PssngrTrnsprt.setter
	def PssngrTrnsprt(self, value):
		self._PssngrTrnsprt = value if value is not None else base_types.UninitialisedField(self, 'PssngrTrnsprt', PassengerTransport3, False)

	@PssngrTrnsprt.deleter
	def PssngrTrnsprt(self):
		del self._PssngrTrnsprt
		self._PssngrTrnsprt = base_types.UninitialisedField(self, 'PssngrTrnsprt', PassengerTransport3, False)

	@property
	def Sale(self):
		return self._Sale

	@Sale.setter
	def Sale(self, value):
		self._Sale = value if value is not None else base_types.UninitialisedField(self, 'Sale', Sale3, False)

	@Sale.deleter
	def Sale(self):
		del self._Sale
		self._Sale = base_types.UninitialisedField(self, 'Sale', Sale3, False)

	@property
	def ShppgData(self):
		return self._ShppgData

	@ShppgData.setter
	def ShppgData(self, value):
		self._ShppgData = value if value is not None else base_types.UninitialisedField(self, 'ShppgData', ShippingData3, False)

	@ShppgData.deleter
	def ShppgData(self):
		del self._ShppgData
		self._ShppgData = base_types.UninitialisedField(self, 'ShppgData', ShippingData3, False)

	@property
	def TelecomSvcs(self):
		return self._TelecomSvcs

	@TelecomSvcs.setter
	def TelecomSvcs(self, value):
		self._TelecomSvcs = value if value is not None else base_types.UninitialisedField(self, 'TelecomSvcs', TelecomServices3, False)

	@TelecomSvcs.deleter
	def TelecomSvcs(self):
		del self._TelecomSvcs
		self._TelecomSvcs = base_types.UninitialisedField(self, 'TelecomSvcs', TelecomServices3, False)

	@property
	def TempSvcs(self):
		return self._TempSvcs

	@TempSvcs.setter
	def TempSvcs(self, value):
		self._TempSvcs = value if value is not None else base_types.UninitialisedField(self, 'TempSvcs', TemporaryServices3, True)

	@TempSvcs.deleter
	def TempSvcs(self):
		del self._TempSvcs
		self._TempSvcs = base_types.UninitialisedField(self, 'TempSvcs', TemporaryServices3, True)

	@property
	def TrvlAgcy(self):
		return self._TrvlAgcy

	@TrvlAgcy.setter
	def TrvlAgcy(self, value):
		self._TrvlAgcy = value if value is not None else base_types.UninitialisedField(self, 'TrvlAgcy', TravelAgency4, True)

	@TrvlAgcy.deleter
	def TrvlAgcy(self):
		del self._TrvlAgcy
		self._TrvlAgcy = base_types.UninitialisedField(self, 'TrvlAgcy', TravelAgency4, True)

	@property
	def VhclRntl(self):
		return self._VhclRntl

	@VhclRntl.setter
	def VhclRntl(self, value):
		self._VhclRntl = value if value is not None else base_types.UninitialisedField(self, 'VhclRntl', VehicleRentalService3, True)

	@VhclRntl.deleter
	def VhclRntl(self):
		del self._VhclRntl
		self._VhclRntl = base_types.UninitialisedField(self, 'VhclRntl', VehicleRentalService3, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlData', type=AdditionalData2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Fleet', type=FleetData6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Invc', type=Invoice3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ldgg', type=Lodging4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PssngrTrnsprt', type=PassengerTransport3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sale', type=Sale3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShppgData', type=ShippingData3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TelecomSvcs', type=TelecomServices3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TempSvcs', type=TemporaryServices3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TrvlAgcy', type=TravelAgency4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='VhclRntl', type=VehicleRentalService3, min=0, max=None, mutex_group=None, array=True),
	))