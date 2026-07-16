# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMStatus3Code
from . import CryptographicKeyType5Code
from . import FailureReason6Code
from . import ISODateTime
from . import KeyUsage1Code
from . import Max140Text
from . import Max256Text
from . import Max35Binary
from . import Max35Text
from . import Number

class CryptographicKey20(base_types._BaseFieldType):

	__slots__ = ["_ActvtnDt", "_AddtlId", "_CurSts", "_DeactvtnDt", "_FailrRsn", "_Fctn", "_Id", "_KeyChckVal", "_Nm", "_SctyDomnId", "_SeqCntr", "_Tp", "_Vrsn"]
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
	def CurSts(self):
		return self._CurSts

	@CurSts.setter
	def CurSts(self, value):
		self._CurSts = value if value is not None else base_types.UninitialisedField(self, 'CurSts', ATMStatus3Code, False)

	@CurSts.deleter
	def CurSts(self):
		del self._CurSts
		self._CurSts = base_types.UninitialisedField(self, 'CurSts', ATMStatus3Code, False)

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
	def FailrRsn(self):
		return self._FailrRsn

	@FailrRsn.setter
	def FailrRsn(self, value):
		self._FailrRsn = value if value is not None else base_types.UninitialisedField(self, 'FailrRsn', FailureReason6Code, False)

	@FailrRsn.deleter
	def FailrRsn(self):
		del self._FailrRsn
		self._FailrRsn = base_types.UninitialisedField(self, 'FailrRsn', FailureReason6Code, False)

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
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max140Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max140Text, False)

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
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if value is not None else base_types.UninitialisedField(self, 'Nm', Max140Text, False)

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = base_types.UninitialisedField(self, 'Nm', Max140Text, False)

	@property
	def SctyDomnId(self):
		return self._SctyDomnId

	@SctyDomnId.setter
	def SctyDomnId(self, value):
		self._SctyDomnId = value if value is not None else base_types.UninitialisedField(self, 'SctyDomnId', Max35Text, False)

	@SctyDomnId.deleter
	def SctyDomnId(self):
		del self._SctyDomnId
		self._SctyDomnId = base_types.UninitialisedField(self, 'SctyDomnId', Max35Text, False)

	@property
	def SeqCntr(self):
		return self._SeqCntr

	@SeqCntr.setter
	def SeqCntr(self, value):
		self._SeqCntr = value if value is not None else base_types.UninitialisedField(self, 'SeqCntr', Number, False)

	@SeqCntr.deleter
	def SeqCntr(self):
		del self._SeqCntr
		self._SeqCntr = base_types.UninitialisedField(self, 'SeqCntr', Number, False)

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
		base_types.FieldEntry(name='CurSts', type=ATMStatus3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DeactvtnDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FailrRsn', type=FailureReason6Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Fctn', type=KeyUsage1Code, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Id', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='KeyChckVal', type=Max35Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyDomnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SeqCntr', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=CryptographicKeyType5Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vrsn', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
	))