from . import base_types
from ._CryptographicKeyType5Code import CryptographicKeyType5Code
from ._ISODateTime import ISODateTime
from ._KeyUsage1Code import KeyUsage1Code
from ._KeyValue3Choice import KeyValue3Choice
from ._Max140Text import Max140Text
from ._Max256Text import Max256Text
from ._Max35Binary import Max35Binary
from ._Max35Text import Max35Text
from ._Number import Number
from ._PublicRSAKey1 import PublicRSAKey1

class CryptographicKey21(base_types._BaseFieldType):

	__slots__ = ["_ActvtnDt", "_AddtlId", "_DeactvtnDt", "_Fctn", "_Id", "_KeyChcVal", "_KeyChckVal", "_Nm", "_PblcKeyVal", "_SctyDomnId", "_SeqCntr", "_Tp", "_Vrsn"]
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
	def KeyChcVal(self):
		return self._KeyChcVal

	@KeyChcVal.setter
	def KeyChcVal(self, value):
		self._KeyChcVal = value if type(value) != base_types.auto else self.make_default("KeyChcVal")

	@KeyChcVal.deleter
	def KeyChcVal(self):
		del self._KeyChcVal
		self._KeyChcVal = None

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
	def PblcKeyVal(self):
		return self._PblcKeyVal

	@PblcKeyVal.setter
	def PblcKeyVal(self, value):
		self._PblcKeyVal = value if type(value) != base_types.auto else self.make_default("PblcKeyVal")

	@PblcKeyVal.deleter
	def PblcKeyVal(self):
		del self._PblcKeyVal
		self._PblcKeyVal = None

	@property
	def SctyDomnId(self):
		return self._SctyDomnId

	@SctyDomnId.setter
	def SctyDomnId(self, value):
		self._SctyDomnId = value if type(value) != base_types.auto else self.make_default("SctyDomnId")

	@SctyDomnId.deleter
	def SctyDomnId(self):
		del self._SctyDomnId
		self._SctyDomnId = None

	@property
	def SeqCntr(self):
		return self._SeqCntr

	@SeqCntr.setter
	def SeqCntr(self, value):
		self._SeqCntr = value if type(value) != base_types.auto else self.make_default("SeqCntr")

	@SeqCntr.deleter
	def SeqCntr(self):
		del self._SeqCntr
		self._SeqCntr = None

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
		base_types.FieldEntry(name='DeactvtnDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Fctn', type=KeyUsage1Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Id', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='KeyChcVal', type=KeyValue3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='KeyChckVal', type=Max35Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PblcKeyVal', type=PublicRSAKey1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyDomnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SeqCntr', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=CryptographicKeyType5Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vrsn', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
	))

