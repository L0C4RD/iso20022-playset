# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CancellationReason16Choice
from . import DatePeriod2
from . import ISODate
from . import InvoiceLegalIssue5
from . import Max35Text
from . import SystemAndCurrency1

class BillingCancellationReport3(base_types._BaseFieldType):

	__slots__ = ["_BllgId", "_BllgPrd", "_CxlRsn", "_InvcDt", "_RgltryData", "_Svc"]
	@property
	def BllgId(self):
		return self._BllgId

	@BllgId.setter
	def BllgId(self, value):
		self._BllgId = value if value is not None else base_types.UninitialisedField(self, 'BllgId', Max35Text, False)

	@BllgId.deleter
	def BllgId(self):
		del self._BllgId
		self._BllgId = base_types.UninitialisedField(self, 'BllgId', Max35Text, False)

	@property
	def BllgPrd(self):
		return self._BllgPrd

	@BllgPrd.setter
	def BllgPrd(self, value):
		self._BllgPrd = value if value is not None else base_types.UninitialisedField(self, 'BllgPrd', DatePeriod2, False)

	@BllgPrd.deleter
	def BllgPrd(self):
		del self._BllgPrd
		self._BllgPrd = base_types.UninitialisedField(self, 'BllgPrd', DatePeriod2, False)

	@property
	def CxlRsn(self):
		return self._CxlRsn

	@CxlRsn.setter
	def CxlRsn(self, value):
		self._CxlRsn = value if value is not None else base_types.UninitialisedField(self, 'CxlRsn', CancellationReason16Choice, False)

	@CxlRsn.deleter
	def CxlRsn(self):
		del self._CxlRsn
		self._CxlRsn = base_types.UninitialisedField(self, 'CxlRsn', CancellationReason16Choice, False)

	@property
	def InvcDt(self):
		return self._InvcDt

	@InvcDt.setter
	def InvcDt(self, value):
		self._InvcDt = value if value is not None else base_types.UninitialisedField(self, 'InvcDt', ISODate, False)

	@InvcDt.deleter
	def InvcDt(self):
		del self._InvcDt
		self._InvcDt = base_types.UninitialisedField(self, 'InvcDt', ISODate, False)

	@property
	def RgltryData(self):
		return self._RgltryData

	@RgltryData.setter
	def RgltryData(self, value):
		self._RgltryData = value if value is not None else base_types.UninitialisedField(self, 'RgltryData', InvoiceLegalIssue5, False)

	@RgltryData.deleter
	def RgltryData(self):
		del self._RgltryData
		self._RgltryData = base_types.UninitialisedField(self, 'RgltryData', InvoiceLegalIssue5, False)

	@property
	def Svc(self):
		return self._Svc

	@Svc.setter
	def Svc(self, value):
		self._Svc = value if value is not None else base_types.UninitialisedField(self, 'Svc', SystemAndCurrency1, False)

	@Svc.deleter
	def Svc(self):
		del self._Svc
		self._Svc = base_types.UninitialisedField(self, 'Svc', SystemAndCurrency1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BllgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BllgPrd', type=DatePeriod2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlRsn', type=CancellationReason16Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvcDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RgltryData', type=InvoiceLegalIssue5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Svc', type=SystemAndCurrency1, min=0, max=1, mutex_group=None, array=False),
	))