# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Acquirer10
from . import Cardholder21
from . import Check1
from . import ContentInformationType40
from . import CustomerDevice3
from . import LoyaltyAccount3
from . import MerchantToken2
from . import Organisation45
from . import PaymentCard35
from . import PointOfInteraction16
from . import RetailerSaleEnvironment2
from . import StoredValueAccount2
from . import Token1

class CardPaymentEnvironment82(base_types._BaseFieldType):

	__slots__ = ["_Acqrr", "_Card", "_Chck", "_Crdhldr", "_CstmrDvc", "_LltyAcct", "_Mrchnt", "_MrchntTkn", "_POI", "_PmtTkn", "_PrtctdCrdhldrData", "_SaleEnvt", "_StordValAcct", "_SvcPrvdr", "_Wllt"]
	@property
	def Acqrr(self):
		return self._Acqrr

	@Acqrr.setter
	def Acqrr(self, value):
		self._Acqrr = value if value is not None else base_types.UninitialisedField(self, 'Acqrr', Acquirer10, False)

	@Acqrr.deleter
	def Acqrr(self):
		del self._Acqrr
		self._Acqrr = base_types.UninitialisedField(self, 'Acqrr', Acquirer10, False)

	@property
	def Card(self):
		return self._Card

	@Card.setter
	def Card(self, value):
		self._Card = value if value is not None else base_types.UninitialisedField(self, 'Card', PaymentCard35, False)

	@Card.deleter
	def Card(self):
		del self._Card
		self._Card = base_types.UninitialisedField(self, 'Card', PaymentCard35, False)

	@property
	def Chck(self):
		return self._Chck

	@Chck.setter
	def Chck(self, value):
		self._Chck = value if value is not None else base_types.UninitialisedField(self, 'Chck', Check1, False)

	@Chck.deleter
	def Chck(self):
		del self._Chck
		self._Chck = base_types.UninitialisedField(self, 'Chck', Check1, False)

	@property
	def Crdhldr(self):
		return self._Crdhldr

	@Crdhldr.setter
	def Crdhldr(self, value):
		self._Crdhldr = value if value is not None else base_types.UninitialisedField(self, 'Crdhldr', Cardholder21, False)

	@Crdhldr.deleter
	def Crdhldr(self):
		del self._Crdhldr
		self._Crdhldr = base_types.UninitialisedField(self, 'Crdhldr', Cardholder21, False)

	@property
	def CstmrDvc(self):
		return self._CstmrDvc

	@CstmrDvc.setter
	def CstmrDvc(self, value):
		self._CstmrDvc = value if value is not None else base_types.UninitialisedField(self, 'CstmrDvc', CustomerDevice3, False)

	@CstmrDvc.deleter
	def CstmrDvc(self):
		del self._CstmrDvc
		self._CstmrDvc = base_types.UninitialisedField(self, 'CstmrDvc', CustomerDevice3, False)

	@property
	def LltyAcct(self):
		return self._LltyAcct

	@LltyAcct.setter
	def LltyAcct(self, value):
		self._LltyAcct = value if value is not None else base_types.UninitialisedField(self, 'LltyAcct', LoyaltyAccount3, True)

	@LltyAcct.deleter
	def LltyAcct(self):
		del self._LltyAcct
		self._LltyAcct = base_types.UninitialisedField(self, 'LltyAcct', LoyaltyAccount3, True)

	@property
	def Mrchnt(self):
		return self._Mrchnt

	@Mrchnt.setter
	def Mrchnt(self, value):
		self._Mrchnt = value if value is not None else base_types.UninitialisedField(self, 'Mrchnt', Organisation45, False)

	@Mrchnt.deleter
	def Mrchnt(self):
		del self._Mrchnt
		self._Mrchnt = base_types.UninitialisedField(self, 'Mrchnt', Organisation45, False)

	@property
	def MrchntTkn(self):
		return self._MrchntTkn

	@MrchntTkn.setter
	def MrchntTkn(self, value):
		self._MrchntTkn = value if value is not None else base_types.UninitialisedField(self, 'MrchntTkn', MerchantToken2, False)

	@MrchntTkn.deleter
	def MrchntTkn(self):
		del self._MrchntTkn
		self._MrchntTkn = base_types.UninitialisedField(self, 'MrchntTkn', MerchantToken2, False)

	@property
	def POI(self):
		return self._POI

	@POI.setter
	def POI(self, value):
		self._POI = value if value is not None else base_types.UninitialisedField(self, 'POI', PointOfInteraction16, False)

	@POI.deleter
	def POI(self):
		del self._POI
		self._POI = base_types.UninitialisedField(self, 'POI', PointOfInteraction16, False)

	@property
	def PmtTkn(self):
		return self._PmtTkn

	@PmtTkn.setter
	def PmtTkn(self, value):
		self._PmtTkn = value if value is not None else base_types.UninitialisedField(self, 'PmtTkn', Token1, False)

	@PmtTkn.deleter
	def PmtTkn(self):
		del self._PmtTkn
		self._PmtTkn = base_types.UninitialisedField(self, 'PmtTkn', Token1, False)

	@property
	def PrtctdCrdhldrData(self):
		return self._PrtctdCrdhldrData

	@PrtctdCrdhldrData.setter
	def PrtctdCrdhldrData(self, value):
		self._PrtctdCrdhldrData = value if value is not None else base_types.UninitialisedField(self, 'PrtctdCrdhldrData', ContentInformationType40, False)

	@PrtctdCrdhldrData.deleter
	def PrtctdCrdhldrData(self):
		del self._PrtctdCrdhldrData
		self._PrtctdCrdhldrData = base_types.UninitialisedField(self, 'PrtctdCrdhldrData', ContentInformationType40, False)

	@property
	def SaleEnvt(self):
		return self._SaleEnvt

	@SaleEnvt.setter
	def SaleEnvt(self, value):
		self._SaleEnvt = value if value is not None else base_types.UninitialisedField(self, 'SaleEnvt', RetailerSaleEnvironment2, False)

	@SaleEnvt.deleter
	def SaleEnvt(self):
		del self._SaleEnvt
		self._SaleEnvt = base_types.UninitialisedField(self, 'SaleEnvt', RetailerSaleEnvironment2, False)

	@property
	def StordValAcct(self):
		return self._StordValAcct

	@StordValAcct.setter
	def StordValAcct(self, value):
		self._StordValAcct = value if value is not None else base_types.UninitialisedField(self, 'StordValAcct', StoredValueAccount2, True)

	@StordValAcct.deleter
	def StordValAcct(self):
		del self._StordValAcct
		self._StordValAcct = base_types.UninitialisedField(self, 'StordValAcct', StoredValueAccount2, True)

	@property
	def SvcPrvdr(self):
		return self._SvcPrvdr

	@SvcPrvdr.setter
	def SvcPrvdr(self, value):
		self._SvcPrvdr = value if value is not None else base_types.UninitialisedField(self, 'SvcPrvdr', Acquirer10, False)

	@SvcPrvdr.deleter
	def SvcPrvdr(self):
		del self._SvcPrvdr
		self._SvcPrvdr = base_types.UninitialisedField(self, 'SvcPrvdr', Acquirer10, False)

	@property
	def Wllt(self):
		return self._Wllt

	@Wllt.setter
	def Wllt(self, value):
		self._Wllt = value if value is not None else base_types.UninitialisedField(self, 'Wllt', CustomerDevice3, False)

	@Wllt.deleter
	def Wllt(self):
		del self._Wllt
		self._Wllt = base_types.UninitialisedField(self, 'Wllt', CustomerDevice3, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Acqrr', type=Acquirer10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Card', type=PaymentCard35, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Chck', type=Check1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Crdhldr', type=Cardholder21, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrDvc', type=CustomerDevice3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LltyAcct', type=LoyaltyAccount3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Mrchnt', type=Organisation45, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrchntTkn', type=MerchantToken2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POI', type=PointOfInteraction16, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtTkn', type=Token1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdCrdhldrData', type=ContentInformationType40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleEnvt', type=RetailerSaleEnvironment2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StordValAcct', type=StoredValueAccount2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SvcPrvdr', type=Acquirer10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Wllt', type=CustomerDevice3, min=0, max=1, mutex_group=None, array=False),
	))