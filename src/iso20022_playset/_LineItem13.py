# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Adjustment7
from . import Charge24
from . import CurrencyAndAmount
from . import Incoterms4
from . import LineItemDetails13
from . import Max70Text
from . import ShipmentDateRange1
from . import Tax23
from . import TransportMeans5
from . import UserDefinedInformation1
from . import YesNoIndicator

class LineItem13(base_types._BaseFieldType):

	__slots__ = ["_Adjstmnt", "_BuyrDfndInf", "_FrghtChrgs", "_GoodsAndOrSvcsDesc", "_Incotrms", "_LineItmDtls", "_LineItmsTtlAmt", "_PrtlShipmnt", "_RtgSummry", "_SellrDfndInf", "_ShipmntDtRg", "_Tax", "_TrnsShipmnt", "_TtlNetAmt"]
	@property
	def Adjstmnt(self):
		return self._Adjstmnt

	@Adjstmnt.setter
	def Adjstmnt(self, value):
		self._Adjstmnt = value if value is not None else base_types.UninitialisedField(self, 'Adjstmnt', Adjustment7, True)

	@Adjstmnt.deleter
	def Adjstmnt(self):
		del self._Adjstmnt
		self._Adjstmnt = base_types.UninitialisedField(self, 'Adjstmnt', Adjustment7, True)

	@property
	def BuyrDfndInf(self):
		return self._BuyrDfndInf

	@BuyrDfndInf.setter
	def BuyrDfndInf(self, value):
		self._BuyrDfndInf = value if value is not None else base_types.UninitialisedField(self, 'BuyrDfndInf', UserDefinedInformation1, True)

	@BuyrDfndInf.deleter
	def BuyrDfndInf(self):
		del self._BuyrDfndInf
		self._BuyrDfndInf = base_types.UninitialisedField(self, 'BuyrDfndInf', UserDefinedInformation1, True)

	@property
	def FrghtChrgs(self):
		return self._FrghtChrgs

	@FrghtChrgs.setter
	def FrghtChrgs(self, value):
		self._FrghtChrgs = value if value is not None else base_types.UninitialisedField(self, 'FrghtChrgs', Charge24, False)

	@FrghtChrgs.deleter
	def FrghtChrgs(self):
		del self._FrghtChrgs
		self._FrghtChrgs = base_types.UninitialisedField(self, 'FrghtChrgs', Charge24, False)

	@property
	def GoodsAndOrSvcsDesc(self):
		return self._GoodsAndOrSvcsDesc

	@GoodsAndOrSvcsDesc.setter
	def GoodsAndOrSvcsDesc(self, value):
		self._GoodsAndOrSvcsDesc = value if value is not None else base_types.UninitialisedField(self, 'GoodsAndOrSvcsDesc', Max70Text, False)

	@GoodsAndOrSvcsDesc.deleter
	def GoodsAndOrSvcsDesc(self):
		del self._GoodsAndOrSvcsDesc
		self._GoodsAndOrSvcsDesc = base_types.UninitialisedField(self, 'GoodsAndOrSvcsDesc', Max70Text, False)

	@property
	def Incotrms(self):
		return self._Incotrms

	@Incotrms.setter
	def Incotrms(self, value):
		self._Incotrms = value if value is not None else base_types.UninitialisedField(self, 'Incotrms', Incoterms4, False)

	@Incotrms.deleter
	def Incotrms(self):
		del self._Incotrms
		self._Incotrms = base_types.UninitialisedField(self, 'Incotrms', Incoterms4, False)

	@property
	def LineItmDtls(self):
		return self._LineItmDtls

	@LineItmDtls.setter
	def LineItmDtls(self, value):
		self._LineItmDtls = value if value is not None else base_types.UninitialisedField(self, 'LineItmDtls', LineItemDetails13, True)

	@LineItmDtls.deleter
	def LineItmDtls(self):
		del self._LineItmDtls
		self._LineItmDtls = base_types.UninitialisedField(self, 'LineItmDtls', LineItemDetails13, True)

	@property
	def LineItmsTtlAmt(self):
		return self._LineItmsTtlAmt

	@LineItmsTtlAmt.setter
	def LineItmsTtlAmt(self, value):
		self._LineItmsTtlAmt = value if value is not None else base_types.UninitialisedField(self, 'LineItmsTtlAmt', CurrencyAndAmount, False)

	@LineItmsTtlAmt.deleter
	def LineItmsTtlAmt(self):
		del self._LineItmsTtlAmt
		self._LineItmsTtlAmt = base_types.UninitialisedField(self, 'LineItmsTtlAmt', CurrencyAndAmount, False)

	@property
	def PrtlShipmnt(self):
		return self._PrtlShipmnt

	@PrtlShipmnt.setter
	def PrtlShipmnt(self, value):
		self._PrtlShipmnt = value if value is not None else base_types.UninitialisedField(self, 'PrtlShipmnt', YesNoIndicator, False)

	@PrtlShipmnt.deleter
	def PrtlShipmnt(self):
		del self._PrtlShipmnt
		self._PrtlShipmnt = base_types.UninitialisedField(self, 'PrtlShipmnt', YesNoIndicator, False)

	@property
	def RtgSummry(self):
		return self._RtgSummry

	@RtgSummry.setter
	def RtgSummry(self, value):
		self._RtgSummry = value if value is not None else base_types.UninitialisedField(self, 'RtgSummry', TransportMeans5, False)

	@RtgSummry.deleter
	def RtgSummry(self):
		del self._RtgSummry
		self._RtgSummry = base_types.UninitialisedField(self, 'RtgSummry', TransportMeans5, False)

	@property
	def SellrDfndInf(self):
		return self._SellrDfndInf

	@SellrDfndInf.setter
	def SellrDfndInf(self, value):
		self._SellrDfndInf = value if value is not None else base_types.UninitialisedField(self, 'SellrDfndInf', UserDefinedInformation1, True)

	@SellrDfndInf.deleter
	def SellrDfndInf(self):
		del self._SellrDfndInf
		self._SellrDfndInf = base_types.UninitialisedField(self, 'SellrDfndInf', UserDefinedInformation1, True)

	@property
	def ShipmntDtRg(self):
		return self._ShipmntDtRg

	@ShipmntDtRg.setter
	def ShipmntDtRg(self, value):
		self._ShipmntDtRg = value if value is not None else base_types.UninitialisedField(self, 'ShipmntDtRg', ShipmentDateRange1, False)

	@ShipmntDtRg.deleter
	def ShipmntDtRg(self):
		del self._ShipmntDtRg
		self._ShipmntDtRg = base_types.UninitialisedField(self, 'ShipmntDtRg', ShipmentDateRange1, False)

	@property
	def Tax(self):
		return self._Tax

	@Tax.setter
	def Tax(self, value):
		self._Tax = value if value is not None else base_types.UninitialisedField(self, 'Tax', Tax23, True)

	@Tax.deleter
	def Tax(self):
		del self._Tax
		self._Tax = base_types.UninitialisedField(self, 'Tax', Tax23, True)

	@property
	def TrnsShipmnt(self):
		return self._TrnsShipmnt

	@TrnsShipmnt.setter
	def TrnsShipmnt(self, value):
		self._TrnsShipmnt = value if value is not None else base_types.UninitialisedField(self, 'TrnsShipmnt', YesNoIndicator, False)

	@TrnsShipmnt.deleter
	def TrnsShipmnt(self):
		del self._TrnsShipmnt
		self._TrnsShipmnt = base_types.UninitialisedField(self, 'TrnsShipmnt', YesNoIndicator, False)

	@property
	def TtlNetAmt(self):
		return self._TtlNetAmt

	@TtlNetAmt.setter
	def TtlNetAmt(self, value):
		self._TtlNetAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlNetAmt', CurrencyAndAmount, False)

	@TtlNetAmt.deleter
	def TtlNetAmt(self):
		del self._TtlNetAmt
		self._TtlNetAmt = base_types.UninitialisedField(self, 'TtlNetAmt', CurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Adjstmnt', type=Adjustment7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BuyrDfndInf', type=UserDefinedInformation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FrghtChrgs', type=Charge24, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GoodsAndOrSvcsDesc', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Incotrms', type=Incoterms4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LineItmDtls', type=LineItemDetails13, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LineItmsTtlAmt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtlShipmnt', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtgSummry', type=TransportMeans5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SellrDfndInf', type=UserDefinedInformation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ShipmntDtRg', type=ShipmentDateRange1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tax', type=Tax23, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TrnsShipmnt', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNetAmt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))