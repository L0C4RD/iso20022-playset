from . import base_types
from ._ContentInformationType39 import ContentInformationType39
from ._KeyUsage1Code import KeyUsage1Code
from ._Max256Text import Max256Text
from ._GenericInformation1 import GenericInformation1
from ._CryptographicKeyType3Code import CryptographicKeyType3Code
from ._Max35Text import Max35Text
from ._Max35Binary import Max35Binary
from ._Max350Text import Max350Text
from ._ISODateTime import ISODateTime
from ._GenericIdentification186 import GenericIdentification186

class CryptographicKey18(base_types._BaseFieldType):

	__slots__ = ["_Fctn", "_AddtlMgmtInf", "_SctyPrfl", "_CmpntWthAuthrsdAccs", "_ItmNb", "_AddtlId", "_KeyVal", "_Id", "_Vrsn", "_PrtctdCmpntWthAuthrsdAccs", "_ActvtnDt", "_Nm", "_DeactvtnDt", "_KeyChckVal", "_Tp"]
	@property
	def ActvtnDt(self):
		return self._ActvtnDt

	@ActvtnDt.setter
	def ActvtnDt(self, value):
		self._ActvtnDt = value if type(value) != base_types.auto else self.make_default("ActvtnDt")

	@ActvtnDt.deleter
	def ActvtnDt(self):
		del self._ActvtnDt
		self._ActvtnDt = None

	@property
	def AddtlId(self):
		return self._AddtlId

	@AddtlId.setter
	def AddtlId(self, value):
		self._AddtlId = value if type(value) != base_types.auto else self.make_default("AddtlId")

	@AddtlId.deleter
	def AddtlId(self):
		del self._AddtlId
		self._AddtlId = None

	@property
	def AddtlMgmtInf(self):
		return self._AddtlMgmtInf

	@AddtlMgmtInf.setter
	def AddtlMgmtInf(self, value):
		self._AddtlMgmtInf = value if type(value) != base_types.auto else self.make_default("AddtlMgmtInf")

	@AddtlMgmtInf.deleter
	def AddtlMgmtInf(self):
		del self._AddtlMgmtInf
		self._AddtlMgmtInf = None

	@property
	def CmpntWthAuthrsdAccs(self):
		return self._CmpntWthAuthrsdAccs

	@CmpntWthAuthrsdAccs.setter
	def CmpntWthAuthrsdAccs(self, value):
		self._CmpntWthAuthrsdAccs = value if type(value) != base_types.auto else self.make_default("CmpntWthAuthrsdAccs")

	@CmpntWthAuthrsdAccs.deleter
	def CmpntWthAuthrsdAccs(self):
		del self._CmpntWthAuthrsdAccs
		self._CmpntWthAuthrsdAccs = None

	@property
	def DeactvtnDt(self):
		return self._DeactvtnDt

	@DeactvtnDt.setter
	def DeactvtnDt(self, value):
		self._DeactvtnDt = value if type(value) != base_types.auto else self.make_default("DeactvtnDt")

	@DeactvtnDt.deleter
	def DeactvtnDt(self):
		del self._DeactvtnDt
		self._DeactvtnDt = None

	@property
	def Fctn(self):
		return self._Fctn

	@Fctn.setter
	def Fctn(self, value):
		self._Fctn = value if type(value) != base_types.auto else self.make_default("Fctn")

	@Fctn.deleter
	def Fctn(self):
		del self._Fctn
		self._Fctn = None

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
	def ItmNb(self):
		return self._ItmNb

	@ItmNb.setter
	def ItmNb(self, value):
		self._ItmNb = value if type(value) != base_types.auto else self.make_default("ItmNb")

	@ItmNb.deleter
	def ItmNb(self):
		del self._ItmNb
		self._ItmNb = None

	@property
	def KeyChckVal(self):
		return self._KeyChckVal

	@KeyChckVal.setter
	def KeyChckVal(self, value):
		self._KeyChckVal = value if type(value) != base_types.auto else self.make_default("KeyChckVal")

	@KeyChckVal.deleter
	def KeyChckVal(self):
		del self._KeyChckVal
		self._KeyChckVal = None

	@property
	def KeyVal(self):
		return self._KeyVal

	@KeyVal.setter
	def KeyVal(self, value):
		self._KeyVal = value if type(value) != base_types.auto else self.make_default("KeyVal")

	@KeyVal.deleter
	def KeyVal(self):
		del self._KeyVal
		self._KeyVal = None

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
	def PrtctdCmpntWthAuthrsdAccs(self):
		return self._PrtctdCmpntWthAuthrsdAccs

	@PrtctdCmpntWthAuthrsdAccs.setter
	def PrtctdCmpntWthAuthrsdAccs(self, value):
		self._PrtctdCmpntWthAuthrsdAccs = value if type(value) != base_types.auto else self.make_default("PrtctdCmpntWthAuthrsdAccs")

	@PrtctdCmpntWthAuthrsdAccs.deleter
	def PrtctdCmpntWthAuthrsdAccs(self):
		del self._PrtctdCmpntWthAuthrsdAccs
		self._PrtctdCmpntWthAuthrsdAccs = None

	@property
	def SctyPrfl(self):
		return self._SctyPrfl

	@SctyPrfl.setter
	def SctyPrfl(self, value):
		self._SctyPrfl = value if type(value) != base_types.auto else self.make_default("SctyPrfl")

	@SctyPrfl.deleter
	def SctyPrfl(self):
		del self._SctyPrfl
		self._SctyPrfl = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def Vrsn(self):
		return self._Vrsn

	@Vrsn.setter
	def Vrsn(self, value):
		self._Vrsn = value if type(value) != base_types.auto else self.make_default("Vrsn")

	@Vrsn.deleter
	def Vrsn(self):
		del self._Vrsn
		self._Vrsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActvtnDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlId', type=Max35Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlMgmtInf', type=GenericInformation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CmpntWthAuthrsdAccs', type=GenericIdentification186, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DeactvtnDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Fctn', type=KeyUsage1Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Id', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ItmNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='KeyChckVal', type=Max35Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='KeyVal', type=ContentInformationType39, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdCmpntWthAuthrsdAccs', type=ContentInformationType39, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SctyPrfl', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=CryptographicKeyType3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vrsn', type=Max256Text, min=1, max=1, mutex_group=None, array=False),
	))

