# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateAndDateTime2Choice
from . import DocumentFormat1Choice
from . import DocumentType1Choice
from . import LanguageCode
from . import Max10MbBinary
from . import Max140Text
from . import Max35Text
from . import PartyAndSignature4

class Document15(base_types._BaseFieldType):

	__slots__ = ["_DgtlSgntr", "_FileNm", "_Frmt", "_Id", "_IsseDt", "_LangCd", "_Nclsr", "_Nm", "_Tp"]
	@property
	def DgtlSgntr(self):
		return self._DgtlSgntr

	@DgtlSgntr.setter
	def DgtlSgntr(self, value):
		self._DgtlSgntr = value if value is not None else base_types.UninitialisedField(self, 'DgtlSgntr', PartyAndSignature4, False)

	@DgtlSgntr.deleter
	def DgtlSgntr(self):
		del self._DgtlSgntr
		self._DgtlSgntr = base_types.UninitialisedField(self, 'DgtlSgntr', PartyAndSignature4, False)

	@property
	def FileNm(self):
		return self._FileNm

	@FileNm.setter
	def FileNm(self, value):
		self._FileNm = value if value is not None else base_types.UninitialisedField(self, 'FileNm', Max140Text, False)

	@FileNm.deleter
	def FileNm(self):
		del self._FileNm
		self._FileNm = base_types.UninitialisedField(self, 'FileNm', Max140Text, False)

	@property
	def Frmt(self):
		return self._Frmt

	@Frmt.setter
	def Frmt(self, value):
		self._Frmt = value if value is not None else base_types.UninitialisedField(self, 'Frmt', DocumentFormat1Choice, False)

	@Frmt.deleter
	def Frmt(self):
		del self._Frmt
		self._Frmt = base_types.UninitialisedField(self, 'Frmt', DocumentFormat1Choice, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@property
	def IsseDt(self):
		return self._IsseDt

	@IsseDt.setter
	def IsseDt(self, value):
		self._IsseDt = value if value is not None else base_types.UninitialisedField(self, 'IsseDt', DateAndDateTime2Choice, False)

	@IsseDt.deleter
	def IsseDt(self):
		del self._IsseDt
		self._IsseDt = base_types.UninitialisedField(self, 'IsseDt', DateAndDateTime2Choice, False)

	@property
	def LangCd(self):
		return self._LangCd

	@LangCd.setter
	def LangCd(self, value):
		self._LangCd = value if value is not None else base_types.UninitialisedField(self, 'LangCd', LanguageCode, False)

	@LangCd.deleter
	def LangCd(self):
		del self._LangCd
		self._LangCd = base_types.UninitialisedField(self, 'LangCd', LanguageCode, False)

	@property
	def Nclsr(self):
		return self._Nclsr

	@Nclsr.setter
	def Nclsr(self, value):
		self._Nclsr = value if value is not None else base_types.UninitialisedField(self, 'Nclsr', Max10MbBinary, False)

	@Nclsr.deleter
	def Nclsr(self):
		del self._Nclsr
		self._Nclsr = base_types.UninitialisedField(self, 'Nclsr', Max10MbBinary, False)

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
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', DocumentType1Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', DocumentType1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FileNm', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frmt', type=DocumentFormat1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IsseDt', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LangCd', type=LanguageCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nclsr', type=Max10MbBinary, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=DocumentType1Choice, min=1, max=1, mutex_group=None, array=False),
	))