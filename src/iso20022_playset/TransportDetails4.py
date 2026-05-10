from . import base_types
from .TransportMeans6 import TransportMeans6
from .TransportedGoods1 import TransportedGoods1
from .ShipmentDate1Choice import ShipmentDate1Choice
from .Charge25 import Charge25
from .Incoterms4 import Incoterms4
from .Consignment3 import Consignment3
from .DocumentIdentification7 import DocumentIdentification7

class TransportDetails4(base_types._BaseFieldType):

	__slots__ = ["_Consgnmt", "_Incotrms", "_TrnsprtDocRef", "_ShipmntDt", "_TrnsprtdGoods", "_FrghtChrgs", "_RtgSummry"]
	@property
	def Consgnmt(self):
		return self._Consgnmt

	@Consgnmt.setter
	def Consgnmt(self, value):
		self._Consgnmt = value if type(value) != auto else self.make_default("Consgnmt")

	@Consgnmt.deleter
	def Consgnmt(self):
		del self._Consgnmt
		self._Consgnmt = None

	@property
	def Incotrms(self):
		return self._Incotrms

	@Incotrms.setter
	def Incotrms(self, value):
		self._Incotrms = value if type(value) != auto else self.make_default("Incotrms")

	@Incotrms.deleter
	def Incotrms(self):
		del self._Incotrms
		self._Incotrms = None

	@property
	def TrnsprtDocRef(self):
		return self._TrnsprtDocRef

	@TrnsprtDocRef.setter
	def TrnsprtDocRef(self, value):
		self._TrnsprtDocRef = value if type(value) != auto else self.make_default("TrnsprtDocRef")

	@TrnsprtDocRef.deleter
	def TrnsprtDocRef(self):
		del self._TrnsprtDocRef
		self._TrnsprtDocRef = None

	@property
	def ShipmntDt(self):
		return self._ShipmntDt

	@ShipmntDt.setter
	def ShipmntDt(self, value):
		self._ShipmntDt = value if type(value) != auto else self.make_default("ShipmntDt")

	@ShipmntDt.deleter
	def ShipmntDt(self):
		del self._ShipmntDt
		self._ShipmntDt = None

	@property
	def TrnsprtdGoods(self):
		return self._TrnsprtdGoods

	@TrnsprtdGoods.setter
	def TrnsprtdGoods(self, value):
		self._TrnsprtdGoods = value if type(value) != auto else self.make_default("TrnsprtdGoods")

	@TrnsprtdGoods.deleter
	def TrnsprtdGoods(self):
		del self._TrnsprtdGoods
		self._TrnsprtdGoods = None

	@property
	def FrghtChrgs(self):
		return self._FrghtChrgs

	@FrghtChrgs.setter
	def FrghtChrgs(self, value):
		self._FrghtChrgs = value if type(value) != auto else self.make_default("FrghtChrgs")

	@FrghtChrgs.deleter
	def FrghtChrgs(self):
		del self._FrghtChrgs
		self._FrghtChrgs = None

	@property
	def RtgSummry(self):
		return self._RtgSummry

	@RtgSummry.setter
	def RtgSummry(self, value):
		self._RtgSummry = value if type(value) != auto else self.make_default("RtgSummry")

	@RtgSummry.deleter
	def RtgSummry(self):
		del self._RtgSummry
		self._RtgSummry = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Consgnmt', type=Consignment3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Incotrms', type=Incoterms4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrnsprtDocRef', type=DocumentIdentification7, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ShipmntDt', type=ShipmentDate1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrnsprtdGoods', type=TransportedGoods1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FrghtChrgs', type=Charge25, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtgSummry', type=TransportMeans6, min=1, max=1, mutex_group=None, array=False),
	))

