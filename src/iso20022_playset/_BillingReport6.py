# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DatePeriod2
from . import ISODate
from . import InvoiceLegalIssue5
from . import InvoiceTotals7
from . import InvoiceTotals8
from . import Max35Text
from . import PartyIdentification136
from . import ServiceCategoryTotals8
from . import SystemAndCurrency1

class BillingReport6(base_types._BaseFieldType):

	__slots__ = ["_AcctInvcTtls", "_BllgId", "_BllgPrd", "_InvcDt", "_InvcTtls", "_PtyId", "_RgltryData", "_RspnsblPtyId", "_Svc", "_SvcCtgyTtls"]
	@property
	def AcctInvcTtls(self):
		return self._AcctInvcTtls

	@AcctInvcTtls.setter
	def AcctInvcTtls(self, value):
		self._AcctInvcTtls = value if value is not None else base_types.UninitialisedField(self, 'AcctInvcTtls', InvoiceTotals8, True)

	@AcctInvcTtls.deleter
	def AcctInvcTtls(self):
		del self._AcctInvcTtls
		self._AcctInvcTtls = base_types.UninitialisedField(self, 'AcctInvcTtls', InvoiceTotals8, True)

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
	def InvcTtls(self):
		return self._InvcTtls

	@InvcTtls.setter
	def InvcTtls(self, value):
		self._InvcTtls = value if value is not None else base_types.UninitialisedField(self, 'InvcTtls', InvoiceTotals7, False)

	@InvcTtls.deleter
	def InvcTtls(self):
		del self._InvcTtls
		self._InvcTtls = base_types.UninitialisedField(self, 'InvcTtls', InvoiceTotals7, False)

	@property
	def PtyId(self):
		return self._PtyId

	@PtyId.setter
	def PtyId(self, value):
		self._PtyId = value if value is not None else base_types.UninitialisedField(self, 'PtyId', PartyIdentification136, False)

	@PtyId.deleter
	def PtyId(self):
		del self._PtyId
		self._PtyId = base_types.UninitialisedField(self, 'PtyId', PartyIdentification136, False)

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
	def RspnsblPtyId(self):
		return self._RspnsblPtyId

	@RspnsblPtyId.setter
	def RspnsblPtyId(self, value):
		self._RspnsblPtyId = value if value is not None else base_types.UninitialisedField(self, 'RspnsblPtyId', PartyIdentification136, False)

	@RspnsblPtyId.deleter
	def RspnsblPtyId(self):
		del self._RspnsblPtyId
		self._RspnsblPtyId = base_types.UninitialisedField(self, 'RspnsblPtyId', PartyIdentification136, False)

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

	@property
	def SvcCtgyTtls(self):
		return self._SvcCtgyTtls

	@SvcCtgyTtls.setter
	def SvcCtgyTtls(self, value):
		self._SvcCtgyTtls = value if value is not None else base_types.UninitialisedField(self, 'SvcCtgyTtls', ServiceCategoryTotals8, True)

	@SvcCtgyTtls.deleter
	def SvcCtgyTtls(self):
		del self._SvcCtgyTtls
		self._SvcCtgyTtls = base_types.UninitialisedField(self, 'SvcCtgyTtls', ServiceCategoryTotals8, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctInvcTtls', type=InvoiceTotals8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BllgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BllgPrd', type=DatePeriod2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvcDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvcTtls', type=InvoiceTotals7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyId', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RgltryData', type=InvoiceLegalIssue5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnsblPtyId', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Svc', type=SystemAndCurrency1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcCtgyTtls', type=ServiceCategoryTotals8, min=0, max=None, mutex_group=None, array=True),
	))