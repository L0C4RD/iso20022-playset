from . import base_types
from .Incoterms4 import Incoterms4
from .UnitPrice18 import UnitPrice18
from .Adjustment7 import Adjustment7
from .PercentageTolerance1 import PercentageTolerance1
from .Tax23 import Tax23
from .TransportMeans5 import TransportMeans5
from .CountryCode import CountryCode
from .CurrencyAndAmount import CurrencyAndAmount
from .Quantity9 import Quantity9
from .Max70Text import Max70Text
from .ProductCharacteristics1Choice import ProductCharacteristics1Choice
from .ProductIdentifier2Choice import ProductIdentifier2Choice
from .ShipmentSchedule2Choice import ShipmentSchedule2Choice
from .ProductCategory1Choice import ProductCategory1Choice
from .Charge24 import Charge24

class LineItemDetails13(base_types._BaseFieldType):

	__slots__ = ["_PdctChrtcs", "_PricTlrnce", "_UnitPric", "_TtlAmt", "_FrghtChrgs", "_Tax", "_PdctCtgy", "_PdctNm", "_ShipmntSchdl", "_LineItmId", "_QtyTlrnce", "_RtgSummry", "_Incotrms", "_PdctIdr", "_Adjstmnt", "_PdctOrgn", "_Qty"]
	@property
	def PdctChrtcs(self):
		return self._PdctChrtcs

	@PdctChrtcs.setter
	def PdctChrtcs(self, value):
		self._PdctChrtcs = value if type(value) != base_types.auto else self.make_default("PdctChrtcs")

	@PdctChrtcs.deleter
	def PdctChrtcs(self):
		del self._PdctChrtcs
		self._PdctChrtcs = None

	@property
	def PricTlrnce(self):
		return self._PricTlrnce

	@PricTlrnce.setter
	def PricTlrnce(self, value):
		self._PricTlrnce = value if type(value) != base_types.auto else self.make_default("PricTlrnce")

	@PricTlrnce.deleter
	def PricTlrnce(self):
		del self._PricTlrnce
		self._PricTlrnce = None

	@property
	def UnitPric(self):
		return self._UnitPric

	@UnitPric.setter
	def UnitPric(self, value):
		self._UnitPric = value if type(value) != base_types.auto else self.make_default("UnitPric")

	@UnitPric.deleter
	def UnitPric(self):
		del self._UnitPric
		self._UnitPric = None

	@property
	def TtlAmt(self):
		return self._TtlAmt

	@TtlAmt.setter
	def TtlAmt(self, value):
		self._TtlAmt = value if type(value) != base_types.auto else self.make_default("TtlAmt")

	@TtlAmt.deleter
	def TtlAmt(self):
		del self._TtlAmt
		self._TtlAmt = None

	@property
	def FrghtChrgs(self):
		return self._FrghtChrgs

	@FrghtChrgs.setter
	def FrghtChrgs(self, value):
		self._FrghtChrgs = value if type(value) != base_types.auto else self.make_default("FrghtChrgs")

	@FrghtChrgs.deleter
	def FrghtChrgs(self):
		del self._FrghtChrgs
		self._FrghtChrgs = None

	@property
	def Tax(self):
		return self._Tax

	@Tax.setter
	def Tax(self, value):
		self._Tax = value if type(value) != base_types.auto else self.make_default("Tax")

	@Tax.deleter
	def Tax(self):
		del self._Tax
		self._Tax = None

	@property
	def PdctCtgy(self):
		return self._PdctCtgy

	@PdctCtgy.setter
	def PdctCtgy(self, value):
		self._PdctCtgy = value if type(value) != base_types.auto else self.make_default("PdctCtgy")

	@PdctCtgy.deleter
	def PdctCtgy(self):
		del self._PdctCtgy
		self._PdctCtgy = None

	@property
	def PdctNm(self):
		return self._PdctNm

	@PdctNm.setter
	def PdctNm(self, value):
		self._PdctNm = value if type(value) != base_types.auto else self.make_default("PdctNm")

	@PdctNm.deleter
	def PdctNm(self):
		del self._PdctNm
		self._PdctNm = None

	@property
	def ShipmntSchdl(self):
		return self._ShipmntSchdl

	@ShipmntSchdl.setter
	def ShipmntSchdl(self, value):
		self._ShipmntSchdl = value if type(value) != base_types.auto else self.make_default("ShipmntSchdl")

	@ShipmntSchdl.deleter
	def ShipmntSchdl(self):
		del self._ShipmntSchdl
		self._ShipmntSchdl = None

	@property
	def LineItmId(self):
		return self._LineItmId

	@LineItmId.setter
	def LineItmId(self, value):
		self._LineItmId = value if type(value) != base_types.auto else self.make_default("LineItmId")

	@LineItmId.deleter
	def LineItmId(self):
		del self._LineItmId
		self._LineItmId = None

	@property
	def QtyTlrnce(self):
		return self._QtyTlrnce

	@QtyTlrnce.setter
	def QtyTlrnce(self, value):
		self._QtyTlrnce = value if type(value) != base_types.auto else self.make_default("QtyTlrnce")

	@QtyTlrnce.deleter
	def QtyTlrnce(self):
		del self._QtyTlrnce
		self._QtyTlrnce = None

	@property
	def RtgSummry(self):
		return self._RtgSummry

	@RtgSummry.setter
	def RtgSummry(self, value):
		self._RtgSummry = value if type(value) != base_types.auto else self.make_default("RtgSummry")

	@RtgSummry.deleter
	def RtgSummry(self):
		del self._RtgSummry
		self._RtgSummry = None

	@property
	def Incotrms(self):
		return self._Incotrms

	@Incotrms.setter
	def Incotrms(self, value):
		self._Incotrms = value if type(value) != base_types.auto else self.make_default("Incotrms")

	@Incotrms.deleter
	def Incotrms(self):
		del self._Incotrms
		self._Incotrms = None

	@property
	def PdctIdr(self):
		return self._PdctIdr

	@PdctIdr.setter
	def PdctIdr(self, value):
		self._PdctIdr = value if type(value) != base_types.auto else self.make_default("PdctIdr")

	@PdctIdr.deleter
	def PdctIdr(self):
		del self._PdctIdr
		self._PdctIdr = None

	@property
	def Adjstmnt(self):
		return self._Adjstmnt

	@Adjstmnt.setter
	def Adjstmnt(self, value):
		self._Adjstmnt = value if type(value) != base_types.auto else self.make_default("Adjstmnt")

	@Adjstmnt.deleter
	def Adjstmnt(self):
		del self._Adjstmnt
		self._Adjstmnt = None

	@property
	def PdctOrgn(self):
		return self._PdctOrgn

	@PdctOrgn.setter
	def PdctOrgn(self, value):
		self._PdctOrgn = value if type(value) != base_types.auto else self.make_default("PdctOrgn")

	@PdctOrgn.deleter
	def PdctOrgn(self):
		del self._PdctOrgn
		self._PdctOrgn = None

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if type(value) != base_types.auto else self.make_default("Qty")

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PdctChrtcs', type=ProductCharacteristics1Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PricTlrnce', type=PercentageTolerance1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitPric', type=UnitPrice18, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlAmt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrghtChrgs', type=Charge24, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tax', type=Tax23, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PdctCtgy', type=ProductCategory1Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PdctNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShipmntSchdl', type=ShipmentSchedule2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LineItmId', type=Max70Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtyTlrnce', type=PercentageTolerance1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtgSummry', type=TransportMeans5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Incotrms', type=Incoterms4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctIdr', type=ProductIdentifier2Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Adjstmnt', type=Adjustment7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PdctOrgn', type=CountryCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Qty', type=Quantity9, min=1, max=1, mutex_group=None, array=False),
	))

