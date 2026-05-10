import base_types
import Max35Text
import Max2048Text
import DocumentFormat1Choice
import DocumentType1Choice
import DateAndDateTime2Choice
import Max140Text

class FileData1(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_Id", "_IsseDt", "_FileLctnElctrncAdr", "_Frmt", "_FileNm", "_NtwkRef"]
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
	def IsseDt(self):
		return self._IsseDt

	@IsseDt.setter
	def IsseDt(self, value):
		self._IsseDt = value if type(value) != auto else self.make_default("IsseDt")

	@IsseDt.deleter
	def IsseDt(self):
		del self._IsseDt
		self._IsseDt = None

	@property
	def FileLctnElctrncAdr(self):
		return self._FileLctnElctrncAdr

	@FileLctnElctrncAdr.setter
	def FileLctnElctrncAdr(self, value):
		self._FileLctnElctrncAdr = value if type(value) != auto else self.make_default("FileLctnElctrncAdr")

	@FileLctnElctrncAdr.deleter
	def FileLctnElctrncAdr(self):
		del self._FileLctnElctrncAdr
		self._FileLctnElctrncAdr = None

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
	def FileNm(self):
		return self._FileNm

	@FileNm.setter
	def FileNm(self, value):
		self._FileNm = value if type(value) != auto else self.make_default("FileNm")

	@FileNm.deleter
	def FileNm(self):
		del self._FileNm
		self._FileNm = None

	@property
	def NtwkRef(self):
		return self._NtwkRef

	@NtwkRef.setter
	def NtwkRef(self, value):
		self._NtwkRef = value if type(value) != auto else self.make_default("NtwkRef")

	@NtwkRef.deleter
	def NtwkRef(self):
		del self._NtwkRef
		self._NtwkRef = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tp', type=DocumentType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IsseDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FileLctnElctrncAdr', type=Max2048Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frmt', type=DocumentFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FileNm', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtwkRef', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
	))

