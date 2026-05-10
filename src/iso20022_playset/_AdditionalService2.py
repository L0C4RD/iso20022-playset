from . import base_types
from ._Max35Text import Max35Text
from ._AdditionalServiceType2Code import AdditionalServiceType2Code
from ._AdditionalServiceResult1Code import AdditionalServiceResult1Code
from ._AdditionalData1 import AdditionalData1

class AdditionalService2(base_types._BaseFieldType):

	__slots__ = ["_SvcDtl", "_Rslt", "_Tp", "_OthrRslt", "_OthrTp"]
	@property
	def OthrRslt(self):
		return self._OthrRslt

	@OthrRslt.setter
	def OthrRslt(self, value):
		self._OthrRslt = value if type(value) != base_types.auto else self.make_default("OthrRslt")

	@OthrRslt.deleter
	def OthrRslt(self):
		del self._OthrRslt
		self._OthrRslt = None

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

	@property
	def Rslt(self):
		return self._Rslt

	@Rslt.setter
	def Rslt(self, value):
		self._Rslt = value if type(value) != base_types.auto else self.make_default("Rslt")

	@Rslt.deleter
	def Rslt(self):
		del self._Rslt
		self._Rslt = None

	@property
	def SvcDtl(self):
		return self._SvcDtl

	@SvcDtl.setter
	def SvcDtl(self, value):
		self._SvcDtl = value if type(value) != base_types.auto else self.make_default("SvcDtl")

	@SvcDtl.deleter
	def SvcDtl(self):
		del self._SvcDtl
		self._SvcDtl = None

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
		base_types.FieldEntry(name='OthrRslt', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rslt', type=AdditionalServiceResult1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcDtl', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tp', type=AdditionalServiceType2Code, min=1, max=1, mutex_group=None, array=False),
	))

