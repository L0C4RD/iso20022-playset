# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ATICALaxProcessing import ATICALaxProcessing
from ._FleetData7 import FleetData7
from ._Invoice4 import Invoice4
from ._Lodging5 import Lodging5
from ._PassengerTransport4 import PassengerTransport4
from ._Sale4 import Sale4
from ._ShippingData4 import ShippingData4
from ._TelecomServices4 import TelecomServices4
from ._TemporaryServices4 import TemporaryServices4
from ._TravelAgency5 import TravelAgency5
from ._VehicleRentalService4 import VehicleRentalService4

class TransactionSpecificData1(base_types._BaseFieldType):

	__slots__ = ["_Fleet", "_Invc", "_Ldgg", "_NtlData", "_PrvtData", "_PssngrTrnsprt", "_Sale", "_ShppgData", "_TelecomSvcs", "_TempSvcs", "_TrvlAgcy", "_VhclRntl"]
	@property
	def Fleet(self):
		return self._Fleet

	@Fleet.setter
	def Fleet(self, value):
		self._Fleet = value if type(value) != base_types.auto else self.make_default("Fleet")

	@Fleet.deleter
	def Fleet(self):
		del self._Fleet
		self._Fleet = None

	@property
	def Invc(self):
		return self._Invc

	@Invc.setter
	def Invc(self, value):
		self._Invc = value if type(value) != base_types.auto else self.make_default("Invc")

	@Invc.deleter
	def Invc(self):
		del self._Invc
		self._Invc = None

	@property
	def Ldgg(self):
		return self._Ldgg

	@Ldgg.setter
	def Ldgg(self, value):
		self._Ldgg = value if type(value) != base_types.auto else self.make_default("Ldgg")

	@Ldgg.deleter
	def Ldgg(self):
		del self._Ldgg
		self._Ldgg = None

	@property
	def NtlData(self):
		return self._NtlData

	@NtlData.setter
	def NtlData(self, value):
		self._NtlData = value if type(value) != base_types.auto else self.make_default("NtlData")

	@NtlData.deleter
	def NtlData(self):
		del self._NtlData
		self._NtlData = None

	@property
	def PrvtData(self):
		return self._PrvtData

	@PrvtData.setter
	def PrvtData(self, value):
		self._PrvtData = value if type(value) != base_types.auto else self.make_default("PrvtData")

	@PrvtData.deleter
	def PrvtData(self):
		del self._PrvtData
		self._PrvtData = None

	@property
	def PssngrTrnsprt(self):
		return self._PssngrTrnsprt

	@PssngrTrnsprt.setter
	def PssngrTrnsprt(self, value):
		self._PssngrTrnsprt = value if type(value) != base_types.auto else self.make_default("PssngrTrnsprt")

	@PssngrTrnsprt.deleter
	def PssngrTrnsprt(self):
		del self._PssngrTrnsprt
		self._PssngrTrnsprt = None

	@property
	def Sale(self):
		return self._Sale

	@Sale.setter
	def Sale(self, value):
		self._Sale = value if type(value) != base_types.auto else self.make_default("Sale")

	@Sale.deleter
	def Sale(self):
		del self._Sale
		self._Sale = None

	@property
	def ShppgData(self):
		return self._ShppgData

	@ShppgData.setter
	def ShppgData(self, value):
		self._ShppgData = value if type(value) != base_types.auto else self.make_default("ShppgData")

	@ShppgData.deleter
	def ShppgData(self):
		del self._ShppgData
		self._ShppgData = None

	@property
	def TelecomSvcs(self):
		return self._TelecomSvcs

	@TelecomSvcs.setter
	def TelecomSvcs(self, value):
		self._TelecomSvcs = value if type(value) != base_types.auto else self.make_default("TelecomSvcs")

	@TelecomSvcs.deleter
	def TelecomSvcs(self):
		del self._TelecomSvcs
		self._TelecomSvcs = None

	@property
	def TempSvcs(self):
		return self._TempSvcs

	@TempSvcs.setter
	def TempSvcs(self, value):
		self._TempSvcs = value if type(value) != base_types.auto else self.make_default("TempSvcs")

	@TempSvcs.deleter
	def TempSvcs(self):
		del self._TempSvcs
		self._TempSvcs = None

	@property
	def TrvlAgcy(self):
		return self._TrvlAgcy

	@TrvlAgcy.setter
	def TrvlAgcy(self, value):
		self._TrvlAgcy = value if type(value) != base_types.auto else self.make_default("TrvlAgcy")

	@TrvlAgcy.deleter
	def TrvlAgcy(self):
		del self._TrvlAgcy
		self._TrvlAgcy = None

	@property
	def VhclRntl(self):
		return self._VhclRntl

	@VhclRntl.setter
	def VhclRntl(self, value):
		self._VhclRntl = value if type(value) != base_types.auto else self.make_default("VhclRntl")

	@VhclRntl.deleter
	def VhclRntl(self):
		del self._VhclRntl
		self._VhclRntl = None

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