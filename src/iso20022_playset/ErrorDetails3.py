import base_types
import Max35Text
import Max4000Text
import MessageError1Code
import Max500Text

class ErrorDetails3(base_types._BaseFieldType):

	__slots__ = ["_DataElmtInErr", "_Tp", "_OthrTp", "_Cd", "_Desc"]
	@property
	def DataElmtInErr(self):
		return self._DataElmtInErr

	@DataElmtInErr.setter
	def DataElmtInErr(self, value):
		self._DataElmtInErr = value if type(value) != auto else self.make_default("DataElmtInErr")

	@DataElmtInErr.deleter
	def DataElmtInErr(self):
		del self._DataElmtInErr
		self._DataElmtInErr = None

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
	def OthrTp(self):
		return self._OthrTp

	@OthrTp.setter
	def OthrTp(self, value):
		self._OthrTp = value if type(value) != auto else self.make_default("OthrTp")

	@OthrTp.deleter
	def OthrTp(self):
		del self._OthrTp
		self._OthrTp = None

	@property
	def Cd(self):
		return self._Cd

	@Cd.setter
	def Cd(self, value):
		self._Cd = value if type(value) != auto else self.make_default("Cd")

	@Cd.deleter
	def Cd(self):
		del self._Cd
		self._Cd = None

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if type(value) != auto else self.make_default("Desc")

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DataElmtInErr', type=Max4000Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tp', type=MessageError1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Desc', type=Max500Text, min=0, max=1, mutex_group=None, array=False),
	))

