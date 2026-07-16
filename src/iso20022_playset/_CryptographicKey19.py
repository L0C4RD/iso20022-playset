# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ContentInformationType39
from . import CryptographicKeyType5Code
from . import GenericIdentification186
from . import GenericInformation1
from . import ISODateTime
from . import KeyUsage1Code
from . import Max140Text
from . import Max256Text
from . import Max350Text
from . import Max35Binary
from . import Max35Text
from . import Number

class CryptographicKey19(base_types._BaseFieldType):

	__slots__ = ["_ActvtnDt", "_AddtlId", "_AddtlMgmtInf", "_AlgoIdr", "_CmpntWthAuthrsdAccs", "_DeactvtnDt", "_DerivtnAlgoIdr", "_Fctn", "_Id", "_ItmNb", "_KeyChckVal", "_KeyId", "_KeyVal", "_KeyVrsn", "_Nm", "_PrtctdCmpntWthAuthrsdAccs", "_SctyPrfl", "_SeqNb", "_Tp", "_Vrsn"]
	@property
	def ActvtnDt(self):
		return self._ActvtnDt

	@ActvtnDt.setter
	def ActvtnDt(self, value):
		self._ActvtnDt = value if value is not None else base_types.UninitialisedField(self, 'ActvtnDt', ISODateTime, False)

	@ActvtnDt.deleter
	def ActvtnDt(self):
		del self._ActvtnDt
		self._ActvtnDt = base_types.UninitialisedField(self, 'ActvtnDt', ISODateTime, False)

	@property
	def AddtlId(self):
		return self._AddtlId

	@AddtlId.setter
	def AddtlId(self, value):
		self._AddtlId = value if value is not None else base_types.UninitialisedField(self, 'AddtlId', Max35Binary, False)

	@AddtlId.deleter
	def AddtlId(self):
		del self._AddtlId
		self._AddtlId = base_types.UninitialisedField(self, 'AddtlId', Max35Binary, False)

	@property
	def AddtlMgmtInf(self):
		return self._AddtlMgmtInf

	@AddtlMgmtInf.setter
	def AddtlMgmtInf(self, value):
		self._AddtlMgmtInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlMgmtInf', GenericInformation1, True)

	@AddtlMgmtInf.deleter
	def AddtlMgmtInf(self):
		del self._AddtlMgmtInf
		self._AddtlMgmtInf = base_types.UninitialisedField(self, 'AddtlMgmtInf', GenericInformation1, True)

	@property
	def AlgoIdr(self):
		return self._AlgoIdr

	@AlgoIdr.setter
	def AlgoIdr(self, value):
		self._AlgoIdr = value if value is not None else base_types.UninitialisedField(self, 'AlgoIdr', Max140Text, False)

	@AlgoIdr.deleter
	def AlgoIdr(self):
		del self._AlgoIdr
		self._AlgoIdr = base_types.UninitialisedField(self, 'AlgoIdr', Max140Text, False)

	@property
	def CmpntWthAuthrsdAccs(self):
		return self._CmpntWthAuthrsdAccs

	@CmpntWthAuthrsdAccs.setter
	def CmpntWthAuthrsdAccs(self, value):
		self._CmpntWthAuthrsdAccs = value if value is not None else base_types.UninitialisedField(self, 'CmpntWthAuthrsdAccs', GenericIdentification186, True)

	@CmpntWthAuthrsdAccs.deleter
	def CmpntWthAuthrsdAccs(self):
		del self._CmpntWthAuthrsdAccs
		self._CmpntWthAuthrsdAccs = base_types.UninitialisedField(self, 'CmpntWthAuthrsdAccs', GenericIdentification186, True)

	@property
	def DeactvtnDt(self):
		return self._DeactvtnDt

	@DeactvtnDt.setter
	def DeactvtnDt(self, value):
		self._DeactvtnDt = value if value is not None else base_types.UninitialisedField(self, 'DeactvtnDt', ISODateTime, False)

	@DeactvtnDt.deleter
	def DeactvtnDt(self):
		del self._DeactvtnDt
		self._DeactvtnDt = base_types.UninitialisedField(self, 'DeactvtnDt', ISODateTime, False)

	@property
	def DerivtnAlgoIdr(self):
		return self._DerivtnAlgoIdr

	@DerivtnAlgoIdr.setter
	def DerivtnAlgoIdr(self, value):
		self._DerivtnAlgoIdr = value if value is not None else base_types.UninitialisedField(self, 'DerivtnAlgoIdr', Max140Text, False)

	@DerivtnAlgoIdr.deleter
	def DerivtnAlgoIdr(self):
		del self._DerivtnAlgoIdr
		self._DerivtnAlgoIdr = base_types.UninitialisedField(self, 'DerivtnAlgoIdr', Max140Text, False)

	@property
	def Fctn(self):
		return self._Fctn

	@Fctn.setter
	def Fctn(self, value):
		self._Fctn = value if value is not None else base_types.UninitialisedField(self, 'Fctn', KeyUsage1Code, True)

	@Fctn.deleter
	def Fctn(self):
		del self._Fctn
		self._Fctn = base_types.UninitialisedField(self, 'Fctn', KeyUsage1Code, True)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max350Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max350Text, False)

	@property
	def ItmNb(self):
		return self._ItmNb

	@ItmNb.setter
	def ItmNb(self, value):
		self._ItmNb = value if value is not None else base_types.UninitialisedField(self, 'ItmNb', Max35Text, False)

	@ItmNb.deleter
	def ItmNb(self):
		del self._ItmNb
		self._ItmNb = base_types.UninitialisedField(self, 'ItmNb', Max35Text, False)

	@property
	def KeyChckVal(self):
		return self._KeyChckVal

	@KeyChckVal.setter
	def KeyChckVal(self, value):
		self._KeyChckVal = value if value is not None else base_types.UninitialisedField(self, 'KeyChckVal', Max35Binary, False)

	@KeyChckVal.deleter
	def KeyChckVal(self):
		del self._KeyChckVal
		self._KeyChckVal = base_types.UninitialisedField(self, 'KeyChckVal', Max35Binary, False)

	@property
	def KeyId(self):
		return self._KeyId

	@KeyId.setter
	def KeyId(self, value):
		self._KeyId = value if value is not None else base_types.UninitialisedField(self, 'KeyId', Max350Text, False)

	@KeyId.deleter
	def KeyId(self):
		del self._KeyId
		self._KeyId = base_types.UninitialisedField(self, 'KeyId', Max350Text, False)

	@property
	def KeyVal(self):
		return self._KeyVal

	@KeyVal.setter
	def KeyVal(self, value):
		self._KeyVal = value if value is not None else base_types.UninitialisedField(self, 'KeyVal', ContentInformationType39, False)

	@KeyVal.deleter
	def KeyVal(self):
		del self._KeyVal
		self._KeyVal = base_types.UninitialisedField(self, 'KeyVal', ContentInformationType39, False)

	@property
	def KeyVrsn(self):
		return self._KeyVrsn

	@KeyVrsn.setter
	def KeyVrsn(self, value):
		self._KeyVrsn = value if value is not None else base_types.UninitialisedField(self, 'KeyVrsn', Max256Text, False)

	@KeyVrsn.deleter
	def KeyVrsn(self):
		del self._KeyVrsn
		self._KeyVrsn = base_types.UninitialisedField(self, 'KeyVrsn', Max256Text, False)

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if value is not None else base_types.UninitialisedField(self, 'Nm', Max256Text, False)

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = base_types.UninitialisedField(self, 'Nm', Max256Text, False)

	@property
	def PrtctdCmpntWthAuthrsdAccs(self):
		return self._PrtctdCmpntWthAuthrsdAccs

	@PrtctdCmpntWthAuthrsdAccs.setter
	def PrtctdCmpntWthAuthrsdAccs(self, value):
		self._PrtctdCmpntWthAuthrsdAccs = value if value is not None else base_types.UninitialisedField(self, 'PrtctdCmpntWthAuthrsdAccs', ContentInformationType39, True)

	@PrtctdCmpntWthAuthrsdAccs.deleter
	def PrtctdCmpntWthAuthrsdAccs(self):
		del self._PrtctdCmpntWthAuthrsdAccs
		self._PrtctdCmpntWthAuthrsdAccs = base_types.UninitialisedField(self, 'PrtctdCmpntWthAuthrsdAccs', ContentInformationType39, True)

	@property
	def SctyPrfl(self):
		return self._SctyPrfl

	@SctyPrfl.setter
	def SctyPrfl(self, value):
		self._SctyPrfl = value if value is not None else base_types.UninitialisedField(self, 'SctyPrfl', Max35Text, False)

	@SctyPrfl.deleter
	def SctyPrfl(self):
		del self._SctyPrfl
		self._SctyPrfl = base_types.UninitialisedField(self, 'SctyPrfl', Max35Text, False)

	@property
	def SeqNb(self):
		return self._SeqNb

	@SeqNb.setter
	def SeqNb(self, value):
		self._SeqNb = value if value is not None else base_types.UninitialisedField(self, 'SeqNb', Number, False)

	@SeqNb.deleter
	def SeqNb(self):
		del self._SeqNb
		self._SeqNb = base_types.UninitialisedField(self, 'SeqNb', Number, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', CryptographicKeyType5Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', CryptographicKeyType5Code, False)

	@property
	def Vrsn(self):
		return self._Vrsn

	@Vrsn.setter
	def Vrsn(self, value):
		self._Vrsn = value if value is not None else base_types.UninitialisedField(self, 'Vrsn', Max256Text, False)

	@Vrsn.deleter
	def Vrsn(self):
		del self._Vrsn
		self._Vrsn = base_types.UninitialisedField(self, 'Vrsn', Max256Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActvtnDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlId', type=Max35Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlMgmtInf', type=GenericInformation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AlgoIdr', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmpntWthAuthrsdAccs', type=GenericIdentification186, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DeactvtnDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DerivtnAlgoIdr', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Fctn', type=KeyUsage1Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Id', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ItmNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='KeyChckVal', type=Max35Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='KeyId', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='KeyVal', type=ContentInformationType39, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='KeyVrsn', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdCmpntWthAuthrsdAccs', type=ContentInformationType39, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SctyPrfl', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SeqNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=CryptographicKeyType5Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vrsn', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
	))