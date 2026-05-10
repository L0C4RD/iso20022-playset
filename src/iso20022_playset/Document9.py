from . import base_types
import Max2MBBinary
import PartyAndSignature2
import UndertakingDocumentType1Choice
import DocumentFormat1Choice
import Max35Text

class Document9(base_types._BaseFieldType):

	__slots__ = ["_DgtlSgntr", "_Id", "_Frmt", "_Tp", "_Nclsr"]
	@property
	def DgtlSgntr(self):
		return self._DgtlSgntr

	@DgtlSgntr.setter
	def DgtlSgntr(self, value):
		self._DgtlSgntr = value if type(value) != auto else self.make_default("DgtlSgntr")

	@DgtlSgntr.deleter
	def DgtlSgntr(self):
		del self._DgtlSgntr
		self._DgtlSgntr = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def Frmt(self):
		return self._Frmt

	@Frmt.setter
	def Frmt(self, value):
		self._Frmt = value if type(value) != auto else self.make_default("Frmt")

	@Frmt.deleter
	def Frmt(self):
		del self._Frmt
		self._Frmt = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def Nclsr(self):
		return self._Nclsr

	@Nclsr.setter
	def Nclsr(self, value):
		self._Nclsr = value if type(value) != auto else self.make_default("Nclsr")

	@Nclsr.deleter
	def Nclsr(self):
		del self._Nclsr
		self._Nclsr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frmt', type=DocumentFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=UndertakingDocumentType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nclsr', type=Max2MBBinary, min=1, max=1, mutex_group=None, array=False),
	))

