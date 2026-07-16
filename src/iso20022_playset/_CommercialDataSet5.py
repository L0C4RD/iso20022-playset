# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DocumentIdentification1
from . import InvoiceIdentification1
from . import LineItem15
from . import PartyIdentification26
from . import PaymentTerms4
from . import SettlementTerms3

class CommercialDataSet5(base_types._BaseFieldType):

	__slots__ = ["_BllTo", "_Buyr", "_ComrclDocRef", "_DataSetId", "_Goods", "_PmtTerms", "_Sellr", "_SttlmTerms"]
	@property
	def BllTo(self):
		return self._BllTo

	@BllTo.setter
	def BllTo(self, value):
		self._BllTo = value if value is not None else base_types.UninitialisedField(self, 'BllTo', PartyIdentification26, False)

	@BllTo.deleter
	def BllTo(self):
		del self._BllTo
		self._BllTo = base_types.UninitialisedField(self, 'BllTo', PartyIdentification26, False)

	@property
	def Buyr(self):
		return self._Buyr

	@Buyr.setter
	def Buyr(self, value):
		self._Buyr = value if value is not None else base_types.UninitialisedField(self, 'Buyr', PartyIdentification26, False)

	@Buyr.deleter
	def Buyr(self):
		del self._Buyr
		self._Buyr = base_types.UninitialisedField(self, 'Buyr', PartyIdentification26, False)

	@property
	def ComrclDocRef(self):
		return self._ComrclDocRef

	@ComrclDocRef.setter
	def ComrclDocRef(self, value):
		self._ComrclDocRef = value if value is not None else base_types.UninitialisedField(self, 'ComrclDocRef', InvoiceIdentification1, False)

	@ComrclDocRef.deleter
	def ComrclDocRef(self):
		del self._ComrclDocRef
		self._ComrclDocRef = base_types.UninitialisedField(self, 'ComrclDocRef', InvoiceIdentification1, False)

	@property
	def DataSetId(self):
		return self._DataSetId

	@DataSetId.setter
	def DataSetId(self, value):
		self._DataSetId = value if value is not None else base_types.UninitialisedField(self, 'DataSetId', DocumentIdentification1, False)

	@DataSetId.deleter
	def DataSetId(self):
		del self._DataSetId
		self._DataSetId = base_types.UninitialisedField(self, 'DataSetId', DocumentIdentification1, False)

	@property
	def Goods(self):
		return self._Goods

	@Goods.setter
	def Goods(self, value):
		self._Goods = value if value is not None else base_types.UninitialisedField(self, 'Goods', LineItem15, True)

	@Goods.deleter
	def Goods(self):
		del self._Goods
		self._Goods = base_types.UninitialisedField(self, 'Goods', LineItem15, True)

	@property
	def PmtTerms(self):
		return self._PmtTerms

	@PmtTerms.setter
	def PmtTerms(self, value):
		self._PmtTerms = value if value is not None else base_types.UninitialisedField(self, 'PmtTerms', PaymentTerms4, True)

	@PmtTerms.deleter
	def PmtTerms(self):
		del self._PmtTerms
		self._PmtTerms = base_types.UninitialisedField(self, 'PmtTerms', PaymentTerms4, True)

	@property
	def Sellr(self):
		return self._Sellr

	@Sellr.setter
	def Sellr(self, value):
		self._Sellr = value if value is not None else base_types.UninitialisedField(self, 'Sellr', PartyIdentification26, False)

	@Sellr.deleter
	def Sellr(self):
		del self._Sellr
		self._Sellr = base_types.UninitialisedField(self, 'Sellr', PartyIdentification26, False)

	@property
	def SttlmTerms(self):
		return self._SttlmTerms

	@SttlmTerms.setter
	def SttlmTerms(self, value):
		self._SttlmTerms = value if value is not None else base_types.UninitialisedField(self, 'SttlmTerms', SettlementTerms3, False)

	@SttlmTerms.deleter
	def SttlmTerms(self):
		del self._SttlmTerms
		self._SttlmTerms = base_types.UninitialisedField(self, 'SttlmTerms', SettlementTerms3, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BllTo', type=PartyIdentification26, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Buyr', type=PartyIdentification26, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ComrclDocRef', type=InvoiceIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DataSetId', type=DocumentIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Goods', type=LineItem15, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PmtTerms', type=PaymentTerms4, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sellr', type=PartyIdentification26, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmTerms', type=SettlementTerms3, min=1, max=1, mutex_group=None, array=False),
	))