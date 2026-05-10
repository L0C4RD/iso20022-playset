import base_types
import TransportDetails4
import DocumentIdentification1
import PartyIdentification26

class TransportDataSet5(base_types._BaseFieldType):

	__slots__ = ["_Sellr", "_TrnsprtInf", "_DataSetId", "_ShipTo", "_Consgn", "_Buyr", "_Consgnr"]
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
	def TrnsprtInf(self):
		return self._TrnsprtInf

	@TrnsprtInf.setter
	def TrnsprtInf(self, value):
		self._TrnsprtInf = value if type(value) != auto else self.make_default("TrnsprtInf")

	@TrnsprtInf.deleter
	def TrnsprtInf(self):
		del self._TrnsprtInf
		self._TrnsprtInf = None

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
	def ShipTo(self):
		return self._ShipTo

	@ShipTo.setter
	def ShipTo(self, value):
		self._ShipTo = value if type(value) != auto else self.make_default("ShipTo")

	@ShipTo.deleter
	def ShipTo(self):
		del self._ShipTo
		self._ShipTo = None

	@property
	def Consgn(self):
		return self._Consgn

	@Consgn.setter
	def Consgn(self, value):
		self._Consgn = value if type(value) != auto else self.make_default("Consgn")

	@Consgn.deleter
	def Consgn(self):
		del self._Consgn
		self._Consgn = None

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
	def Consgnr(self):
		return self._Consgnr

	@Consgnr.setter
	def Consgnr(self, value):
		self._Consgnr = value if type(value) != auto else self.make_default("Consgnr")

	@Consgnr.deleter
	def Consgnr(self):
		del self._Consgnr
		self._Consgnr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Sellr', type=PartyIdentification26, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrnsprtInf', type=TransportDetails4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DataSetId', type=DocumentIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShipTo', type=PartyIdentification26, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Consgn', type=PartyIdentification26, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Buyr', type=PartyIdentification26, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Consgnr', type=PartyIdentification26, min=1, max=1, mutex_group=None, array=False),
	))

