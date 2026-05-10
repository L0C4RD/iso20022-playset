from . import base_types
from ._TrueFalseIndicator import TrueFalseIndicator
from ._ISODate import ISODate
from ._ContactPersonal1 import ContactPersonal1
from ._AdditionalData1 import AdditionalData1
from ._Address2 import Address2
from ._CardholderName3 import CardholderName3
from ._LocalData13 import LocalData13
from ._Credentials3 import Credentials3

class Cardholder22(base_types._BaseFieldType):

	__slots__ = ["_Id", "_DtOfBirth", "_Adr", "_HghVal", "_AddtlData", "_CtctInf", "_LclData", "_Nm"]
	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if type(value) != base_types.auto else self.make_default("AddtlData")

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = None

	@property
	def Adr(self):
		return self._Adr

	@Adr.setter
	def Adr(self, value):
		self._Adr = value if type(value) != base_types.auto else self.make_default("Adr")

	@Adr.deleter
	def Adr(self):
		del self._Adr
		self._Adr = None

	@property
	def CtctInf(self):
		return self._CtctInf

	@CtctInf.setter
	def CtctInf(self, value):
		self._CtctInf = value if type(value) != base_types.auto else self.make_default("CtctInf")

	@CtctInf.deleter
	def CtctInf(self):
		del self._CtctInf
		self._CtctInf = None

	@property
	def DtOfBirth(self):
		return self._DtOfBirth

	@DtOfBirth.setter
	def DtOfBirth(self, value):
		self._DtOfBirth = value if type(value) != base_types.auto else self.make_default("DtOfBirth")

	@DtOfBirth.deleter
	def DtOfBirth(self):
		del self._DtOfBirth
		self._DtOfBirth = None

	@property
	def HghVal(self):
		return self._HghVal

	@HghVal.setter
	def HghVal(self, value):
		self._HghVal = value if type(value) != base_types.auto else self.make_default("HghVal")

	@HghVal.deleter
	def HghVal(self):
		del self._HghVal
		self._HghVal = None

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
	def LclData(self):
		return self._LclData

	@LclData.setter
	def LclData(self, value):
		self._LclData = value if type(value) != base_types.auto else self.make_default("LclData")

	@LclData.deleter
	def LclData(self):
		del self._LclData
		self._LclData = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlData', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Adr', type=Address2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtctInf', type=ContactPersonal1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtOfBirth', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HghVal', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Credentials3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LclData', type=LocalData13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=CardholderName3, min=0, max=1, mutex_group=None, array=False),
	))

