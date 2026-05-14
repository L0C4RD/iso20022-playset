# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._DatePeriod2 import DatePeriod2
from ._ISODate import ISODate
from ._InvoiceLegalIssue5 import InvoiceLegalIssue5
from ._InvoiceTotals7 import InvoiceTotals7
from ._InvoiceTotals8 import InvoiceTotals8
from ._Max35Text import Max35Text
from ._PartyIdentification136 import PartyIdentification136
from ._ServiceCategoryTotals8 import ServiceCategoryTotals8
from ._SystemAndCurrency1 import SystemAndCurrency1

class BillingReport6(base_types._BaseFieldType):

	__slots__ = ["_AcctInvcTtls", "_BllgId", "_BllgPrd", "_InvcDt", "_InvcTtls", "_PtyId", "_RgltryData", "_RspnsblPtyId", "_Svc", "_SvcCtgyTtls"]
	@property
	def AcctInvcTtls(self):
		return self._AcctInvcTtls

	@AcctInvcTtls.setter
	def AcctInvcTtls(self, value):
		self._AcctInvcTtls = value if type(value) != base_types.auto else self.make_default("AcctInvcTtls")

	@AcctInvcTtls.deleter
	def AcctInvcTtls(self):
		del self._AcctInvcTtls
		self._AcctInvcTtls = None

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
	def InvcTtls(self):
		return self._InvcTtls

	@InvcTtls.setter
	def InvcTtls(self, value):
		self._InvcTtls = value if type(value) != base_types.auto else self.make_default("InvcTtls")

	@InvcTtls.deleter
	def InvcTtls(self):
		del self._InvcTtls
		self._InvcTtls = None

	@property
	def PtyId(self):
		return self._PtyId

	@PtyId.setter
	def PtyId(self, value):
		self._PtyId = value if type(value) != base_types.auto else self.make_default("PtyId")

	@PtyId.deleter
	def PtyId(self):
		del self._PtyId
		self._PtyId = None

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
	def RspnsblPtyId(self):
		return self._RspnsblPtyId

	@RspnsblPtyId.setter
	def RspnsblPtyId(self, value):
		self._RspnsblPtyId = value if type(value) != base_types.auto else self.make_default("RspnsblPtyId")

	@RspnsblPtyId.deleter
	def RspnsblPtyId(self):
		del self._RspnsblPtyId
		self._RspnsblPtyId = None

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

	@property
	def SvcCtgyTtls(self):
		return self._SvcCtgyTtls

	@SvcCtgyTtls.setter
	def SvcCtgyTtls(self, value):
		self._SvcCtgyTtls = value if type(value) != base_types.auto else self.make_default("SvcCtgyTtls")

	@SvcCtgyTtls.deleter
	def SvcCtgyTtls(self):
		del self._SvcCtgyTtls
		self._SvcCtgyTtls = None

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