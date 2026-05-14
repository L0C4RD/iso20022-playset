# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CancellationReason16Choice import CancellationReason16Choice
from ._DatePeriod2 import DatePeriod2
from ._ISODate import ISODate
from ._InvoiceLegalIssue5 import InvoiceLegalIssue5
from ._Max35Text import Max35Text
from ._SystemAndCurrency1 import SystemAndCurrency1

class BillingCancellationReport3(base_types._BaseFieldType):

	__slots__ = ["_BllgId", "_BllgPrd", "_CxlRsn", "_InvcDt", "_RgltryData", "_Svc"]
	@property
	def BllgId(self):
		return self._BllgId

	@BllgId.setter
	def BllgId(self, value):
		self._BllgId = value if type(value) != base_types.auto else self.make_default("BllgId")

	@BllgId.deleter
	def BllgId(self):
		del self._BllgId
		self._BllgId = None

	@property
	def BllgPrd(self):
		return self._BllgPrd

	@BllgPrd.setter
	def BllgPrd(self, value):
		self._BllgPrd = value if type(value) != base_types.auto else self.make_default("BllgPrd")

	@BllgPrd.deleter
	def BllgPrd(self):
		del self._BllgPrd
		self._BllgPrd = None

	@property
	def CxlRsn(self):
		return self._CxlRsn

	@CxlRsn.setter
	def CxlRsn(self, value):
		self._CxlRsn = value if type(value) != base_types.auto else self.make_default("CxlRsn")

	@CxlRsn.deleter
	def CxlRsn(self):
		del self._CxlRsn
		self._CxlRsn = None

	@property
	def InvcDt(self):
		return self._InvcDt

	@InvcDt.setter
	def InvcDt(self, value):
		self._InvcDt = value if type(value) != base_types.auto else self.make_default("InvcDt")

	@InvcDt.deleter
	def InvcDt(self):
		del self._InvcDt
		self._InvcDt = None

	@property
	def RgltryData(self):
		return self._RgltryData

	@RgltryData.setter
	def RgltryData(self, value):
		self._RgltryData = value if type(value) != base_types.auto else self.make_default("RgltryData")

	@RgltryData.deleter
	def RgltryData(self):
		del self._RgltryData
		self._RgltryData = None

	@property
	def Svc(self):
		return self._Svc

	@Svc.setter
	def Svc(self, value):
		self._Svc = value if type(value) != base_types.auto else self.make_default("Svc")

	@Svc.deleter
	def Svc(self):
		del self._Svc
		self._Svc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BllgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BllgPrd', type=DatePeriod2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlRsn', type=CancellationReason16Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvcDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RgltryData', type=InvoiceLegalIssue5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Svc', type=SystemAndCurrency1, min=0, max=1, mutex_group=None, array=False),
	))