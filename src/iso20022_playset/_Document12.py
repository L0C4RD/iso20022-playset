from . import base_types
from ._Max140Text import Max140Text
from ._LanguageCode import LanguageCode
from ._Max10MbBinary import Max10MbBinary
from ._DocumentFormat1Choice import DocumentFormat1Choice
from ._PartyAndSignature3 import PartyAndSignature3
from ._Max35Text import Max35Text
from ._DateAndDateTime2Choice import DateAndDateTime2Choice
from ._DocumentType1Choice import DocumentType1Choice

class Document12(base_types._BaseFieldType):

	__slots__ = ["_FileNm", "_Nm", "_Tp", "_Id", "_IsseDt", "_LangCd", "_Nclsr", "_DgtlSgntr", "_Frmt"]
	@property
	def DgtlSgntr(self):
		return self._DgtlSgntr

	@DgtlSgntr.setter
	def DgtlSgntr(self, value):
		self._DgtlSgntr = value if type(value) != base_types.auto else self.make_default("DgtlSgntr")

	@DgtlSgntr.deleter
	def DgtlSgntr(self):
		del self._DgtlSgntr
		self._DgtlSgntr = None

	@property
	def FileNm(self):
		return self._FileNm

	@FileNm.setter
	def FileNm(self, value):
		self._FileNm = value if type(value) != base_types.auto else self.make_default("FileNm")

	@FileNm.deleter
	def FileNm(self):
		del self._FileNm
		self._FileNm = None

	@property
	def Frmt(self):
		return self._Frmt

	@Frmt.setter
	def Frmt(self, value):
		self._Frmt = value if type(value) != base_types.auto else self.make_default("Frmt")

	@Frmt.deleter
	def Frmt(self):
		del self._Frmt
		self._Frmt = None

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
	def IsseDt(self):
		return self._IsseDt

	@IsseDt.setter
	def IsseDt(self, value):
		self._IsseDt = value if type(value) != base_types.auto else self.make_default("IsseDt")

	@IsseDt.deleter
	def IsseDt(self):
		del self._IsseDt
		self._IsseDt = None

	@property
	def LangCd(self):
		return self._LangCd

	@LangCd.setter
	def LangCd(self, value):
		self._LangCd = value if type(value) != base_types.auto else self.make_default("LangCd")

	@LangCd.deleter
	def LangCd(self):
		del self._LangCd
		self._LangCd = None

	@property
	def Nclsr(self):
		return self._Nclsr

	@Nclsr.setter
	def Nclsr(self, value):
		self._Nclsr = value if type(value) != base_types.auto else self.make_default("Nclsr")

	@Nclsr.deleter
	def Nclsr(self):
		del self._Nclsr
		self._Nclsr = None

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
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FileNm', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frmt', type=DocumentFormat1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IsseDt', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LangCd', type=LanguageCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nclsr', type=Max10MbBinary, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=DocumentType1Choice, min=1, max=1, mutex_group=None, array=False),
	))

