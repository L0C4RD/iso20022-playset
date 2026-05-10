from . import base_types
from .FinancialInstitution8 import FinancialInstitution8
from .Credentials3 import Credentials3
from .ISODate import ISODate
from .LocalData15 import LocalData15
from .CardholderName3 import CardholderName3
from .ContactPersonal1 import ContactPersonal1
from .Address2 import Address2
from .Max35Text import Max35Text
from .Max2NumericText import Max2NumericText
from .AdditionalData1 import AdditionalData1
from .ISOMax3ACountryCode import ISOMax3ACountryCode

class PartyIdentification287(base_types._BaseFieldType):

	__slots__ = ["_LclData", "_Adr", "_Dsgnt", "_Ntlty", "_AddtlData", "_Crdntls", "_DtOfBirth", "_FI", "_Id", "_Nm", "_Ctct", "_CtryOfBirth"]
	@property
	def LclData(self):
		return self._LclData

	@LclData.setter
	def LclData(self, value):
		self._LclData = value if type(value) != base_types.auto else self.make_default("LclData")

	@LclData.deleter
	def LclData(self):
		del self._LclData
		self._LclData = None

	@property
	def Adr(self):
		return self._Adr

	@Adr.setter
	def Adr(self, value):
		self._Adr = value if type(value) != base_types.auto else self.make_default("Adr")

	@Adr.deleter
	def Adr(self):
		del self._Adr
		self._Adr = None

	@property
	def Dsgnt(self):
		return self._Dsgnt

	@Dsgnt.setter
	def Dsgnt(self, value):
		self._Dsgnt = value if type(value) != base_types.auto else self.make_default("Dsgnt")

	@Dsgnt.deleter
	def Dsgnt(self):
		del self._Dsgnt
		self._Dsgnt = None

	@property
	def Ntlty(self):
		return self._Ntlty

	@Ntlty.setter
	def Ntlty(self, value):
		self._Ntlty = value if type(value) != base_types.auto else self.make_default("Ntlty")

	@Ntlty.deleter
	def Ntlty(self):
		del self._Ntlty
		self._Ntlty = None

	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if type(value) != base_types.auto else self.make_default("AddtlData")

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = None

	@property
	def Crdntls(self):
		return self._Crdntls

	@Crdntls.setter
	def Crdntls(self, value):
		self._Crdntls = value if type(value) != base_types.auto else self.make_default("Crdntls")

	@Crdntls.deleter
	def Crdntls(self):
		del self._Crdntls
		self._Crdntls = None

	@property
	def DtOfBirth(self):
		return self._DtOfBirth

	@DtOfBirth.setter
	def DtOfBirth(self, value):
		self._DtOfBirth = value if type(value) != base_types.auto else self.make_default("DtOfBirth")

	@DtOfBirth.deleter
	def DtOfBirth(self):
		del self._DtOfBirth
		self._DtOfBirth = None

	@property
	def FI(self):
		return self._FI

	@FI.setter
	def FI(self, value):
		self._FI = value if type(value) != base_types.auto else self.make_default("FI")

	@FI.deleter
	def FI(self):
		del self._FI
		self._FI = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if type(value) != base_types.auto else self.make_default("Nm")

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = None

	@property
	def Ctct(self):
		return self._Ctct

	@Ctct.setter
	def Ctct(self, value):
		self._Ctct = value if type(value) != base_types.auto else self.make_default("Ctct")

	@Ctct.deleter
	def Ctct(self):
		del self._Ctct
		self._Ctct = None

	@property
	def CtryOfBirth(self):
		return self._CtryOfBirth

	@CtryOfBirth.setter
	def CtryOfBirth(self, value):
		self._CtryOfBirth = value if type(value) != base_types.auto else self.make_default("CtryOfBirth")

	@CtryOfBirth.deleter
	def CtryOfBirth(self):
		del self._CtryOfBirth
		self._CtryOfBirth = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LclData', type=LocalData15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Adr', type=Address2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dsgnt', type=Max2NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ntlty', type=ISOMax3ACountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlData', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Crdntls', type=Credentials3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DtOfBirth', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FI', type=FinancialInstitution8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=CardholderName3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctct', type=ContactPersonal1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryOfBirth', type=ISOMax3ACountryCode, min=0, max=1, mutex_group=None, array=False),
	))

