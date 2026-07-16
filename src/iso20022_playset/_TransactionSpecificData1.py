# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATICALaxProcessing
from . import FleetData7
from . import Invoice4
from . import Lodging5
from . import PassengerTransport4
from . import Sale4
from . import ShippingData4
from . import TelecomServices4
from . import TemporaryServices4
from . import TravelAgency5
from . import VehicleRentalService4

class TransactionSpecificData1(base_types._BaseFieldType):

	__slots__ = ["_Fleet", "_Invc", "_Ldgg", "_NtlData", "_PrvtData", "_PssngrTrnsprt", "_Sale", "_ShppgData", "_TelecomSvcs", "_TempSvcs", "_TrvlAgcy", "_VhclRntl"]
	@property
	def Fleet(self):
		return self._Fleet

	@Fleet.setter
	def Fleet(self, value):
		self._Fleet = value if value is not None else base_types.UninitialisedField(self, 'Fleet', FleetData7, False)

	@Fleet.deleter
	def Fleet(self):
		del self._Fleet
		self._Fleet = base_types.UninitialisedField(self, 'Fleet', FleetData7, False)

	@property
	def Invc(self):
		return self._Invc

	@Invc.setter
	def Invc(self, value):
		self._Invc = value if value is not None else base_types.UninitialisedField(self, 'Invc', Invoice4, False)

	@Invc.deleter
	def Invc(self):
		del self._Invc
		self._Invc = base_types.UninitialisedField(self, 'Invc', Invoice4, False)

	@property
	def Ldgg(self):
		return self._Ldgg

	@Ldgg.setter
	def Ldgg(self, value):
		self._Ldgg = value if value is not None else base_types.UninitialisedField(self, 'Ldgg', Lodging5, True)

	@Ldgg.deleter
	def Ldgg(self):
		del self._Ldgg
		self._Ldgg = base_types.UninitialisedField(self, 'Ldgg', Lodging5, True)

	@property
	def NtlData(self):
		return self._NtlData

	@NtlData.setter
	def NtlData(self, value):
		self._NtlData = value if value is not None else base_types.UninitialisedField(self, 'NtlData', ATICALaxProcessing, True)

	@NtlData.deleter
	def NtlData(self):
		del self._NtlData
		self._NtlData = base_types.UninitialisedField(self, 'NtlData', ATICALaxProcessing, True)

	@property
	def PrvtData(self):
		return self._PrvtData

	@PrvtData.setter
	def PrvtData(self, value):
		self._PrvtData = value if value is not None else base_types.UninitialisedField(self, 'PrvtData', ATICALaxProcessing, True)

	@PrvtData.deleter
	def PrvtData(self):
		del self._PrvtData
		self._PrvtData = base_types.UninitialisedField(self, 'PrvtData', ATICALaxProcessing, True)

	@property
	def PssngrTrnsprt(self):
		return self._PssngrTrnsprt

	@PssngrTrnsprt.setter
	def PssngrTrnsprt(self, value):
		self._PssngrTrnsprt = value if value is not None else base_types.UninitialisedField(self, 'PssngrTrnsprt', PassengerTransport4, False)

	@PssngrTrnsprt.deleter
	def PssngrTrnsprt(self):
		del self._PssngrTrnsprt
		self._PssngrTrnsprt = base_types.UninitialisedField(self, 'PssngrTrnsprt', PassengerTransport4, False)

	@property
	def Sale(self):
		return self._Sale

	@Sale.setter
	def Sale(self, value):
		self._Sale = value if value is not None else base_types.UninitialisedField(self, 'Sale', Sale4, False)

	@Sale.deleter
	def Sale(self):
		del self._Sale
		self._Sale = base_types.UninitialisedField(self, 'Sale', Sale4, False)

	@property
	def ShppgData(self):
		return self._ShppgData

	@ShppgData.setter
	def ShppgData(self, value):
		self._ShppgData = value if value is not None else base_types.UninitialisedField(self, 'ShppgData', ShippingData4, False)

	@ShppgData.deleter
	def ShppgData(self):
		del self._ShppgData
		self._ShppgData = base_types.UninitialisedField(self, 'ShppgData', ShippingData4, False)

	@property
	def TelecomSvcs(self):
		return self._TelecomSvcs

	@TelecomSvcs.setter
	def TelecomSvcs(self, value):
		self._TelecomSvcs = value if value is not None else base_types.UninitialisedField(self, 'TelecomSvcs', TelecomServices4, False)

	@TelecomSvcs.deleter
	def TelecomSvcs(self):
		del self._TelecomSvcs
		self._TelecomSvcs = base_types.UninitialisedField(self, 'TelecomSvcs', TelecomServices4, False)

	@property
	def TempSvcs(self):
		return self._TempSvcs

	@TempSvcs.setter
	def TempSvcs(self, value):
		self._TempSvcs = value if value is not None else base_types.UninitialisedField(self, 'TempSvcs', TemporaryServices4, True)

	@TempSvcs.deleter
	def TempSvcs(self):
		del self._TempSvcs
		self._TempSvcs = base_types.UninitialisedField(self, 'TempSvcs', TemporaryServices4, True)

	@property
	def TrvlAgcy(self):
		return self._TrvlAgcy

	@TrvlAgcy.setter
	def TrvlAgcy(self, value):
		self._TrvlAgcy = value if value is not None else base_types.UninitialisedField(self, 'TrvlAgcy', TravelAgency5, True)

	@TrvlAgcy.deleter
	def TrvlAgcy(self):
		del self._TrvlAgcy
		self._TrvlAgcy = base_types.UninitialisedField(self, 'TrvlAgcy', TravelAgency5, True)

	@property
	def VhclRntl(self):
		return self._VhclRntl

	@VhclRntl.setter
	def VhclRntl(self, value):
		self._VhclRntl = value if value is not None else base_types.UninitialisedField(self, 'VhclRntl', VehicleRentalService4, True)

	@VhclRntl.deleter
	def VhclRntl(self):
		del self._VhclRntl
		self._VhclRntl = base_types.UninitialisedField(self, 'VhclRntl', VehicleRentalService4, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Fleet', type=FleetData7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Invc', type=Invoice4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ldgg', type=Lodging5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NtlData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrvtData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PssngrTrnsprt', type=PassengerTransport4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sale', type=Sale4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShppgData', type=ShippingData4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TelecomSvcs', type=TelecomServices4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TempSvcs', type=TemporaryServices4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TrvlAgcy', type=TravelAgency5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='VhclRntl', type=VehicleRentalService4, min=0, max=None, mutex_group=None, array=True),
	))