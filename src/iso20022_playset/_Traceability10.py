from . import base_types
from ._PartyType17Code import PartyType17Code
from ._ISOMax3ACountryCode import ISOMax3ACountryCode
from ._PartyType18Code import PartyType18Code
from ._Max35Text import Max35Text
from ._ISODateTime import ISODateTime

class Traceability10(base_types._BaseFieldType):

	__slots__ = ["_ShrtNm", "_Ctry", "_Assgnr", "_DtTmIn", "_Tp", "_DtTmOut", "_Id", "_OthrTp"]
	@property
	def ShrtNm(self):
		return self._ShrtNm

	@ShrtNm.setter
	def ShrtNm(self, value):
		self._ShrtNm = value if type(value) != base_types.auto else self.make_default("ShrtNm")

	@ShrtNm.deleter
	def ShrtNm(self):
		del self._ShrtNm
		self._ShrtNm = None

	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if type(value) != base_types.auto else self.make_default("Ctry")

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = None

	@property
	def Assgnr(self):
		return self._Assgnr

	@Assgnr.setter
	def Assgnr(self, value):
		self._Assgnr = value if type(value) != base_types.auto else self.make_default("Assgnr")

	@Assgnr.deleter
	def Assgnr(self):
		del self._Assgnr
		self._Assgnr = None

	@property
	def DtTmIn(self):
		return self._DtTmIn

	@DtTmIn.setter
	def DtTmIn(self, value):
		self._DtTmIn = value if type(value) != base_types.auto else self.make_default("DtTmIn")

	@DtTmIn.deleter
	def DtTmIn(self):
		del self._DtTmIn
		self._DtTmIn = None

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
	def DtTmOut(self):
		return self._DtTmOut

	@DtTmOut.setter
	def DtTmOut(self, value):
		self._DtTmOut = value if type(value) != base_types.auto else self.make_default("DtTmOut")

	@DtTmOut.deleter
	def DtTmOut(self):
		del self._DtTmOut
		self._DtTmOut = None

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
	def OthrTp(self):
		return self._OthrTp

	@OthrTp.setter
	def OthrTp(self, value):
		self._OthrTp = value if type(value) != base_types.auto else self.make_default("OthrTp")

	@OthrTp.deleter
	def OthrTp(self):
		del self._OthrTp
		self._OthrTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ShrtNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctry', type=ISOMax3ACountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Assgnr', type=PartyType18Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtTmIn', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=PartyType17Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtTmOut', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

