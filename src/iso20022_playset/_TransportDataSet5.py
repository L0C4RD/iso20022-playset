# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DocumentIdentification1
from . import PartyIdentification26
from . import TransportDetails4

class TransportDataSet5(base_types._BaseFieldType):

	__slots__ = ["_Buyr", "_Consgn", "_Consgnr", "_DataSetId", "_Sellr", "_ShipTo", "_TrnsprtInf"]
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
	def Consgn(self):
		return self._Consgn

	@Consgn.setter
	def Consgn(self, value):
		self._Consgn = value if value is not None else base_types.UninitialisedField(self, 'Consgn', PartyIdentification26, False)

	@Consgn.deleter
	def Consgn(self):
		del self._Consgn
		self._Consgn = base_types.UninitialisedField(self, 'Consgn', PartyIdentification26, False)

	@property
	def Consgnr(self):
		return self._Consgnr

	@Consgnr.setter
	def Consgnr(self, value):
		self._Consgnr = value if value is not None else base_types.UninitialisedField(self, 'Consgnr', PartyIdentification26, False)

	@Consgnr.deleter
	def Consgnr(self):
		del self._Consgnr
		self._Consgnr = base_types.UninitialisedField(self, 'Consgnr', PartyIdentification26, False)

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
	def ShipTo(self):
		return self._ShipTo

	@ShipTo.setter
	def ShipTo(self, value):
		self._ShipTo = value if value is not None else base_types.UninitialisedField(self, 'ShipTo', PartyIdentification26, False)

	@ShipTo.deleter
	def ShipTo(self):
		del self._ShipTo
		self._ShipTo = base_types.UninitialisedField(self, 'ShipTo', PartyIdentification26, False)

	@property
	def TrnsprtInf(self):
		return self._TrnsprtInf

	@TrnsprtInf.setter
	def TrnsprtInf(self, value):
		self._TrnsprtInf = value if value is not None else base_types.UninitialisedField(self, 'TrnsprtInf', TransportDetails4, False)

	@TrnsprtInf.deleter
	def TrnsprtInf(self):
		del self._TrnsprtInf
		self._TrnsprtInf = base_types.UninitialisedField(self, 'TrnsprtInf', TransportDetails4, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Buyr', type=PartyIdentification26, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Consgn', type=PartyIdentification26, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Consgnr', type=PartyIdentification26, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DataSetId', type=DocumentIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sellr', type=PartyIdentification26, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShipTo', type=PartyIdentification26, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrnsprtInf', type=TransportDetails4, min=1, max=1, mutex_group=None, array=False),
	))