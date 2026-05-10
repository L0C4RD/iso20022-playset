from . import base_types
from .SettlementTerms3 import SettlementTerms3
from .PaymentTerms4 import PaymentTerms4
from .DocumentIdentification1 import DocumentIdentification1
from .PartyIdentification26 import PartyIdentification26
from .LineItem15 import LineItem15
from .InvoiceIdentification1 import InvoiceIdentification1

class CommercialDataSet5(base_types._BaseFieldType):

	__slots__ = ["_Sellr", "_SttlmTerms", "_BllTo", "_DataSetId", "_ComrclDocRef", "_Buyr", "_Goods", "_PmtTerms"]
	@property
	def Sellr(self):
		return self._Sellr

	@Sellr.setter
	def Sellr(self, value):
		self._Sellr = value if type(value) != auto else self.make_default("Sellr")

	@Sellr.deleter
	def Sellr(self):
		del self._Sellr
		self._Sellr = None

	@property
	def SttlmTerms(self):
		return self._SttlmTerms

	@SttlmTerms.setter
	def SttlmTerms(self, value):
		self._SttlmTerms = value if type(value) != auto else self.make_default("SttlmTerms")

	@SttlmTerms.deleter
	def SttlmTerms(self):
		del self._SttlmTerms
		self._SttlmTerms = None

	@property
	def BllTo(self):
		return self._BllTo

	@BllTo.setter
	def BllTo(self, value):
		self._BllTo = value if type(value) != auto else self.make_default("BllTo")

	@BllTo.deleter
	def BllTo(self):
		del self._BllTo
		self._BllTo = None

	@property
	def DataSetId(self):
		return self._DataSetId

	@DataSetId.setter
	def DataSetId(self, value):
		self._DataSetId = value if type(value) != auto else self.make_default("DataSetId")

	@DataSetId.deleter
	def DataSetId(self):
		del self._DataSetId
		self._DataSetId = None

	@property
	def ComrclDocRef(self):
		return self._ComrclDocRef

	@ComrclDocRef.setter
	def ComrclDocRef(self, value):
		self._ComrclDocRef = value if type(value) != auto else self.make_default("ComrclDocRef")

	@ComrclDocRef.deleter
	def ComrclDocRef(self):
		del self._ComrclDocRef
		self._ComrclDocRef = None

	@property
	def Buyr(self):
		return self._Buyr

	@Buyr.setter
	def Buyr(self, value):
		self._Buyr = value if type(value) != auto else self.make_default("Buyr")

	@Buyr.deleter
	def Buyr(self):
		del self._Buyr
		self._Buyr = None

	@property
	def Goods(self):
		return self._Goods

	@Goods.setter
	def Goods(self, value):
		self._Goods = value if type(value) != auto else self.make_default("Goods")

	@Goods.deleter
	def Goods(self):
		del self._Goods
		self._Goods = None

	@property
	def PmtTerms(self):
		return self._PmtTerms

	@PmtTerms.setter
	def PmtTerms(self, value):
		self._PmtTerms = value if type(value) != auto else self.make_default("PmtTerms")

	@PmtTerms.deleter
	def PmtTerms(self):
		del self._PmtTerms
		self._PmtTerms = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Sellr', type=PartyIdentification26, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmTerms', type=SettlementTerms3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BllTo', type=PartyIdentification26, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DataSetId', type=DocumentIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ComrclDocRef', type=InvoiceIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Buyr', type=PartyIdentification26, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Goods', type=LineItem15, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PmtTerms', type=PaymentTerms4, min=1, max=None, mutex_group=None, array=True),
	))

