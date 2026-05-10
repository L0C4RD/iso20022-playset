import base_types
import TransportMeans5
import Adjustment7
import Charge24
import YesNoIndicator
import Max70Text
import CurrencyAndAmount
import Tax23
import Incoterms4
import LineItemDetails13
import ShipmentDateRange1
import UserDefinedInformation1

class LineItem13(base_types._BaseFieldType):

	__slots__ = ["_LineItmsTtlAmt", "_PrtlShipmnt", "_TrnsShipmnt", "_FrghtChrgs", "_Incotrms", "_Tax", "_BuyrDfndInf", "_LineItmDtls", "_Adjstmnt", "_RtgSummry", "_ShipmntDtRg", "_SellrDfndInf", "_TtlNetAmt", "_GoodsAndOrSvcsDesc"]
	@property
	def LineItmsTtlAmt(self):
		return self._LineItmsTtlAmt

	@LineItmsTtlAmt.setter
	def LineItmsTtlAmt(self, value):
		self._LineItmsTtlAmt = value if type(value) != auto else self.make_default("LineItmsTtlAmt")

	@LineItmsTtlAmt.deleter
	def LineItmsTtlAmt(self):
		del self._LineItmsTtlAmt
		self._LineItmsTtlAmt = None

	@property
	def PrtlShipmnt(self):
		return self._PrtlShipmnt

	@PrtlShipmnt.setter
	def PrtlShipmnt(self, value):
		self._PrtlShipmnt = value if type(value) != auto else self.make_default("PrtlShipmnt")

	@PrtlShipmnt.deleter
	def PrtlShipmnt(self):
		del self._PrtlShipmnt
		self._PrtlShipmnt = None

	@property
	def TrnsShipmnt(self):
		return self._TrnsShipmnt

	@TrnsShipmnt.setter
	def TrnsShipmnt(self, value):
		self._TrnsShipmnt = value if type(value) != auto else self.make_default("TrnsShipmnt")

	@TrnsShipmnt.deleter
	def TrnsShipmnt(self):
		del self._TrnsShipmnt
		self._TrnsShipmnt = None

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
	def Tax(self):
		return self._Tax

	@Tax.setter
	def Tax(self, value):
		self._Tax = value if type(value) != auto else self.make_default("Tax")

	@Tax.deleter
	def Tax(self):
		del self._Tax
		self._Tax = None

	@property
	def BuyrDfndInf(self):
		return self._BuyrDfndInf

	@BuyrDfndInf.setter
	def BuyrDfndInf(self, value):
		self._BuyrDfndInf = value if type(value) != auto else self.make_default("BuyrDfndInf")

	@BuyrDfndInf.deleter
	def BuyrDfndInf(self):
		del self._BuyrDfndInf
		self._BuyrDfndInf = None

	@property
	def LineItmDtls(self):
		return self._LineItmDtls

	@LineItmDtls.setter
	def LineItmDtls(self, value):
		self._LineItmDtls = value if type(value) != auto else self.make_default("LineItmDtls")

	@LineItmDtls.deleter
	def LineItmDtls(self):
		del self._LineItmDtls
		self._LineItmDtls = None

	@property
	def Adjstmnt(self):
		return self._Adjstmnt

	@Adjstmnt.setter
	def Adjstmnt(self, value):
		self._Adjstmnt = value if type(value) != auto else self.make_default("Adjstmnt")

	@Adjstmnt.deleter
	def Adjstmnt(self):
		del self._Adjstmnt
		self._Adjstmnt = None

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

	@property
	def ShipmntDtRg(self):
		return self._ShipmntDtRg

	@ShipmntDtRg.setter
	def ShipmntDtRg(self, value):
		self._ShipmntDtRg = value if type(value) != auto else self.make_default("ShipmntDtRg")

	@ShipmntDtRg.deleter
	def ShipmntDtRg(self):
		del self._ShipmntDtRg
		self._ShipmntDtRg = None

	@property
	def SellrDfndInf(self):
		return self._SellrDfndInf

	@SellrDfndInf.setter
	def SellrDfndInf(self, value):
		self._SellrDfndInf = value if type(value) != auto else self.make_default("SellrDfndInf")

	@SellrDfndInf.deleter
	def SellrDfndInf(self):
		del self._SellrDfndInf
		self._SellrDfndInf = None

	@property
	def TtlNetAmt(self):
		return self._TtlNetAmt

	@TtlNetAmt.setter
	def TtlNetAmt(self, value):
		self._TtlNetAmt = value if type(value) != auto else self.make_default("TtlNetAmt")

	@TtlNetAmt.deleter
	def TtlNetAmt(self):
		del self._TtlNetAmt
		self._TtlNetAmt = None

	@property
	def GoodsAndOrSvcsDesc(self):
		return self._GoodsAndOrSvcsDesc

	@GoodsAndOrSvcsDesc.setter
	def GoodsAndOrSvcsDesc(self, value):
		self._GoodsAndOrSvcsDesc = value if type(value) != auto else self.make_default("GoodsAndOrSvcsDesc")

	@GoodsAndOrSvcsDesc.deleter
	def GoodsAndOrSvcsDesc(self):
		del self._GoodsAndOrSvcsDesc
		self._GoodsAndOrSvcsDesc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LineItmsTtlAmt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtlShipmnt', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrnsShipmnt', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrghtChrgs', type=Charge24, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Incotrms', type=Incoterms4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tax', type=Tax23, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BuyrDfndInf', type=UserDefinedInformation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LineItmDtls', type=LineItemDetails13, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Adjstmnt', type=Adjustment7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RtgSummry', type=TransportMeans5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShipmntDtRg', type=ShipmentDateRange1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SellrDfndInf', type=UserDefinedInformation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlNetAmt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GoodsAndOrSvcsDesc', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
	))

