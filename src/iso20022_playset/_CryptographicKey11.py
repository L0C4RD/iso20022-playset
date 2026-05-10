from . import base_types
from ._KeyUsage1Code import KeyUsage1Code
from ._FailureReason6Code import FailureReason6Code
from ._Number import Number
from ._Max256Text import Max256Text
from ._CryptographicKeyType3Code import CryptographicKeyType3Code
from ._Max35Text import Max35Text
from ._Max35Binary import Max35Binary
from ._ATMStatus3Code import ATMStatus3Code
from ._ISODateTime import ISODateTime
from ._Max140Text import Max140Text

class CryptographicKey11(base_types._BaseFieldType):

	__slots__ = ["_Fctn", "_SctyDomnId", "_Nm", "_FailrRsn", "_AddtlId", "_Id", "_ActvtnDt", "_DeactvtnDt", "_SeqCntr", "_KeyChckVal", "_Tp", "_Vrsn", "_CurSts"]
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
	def CurSts(self):
		return self._CurSts

	@CurSts.setter
	def CurSts(self, value):
		self._CurSts = value if type(value) != base_types.auto else self.make_default("CurSts")

	@CurSts.deleter
	def CurSts(self):
		del self._CurSts
		self._CurSts = None

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
	def FailrRsn(self):
		return self._FailrRsn

	@FailrRsn.setter
	def FailrRsn(self, value):
		self._FailrRsn = value if type(value) != base_types.auto else self.make_default("FailrRsn")

	@FailrRsn.deleter
	def FailrRsn(self):
		del self._FailrRsn
		self._FailrRsn = None

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
		base_types.FieldEntry(name='CurSts', type=ATMStatus3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DeactvtnDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FailrRsn', type=FailureReason6Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Fctn', type=KeyUsage1Code, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Id', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='KeyChckVal', type=Max35Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyDomnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SeqCntr', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=CryptographicKeyType3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vrsn', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
	))

