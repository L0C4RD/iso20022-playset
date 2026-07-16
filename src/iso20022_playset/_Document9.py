# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DocumentFormat1Choice
from . import Max2MBBinary
from . import Max35Text
from . import PartyAndSignature2
from . import UndertakingDocumentType1Choice

class Document9(base_types._BaseFieldType):

	__slots__ = ["_DgtlSgntr", "_Frmt", "_Id", "_Nclsr", "_Tp"]
	@property
	def DgtlSgntr(self):
		return self._DgtlSgntr

	@DgtlSgntr.setter
	def DgtlSgntr(self, value):
		self._DgtlSgntr = value if value is not None else base_types.UninitialisedField(self, 'DgtlSgntr', PartyAndSignature2, False)

	@DgtlSgntr.deleter
	def DgtlSgntr(self):
		del self._DgtlSgntr
		self._DgtlSgntr = base_types.UninitialisedField(self, 'DgtlSgntr', PartyAndSignature2, False)

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
	def Nclsr(self):
		return self._Nclsr

	@Nclsr.setter
	def Nclsr(self, value):
		self._Nclsr = value if value is not None else base_types.UninitialisedField(self, 'Nclsr', Max2MBBinary, False)

	@Nclsr.deleter
	def Nclsr(self):
		del self._Nclsr
		self._Nclsr = base_types.UninitialisedField(self, 'Nclsr', Max2MBBinary, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', UndertakingDocumentType1Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', UndertakingDocumentType1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frmt', type=DocumentFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nclsr', type=Max2MBBinary, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=UndertakingDocumentType1Choice, min=1, max=1, mutex_group=None, array=False),
	))