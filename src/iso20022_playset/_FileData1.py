# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateAndDateTime2Choice
from . import DocumentFormat1Choice
from . import DocumentType1Choice
from . import Max140Text
from . import Max2048Text
from . import Max35Text

class FileData1(base_types._BaseFieldType):

	__slots__ = ["_FileLctnElctrncAdr", "_FileNm", "_Frmt", "_Id", "_IsseDt", "_NtwkRef", "_Tp"]
	@property
	def FileLctnElctrncAdr(self):
		return self._FileLctnElctrncAdr

	@FileLctnElctrncAdr.setter
	def FileLctnElctrncAdr(self, value):
		self._FileLctnElctrncAdr = value if value is not None else base_types.UninitialisedField(self, 'FileLctnElctrncAdr', Max2048Text, False)

	@FileLctnElctrncAdr.deleter
	def FileLctnElctrncAdr(self):
		del self._FileLctnElctrncAdr
		self._FileLctnElctrncAdr = base_types.UninitialisedField(self, 'FileLctnElctrncAdr', Max2048Text, False)

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
	def NtwkRef(self):
		return self._NtwkRef

	@NtwkRef.setter
	def NtwkRef(self, value):
		self._NtwkRef = value if value is not None else base_types.UninitialisedField(self, 'NtwkRef', Max140Text, False)

	@NtwkRef.deleter
	def NtwkRef(self):
		del self._NtwkRef
		self._NtwkRef = base_types.UninitialisedField(self, 'NtwkRef', Max140Text, False)

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
		base_types.FieldEntry(name='FileLctnElctrncAdr', type=Max2048Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FileNm', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frmt', type=DocumentFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IsseDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtwkRef', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=DocumentType1Choice, min=0, max=1, mutex_group=None, array=False),
	))