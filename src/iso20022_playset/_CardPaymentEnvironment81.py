from . import base_types
from .PointOfInteraction15 import PointOfInteraction15
from .MerchantToken2 import MerchantToken2
from .LoyaltyAccount3 import LoyaltyAccount3
from .Organisation41 import Organisation41
from .Check1 import Check1
from .Acquirer10 import Acquirer10
from .Token1 import Token1
from .StoredValueAccount2 import StoredValueAccount2
from .RetailerSaleEnvironment2 import RetailerSaleEnvironment2
from .PaymentCard35 import PaymentCard35
from .CustomerDevice3 import CustomerDevice3
from .ContentInformationType40 import ContentInformationType40
from .Cardholder21 import Cardholder21

class CardPaymentEnvironment81(base_types._BaseFieldType):

	__slots__ = ["_Mrchnt", "_PmtTkn", "_SvcPrvdr", "_Wllt", "_MrchntTkn", "_Acqrr", "_LltyAcct", "_POI", "_StordValAcct", "_CstmrDvc", "_Chck", "_Crdhldr", "_SaleEnvt", "_PrtctdCrdhldrData", "_Card"]
	@property
	def Mrchnt(self):
		return self._Mrchnt

	@Mrchnt.setter
	def Mrchnt(self, value):
		self._Mrchnt = value if type(value) != base_types.auto else self.make_default("Mrchnt")

	@Mrchnt.deleter
	def Mrchnt(self):
		del self._Mrchnt
		self._Mrchnt = None

	@property
	def PmtTkn(self):
		return self._PmtTkn

	@PmtTkn.setter
	def PmtTkn(self, value):
		self._PmtTkn = value if type(value) != base_types.auto else self.make_default("PmtTkn")

	@PmtTkn.deleter
	def PmtTkn(self):
		del self._PmtTkn
		self._PmtTkn = None

	@property
	def SvcPrvdr(self):
		return self._SvcPrvdr

	@SvcPrvdr.setter
	def SvcPrvdr(self, value):
		self._SvcPrvdr = value if type(value) != base_types.auto else self.make_default("SvcPrvdr")

	@SvcPrvdr.deleter
	def SvcPrvdr(self):
		del self._SvcPrvdr
		self._SvcPrvdr = None

	@property
	def Wllt(self):
		return self._Wllt

	@Wllt.setter
	def Wllt(self, value):
		self._Wllt = value if type(value) != base_types.auto else self.make_default("Wllt")

	@Wllt.deleter
	def Wllt(self):
		del self._Wllt
		self._Wllt = None

	@property
	def MrchntTkn(self):
		return self._MrchntTkn

	@MrchntTkn.setter
	def MrchntTkn(self, value):
		self._MrchntTkn = value if type(value) != base_types.auto else self.make_default("MrchntTkn")

	@MrchntTkn.deleter
	def MrchntTkn(self):
		del self._MrchntTkn
		self._MrchntTkn = None

	@property
	def Acqrr(self):
		return self._Acqrr

	@Acqrr.setter
	def Acqrr(self, value):
		self._Acqrr = value if type(value) != base_types.auto else self.make_default("Acqrr")

	@Acqrr.deleter
	def Acqrr(self):
		del self._Acqrr
		self._Acqrr = None

	@property
	def LltyAcct(self):
		return self._LltyAcct

	@LltyAcct.setter
	def LltyAcct(self, value):
		self._LltyAcct = value if type(value) != base_types.auto else self.make_default("LltyAcct")

	@LltyAcct.deleter
	def LltyAcct(self):
		del self._LltyAcct
		self._LltyAcct = None

	@property
	def POI(self):
		return self._POI

	@POI.setter
	def POI(self, value):
		self._POI = value if type(value) != base_types.auto else self.make_default("POI")

	@POI.deleter
	def POI(self):
		del self._POI
		self._POI = None

	@property
	def StordValAcct(self):
		return self._StordValAcct

	@StordValAcct.setter
	def StordValAcct(self, value):
		self._StordValAcct = value if type(value) != base_types.auto else self.make_default("StordValAcct")

	@StordValAcct.deleter
	def StordValAcct(self):
		del self._StordValAcct
		self._StordValAcct = None

	@property
	def CstmrDvc(self):
		return self._CstmrDvc

	@CstmrDvc.setter
	def CstmrDvc(self, value):
		self._CstmrDvc = value if type(value) != base_types.auto else self.make_default("CstmrDvc")

	@CstmrDvc.deleter
	def CstmrDvc(self):
		del self._CstmrDvc
		self._CstmrDvc = None

	@property
	def Chck(self):
		return self._Chck

	@Chck.setter
	def Chck(self, value):
		self._Chck = value if type(value) != base_types.auto else self.make_default("Chck")

	@Chck.deleter
	def Chck(self):
		del self._Chck
		self._Chck = None

	@property
	def Crdhldr(self):
		return self._Crdhldr

	@Crdhldr.setter
	def Crdhldr(self, value):
		self._Crdhldr = value if type(value) != base_types.auto else self.make_default("Crdhldr")

	@Crdhldr.deleter
	def Crdhldr(self):
		del self._Crdhldr
		self._Crdhldr = None

	@property
	def SaleEnvt(self):
		return self._SaleEnvt

	@SaleEnvt.setter
	def SaleEnvt(self, value):
		self._SaleEnvt = value if type(value) != base_types.auto else self.make_default("SaleEnvt")

	@SaleEnvt.deleter
	def SaleEnvt(self):
		del self._SaleEnvt
		self._SaleEnvt = None

	@property
	def PrtctdCrdhldrData(self):
		return self._PrtctdCrdhldrData

	@PrtctdCrdhldrData.setter
	def PrtctdCrdhldrData(self, value):
		self._PrtctdCrdhldrData = value if type(value) != base_types.auto else self.make_default("PrtctdCrdhldrData")

	@PrtctdCrdhldrData.deleter
	def PrtctdCrdhldrData(self):
		del self._PrtctdCrdhldrData
		self._PrtctdCrdhldrData = None

	@property
	def Card(self):
		return self._Card

	@Card.setter
	def Card(self, value):
		self._Card = value if type(value) != base_types.auto else self.make_default("Card")

	@Card.deleter
	def Card(self):
		del self._Card
		self._Card = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Mrchnt', type=Organisation41, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtTkn', type=Token1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcPrvdr', type=Acquirer10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Wllt', type=CustomerDevice3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrchntTkn', type=MerchantToken2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Acqrr', type=Acquirer10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LltyAcct', type=LoyaltyAccount3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='POI', type=PointOfInteraction15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StordValAcct', type=StoredValueAccount2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CstmrDvc', type=CustomerDevice3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Chck', type=Check1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Crdhldr', type=Cardholder21, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleEnvt', type=RetailerSaleEnvironment2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdCrdhldrData', type=ContentInformationType40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Card', type=PaymentCard35, min=0, max=1, mutex_group=None, array=False),
	))

